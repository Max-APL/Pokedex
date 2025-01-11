from fastapi import APIRouter, HTTPException
from app.bl.habitat_pokemon_bl import HabitatPokemonBL
from app.schema.habitat_pokemon import HabitatPokemonListResponse

router = APIRouter(prefix="/habitat", tags=["Pokemon Habitats"])

@router.get("/", response_model=HabitatPokemonListResponse)
async def get_all_habitats():
    """Obtiene la lista de todos los habitats de Pokémon."""
    try:
        habitats = await HabitatPokemonBL.get_all_habitats()
        return habitats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
