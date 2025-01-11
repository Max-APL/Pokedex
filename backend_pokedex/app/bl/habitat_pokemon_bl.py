from app.repository.habitat_pokemon_repository import HabitatPokemonRepository
from app.schema.habitat_pokemon import HabitatPokemonListResponse, HabitatDetailsResponse


class HabitatPokemonBL:
    @staticmethod
    async def get_all_habitats() -> HabitatPokemonListResponse:
        """Lógica de negocio para obtener todos los habitats de Pokémon."""
        return await HabitatPokemonRepository.get_all_habitats()

    @staticmethod
    async def get_habitat_details(name_or_id: str) -> HabitatDetailsResponse:
        """Lógica de negocio para obtener los detalles de un habitat."""
        return await HabitatPokemonRepository.get_habitat_details(name_or_id)