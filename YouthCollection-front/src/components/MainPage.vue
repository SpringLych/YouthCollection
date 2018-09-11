<template>
  <div class="hello">

    <carousel></carousel>
    <!-- <mu-container> -->
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
          <simplelist v-for="item of index0.articles" :key="item.id" :img_name="item.img_name" :address="item.address" :title="item.title" :introduction="item.introduction">
          </simplelist>
        </div>
        <div v-if="index===1">
          <p>{{index1.title}}</p>
          <simplelist v-for="item of index1.articles" :key="item.id" :img_name="item.img_name" :address="item.address" :title="item.title" :introduction="item.introduction">
          </simplelist>
        </div>
        <div v-if="index===2">
          <p>{{index2.title}}</p>
          <simplelist v-for="item of index2.articles" :key="item.id" :img_name="item.img_name" :address="item.address" :title="item.title" :introduction="item.introduction">
          </simplelist>
        </div>
        <div v-if="index===3">
          <p>{{index3.title}}</p>
          <simplelist v-for="item of index3.articles" :key="item.id" :img_name="item.img_name" :address="item.address" :title="item.title" :introduction="item.introduction">
          </simplelist>
        </div>
        <div v-if="index===4">
          <p>{{index4.title}}</p>
          <simplelist v-for="item of index4.articles" :key="item.id" :img_name="item.img_name" :address="item.address" :title="item.title" :introduction="item.introduction">
          </simplelist>
        </div>
        <div v-if="index===5">
          <p>{{index5.title}}</p>
          <simplelist v-for="item of index5.articles" :key="item.id" :img_name="item.img_name" :address="item.address" :title="item.title" :introduction="item.introduction">
          </simplelist>
        </div>
        <div v-if="index===6">
          <p>{{index6.title}}</p>
          <simplelist v-for="item of index6.articles" :key="item.id" :img_name="item.img_name" :address="item.address" :title="item.title" :introduction="item.introduction">
          </simplelist>
        </div>
      </view-box>
      <!-- <swiper v-model="index" :show-dots="false">
        <swiper-item>
        </swiper-item>
      </swiper> -->
    </div>

  </div>
</template>

<script>
// import list from "./List";
import simplelist from "./SimpleList";
import carousel from "./Carousel";
import menud from "./MenuD";

import { Tab, TabItem, Swiper, SwiperItem, ViewBox } from "vux";

export default {
  name: "MainPage",
  components: {
    // list,
    simplelist,
    carousel,
    menud,
    Tab,
    TabItem,
    Swiper,
    SwiperItem,
    ViewBox
  },
  data() {
    return {
      active2: 0,
      data: "",
      info: "",
      // 栏目名称
      "index0": {
        title: "美人志",
        data: "meirenzhi",
        articles:'',
      },
      "index1": {
        title: "男神志",
        data: "nanshenzhi",
        articles:'',
      },
      "index2": {
        title: "深度好文",
        data: "shenduhaowen",
        articles:'',
      },
      "index3": {
        title: "线上活动",
        data: "xianshanghuodong",
        articles:'',
      },
      "index4": {
        title: "牛人志",
        data: "niurenzhi",
        articles:'',
      },
      "index5": {
        title: "美食志",
        data: "meishizhi",
        articles:'',
      },
      "index6": {
        title: "路人志",
        data: "lurenzhi",
        articles:'',
      },

      index: 0,
      itemselect: "美人志",

      categoryUrl: "",
      // articles: "",
      // meirenzhiArticles: "",
      // nanshenzhiArticles: "",
      // meishizhiArticles: "",
      otherArticles: ""
    };
  },
  mounted: function() {
    this.$nextTick(function() {
      // Code that will run only after the
      // entire view has been rendered
      this.getArticles("meirenzhi");
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
            this.nanshenzhiArticles = response.data.articles;
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
<style scoped lang='less'>
.hello {
  height: 100%;
}
html,
body {
  height: 100%;
  width: 100%;
  overflow-x: hidden;
}
</style>
