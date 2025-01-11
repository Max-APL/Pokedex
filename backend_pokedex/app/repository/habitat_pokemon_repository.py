import httpx
from app.schema.habitat_pokemon import HabitatPokemonListResponse


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
