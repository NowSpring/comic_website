<template>
    <v-container>
        <h1>{{ title }} Review</h1>
        <v-row>
            <v-col cols="3">
                <v-img 
                    v-bind:src="cover"
                    class="image-style"
                    aspect-ratio="1"
                ></v-img>
            </v-col>

            <v-col>
                <v-form @submit.prevent="onSubmit">
                
                </v-form>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
// import axios from 'axios';
export default {
    data() {
        return {
            title: this.$route.params.title,
            cover: this.$route.params.cover,
            form: {
                
            }
        };
    },
    methods: {
        onSubmit() {

        }
    },

};
</script>
<style>
.image-style {
  max-width: 100%;
  height: auto;
}
</style>