from app.repository.habitat_pokemon_repository import HabitatPokemonRepository
from app.schema.habitat_pokemon import HabitatPokemonListResponse, HabitatDetailsResponse, Species


class HabitatPokemonBL:
    @staticmethod
    async def get_all_habitats() -> HabitatPokemonListResponse:
        """Lógica de negocio para obtener todos los habitats de Pokémon."""
        return await HabitatPokemonRepository.get_all_habitats()

    @staticmethod
    async def get_habitat_details(name_or_id: str) -> HabitatDetailsResponse:
        """Lógica de negocio para obtener los detalles de un habitat."""
        return await HabitatPokemonRepository.get_habitat_details(name_or_id)

    @staticmethod
    async def get_species_by_habitat(name_or_id: str, page: int, per_page: int) -> list[Species]:
        """
        Lógica de negocio para obtener especies de un hábitat con paginación.
        """
        all_species = await HabitatPokemonRepository.get_habitat_species(name_or_id)

        # Paginación
        start = (page - 1) * per_page
        end = start + per_page
        return all_species[start:end]
