import Vue from "vue";
import VueRouter from "vue-router";
import Signin from "../views/Signin.vue";
import Signup from "../views/Signup.vue";
import ComicList from "../views/ComicList.vue";
import ComicReview from "../views/ComicReview.vue";
import ComicRegister from "../views/ComicRegister.vue";
import Test from "../views/Test.vue";
import store from "@/store";

Vue.use(VueRouter);

const routes = [
  {
    path: "/signin",
    name: "signin",
    component: Signin,
  },
  {
    path: "/signup",
    name: "signup",
    component: Signup,
  },
  {
    path: "/",
    name: "comic_list",
    component: ComicList,
    beforeEnter: (to, from, next) => {
      if (!store.state.isLoggedIn) {
        next('/signin')
      } else {
        next()
      }
    }
  },
  {
    path: "/comic_review/:title",
    name: "comic_review",
    component: ComicReview,
    props: true
  },
  {
    path: "/comic_register",
    name: "comic_register",
    component: ComicRegister,
    props: true
  },
  {
    path: "/test",
    name: "test",
    component: Test,
    props: true
  }
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes,
});

export default router;
