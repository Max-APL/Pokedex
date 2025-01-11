from typing import Optional, List
import httpx
from app.schema.pokemon import (
    PokemonSchema, PokemonAbility, PokemonType, PokemonSpritesHome, PaginatedPokemonResponse, PokemonSpecies
)


class PokemonRepository:
    BASE_URL = "https://pokeapi.co/api/v2"

    @staticmethod
    async def get_evolution_chain(species_url: str) -> Optional[List[str]]:
        """Obtiene la cadena de evoluciones a partir de la URL de especie."""
        async with httpx.AsyncClient() as client:
            # Obtener datos de la especie
            species_response = await client.get(species_url)
            if species_response.status_code != 200:
                return None
            species_data = species_response.json()

            # Obtener URL de la cadena evolutiva
            evolution_chain_url = species_data["evolution_chain"]["url"]
            evolution_response = await client.get(evolution_chain_url)
            if evolution_response.status_code != 200:
                return None

            # Procesar la cadena evolutiva
            evolution_data = evolution_response.json()
            chain = evolution_data["chain"]

            def get_evolution_chain(chain):
                evolutions = []
                current = chain
                while current:
                    evolutions.append(current["species"]["name"])
                    current = current["evolves_to"][0] if current["evolves_to"] else None
                return evolutions

            return get_evolution_chain(chain)


    @staticmethod
    async def get_pokemon_details(name_or_id: str) -> Optional[PokemonSchema]:
        """Obtiene los datos de un Pokémon y los mapea al esquema interno."""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{PokemonRepository.BASE_URL}/pokemon/{name_or_id}")
            if response.status_code != 200:
                return None
            data = response.json()

            # Obtener la lista de evoluciones
            species_url = data["species"]["url"]
            evolutions = await PokemonRepository.get_evolution_chain(species_url)

            # Mapeo de datos al esquema interno
            return PokemonSchema(
                id=data["id"],
                name=data["name"],
                height=data["height"],
                weight=data["weight"],
                base_experience=data["base_experience"],
                is_default=data["is_default"],
                location_area_encounters=data["location_area_encounters"],
                abilities=[
                    PokemonAbility(
                        ability={"name": a["ability"]["name"], "url": a["ability"]["url"]},
                        is_hidden=a["is_hidden"],
                        slot=a["slot"]
                    ) for a in data["abilities"]
                ],
                types=[
                    PokemonType(
                        slot=t["slot"],
                        type={"name": t["type"]["name"], "url": t["type"]["url"]}
                    ) for t in data["types"]
                ],
                sprites=PokemonSpritesHome(
                    front_default=data["sprites"]["other"]["home"]["front_default"],
                    front_female=data["sprites"]["other"]["home"].get("front_female"),
                    front_shiny=data["sprites"]["other"]["home"]["front_shiny"],
                    front_shiny_female=data["sprites"]["other"]["home"].get("front_shiny_female")
                ),
                species=PokemonSpecies(
                    name=data["species"]["name"],
                    url=data["species"]["url"]
                ),
                evolutions=evolutions
            )


    @staticmethod
    async def get_pokemon_by_type(type_name: str, page: int, per_page: int) -> Optional[PaginatedPokemonResponse]:
        """Obtiene los Pokémon por tipo con paginación e incluye la imagen."""
        async with httpx.AsyncClient() as client:
            # Obtener los Pokémon del tipo
            response = await client.get(f"{PokemonRepository.BASE_URL}/type/{type_name}")
            #print(response)
            if response.status_code != 200:
                return None

            data = response.json()

            # Extraer la lista completa de Pokémon
            all_pokemons = [
                {"name": p["pokemon"]["name"], "url": p["pokemon"]["url"]}
                for p in data["pokemon"]
            ]

            # Calcular paginación
            total = len(all_pokemons)
            start = (page - 1) * per_page
            end = start + per_page
            paginated_pokemons = all_pokemons[start:end]

            # Obtener la imagen `front_default` para cada Pokémon
            pokemons_with_images = []
            for p in paginated_pokemons:
                pokemon_response = await client.get(p["url"])
                if pokemon_response.status_code == 200:
                    pokemon_data = pokemon_response.json()
                    pokemons_with_images.append({
                        "name": p["name"],
                        "url": p["url"],
                        "image": pokemon_data["sprites"]["other"]["home"].get("front_default")
                    })

            return PaginatedPokemonResponse(
                total=total,
                page=page,
                per_page=per_page,
                pokemons=pokemons_with_images
            )