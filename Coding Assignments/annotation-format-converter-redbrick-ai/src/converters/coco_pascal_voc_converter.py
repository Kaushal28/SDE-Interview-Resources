import json
from typing import Tuple, List

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


class CocoPascalVocConverter(ConverterBase):
    """Pascal VOC to COCO converter class."""

    def load(self, annotation: dict) -> Coco:
        """
        Load the COCO annotation into python object from given dict.

        :param annotation: Annotation to be loaded.
        :return: COCO annotation object.
        """
        try:
            # load images
            images, images_arr = annotation["images"], []
            for image in images:
                images_arr.append(
                    Image(
                        id=image["id"],
                        file_name=image["file_name"],
                        height=image["height"],
                        width=image["width"],
                    )
                )

            # load annotations
            annotations, annotations_arr = annotation["annotations"], []
            for ann in annotations:
                annotations_arr.append(
                    Annotation(
                        id=ann["id"],
                        image_id=ann["image_id"],
                        category_id=ann["category_id"],
                        bbox=ann["bbox"],
                        iscrowd=ann["iscrowd"],
                        segmentation=ann["segmentation"],
                    )
                )

            # load categories
            categories, categories_arr = annotation["categories"], []
            for cat in categories:
                categories_arr.append(
                    CocoCategory(
                        name=cat["name"],
                        id=cat["id"],
                    )
                )

            # construct final COCO object
            return Coco(
                images=images_arr,
                annotations=annotations_arr,
                categories=categories_arr
            )
        except KeyError as err:
            # TODO raise
            pass

    def _convert_bbox(self, coco_bbox: List[float], dim: Tuple[int, int]) -> BBox2d:
        """
        Convert pascal VOC bbox to COCO bbox.

        :param coco_bbox: COCO bounding box.
        :return: COCO bbox.
        """
        pass

    def convert(self, annotation: Coco) -> PascalVoc:
        """
        Convert pascal VOC to COCO format.

        :param annotation: Pascal VOC annotation object.
        :return: Coco annotation object.
        """
        try:
            # create categories object
            category_children = []
            for cat in annotation.categories:
                category_children.append(
                    CategoryChild(
                        name=cat.name,
                        classId=cat.id,
                        children=[],
                    )
                )

            # create taxonomy
            taxonomy = Taxonomy(
                name="basicTaxonomy",
                version=1,
                attributes=[],
                categoies=PascalVocCategory(
                    name="object",
                    children=category_children,
                )
            )

            # create data points

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
