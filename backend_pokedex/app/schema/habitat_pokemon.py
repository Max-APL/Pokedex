from pydantic import BaseModel
from typing import List


class HabitatPokemon(BaseModel):
    name: str
    url: str


class HabitatPokemonListResponse(BaseModel):
    count: int
    results: List[HabitatPokemon]


class Species(BaseModel):
    name: str
    url: str


class HabitatDetailsResponse(BaseModel):
    id: int
    name: str
    species: List[Species]
