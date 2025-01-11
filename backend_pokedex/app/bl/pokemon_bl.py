from typing import Optional
from app.repository.pokemon_repository import PokemonRepository
from app.schema.pokemon import PokemonSchema, PaginatedPokemonResponse

class PokemonBL:
    @staticmethod
    async def get_pokemon(name_or_id: str) -> Optional[PokemonSchema]:
        """Lógica de negocio para obtener un Pokémon."""
        pokemon = await PokemonRepository.get_pokemon_details(name_or_id)
        if not pokemon:
            return None
        return pokemon

    @staticmethod
    async def get_pokemon_by_type1(type_name: str, page: int, per_page: int) -> Optional[PaginatedPokemonResponse]:
        """Lógica de negocio para obtener los Pokémon por tipo con paginación."""
        pokemon = await PokemonRepository.get_pokemon_by_type(type_name, page, per_page)
        print(pokemon)
        if not pokemon:
            return None
        return pokemon