<template>
  <div id="app">

    <!-- <img src="./assets/logo.png"> -->
    <Page/>
  </div>
</template>

<script>
import Page from "./components/Home";

export default {
  name: "App",
  components: {
    Page
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
a {
  text-decoration: none;
}
</style>
