<template>
  <div class="hello">
    <div style="height:100%;">
      <tab active-color='#3295D8' v-model="index">
        <!-- <tab-item v-for="(item,index) in tabItem" :key="index" :selected="itemselect===item.title" @click="itemselect=item.title" @on-item-click="handler(item.title)">{{item.title}}</tab-item> -->
        <tab-item selected @on-item-click="getArticles(index0.data)">{{index0.title}}</tab-item>
        <tab-item @on-item-click="getArticles(index1.data)">{{index1.title}}</tab-item>
        <tab-item>{{index2.title}}</tab-item>
        <tab-item>{{index3.title}}</tab-item>
        <tab-item>{{index4.title}}</tab-item>
        <tab-item @on-item-click="getArticles(index5.data)">{{index5.title}}</tab-item>
        <tab-item>{{index6.title}}</tab-item>
      </tab>

      <view-box ref="viewBox" v-model="index">
        <div v-if="index===0">
          <panel :list="list" :type="type" :footer="footer"></panel>
        </div>
        <div v-if="index===1">
          <panel :list="index1.articles" :type="type" :footer="footer"></panel>
        </div>
        <div v-if="index===2">
          <panel :list="index2.articles" :type="type" :footer="footer"></panel>
        </div>
        <div v-if="index===3">
          <panel :list="index3.articles" :type="type" :footer="footer"></panel>
        </div>
        <div v-if="index===4">
          <panel :list="index4.articles" :type="type" :footer="footer"></panel>
        </div>
        <div v-if="index===5">
          <panel :list="list" :type="type" :footer="footer"></panel>
        </div>
        <div v-if="index===6">
          <!-- <simplelist v-for="item of index6.articles" :key="item.id" :img_name="item.img_name" :address="item.address" :title="item.title" :introduction="item.introduction">
          </simplelist> -->
          <panel :list="index6.articles" :type="type" :footer="footer"></panel>
        </div>
      </view-box>
    </div>

  </div>
</template>

<script>
// import list from "./List";
// import simplelist from "./SimpleList";
import carousel from "./Carousel";
import menud from "./MenuD";

import { Tab, TabItem, Swiper, SwiperItem, ViewBox, Panel } from "vux";

export default {
  name: "MainPage",
  components: {
    // list,
    // simplelist,
    // carousel,
    menud,
    Tab,
    TabItem,
    Swiper,
    SwiperItem,
    ViewBox,
    Panel,
  },
  data() {
    return {
      active2: 0,
      data: "",
      type: '1', // pannel类型
      // 栏目名称
      index2: {
        title: "美人志",
        data: "meirenzhi",
        articles: ""
      },
      index1: {
        title: "男神志",
        data: "nanshenzhi",
        articles: ""
      },
      index0: {
        title: "精选",
        data: "jingxuan",
        articles: ""
      },
      index3: {
        title: "线上活动",
        data: "xianshanghuodong",
        articles: ""
      },
      index4: {
        title: "牛人志",
        data: "niurenzhi",
        articles: ""
      },
      index5: {
        title: "美食志",
        data: "meishizhi",
        articles: ""
      },
      index6: {
        title: "路人志",
        data: "lurenzhi",
        articles: ""
      },

      index: 0,
      itemselect: "精选",

      
      list: [
        {
          src: "../../static/images/640.webp",
          // fallbackSrc: "http://placeholder.qiniudn.com/60x60/3cc51f/ffffff",
          title: "不会马赛回旋的甜妹不是好dancer",
          desc: '在刚接手这篇美人志时，本思很担心写不出好的文章来介绍这期美人志的主人公，因为她实在是太特别了（内心是崩溃的）。',
          url: "https://mp.weixin.qq.com/s/1FdaSQPsRcilNwrIUCrMmA"
        },
        {
          src: "https://mmbiz.qpic.cn/mmbiz_jpg/H23VLtfialwxibdBmRSHBXdCChlYBEC2kkeAKWyUrePTxtVV1J7FFZSicHclhlfYgZq42VP6TKjsUDUGhxJDQlTqA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1",
          title: "从时尚大片走出来的辅导员",
          desc:
            "看到这些标签，你会想到谁？外国语学院14级本科辅导员\n外国语学院学生会指导老师\n汉语国际教育系三年级研究生",
          url: {
            path: "https://mp.weixin.qq.com/s/wGMriH1AjwLKtknwkWXwYg",
            replace: false
          },
          
        },
        {
          src: "../../static/images/6402.webp",
          // fallbackSrc: "http://placeholder.qiniudn.com/60x60/3cc51f/ffffff",
          title: "山川河海与神明，都是你的",
          desc: '『喔对了思思，你上次问我的用来形容自己的词……我想了想，只想到了爱笑』\n『然后还很好懂，不对，好懂算缺点，我做人太透明了就很没意思』',
          url: "https://mp.weixin.qq.com/s/OxadhOKwKV2U5D87Sea_1Q"
        },
      ],
      footer:{
        title:'@交大有思·实验室'
      },

      categoryUrl: "",
      otherArticles: ""
    };
  },
  mounted: function() {
    this.$nextTick(function() {
      // Code that will run only after the
      // entire view has been rendered
      this.getArticles(this.index0.data);
    });
  },

  created() {
    this.$root.eventHub.$on("fromMenuD", data => {
      this.otherArticles = data;
    });
  },
  methods: {
    getArticles(category) {
      this.articles = "";
      this.categoryUrl = "http://127.0.0.1:8000/collection/article/" + category;
      this.$http({
        method: "GET",
        url: this.categoryUrl,
        headers: {
          // "Access-Control-Allow-Origin": "*",
          // "Access-Control-Allow-Headers": "origin, content-type, accept",
          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
      }).then(response => {
        // this.articles = response.data.articles;
        switch (category) {
          case this.index0.data:
            // this.articleCategory.meirenzhi = response.data.articles;
            // this.meirenzhiArticles = response.data.articles;
            this.index0.articles = response.data.articles;
            break;
          case this.index1.data:
            // this.articleCategory.nanshenzhi = response.data.articles;
            // this.nanshenzhiArticles = response.data.articles;
            this.index1.articles = response.data.articles;
            break;
          case this.index5.data:
            // this.articleCategory.meishizhi = response.data.articles;
            // this.meishizhiArticles = response.data.articles;
            this.index5.articles = response.data.articles;
            break;
          default:
            break;
        }
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='less'>
.hello {
  height: 100%;
}
html,
body {
  height: 100%;
  width: 100%;
  overflow-x: hidden;
}
// 图片外框
.weui-media-box__hd{
  width: 100px !important;
  height: 100px !important;
}
// 图片
.weui-media-box__thumb {
  width: auto !important;
  max-width: 100% !important;
}
.weui-media-box{
  height: 120px;
}
// 列表文字
.weui-media-box__bd{
  text-align: left ;
}
// 列表标题
.weui-media-box__title{
  white-space: unset !important;
  word-break: unset !important;
}
</style>
