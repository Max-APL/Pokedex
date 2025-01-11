from fastapi import APIRouter, HTTPException, Query
from app.bl.pokemon_bl import PokemonBL
from app.schema.pokemon import PokemonSchema, PaginatedPokemonResponse

router = APIRouter(prefix="/pokemon", tags=["Pokemon"])

@router.get("/{name_or_id}", response_model=PokemonSchema)
async def get_pokemon(name_or_id: str):
    """Obtiene los detalles de un Pokémon específico."""
    pokemon = await PokemonBL.get_pokemon(name_or_id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado.")
    return pokemon


@router.get("/type/{type_name}", response_model=PaginatedPokemonResponse)
async def get_pokemon_by_type(
    type_name: str,
    page: int = Query(1, ge=1, description="Número de página"),
    per_page: int = Query(10, ge=1, le=50, description="Cantidad de Pokémon por página")
):
    """Obtiene los Pokémon de un tipo específico con paginación."""
    pokemons = await PokemonBL.get_pokemon_by_type1(type_name, page, per_page)
    if not pokemons:
        raise HTTPException(status_code=404, detail="Tipo no encontrado o sin Pokémon.")
    return pokemons
