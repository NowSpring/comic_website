import Vue from "vue";
import App from "./App.vue";
import store from './store';
import router from "./router";
import vuetify from "./plugins/vuetify";
import VueSession from 'vue-session'
import vSelect from 'vue-select' 
import '@mdi/font/css/materialdesignicons.css' // この行を追加


Vue.use(VueSession)
Vue.component('v-select', vSelect) 
Vue.config.productionTip = false;

new Vue({
  store,
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");