<template>

    <v-container>
      <div class="d-flex justify-end">
        <div><!-- ダミーの div を入れると右にも寄せられる -->
          <v-btn
            icon
            to="/editor"
          >
            <v-icon large>
              mdi-book-plus-outline
            </v-icon>
          </v-btn>
        </div>
      </div>

      <v-row>
        <v-col cols="4" v-for="(card, index) in cards" :key="index">
          <v-card
            class="mx-auto"
            max-width="344"
          >
            <v-img
              :src=card.comic.cover
              height="200px"
              cover
            ></v-img>

            <v-card-title>
              {{ card.comic.title }}
            </v-card-title>

            <v-card-subtitle>
              {{ card.comic.author }}
            </v-card-subtitle>

            <v-card-actions>
              <v-btn
                color="orange-lighten-2"
                variant="text"
                @click="linkToOtherWindow(card.comic.pdf)"
              >
                Read
              </v-btn>

              <v-spacer></v-spacer>

              <v-btn icon>
                <v-icon
                  v-if="card.show" 
                  @click="card.show = !card.show"
                >mdi-chevron-up</v-icon>
                <v-icon
                  v-else
                  @click="card.show = !card.show"
                >mdi-chevron-down</v-icon>
              </v-btn>
            </v-card-actions>

            <v-expand-transition>
              <div v-show="card.show">
                <v-divider></v-divider>

                <!-- <v-tabs v-model="infos">
                  <v-tab value="info">Info</v-tab>
                  <v-tab value="review">Review</v-tab>
                </v-tabs> -->

                <v-card-text>
                  <v-row>
                    <v-col cols="6">テスト</v-col>
                    <v-col cols="6">テスト</v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="6">テスト</v-col>
                    <v-col cols="6">テスト</v-col>
                  </v-row>
                  <!-- <v-window v-model="infos">
                    <v-window-item value="info">
                        info test
                    </v-window-item>

                    <v-window-item value="review">
                      review test
                    </v-window-item>
                  </v-window> -->
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
      cards: [],
      comics: [],
      next: null,
      loadingComics: false,
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
        this.createCards();
      })
    },
    createCards() {
      for(var comic in this.comics){
          var card = {}
          var show = false
          card.comic = this.comics[comic]
          card.show = show
          this.cards.push(card)
          // console.log("comic:", this.comics[comic].author)
          // console.log("card:", card)
        }
        console.log("cards:", this.cards)
    },
    linkToOtherWindow(url) {
      window.open(url, '_blank')
    }
  },
  created() {
    this.getComics();
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