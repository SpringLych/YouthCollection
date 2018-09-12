<template>
  <div class="main">
    <Header></Header>
    <mainpage></mainpage>
  </div>
</template>

<script>
import mainpage from "./MainPage";
import Header from "./Header";

export default {
  name: "Home",
  components: {
    mainpage,
    Header
  },
  data() {
    return {};
  }
};
</script>

<style scoped>
</style>
