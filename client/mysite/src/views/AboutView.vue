<template>

    <v-container>
      <div class="d-flex justify-end">
        <div><!-- ダミーの div を入れると右にも寄せられる -->
          <v-btn
            color="orange-lighten-2"
            variant="text"
            class="column-button"
            to="/editor"
          >
            +
          </v-btn>
        </div>
      </div>

      <v-row>
        <v-col cols="4" v-for="comic in comics" :key="comic.pk">
          <v-card
            class="mx-auto"
            max-width="344"
          >
            <v-img
              :src=comic.cover
              height="200px"
              cover
            ></v-img>

            <v-card-title>
              {{ comic.title }}
            </v-card-title>

            <v-card-subtitle>
              {{ comic.author}}
            </v-card-subtitle>

            <v-card-actions>
              <v-btn
                color="orange-lighten-2"
                variant="text"
                @click="linkToOtherWindow(comic.pdf)"
              >
                Read
              </v-btn>

              <v-spacer></v-spacer>

              <v-btn
                :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'"
                @click="show = !show"
              ></v-btn>
            </v-card-actions>

            <v-expand-transition>
              <div v-show="show">
                <v-divider></v-divider>

                <v-card-text>
                  I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
                </v-card-text>
              </div>
            </v-expand-transition>
          </v-card>
        </v-col>
      </v-row>
      <!-- <div class="my-4">
        <p v-show="loadingComics">...loading...</p>
        <v-btn v-show="next" @click="getComics" color="success"
          >Load More
        </v-btn>
      </div> -->
    </v-container>
</template>

<script>
import axios from 'axios';
import router from "../router";
export default {
  name: "ComicView",
  mounted() {
    this.checkSignin();
  },
  data() {
    return {
      comics: [],
      next: null,
      loadingComics: false,
      show: false,
    };
  },
  methods: {
    checkSignin() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/signin");
      }
    },
    getComics() {
      axios.get("http://localhost:8000/api/comics/").then((response) => {
        // console.log("status:",response.status)
        // console.log("axiosGetData:",response.data)
        this.comics.push(...response.data.results);
        console.log("comics:", this.comics);
      })
    },
    linkToOtherWindow(url) {
      window.open(url, '_blank')
    }
  },
  created() {
    this.getComics();
    console.log(this.comics);
    document.title = "Comic Board";
  },
};
</script>

<style>
.column-button {
  padding: 8px 20px;
  border: solid 2px #ddd;
  border-radius: 10px;
  font-size: 16px;

  &:nth-child(n+2) {
    margin-top: 20px;
  }
}
</style>