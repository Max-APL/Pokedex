<template>
  <div class="habitat-container">
    <!-- Left Section: Habitats -->
    <div class="habitat-list">
      <v-container>
        <v-row>
          <v-col
            v-for="(habitat, index) in habitats"
            :key="index"
            cols="12" md="6" lg="4"
          >
            <v-card
              @click="selectHabitat(habitat)"
              class="mx-auto habitat-card"
              max-width="300"
              elevation="3"
            >
              <v-img src="@/assets/fondo.png" height="200" class="pokemon-image ml-2 mr-2"></v-img>
              <v-card-title class="text-h6 text-center">
                {{ habitat.name }}
              </v-card-title>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>

    <!-- Right Section: Habitat Details -->
    <div class="habitat-details" v-if="selectedHabitat">
      <v-card class="details-card">
        <v-card-title class="text-h5 text-center">
          {{ selectedHabitat.name }}
        </v-card-title>
        <v-card-text>
          <p><strong>Description:</strong> {{ selectedHabitat.description }}</p>
          <p><strong>Pokémon Species:</strong></p>
          <ul>
            <li v-for="(species, index) in selectedHabitat.species" :key="index">
              {{ species }}
            </li>
          </ul>
        </v-card-text>
      </v-card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {

      habitats: [
        {
          name: "Forest",
          description: "A lush green forest with abundant trees.",
          species: ["Bulbasaur", "Caterpie", "Pidgey"],
        },
        {
          name: "Mountain",
          description: "A rocky mountain with steep cliffs.",
          species: ["Geodude", "Machop", "Onix"],
        },
        {
          name: "Ocean",
          description: "A vast ocean filled with water Pokémon.",
          species: ["Magikarp", "Tentacool", "Lapras"],
        },
      ],
      selectedHabitat: null, // Habitat seleccionado

    };
  },
  created() {

  },
  methods: {
    selectHabitat(habitat) {
      this.selectedHabitat = habitat;
    },
  },
};
</script>

<style scoped>

.details-card {
  border-radius: 12px;
}





.habitat-container {
  display: flex;
  flex-direction: row;
  height: 80vh;
  background-color: rgba(0, 0, 0, 0.8);
  border-radius: 15px;
  padding: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
}

.habitat-list {
  width: 65%;
  padding: 20px;
  overflow-y: auto;
  background-color: rgba(30, 30, 30, 0.9);
  border-radius: 10px;
}

.habitat-card {
  border-radius: 12px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.habitat-card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
}

.habitat-details {
  width: 35%;
  padding: 20px;
  overflow-y: auto;
  background-color: rgba(30, 30, 30, 0.9);
  border-radius: 10px;
}


</style>
