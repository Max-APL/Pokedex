from fastapi import APIRouter, HTTPException
from app.bl.type_pokemon_bl import TypePokemonBL
from app.schema.type_pokemon import TypePokemonListResponse

router = APIRouter(prefix="/type", tags=["Pokemon Types"])

@router.get("/", response_model=TypePokemonListResponse)
async def get_all_types():
    """Obtiene la lista de todos los tipos de Pokémon."""
    try:
        types = await TypePokemonBL.get_all_types()
        return types
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
