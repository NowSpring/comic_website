<!-- <template>
  <div>
    <v-container>
      <form @submit.prevent="onSubmit">
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
          v-model="era"
          label="年代"
          required
        ></v-text-field>
        <v-text-field
          v-model="title"
          label="タイトル"
          required
        ></v-text-field>
        <v-text-field
          v-model="title"
          label="タイトル"
          required
        ></v-text-field>
        <v-text-field
          v-model="title"
          label="タイトル"
          required
        ></v-text-field>
      </form>
    </v-container>
  </div>
</template>

<script>
// import axios from 'axios';
export default {
  name: "ComicEditor",
  data() {
    return {
      title: null
    };
  },
  methods: {
    onSubmit() {
      let endpoint = "/api/jobs/";
      let method = "POST";
      if (this.id !== undefined) {
        endpoint += `${this.id}/`;
        method = "PUT";
      }
      apiService(endpoint, method, {
        company_name: this.company_name,
        company_email: this.company_email,
        job_title: this.job_title,
        job_description: this.job_description,
        salary: this.salary,
        prefectures: this.prefectures,
        city: this.city,
      }).then(job_data => {
        this.$router.push({
          name: 'job',
          params: { id: job_data.id }
        })
      })
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
</style> -->
<template>
    <v-icon>
        {{ mdiTwitterSvgPath }}
    </v-icon>
</template>
  
<script>
import { mdiTwitter, mdiGithub } from '@mdi/js'

export default {
data () {
    return {
    mdiTwitterSvgPath: mdiTwitter,
    mdiGithubSvgPath: mdiGithub
    }
}
}
</script>