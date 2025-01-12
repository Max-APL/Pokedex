<template>
  <div class="pokemon-container">
    <!-- Sidebar: Types -->
    <div class="sidebar">

      <v-list dense>
        <h3 style="text-align: center">Types of Pokemon</h3>
        <v-list-item
          v-for="(type, index) in types.results"
          :key="index"

          @click="filterByType(type)"
          :class="{'type-item-selected': selectedType === type.name, 'type-item': selectedType !== type.name}"
        >
          {{ type.name }}
        </v-list-item>
      </v-list>
    </div>

    <!-- Middle Section: Pokemon List -->
    <div class="pokemon-list">
      <!-- Search Bar -->
      <div class="search-bar">
        <v-text-field
          placeholder="Search Pokémon..."
          dense
          solo
          hide-details
          clearable
          v-model="searchQuery"
        ></v-text-field>
        <v-btn
          icon
          color="primary"
          class="search-btn"
          @click="searchPokemon"
        >
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </div>

      <!-- Pokémon Cards -->
      <h3>Type: {{ selectedType }}</h3>

    <v-container>
        <v-row>
          <v-col
            v-for="(pokemon, index) in pokemons"
            :key="index"
            cols="12" md="6" lg="4"
          >
            <v-card
              @click="selectPokemon(pokemon)"
              class="mx-auto pokemon-card"
              max-width="300"
              elevation="3"
            >
              <v-img :src="pokemon.image" height="200" class="pokemon-image"></v-img>
              <v-card-title class="text-h6 text-center">
                {{ pokemon.name }}
              </v-card-title>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
      <!-- Pagination Controls -->
      <div class="pagination-controls" style="text-align: center">
        <v-btn :disabled="currentPage === 1" @click="loadPreviousPage" color="" size="35">
          <
        </v-btn>
        <span class="ml-2 mr-2">Pág. {{ currentPage }} de {{ totalPages }}</span>
        <v-btn :disabled="currentPage === totalPages" @click="loadNextPage" color="" size="35">
          >
        </v-btn>
      </div>
    </div>

    <!-- Right Section: Pokemon Details -->
    <div class="pokemon-details" v-if="selectedPokemon">
      <v-card class="details-card">
        <v-card-title class="text-h5 text-center">
          {{ selectedPokemon.name }}
        </v-card-title>
        <v-img :src="selectedPokemon.sprites.front_default" height="200"></v-img>
        <v-card-text>
          <p><strong>Type:</strong> {{ }}</p>
          <p><strong>Abilities:</strong> {{  }}</p>
          <p><strong>Height:</strong> {{  }}</p>
          <p><strong>Weight:</strong> {{  }}</p>
        </v-card-text>
      </v-card>
    </div>
  </div>
</template>

<script>
import { fetchPokemonByType, fetchPokemonDetails } from "@/service/pokemon_service.js";
import { getAllPokemonTypes } from "@/api/type_pokemon.js";

export default {
  data() {
    return {
      tab: null,
      types: [],
      pokemons: [],
      currentPage: 1,
      perPage: 6,
      totalPages: 1,
      selectedPokemon: null,
      selectedType: "",
      searchQuery: "",

    };
  },
  async created() {
    await this.loadTypesPokemon();
    this.selectedType = this.types.results[0];
    //this.loadPokemons();
    this.filterByType(this.selectedType);
  },
  methods: {
    async filterByType(type) {

      this.selectedType = type.name;
      console.log(this.selectedType);
      this.currentPage = 1; // Reiniciar a la primera página al cambiar de tipo
      await this.loadPokemons();
    },
    async loadPokemons() {
      try {
        const response = await fetchPokemonByType(
          this.selectedType,
          this.currentPage,
          this.perPage
        );

        // Actualizar datos con la respuesta del endpoint
        this.pokemons = response.pokemons;
        this.totalPages = Math.ceil(response.total / this.perPage); // Calcular el total de páginas
      } catch (error) {
        console.error("Error al cargar Pokémon:", error);
      }
    },
    async loadNextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
        await this.loadPokemons();
      }
    },
    async loadPreviousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
        await this.loadPokemons();
      }
    },
    viewPokemonDetails(pokemon) {
      alert(`Details of ${pokemon.name}: ${pokemon.url}`);
    },




    async getDetailsPokemon(pokemon_name) {
      console.log("NAME:" + pokemon_name);
      try {
        const response = await fetchPokemonDetails(pokemon_name);
        console.log(response);
        return response;
      } catch (error) {
        console.error("Error al cargar detalles del Pokémon:", error);
        return null;
      }
    },


    async loadTypesPokemon() {
      try {
        const response = await getAllPokemonTypes();
        this.types = response;
        console.log("Tipos de Pokémon cargados:", response);
      } catch (error) {
        console.error("Error al cargar tipos de Pokémon:", error);
      }
    },





    selectHabitat(habitat) {
      this.selectedHabitat = habitat;
    },
    selectPokemon(pokemon) {


      this.getDetailsPokemon(pokemon.name).then((response) => {
        this.selectedPokemon = response;
      });

    },
    searchPokemon() {
      // Placeholder for search logic
      console.log(`Searching for Pokémon: ${this.searchQuery}`);
      this.getDetailsPokemon(this.searchQuery).then((response) => {
        this.selectedPokemon = response;
      });


    },
  },
};
</script>

<style>

.pokemon-container {
  display: flex;
  flex-direction: row;
  height: 80vh;
  background-color: rgba(0, 0, 0, 0.8);
  border-radius: 15px;
  padding: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
}

.sidebar {
  width: 20%;
  padding: 10px;
  overflow-y: auto;
  max-height: 100%;
  background-color: rgba(30, 30, 30, 0.9);
  border-radius: 10px;
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
}

.type-item {
  margin: 5px 0;
  padding: 5px;
  background-color: rgba(50, 50, 50, 0.9);
  color: #fff;
  border-radius: 8px;
  text-align: center;
  font-size: 0.8rem;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.type-item-selected {
  background-color: #ffcc00;
  color: #000;
}

.type-item:hover {
  background-color: #ffaa00;
  color: #000;
}

.search-bar {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  gap: 10px;
}

.search-btn {
  height: 36px;
  width: 36px;
}

.pokemon-list {
  width: 50%;
  padding: 20px;
  overflow-y: auto;
  background-color: rgba(30, 30, 30, 0.9);
  border-radius: 10px;
}

.pokemon-card {
  border-radius: 12px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.pokemon-card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
}

.pokemon-details {
  width: 30%;
  padding: 20px;
  overflow-y: auto;
  background-color: rgba(30, 30, 30, 0.9);
  border-radius: 10px;
}

.details-card {
  border-radius: 12px;
}





</style>
