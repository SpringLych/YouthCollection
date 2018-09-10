<template>

    <div>
        <!-- Django不对下面渲染 -->
        <div class="hid">
            {% verbatim %}
        </div>

        <mu-list textline="three-line">
            <mu-list-item avatar :ripple="false" button @click="toUrl()">
                <mu-list-item-action>
                    <!-- 这里放简介图 -->
                    <mu-card>
                        <!-- style="width: 90%; max-width: 200px; margin: 0 auto;" -->
                        <mu-card-media>
                            <img :src="'/static/images/'+img_name">
                        </mu-card-media>
                    </mu-card>
                </mu-list-item-action>

                <mu-list-item-content>
                    <!-- 标题 -->
                    <mu-list-item-title>{{title}}</mu-list-item-title>
                    <mu-list-item-sub-title>
                        <!-- 简介 -->
                        <span style="color: rgba(0, 0, 0, .87)">{{introduction}}</span>
                    </mu-list-item-sub-title>
                </mu-list-item-content>
            </mu-list-item>
        </mu-list>
        <mu-divider></mu-divider>
        <div class="hid"> {% endverbatim %}</div>
        <!-- http://127.0.0.1:8000/static/images/ -->
    </div>

</template>

<script>
export default {
  name: "SimpleList",
  data() {
    return {
      //   people:''
    };
  },
  methods: {
    toUrl() {
      //   console.log("点击列表 URL：" + this.address);
      window.location.href = "http://" + this.address;
    }
  },
  props: ["img_name", "address", "title", "introduction"]
};
</script>

<style scoped>

.hid {
  display: none;
}
.my-mu-card-media{
    width: 100px;
}

.mu-card {
  width: 90%;
  max-width: 100px;
  /* margin: 0 auto; */
  max-height: 100px;
  /* position: absolute;
  top: 50%;
  transform: translateY(-50%); */
  /* display: inline-block; */
  /* height: 10%; */
  /* width: 90%; */
  /* max-width: 50%; */
  /* margin: 0 auto; */
}
</style>
