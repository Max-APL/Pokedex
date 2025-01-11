from pydantic import BaseModel
from typing import List


class HabitatPokemon(BaseModel):
    name: str
    url: str


class HabitatPokemonListResponse(BaseModel):
    count: int
    results: List[HabitatPokemon]
