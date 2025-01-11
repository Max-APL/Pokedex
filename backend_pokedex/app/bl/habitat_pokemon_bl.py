from app.repository.habitat_pokemon_repository import HabitatPokemonRepository
from app.schema.habitat_pokemon import HabitatPokemonListResponse


class HabitatPokemonBL:
    @staticmethod
    async def get_all_habitats() -> HabitatPokemonListResponse:
        """Lógica de negocio para obtener todos los habitats de Pokémon."""
        return await HabitatPokemonRepository.get_all_habitats()
