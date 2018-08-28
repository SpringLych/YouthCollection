<template>
  <div class="hello">

    <carousel></carousel>
    <!-- <mu-container> -->
      <mu-tabs :value.sync="active2" inverse color="blue" indicator-color="blue" full-width>
        <mu-tab @click="getMeiren()">美人志</mu-tab>
        <mu-tab @click="getNanshen()">男神志</mu-tab>
        <mu-tab @click="getMeishi()">美食志</mu-tab>
      </mu-tabs>
      <div class="demo-text" v-if="active2 === 0">
        <!-- 美人志 -->
        
        <simplelist v-for="item of meiArticles" :key="item.id" :img_name="item.img_name" :address="item.address">
        </simplelist>
      </div>

      <div class="demo-text" v-if="active2 === 1">
        <!-- 男神志 -->
        <simplelist v-for="item of nanArticles" :key="item.id" :img_name="item.img_name" :address="item.address">
        </simplelist>
      </div>

      <div class="demo-text" v-if="active2 === 2">
        <!-- 美食志、精选？ -->
        <simplelist v-for="item of jingArticles" :key="item.id" :img_name="item.img_name" :address="item.address">
        </simplelist>
      </div>

    <!-- </mu-container> -->

  </div>
</template>

<script>
// import list from "./List";
import simplelist from "./SimpleList";
import carousel from "./Carousel";

export default {
  name: "MainPage",
  data() {
    return {
      active2: 0,
      data: "",
      meiTitle: "",
      meiArticles: "",
      meirenCou: 0,

      nanTitle: "",
      nanArticles: "",
      nanCou: 0,

      jingTitle: "",
      jingArticles: "",
      jingCou: 0
    };
  },
  mounted: function() {
    this.$nextTick(function() {
      // Code that will run only after the
      // entire view has been rendered
      this.getMeiren();
    });
  },
  components: {
    // list,
    simplelist,
    carousel,
  },
  methods: {
    getMeiren() {
      if (this.meirenCou > 0) {
        return;
      }
      console.log("获取美人志...");

      this.$http({
        method: "GET",

        url: "http://127.0.0.1:8000/collection/article/meirenzhi",
        headers: {
          // "Access-Control-Allow-Origin": "*",
          // "Access-Control-Allow-Headers": "origin, content-type, accept",
          'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
        }
      }).then(response => {
        this.meiTitle = response.data.title;
        this.meiArticles = response.data.articles;

        this.meirenCou = 1;
        this.nanshenCou = 0;
        this.jingCou = 0;

        console.log(this.meiTitle);
      });
    },
    getNanshen() {
      if (this.nanCou > 0) {
        return;
      }
      console.log("获取男神志...");
      this.$http({
        method: "GET",
        url: "http://127.0.0.1:8000/collection/article/nanshenzhi",
        headers: {
          // "Access-Control-Allow-Origin": "*",
          // "Access-Control-Allow-Headers": "origin, content-type, accept",
          'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
        }
      }).then(response => {
        console.log(this.nanTitle);

        this.nanTitle = response.data.title;
        this.nanArticles = response.data.articles;

        this.meirenCou = 0;
        this.nanCou = 1;
        this.jingCou = 0;
      });
    },
    getMeishi() {
      if (this.jingCou > 0) {
        return;
      }
      console.log("获取美食志...");
      this.$http({
        method: "GET",
        url: "http://127.0.0.1:8000/collection/article/meishizhi",
        headers: {
          // "Access-Control-Allow-Origin": "*",
          // "Access-Control-Allow-Headers": "origin, content-type, accept",
          'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
        }
      }).then(response => {
        console.log(this.jingTitle);

        this.jingTitle = response.data.title;
        this.jingArticles = response.data.articles;

        this.meirenCou = 0;
        this.nanCou = 0;
        this.jingCou = 1;
      });
    }
  },
  
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello {
  height: 100%;
}
.mu-item {
  padding-top: 0px;
  padding-right: 6px;
  padding-bottom: 0px;
  padding-left: 6px;
}
</style>
