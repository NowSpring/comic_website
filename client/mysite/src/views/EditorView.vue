<template>
  <div class="text-center">
    <v-container>
      <v-form @submit.prevent="onSubmit">
        <v-text-field
          v-model="form.title"
          label="タイトル"
          required
        ></v-text-field>
        <v-text-field
          v-model="form.author"
          label="作者名"
          required
        ></v-text-field>
        <v-select
          v-model="form.era"
          :items="items.era"
          label="年代"
          required
        ></v-select>
        <v-select
          v-model="form.publisher"
          :items="items.publisher"
          label="出版社"
          required
        ></v-select>
        <v-select
          v-model="form.target"
          :items="items.target"
          label="対象"
          required
        ></v-select>
        <v-select
          v-model="form.genre"
          :items="items.genre"
          label="ジャンル"
          required
        ></v-select>
        <v-file-input
          v-model="form.cover"
          label="カバー図"
          accept=".png"
          @change="onCoverChange"
        ></v-file-input>
        <v-file-input 
          v-model="form.pdf"
          label="漫画PDF"
          accept=".pdf"
          @change="onPDFChange"
        ></v-file-input>
        <v-btn
          color="success"
          type="submit"
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
      form: {
        title: "",
        author: "",
        era: "",
        publisher: "",
        target: "",
        genre: "",
        cover: null,
        pdf: null,
      },
      items: {
        era: ["1980", "1990", "2000", "2010"],
        publisher: ["エニックス", "学習研究科", "小学館", "少年画報社", "徳間書店", "朝日ソラノマ", "東京三世社", "白泉社", "秋田書店", "竹書房", "芳文社", "角川書店", "講談社", "集英社"],
        target: ["少年", "少女", "女性", "男性"],
        genre: ["4コマ", "SF", "ギャグ", "サスペンス", "スポーツ", "バトル", "ファンタジー", "ホラー", "ラブコメ", "動物", "恋愛", "時代劇"],
      },
    };
  },
  methods: {
    onCoverChange(file) {
      this.form.cover = file;
    },
    onPDFChange(file) {
      this.form.pdf = file;
    },
    async onSubmit() {
      const formData = new FormData();
      formData.append("title", this.form.title);
      formData.append("author", this.form.author);
      formData.append("era", this.form.era);
      formData.append("publisher", this.form.publisher);
      formData.append("target", this.form.target);
      formData.append("genre", this.form.genre);
      formData.append("cover", this.form.cover);
      formData.append("pdf", this.form.pdf);
      let endpoint = "http://localhost:8000/api/comics/";
      await axios.post(endpoint, formData);
      this.$router.push({ name: 'about'});
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
