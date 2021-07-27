from typing import List
from pydantic import BaseModel


class Category(BaseModel):
    name: str
    id: int


class Annotation(BaseModel):
    id: int
    image_id: int
    category_id: int
    bbox: List[float]
    iscrowd: int
    segmentation: List


class Image(BaseModel):
    id: int
    file_name: str
    height: int
    width: int


class Coco(BaseModel):
    images: List[Image]
    annotations: List[Annotation]
    categories: List[Category]
