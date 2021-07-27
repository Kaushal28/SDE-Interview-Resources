import json

from src.converters.pascal_voc_coco_converter import PascalVocCocoConverter


def read(path: str) -> str:
    """
    Read the file at given path.

    :param path: File path to be read.
    :return: Read content.
    """
    with open(path, "r") as file:
        return file.read()


def write(content: str, path: str) -> None:
    """
    Write the file at given path.

    :param content: Content to be written.
    :param path: File location.
    """
    with open(path, "w+") as file:
        file.write(content)


with open("example_input.json", "r") as file:
    pvoc_coco = PascalVocCocoConverter()
    loaded = pvoc_coco.load(json.load(file))
    converted = pvoc_coco.convert(loaded)
    print(pvoc_coco.to_str(converted))
