<template>
    <div class="main">
        <carousel></carousel>
        <mainpage></mainpage>
    </div>
</template>

<script>
import Carousel from "./Carousel";
import mainpage from "./MainPage";

export default {
  name: "Home",
  components: {
    Carousel,
    mainpage
  },
  data() {
    return {};
  }
};
</script>

<style scoped>
</style>
