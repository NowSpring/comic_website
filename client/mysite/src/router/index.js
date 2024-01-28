import Vue from "vue";
import VueRouter from "vue-router";
import Signin from "../views/Signin.vue";
import HomeView from "../views/HomeView.vue";
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
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
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
