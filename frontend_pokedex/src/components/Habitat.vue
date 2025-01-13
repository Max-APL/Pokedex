<template>
  <div class="habitat-container">
    <!-- Left Section: Habitats -->
    <div class="habitat-list">
      <v-container>
        <v-row>
          <v-col
            v-for="(habitat, index) in habitats.results"
            :key="index"
            cols="12" md="6" lg="4"
          >
            <v-card
              @click="selectHabitat(habitat)"
              class="mx-auto habitat-card"
              max-width="300"
              elevation="3"
            >
              <v-img :src="getHabitatImage(habitat.name)" height="200" class="pokemon-image ml-2 mr-2"></v-img>
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
          Habitat: {{ selectedHabitat.name }}
        </v-card-title>
        <v-card-text>
          <h3>Pokemon Species:</h3>
          <v-container>
            <!-- Species cards displayed as horizontal cards -->
            <v-row dense>
              <v-col
                v-for="(species, index) in speciesList"
                :key="index"
                cols="12"
              >
                <v-card class="species-card">
                  <v-row>
                    <v-col cols="8">
                      <v-card-title class="text-h6">
                        {{ species.name }}
                      </v-card-title>
                    </v-col>
                  </v-row>
                </v-card>
              </v-col>
            </v-row>
            <div ref="speciesListEnd" @scroll="loadMoreSpecies"></div>
          </v-container>
        </v-card-text>
      </v-card>
    </div>
  </div>
</template>

<script>

import forestImage from '@/assets/forest.png';
import caveImage from '@/assets/cave.png';
import grassland from '@/assets/grassland.png';
import mountainImage from '@/assets/mountain.png';
import rareImage from '@/assets/rare.png';
import seaImage from '@/assets/sea.png';
import urbanImage from '@/assets/urban.png';
import roughterrainImage from '@/assets/rough-terrain.png';
import watersedgeImage from '@/assets/waters-edge.png';
import defaultImage from '@/assets/forest.png';

import {
  fetchAllHabitats,
  fetchSpeciesByHabitat,
} from "@/service/habitat_service";

export default {
  data() {
    return {
      habitatImages: {
        forest: forestImage,
        cave: caveImage,
        grassland: grassland,
        mountain: mountainImage,
        rare: rareImage,
        sea: seaImage,
        urban: urbanImage,
        'waters-edge': watersedgeImage,
        'rough-terrain': roughterrainImage
      },
      habitats: [],
      selectedHabitat: null,
      speciesList: [],
      currentPage: 1,
      perPage: 10,
      isLoading: false,
    };
  },
  async created() {
    await this.loadHabitats();
  },
  methods: {
    async loadHabitats() {
      try {
        this.habitats = await fetchAllHabitats();
      } catch (error) {
        console.error("Error al cargar hábitats:", error);
      }
    },
    async selectHabitat(habitat) {
      this.selectedHabitat = habitat;
      this.speciesList = [];
      this.currentPage = 1;
      await this.loadMoreSpecies();
    },
    async loadMoreSpecies() {
      if (this.isLoading || !this.selectedHabitat) return;

      this.isLoading = true;
      try {
        const newSpecies = await fetchSpeciesByHabitat(
          this.selectedHabitat.name,
          this.currentPage,
          this.perPage
        );
        this.speciesList = [...this.speciesList, ...newSpecies];
        this.currentPage++;
      } catch (error) {
        console.error("Error al cargar más especies:", error);
      } finally {
        this.isLoading = false;
      }
    },
    getHabitatImage(habitatName) {
      return this.habitatImages[habitatName] || defaultImage;
    },
  },
  watch: {
    async speciesList() {
      const observer = new IntersectionObserver(async (entries) => {
        if (entries[0].isIntersecting) {
          await this.loadMoreSpecies();
        }
      });
      const speciesListEnd = this.$refs.speciesListEnd;
      if (speciesListEnd) {
        observer.observe(speciesListEnd);
      }
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
.species-card {
  display: flex;
  flex-direction: row;
  border-radius: 12px;
  margin-bottom: 10px;
  padding: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease-in-out;
}
.species-card:hover {
  transform: scale(1.02);
}
</style>
