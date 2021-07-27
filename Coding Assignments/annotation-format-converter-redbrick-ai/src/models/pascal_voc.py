from typing import List
from pydantic import BaseModel


class BBox2d(BaseModel):
    xnorm: float
    ynorm: float
    hnorm: float
    wnorm: float


class Label(BaseModel):
    category: List[List[str]]
    attributes: List
    bbox2d: BBox2d


class Datapoint(BaseModel):
    name: str
    dpId: str
    items: List[str]
    labels: List[Label]


class CategoryChild(BaseModel):
    name: str
    classId: int
    children: List


class Category(BaseModel):
    name: str
    children: List[CategoryChild]


class Taxonomy(BaseModel):
    name: str
    version: int
    attributes: List
    categories: List[Category]


class PascalVoc(BaseModel):
    taxonomy: Taxonomy
    datapoints: List[Datapoint]
