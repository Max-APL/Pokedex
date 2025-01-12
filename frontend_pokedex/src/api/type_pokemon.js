import axios from "axios";

const API_BASE_URL = "http://localhost:8000/type"; // Reemplaza con la URL base de tu backend si es diferente.

export const getAllPokemonTypes = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/`);
    return response.data;
  } catch (error) {
    console.error("Error al obtener la lista de tipos de Pokémon:", error);
    throw error;
  }
};
