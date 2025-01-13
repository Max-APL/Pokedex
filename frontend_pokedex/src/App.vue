<template>
  <div class="app-container">
    <h1 class="header">Pokedex</h1>

    <v-tabs fixed-tabs class="tabs" v-model="tab">
      <v-tab value="Pokemon">Pokemon</v-tab>
      <v-tab value="Habitat">Habitat</v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab">
      <v-tabs-window-item value="Pokemon">
        <Pokemon></Pokemon>
      </v-tabs-window-item>

      <v-tabs-window-item value="Habitat">
        <Habitat></Habitat>
      </v-tabs-window-item>
    </v-tabs-window>



  </div>

</template>

<script>
import Pokemon from "@/components/Pokemon.vue";
import Habitat from "@/components/Habitat.vue";

export default {
  components: {
    Pokemon,
    Habitat,
  },
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
</style>

