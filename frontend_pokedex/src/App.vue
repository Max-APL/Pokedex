<template>
  <div class="app-container">
    <h1 class="header">Pokedex</h1>

    <v-tabs fixed-tabs class="tabs" v-model="tab">
      <v-tab value="Pokemon">Pokemon</v-tab>
      <v-tab value="Habitat">Habitat</v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab">
      <v-tabs-window-item value="Pokemon">
        <div class="pokemon-container">
          <!-- Sidebar: Types -->
          <div class="sidebar">
            <v-list dense>
              <v-list-item
                v-for="(type, index) in types"
                :key="index"
                @click="filterByType(type)"
                :class="{'type-item-selected': selectedType === type, 'type-item': selectedType !== type}"
              >
                {{ type }}
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
            <v-container>
              <v-row>
                <v-col
                  v-for="(pokemon, index) in filteredPokemon"
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
          </div>

          <!-- Right Section: Pokemon Details -->
          <div class="pokemon-details" v-if="selectedPokemon">
            <v-card class="details-card">
              <v-card-title class="text-h5 text-center">
                {{ selectedPokemon.name }}
              </v-card-title>
              <v-img :src="selectedPokemon.image" height="200"></v-img>
              <v-card-text>
                <p><strong>Type:</strong> {{ selectedPokemon.type }}</p>
                <p><strong>Abilities:</strong> {{ selectedPokemon.abilities.join(', ') }}</p>
                <p><strong>Height:</strong> {{ selectedPokemon.height }}</p>
                <p><strong>Weight:</strong> {{ selectedPokemon.weight }}</p>
              </v-card-text>
            </v-card>
          </div>
        </div>
      </v-tabs-window-item>

      <v-tabs-window-item value="Habitat">
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
      </v-tabs-window-item>
    </v-tabs-window>



  </div>

</template>

<script>
export default {
  data() {
    return {
      tab: null,
      types: [
        "Fire", "Water", "Grass", "Electric", "Ice", "Rock", "Ground", "Flying",
        "Psychic", "Bug", "Dark", "Fairy", "Steel", "Fighting", "Ghost", "Dragon",
        "Poison", "Normal"
      ],
      pokemonList: [
        {
          name: "Charmander",
          type: "Fire",
          abilities: ["Blaze"],
          height: "0.6 m",
          weight: "8.5 kg",
          image: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
        },
        {
          name: "Bulbasaur",
          type: "Grass",
          abilities: ["Overgrow"],
          height: "0.7 m",
          weight: "6.9 kg",
          image: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
        },
        {
          name: "Pikachu",
          type: "Electric",
          abilities: ["Static"],
          height: "0.4 m",
          weight: "6.0 kg",
          image: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        },
      ],
      filteredPokemon: [],
      selectedPokemon: null,
      selectedType: "",
      searchQuery: "",

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
    this.selectedType = this.types[0]; // Set the first type as default
    this.filterByType(this.selectedType);
  },
  methods: {
    selectHabitat(habitat) {
      this.selectedHabitat = habitat;
    },
    filterByType(type) {
      this.selectedType = type;
      this.filteredPokemon = this.pokemonList.filter((pokemon) => pokemon.type === type);
    },
    selectPokemon(pokemon) {
      this.selectedPokemon = pokemon;
    },
    searchPokemon() {
      // Placeholder for search logic
      console.log(`Searching for Pokémon: ${this.searchQuery}`);
    },
  },
};
</script>

<style scoped>
.app-container {
  background-image: url("@/assets/fondo.png");
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  min-height: 100vh;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.header {
  text-align: center;
  font-size: 3rem;
  color: #ffcc00;
  text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.8);
}

.tabs {
  background-color: rgba(0, 0, 0, 0.8);
  border-radius: 10px;
  color: #fff;
}

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
  background-color: rgba(255, 255, 255, 0.95);
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
  background-color: rgba(255, 255, 255, 0.95);
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
  background-color: rgba(255, 255, 255, 0.95);
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

.details-card {
  background-color: rgba(255, 255, 255, 0.95);
  border-radius: 12px;
}


</style>
