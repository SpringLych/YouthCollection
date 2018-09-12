<template>
    <div>
        <swiper loop :auto=false :list="baseList" :index="headerindex"></swiper>
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
      headerindex: 0,
      headerList:[],
      baseList: [
        {
          url: "https://www.baidu.com",
          img:
            "https://ww1.sinaimg.cn/large/663d3650gy1fq66vvsr72j20p00gogo2.jpg",
          title: "送你一朵fua"
        },
        {
          url: "https://www.baidu.com",
          img:
            "https://ww1.sinaimg.cn/large/663d3650gy1fq66vw1k2wj20p00goq7n.jpg",
          title: "送你一辆车"
        },
        {
          url: "https://www.baidu.com",
          img: "https://static.vux.li/demo/5.jpg", // 404
          title: "送你一次旅行",
          fallbackImg:
            "https://ww1.sinaimg.cn/large/663d3650gy1fq66vw50iwj20ff0aaaci.jpg"
        }
      ]
    };
  }
};
</script>

<style lang="less">
// 标题相关
.vux-swiper-desc{
  padding: 0px 50px 12px 13px !important;
  font-size: 18px !important;
  text-align: left;
}
// 
.vux-icon-dot.active{
  background-color: #3295D8 !important;
}
</style>
