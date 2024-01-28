<template>
  <div class="text-center">
    <v-container>
      <v-form>
        <v-text-field
          v-model="title"
          label="タイトル"
          required
        ></v-text-field>
        <v-text-field
          v-model="author"
          label="作者名"
          required
        ></v-text-field>
        <v-select
          :items="era"
          label="年代"
          required
        ></v-select>
        <v-select
          :items="publisher"
          label="出版社"
          required
        ></v-select>
        <v-select
          :items="target"
          label="対象"
          required
        ></v-select>
        <v-select
          :items="genre"
          label="ジャンル"
          required
        ></v-select>
        <v-file-input label="カバー図" v-model="cover" accept=".png"
        ></v-file-input>
        <v-file-input label="漫画PDF" v-model="pdf" accept=".pdf"
        ></v-file-input>

        <v-btn
          color="success"
          type="submit"
          @click="onSubmit()"
        >登録
        </v-btn>
      </v-form>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "ComicEditor",
  data() {
    return {
      title: null,
      author: null,
      era: ["1980", "1990", "2000", "2010"],
      publisher: ["エニックス", "学習研究科", "小学館", "少年画報社", "徳間書店", "朝日ソラノマ", "東京三世社", "白泉社", "秋田書店", "竹書房", "芳文社", "角川書店", "講談社", "集英社"],
      target: ["少年", "少女", "女性", "男性"],
      genre: ["4コマ", "SF", "ギャグ", "サスペンス", "スポーツ", "バトル", "ファンタジー", "ホラー", "ラブコメ", "動物", "恋愛", "時代劇"],
      cover: null,
      pdf: null
    };
  },
  methods: {
    onSubmit() {
      let endpoint = "http://localhost:8000/api/comics/";
      axios.post(endpoint, {
        "title":this.title,
        "author": this.author,
        "era": this.era,
        "publisher": this.publisher,
        "target": this.target,
        "genre": this.genre,
        "cover": this.cover,
        "pdf": this.pdf
      }).then(response => {
        console.log(
          "body:", response.body
        )
      })
    },
  }
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
