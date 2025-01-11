import httpx
from app.schema.type_pokemon import TypePokemonListResponse


class TypePokemonRepository:
    BASE_URL = "https://pokeapi.co/api/v2"

    @staticmethod
    async def get_all_types() -> TypePokemonListResponse:
        """Obtiene la lista de todos los tipos de Pokémon."""
        async with httpx.AsyncClient() as client:
            # Cambiar al endpoint que retorna todos los tipos
            response = await client.get(f"{TypePokemonRepository.BASE_URL}/type/?offset=1&limit=21")
            if response.status_code != 200:
                raise Exception("Error al obtener los tipos de Pokémon.")
            data = response.json()

            # Mapeo de datos al esquema interno
            return TypePokemonListResponse(
                count=data["count"],
                results=[
                    {"name": type_data["name"], "url": type_data["url"]}
                    for type_data in data["results"]
                ]
            )
