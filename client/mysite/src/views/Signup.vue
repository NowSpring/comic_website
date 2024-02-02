<template>
    <v-container>
        <v-form @submit.prevent="onSubmit">
        <v-text-field label="Username" v-model="username"></v-text-field>
        <v-text-field label="Email" v-model="email"></v-text-field>
        <v-text-field label="Password" type="password" v-model="password"></v-text-field>
        <v-checkbox label="Is Superuser" v-model="isSuperuser"></v-checkbox>
        <v-btn type="submit">Create Account</v-btn>
        </v-form>
    </v-container>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            username: '',
            email: '',
            password: '',
            isSuperuser: false
        };
    },
    methods: {
        async onSubmit() {
            const userData = {
                username: this.username,
                email: this.email,
                password: this.password,
                is_superuser: this.isSuperuser
            };
            try {
                const response = await axios.post('http://localhost:8000/accounts/signup/', userData);
                console.log(response.data);
                this.$router.push({ name: 'signin' });
            } catch (error) {
                console.error("There was an error!", error);
                // エラーが発生した場合の処理
            }
        }
    }
};
</script>
