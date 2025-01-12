from fastapi import APIRouter, HTTPException, Query
from app.bl.habitat_pokemon_bl import HabitatPokemonBL
from app.schema.habitat_pokemon import HabitatPokemonListResponse, HabitatDetailsResponse, Species

router = APIRouter(prefix="/habitat", tags=["Pokemon Habitats"])

@router.get("/", response_model=HabitatPokemonListResponse)
async def get_all_habitats():
    """Obtiene la lista de todos los habitats de Pokémon."""
    try:
        habitats = await HabitatPokemonBL.get_all_habitats()
        return habitats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{name_or_id}", response_model=HabitatDetailsResponse)
async def get_habitat_details(name_or_id: str):
    """Obtiene los detalles de un habitat, incluyendo sus species."""
    try:
        habitat_details = await HabitatPokemonBL.get_habitat_details(name_or_id)
        return habitat_details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{name_or_id}/species", response_model=list[Species])
async def get_species_by_habitat(
    name_or_id: str, page: int = Query(1, ge=1), per_page: int = Query(10, ge=1, le=50)
):
    """
    Obtiene únicamente las especies de Pokémon de un hábitat con paginación.
    """
    try:
        species = await HabitatPokemonBL.get_species_by_habitat(name_or_id, page, per_page)
        return species
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))