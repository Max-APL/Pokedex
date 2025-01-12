import { getAllHabitats, getHabitatDetails, getSpeciesByHabitat } from "../api/habitat";

// Servicio para obtener todos los hábitats
export const fetchAllHabitats = async () => {
  try {
    const habitats = await getAllHabitats();
    return habitats;
  } catch (error) {
    console.error("Error en el servicio al obtener todos los hábitats:", error);
    throw error;
  }
};

// Servicio para obtener detalles de un hábitat por nombre o ID
export const fetchHabitatDetails = async (nameOrId) => {
  try {
    const habitatDetails = await getHabitatDetails(nameOrId);
    return habitatDetails;
  } catch (error) {
    console.error("Error en el servicio al obtener detalles del hábitat:", error);
    throw error;
  }
};

// Servicio para obtener especies de un hábitat con paginación
export const fetchSpeciesByHabitat = async (nameOrId, page = 1, perPage = 10) => {
  try {
    const speciesList = await getSpeciesByHabitat(nameOrId, page, perPage);
    return speciesList;
  } catch (error) {
    console.error("Error en el servicio al obtener especies del hábitat:", error);
    throw error;
  }
};
