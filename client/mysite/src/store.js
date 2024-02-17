import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// Vuexインスタンス生成
export default new Vuex.Store({
  // state: Vuexで管理する状態を定義
  state: {
    user: null,
    isLoggedIn: false,
    reviews: []
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
      state.isLoggedIn = true;
    },
    logout(state) {
      state.user = null;
      state.isLoggedIn = false;
    },
  },
})