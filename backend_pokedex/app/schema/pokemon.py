from pydantic import BaseModel
from typing import List, Optional


class AbilityDetail(BaseModel):
    name: str
    url: str


class PokemonAbility(BaseModel):
    ability: AbilityDetail
    is_hidden: bool
    slot: int


class PokemonTypeDetail(BaseModel):
    name: str
    url: str


class PokemonType(BaseModel):
    slot: int
    type: PokemonTypeDetail


class PokemonSpritesHome(BaseModel):
    front_default: Optional[str]
    front_female: Optional[str]
    front_shiny: Optional[str]
    front_shiny_female: Optional[str]

class PokemonSpecies(BaseModel):
    name: str
    url: str

class PokemonSchema(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    base_experience: int
    is_default: bool
    location_area_encounters: str
    abilities: List[PokemonAbility]
    types: List[PokemonType]
    sprites: PokemonSpritesHome
    species: PokemonSpecies
    evolutions: Optional[List[str]]


class PokemonByType(BaseModel):
    name: str
    url: str
    image: Optional[str]  # URL de la imagen del Pokémon

class PaginatedPokemonResponse(BaseModel):
    total: int
    page: int
    per_page: int
    pokemons: List[PokemonByType]
