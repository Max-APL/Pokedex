from pydantic import BaseModel
from typing import List


class TypePokemon(BaseModel):
    name: str
    url: str


class TypePokemonListResponse(BaseModel):
    count: int
    results: List[TypePokemon]
