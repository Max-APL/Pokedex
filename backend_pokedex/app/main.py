from fastapi import FastAPI
from app.api import pokemon, type_pokemon

app = FastAPI(title="Pokédex API")

app.include_router(pokemon.router)
app.include_router(type_pokemon.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
