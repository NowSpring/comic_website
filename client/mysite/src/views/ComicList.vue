<template>

    <v-container>
      <div class="d-flex justify-end">
        <div><!-- ダミーの div を入れると右にも寄せられる -->
          <v-btn icon to="/comic_register">
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
          <v-card class="mx-auto" max-width="344">
            <v-img :src=card.comic.cover height="200px" cover></v-img>

            <v-card-title>
              {{ card.comic.title }}
            </v-card-title>

            <v-card-subtitle>
              {{ card.comic.author }}
            </v-card-subtitle>

            <v-card-actions>
              <v-btn icon @click="linkToOtherWindow(card.comic.pdf)">
                <v-icon color="green">
                  mdi-book-open-variant
                </v-icon>
              </v-btn>

              <v-btn icon @click="reviewComic(card.comic)">
                <v-icon color="green">
                  mdi-pencil
                </v-icon>
              </v-btn>

              <v-btn icon @click="toggleFavorite(card, card.review.isfavorite)">
                <v-icon v-if="card.review.isfavorite" color="green">mdi-star</v-icon>
                <v-icon v-else>mdi-star</v-icon>
              </v-btn>

              <v-spacer></v-spacer>

              <v-btn icon>
                <v-icon v-if="card.show" @click="card.show = !card.show">mdi-chevron-up</v-icon>
                <v-icon v-else @click="card.show = !card.show">mdi-chevron-down</v-icon>
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
      reviews: [],
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
    },
  },
  methods: {
    checkSignin() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/signin");
      }
    },
    getComics() {
      return axios.get("http://localhost:8000/api/comics/").then((response) => {
        this.comics.push(...response.data.results);
        console.log("comics:", this.comics);
      })
    },
    getReviews() {
      return axios.get(`http://localhost:8000/api/reviews/?user=${this.$store.state.user.id}`).then((response) => {
        this.reviews.push(...response.data.results);
        console.log("reviews:", this.reviews);
      })
    },
    toggleFavorite(card, review) {
      card.isfavorite = !card.isfavorite;
      review.isfavorite = card.isfavorite;
      this.updateReview(review);
    },
    updateReview(review) {
      axios.put(`http://localhost:8000/api/reviews/${review.id}`, {
        isfavorite: review.isfavorite,
        // 他の必要なフィールドもここに含めるかもしれません
      }).then(response => {
        console.log("Review updated successfully", response.data);
      }).catch(error => {
        console.error("Error updating review", error);
      });
    },
    createCards() {
      this.cards = this.comics.map(comic => {
        const review = this.reviews.find(r => r.comic === comic.id);
        
        return {
          comic: comic,
          show: false, 
          tab: 0, 
          review: review, 
        };
      });
      console.log("cards:", this.cards);
    },
    linkToOtherWindow(url) {
      window.open(url, '_blank')
    },
    search() {

    },
    reviewComic(comic) {
      this.$router.push({ 
        name: 'comic_review', 
        params: { 
          id: comic.id,
          title: comic.title,
          cover: comic.cover,
        } 
      });
    }
  },
  async created() {
    await Promise.all([this.getComics(),this.getReviews()]);
    this.createCards();
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