<template>
    <v-container grid-list-md>
        <v-layout row wrap align-center justify-center fill-height>
            <v-flex xs12 sm8 lg4 md5>
                <v-card class="login-card">

                    <v-card-title>
                        <span class="headline">Signin</span>
                    </v-card-title>

                    <v-spacer/>

                    <v-card-text>

                        <v-layout row fill-height justify-center align-center v-if="loading">
                            <v-progress-circular :size="50" color="primary" indeterminate/>
                        </v-layout>

                        <v-form v-else ref="form" v-model="valid" lazy-validation>
                            <v-container>
                                <v-text-field v-model="credentials.username" :counter="70" label="ユーザー名" :rules="rules.username" maxlength="70" required/>
                                <v-text-field type="password" v-model="credentials.password" :counter="20" label="パスワード" :rules="rules.password" maxlength="20" required/>
                                <v-btn class="pink white--text" :disabled="!valid" @click="signin">Signin</v-btn>
                                <v-btn to="/signup">Signup</v-btn>
                            </v-container>
                        </v-form>

                    </v-card-text>

                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2';
// import router from '../router';
export default {
    name: 'Signin',
    data: () => ({
        credentials: {},
        valid:true,
        loading:false,
        rules: {
            username: [v => !!v || "ユーザー名は必須です"],
            password: [v => !!v || "パスワードは必須です"]
        }
    }),
    methods: {
        signin() {
            if (this.$refs.form.validate()) {
                this.loading = true;
                axios.post('http://localhost:8000/signin/', this.credentials).then(res => {
                    this.$store.commit('setUser', res.data.user);
                    this.$session.start();
                    this.$session.set('token', res.data.token);
                    this.$router.push({ name: 'comic_list' });
                // eslint-disable-next-line
                }).catch(e => {
                    this.loading = false;
                    Swal.fire({
                    type: 'warning',
                    title: 'Error',
                    text: 'ユーザー名もしくはパスワード、または両方が間違っています',
                    showConfirmButton:false,
                    showCloseButton:false,
                    timer:3000
                    })
                })
            }
        }
    }
}
</script>