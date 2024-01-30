import Vue from "vue";
import VueRouter from "vue-router";
import Signin from "../views/Signin.vue";
import Signup from "../views/Signup.vue";
import ComicView from "../views/ComicView.vue"
import EditorView from "../views/EditorView.vue";
import TestView from "../views/TestView.vue";

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
    name: "comic",
    component: ComicView,
  },
  {
    path: "/editor",
    name: "editor",
    component: EditorView,
    props: true
  },
  {
    path: "/test",
    name: "test",
    component: TestView,
    props: true
  }
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes,
});

export default router;
