import httpx
from app.schema.habitat_pokemon import HabitatPokemonListResponse, HabitatDetailsResponse


class HabitatPokemonRepository:
    BASE_URL = "https://pokeapi.co/api/v2"

    @staticmethod
    async def get_all_habitats() -> HabitatPokemonListResponse:
        """Obtiene la lista de todos los habitats de Pokémon."""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{HabitatPokemonRepository.BASE_URL}/pokemon-habitat/")
            if response.status_code != 200:
                raise Exception("Error al obtener los habitats de Pokémon.")
            data = response.json()

            # Mapeo de datos al esquema interno
            return HabitatPokemonListResponse(
                count=data["count"],
                results=[
                    {"name": habitat_data["name"], "url": habitat_data["url"]}
                    for habitat_data in data["results"]
                ]
            )

    @staticmethod
    async def get_habitat_details(name_or_id: str) -> HabitatDetailsResponse:
        """Obtiene los detalles de un habitat incluyendo las species."""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{HabitatPokemonRepository.BASE_URL}/pokemon-habitat/{name_or_id}/")
            if response.status_code != 200:
                raise Exception(f"Error al obtener los detalles del habitat {name_or_id}.")
            data = response.json()

            # Mapeo de datos al esquema interno
            return HabitatDetailsResponse(
                id=data["id"],
                name=data["name"],
                species=[
                    {"name": species["name"], "url": species["url"]}
                    for species in data["pokemon_species"]
                ]
            )