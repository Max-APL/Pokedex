import { getAllPokemonTypes } from "./type_pokemon";

// Servicio para obtener todos los tipos de Pokémon.
export const fetchAllPokemonTypes = async () => {
  try {
    const types = await getAllPokemonTypes();
    return types;
  } catch (error) {
    console.error("Error en el servicio de obtener tipos de Pokémon:", error);
    throw error;
  }
};
