<template>

    <mu-carousel :active="active" interval="4000" transition="fade">
        <mu-icon value="arrow_back" slot="left"></mu-icon>
        <mu-icon value="arrow_forward" slot="right"></mu-icon>
        <template slot="indicator" slot-scope="{ index, active }">
            <mu-button icon class="mu-carousel-indicator-button" :class="{'mu-carousel-indicator-button__active': active}" @click="changeActive(index)">
                <span class="rect-indicator"></span>
            </mu-button>
        </template>
        <!-- <mu-carousel-item>
            <img :src="carouselImg1">
        </mu-carousel-item> -->
        <div class="ima-content">
            <mu-carousel-item>
                <div class="img">
                    <img :src="headPic1" class="img-responsive">
                </div>
            </mu-carousel-item>
            <mu-carousel-item>
                <div class="img">
                    <img :src="headPic2" class="img-responsive">
                </div>

            </mu-carousel-item>
            <mu-carousel-item>
                <div class="img">
                    <img :src="headPic3" class="img-responsive">
                </div>
            </mu-carousel-item>
        </div>
    </mu-carousel>

</template>

<script>

// import headPic1 from "https://muse-ui.org/img/sun.a646a52d.jpg";
import headPic1 from "../assets/headPic1.jpg";
import headPic2 from "../assets/headPic2.jpg";

export default {
  name: "carousel",
  data() {
    return {
      active: 0,
      headPic1,
      headPic2,
      headPic3: "https://muse-ui.org/img/sun.a646a52d.jpg",
    };
  },

  methods: {
    changeActive(index) {
      this.active = index;
    },
    image1(){
        console.log("点击了图1");
        
    },
    image2(){
        console.log("点击了图2");
        
    },
    image3(){
        console.log("点击了图3");
        
    }

  }
};
</script>

<style scoped>
.mu-carousel {
  max-width: 100%;
  height: 250px;
}
.img-responsive {
  /* 图片缩略？ */
  display: inline-block;
  height: auto;
  width: 100%;
  max-width: 100%;
}
.img {
  /* 图片垂直居中 */
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
</style>
