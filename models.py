# generated by fastapi-codegen:
#   filename:  api.yaml
#   timestamp: 2021-05-24T07:37:30+00:00

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import AnyUrl, BaseModel, Field


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Pets(BaseModel):
    __root__: List[Pet]


class Error(BaseModel):
    code: int
    message: str


class InputData(BaseModel):
    id:int
    name:str
    skills:str

class OutputData(BaseModel):
    result:Dict