<template>
    <div class="main">
        <!-- <carousel></carousel> -->
        <Header></Header>
        <mainpage></mainpage>
    </div>
</template>

<script>
import Carousel from "./Carousel";
import mainpage from "./MainPage";
import Header from "./Header";

export default {
  name: "Home",
  components: {
    Carousel,
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
