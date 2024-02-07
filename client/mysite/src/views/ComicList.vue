<template>

    <v-container>
      <div class="d-flex justify-end">
        <div><!-- ダミーの div を入れると右にも寄せられる -->
          <v-btn
            icon
            to="/comic_register"
          >
            <v-icon large>
              mdi-book-plus-outline
            </v-icon>
          </v-btn>
        </div>
      </div>

      <v-row>

        <v-col cols="12">
          <v-text-field
            v-model="searchQuery"
            label="Search"
            append-icon="mdi-mabnify"
            @click:append="search"
          ></v-text-field>
        </v-col>

        <v-col cols="4" v-for="(card, index) in filteredCards" :key="index">
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
                icon
                color="red"
                @click="linkToOtherWindow(card.comic.pdf)"
              >
                <v-icon>
                  mdi-book-open-variant
                </v-icon>
              </v-btn>

              <v-btn
                icon
                color="red"
                v-bind:to = "{
                  name: 'comic_review',
                  query: {title: card.comic.title}
                }
              ">
                <v-icon>
                  mdi-pencil
                </v-icon>
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

                <v-tabs v-model="card.tab" background-color="transparent">
                  <v-tab>Info</v-tab>
                  <v-tab>Review</v-tab>
                </v-tabs>

                <v-card-text>
                  <div v-if="card.tab === 0">
                    <table>
                      <tr>
                        <th :style="{ width: thWidth, textAlign: 'left' }">作品名</th>
                        <td :style="{ width: tdWidth, textAlign: 'left' }">{{ card.comic.title }}</td>
                      </tr>
                      <tr>
                        <th :style="{ width: thWidth, textAlign: 'left' }">作者名</th>
                        <td :style="{ width: tdWidth, textAlign: 'left' }">{{ card.comic.author }}</td>
                      </tr>
                      <tr>
                        <th :style="{ width: thWidth, textAlign: 'left' }">出版年代</th>
                        <td :style="{ width: tdWidth, textAlign: 'left' }">{{ card.comic.era }}</td>
                      </tr>
                      <tr>
                        <th :style="{ width: thWidth, textAlign: 'left' }">出版社</th>
                        <td :style="{ width: tdWidth, textAlign: 'left' }">{{ card.comic.publisher }}</td>
                      </tr>
                      <tr>
                        <th :style="{ width: thWidth, textAlign: 'left' }">対象</th>
                        <td :style="{ width: tdWidth, textAlign: 'left' }">{{ card.comic.target }}</td>
                      </tr>
                      <tr>
                        <th :style="{ width: thWidth, textAlign: 'left' }">ジャンル</th>
                        <td :style="{ width: tdWidth, textAlign: 'left' }">{{ card.comic.genre }}</td>
                      </tr>
                    </table>
                  </div>
                  <div v-if="card.tab === 1">
                    <p>テスト</p>
                  </div>
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
import router from '../router';
export default {
  name: "ComicView",
  mounted() {
    this.checkSignin();
  },
  data() {
    return {
      cards: [],
      comics: [],
      searchQuery: '',
      thWidth: '150px',
      tdWidth: '200px', 
      next: null,
      loadingComics: false,
    };
  },
  computed: {
    filteredCards() {
      if (!this.searchQuery) {
        return this.cards
      }
      return this.cards.filter(card => card.comic.title.includes(this.searchQuery));
    }
  },
  methods: {
    checkSignin() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/signin");
      }
    },
    getComics() {
      axios.get("http://localhost:8000/comics/comics/").then((response) => {
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
          var tab = 0
          card.comic = this.comics[comic]
          card.show = show
          card.tab = tab
          this.cards.push(card)
          // console.log("comic:", this.comics[comic].author)
          // console.log("card:", card)
        }
        console.log("cards:", this.cards)
    },
    linkToOtherWindow(url) {
      window.open(url, '_blank')
    },
    search() {

    },
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