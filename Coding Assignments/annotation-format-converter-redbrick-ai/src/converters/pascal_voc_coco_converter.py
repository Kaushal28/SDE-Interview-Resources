import json
from typing import Tuple, List

import requests
from PIL import Image as PilImage
from io import BytesIO

from src.converters.converter_base import ConverterBase
from src.models.pascal_voc import (
    PascalVoc,
    Taxonomy,
    Datapoint,
    Label,
    Category as PascalVocCategory,
    CategoryChild,
    BBox2d,
)
from src.models.coco import (
    Coco,
    Image,
    Category as CocoCategory,
    Annotation,
)


class PascalVocCocoConverter(ConverterBase):
    """Pascal VOC to COCO converter class."""

    def load(self, annotation: dict) -> PascalVoc:
        """
        Load the Pascal VOC annotation into python object from given dict.

        :param annotation: Annotation to be loaded.
        :return: Pascal VOC annotation object.
        """
        try:
            # load taxonomy
            taxonomy = annotation["taxonomy"]
            taxonomy = Taxonomy(
                name=taxonomy["name"],
                version=taxonomy["version"],
                attributes=taxonomy["attributes"],
                categories=[
                    PascalVocCategory(
                        name=cat["name"],
                        children=[CategoryChild(**child) for child in cat["children"]],
                    )
                    for cat in taxonomy["categories"]
                ],
            )

            # load data points
            datapoints, datapoints_arr = annotation["datapoints"], []
            for point in datapoints:
                datapoints_arr.append(
                    Datapoint(
                        name=point["name"],
                        dpId=point["dpId"],
                        items=point["items"],
                        labels=[
                            Label(
                                category=label["category"],
                                attributes=label["attributes"],
                                bbox2d=BBox2d(**label["bbox2d"]),
                            )
                            for label in point["labels"]
                        ],
                    )
                )

            # construct final Pascal VOC object
            return PascalVoc(taxonomy=taxonomy, datapoints=datapoints_arr)
        except KeyError as err:
            # TODO raise
            pass

    def _get_sizes(self, url) -> Tuple[int, int]:
        """
        Get size of an image from a url.

        :param url: URL where the image is located.
        :return: width, height of the image
        """
        try:
            # return 100, 100
            image_raw = requests.get(url)
            image_raw.raise_for_status()
            image = PilImage.open(BytesIO(image_raw.content))
            return image.size
        except requests.exceptions.HTTPError as err:
            pass
        except requests.exceptions.ConnectTimeout as err:
            pass
        except requests.exceptions.ConnectionError as err:
            pass
        except Exception as err:
            print(err)

        return 0, 0

    def _convert_bbox(self, pascal_bbox: BBox2d, dim: Tuple[int, int]) -> List[float]:
        """
        Convert pascal VOC bbox to COCO bbox.

        :param pascal_bbox: Pascal VOC bbox.
        :return: COCO bounding box.
        """
        width, height = dim
        x = pascal_bbox.xnorm * width
        y = pascal_bbox.ynorm * height
        w = pascal_bbox.wnorm * width
        h = pascal_bbox.hnorm * height
        return [x, y, w, h]

    def convert(self, annotation: PascalVoc) -> Coco:
        """
        Convert pascal VOC to COCO format.

        :param annotation: Pascal VOC annotation object.
        :return: Coco annotation object.
        """
        try:
            # construct images array
            images_arr, dim_map = [], {}
            for idx, datapoint in enumerate(annotation.datapoints):
                width, height = self._get_sizes(datapoint.items[0])
                images_arr.append(
                    Image(
                        id=idx,
                        file_name=datapoint.items[0],
                        height=height,
                        width=width,
                    )
                )
                dim_map[idx] = width, height

            # construct categories array
            category_arr, category_map = [], {}
            for cat in annotation.taxonomy.categories:
                for child in cat.children:
                    category_arr.append(CocoCategory(name=child.name, id=child.classId))
                    category_map[child.name] = child.classId

            # construct annotations array
            annotations_arr = []
            for ann_idx, ann in enumerate(annotation.datapoints):
                for label_idx, label in enumerate(ann.labels):
                    annotations_arr.append(
                        Annotation(
                            id=ann_idx + label_idx,
                            image_id=ann_idx,
                            category_id=category_map[label.category[0][1]],
                            bbox=self._convert_bbox(label.bbox2d, dim_map[ann_idx]),
                            iscrowd=0,
                            segmentation=[],
                        )
                    )

            # construct final COCO object
            return Coco(
                images=images_arr, annotations=annotations_arr, categories=category_arr
            )
        except json.JSONDecodeError:
            pass
            # TODO raise json decodeerror
            # TODO: also catch other conversion errors

    def to_str(self, annotation: Coco):
        """
        Reverse of "load()". Converts the given Pascal VOC annotation
        object to string.

        :param annotation: Pascal VOC Annotation object to be converted to string.
        :return: Pascal VOC annotation string.
        """
        return json.dumps(annotation, default=lambda o: getattr(o, "__dict__", str(o)))
