from app.repository.type_pokemon_repository import TypePokemonRepository
from app.schema.type_pokemon import TypePokemonListResponse


class TypePokemonBL:
    @staticmethod
    async def get_all_types() -> TypePokemonListResponse:
        """Lógica de negocio para obtener todos los tipos de Pokémon."""
        return await TypePokemonRepository.get_all_types()
