import Vue from "vue";
import Router from "vue-router";
import Jogos from "../components/Jogos.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "jogos",
      component: Jogos
    }
  ]
});