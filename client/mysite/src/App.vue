<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-btn
          icon
          to="/"
        >
          <v-icon x-large>
            mdi-book-open-variant
          </v-icon>
        </v-btn>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        v-if="isLoggedIn"
        text
        to="/"
        >
          <span>{{ currentUser.username }}</span>
          <v-icon>mdi-account</v-icon>
      </v-btn>

      <v-btn
        v-if="isLoggedIn"
        target="_blank"
        text
        @click="logout"
      >
        <span class="mr-2">Logout</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",
  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn;
    },
    currentUser() {
      return this.$store.state.user;
    }
  },
  methods: {
    logout() {
      this.$store.commit('logout');
      this.$router.push('/signin');
    }
  }
};
</script>
