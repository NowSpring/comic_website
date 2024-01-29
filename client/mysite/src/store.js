import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// Vuexインスタンス生成
export default new Vuex.Store({
  // state: Vuexで管理する状態を定義
  state: {
    isLoggedIn: false,
  },
  mutations: {
    login(state) {
        state.isLoggedIn = true;
    },
    logout(state) {
        state.isLoggedIn = false;
    }
  },
})