from fastapi import FastAPI
from app.api import pokemon, type_pokemon, habitat_pokemon
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="Pokédex API")





# Configuración del middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las orígenes. Puedes especificar una lista de orígenes permitidos.
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.). Puedes especificar una lista de métodos permitidos.
    allow_headers=["*"],  # Permite todos los headers. Puedes especificar una lista de headers permitidos.
)



app.include_router(pokemon.router)
app.include_router(type_pokemon.router)
app.include_router(habitat_pokemon.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
