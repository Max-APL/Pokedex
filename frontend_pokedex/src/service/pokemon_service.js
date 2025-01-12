import { getPokemon, getPokemonByType } from "../api/pokemon";

// Servicio para obtener un Pokémon por nombre o ID.
export const fetchPokemonDetails = async (nameOrId) => {
  try {
    const pokemon = await getPokemon(nameOrId);
    return pokemon;
  } catch (error) {
    console.error("Error en el servicio de obtener detalles del Pokémon:", error);
    throw error;
  }
};

// Servicio para obtener Pokémon por tipo con paginación.
export const fetchPokemonByType = async (typeName, page = 1, perPage = 10) => {
  try {
    const paginatedPokemons = await getPokemonByType(typeName, page, perPage);
    return paginatedPokemons;
  } catch (error) {
    console.error("Error en el servicio de obtener Pokémon por tipo:", error);
    throw error;
  }
};
