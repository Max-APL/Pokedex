import axios from "axios";

const API_BASE_URL = "http://localhost:8000/habitat"; // Reemplaza con la URL base de tu backend si es diferente.

// Obtener todos los hábitats
export const getAllHabitats = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/`);
    return response.data;
  } catch (error) {
    console.error("Error al obtener los hábitats:", error);
    throw error;
  }
};

// Obtener detalles de un hábitat por nombre o ID
export const getHabitatDetails = async (nameOrId) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/${nameOrId}`);
    return response.data;
  } catch (error) {
    console.error("Error al obtener los detalles del hábitat:", error);
    throw error;
  }
};

// Obtener especies de un hábitat con paginación
export const getSpeciesByHabitat = async (nameOrId, page = 1, perPage = 10) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/${nameOrId}/species`, {
      params: {
        page,
        per_page: perPage,
      },
    });
    return response.data;
  } catch (error) {
    console.error("Error al obtener las especies del hábitat:", error);
    throw error;
  }
};
