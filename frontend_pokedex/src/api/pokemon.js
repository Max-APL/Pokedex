import axios from "axios";

const API_BASE_URL = "http://localhost:8000/pokemon"; // Reemplaza con la URL base de tu backend si es diferente.

export const getPokemon = async (nameOrId) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/${nameOrId}`);
    return response.data;
  } catch (error) {
    console.error("Error al obtener el Pokémon:", error);
    throw error;
  }
};

export const getPokemonByType = async (typeName, page = 1, perPage = 10) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/type/${typeName}`, {
      params: {
        page,
        per_page: perPage,
      },
    });
    return response.data;
  } catch (error) {
    console.error("Error al obtener Pokémon por tipo:", error);
    throw error;
  }
};
