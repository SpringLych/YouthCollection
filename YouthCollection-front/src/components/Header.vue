<template>
  <div>
    <swiper loop auto :list="baseList" :index="headerindex"></swiper>
  </div>
</template>

<script>
import { Swiper, SwiperItem } from "vux";

export default {
  name: "Header",
  components: {
    Swiper,
    SwiperItem
  },
  data() {
    return {
      baseUrl: "http://127.0.0.1:8000/collection/get_head_article/",

      headerindex: 0,
      headerList: [],
      baseList: []
    };
  },
  mounted() {
    this.$nextTick(function() {
      // Code that will run only after the
      // entire view has been rendered
      this.getHeadArt();
    });
  },
  methods: {
    getHeadArt() {
      this.$http({
        method: "GET",
        url: this.baseUrl,
        headers: {
          // "Access-Control-Allow-Origin": "*",
          // "Access-Control-Allow-Headers": "origin, content-type, accept",
          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
      }).then(response => {
        this.baseList = response.data;
      });
    }
  }
};
</script>

<style lang="less">
// 标题相关
.vux-swiper-desc {
  padding: 0px 50px 12px 13px !important;
  font-size: 18px !important;
  text-align: left;
}
//
.vux-icon-dot.active {
  background-color: #3295d8 !important;
}
</style>
