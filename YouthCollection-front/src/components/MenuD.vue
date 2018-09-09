<template>
    <mu-menu cover :open.sync="open">
        <mu-button flat>更多</mu-button>
        <mu-list slot="content">
            <mu-list-item button @click="sendToMainPage('niurenzhi')">
                <mu-list-item-title>牛人志</mu-list-item-title>
            </mu-list-item>
            <mu-list-item button @click="sendToMainPage('lurenzhi')">
                <mu-list-item-title>路人志</mu-list-item-title>
            </mu-list-item>
            <mu-list-item button>
                <mu-list-item-title>线上活动</mu-list-item-title>
            </mu-list-item>
        </mu-list>
    </mu-menu>
</template>

<script>
export default {
  data() {
    return {
      open: false,// 控制menu
      articles:'',
      categoryUrl:''
    };
  },
  methods: {
    //   关闭菜单
    closeMenu() {
      this.open = !this.open;
    },
    // 获取到articles发送至MainPage处理
    sendToMainPage(cate){
        this.closeMenu();
        this.getArticles(cate);
        this.$root.eventHub.$emit('fromMenuD', this.articles);
    },
    // 根据category获取articles
    getArticles(category){
        this.articles=''
        this.categoryUrl='http://127.0.0.1:8000/collection/article/'+category;
        console.log('获取'+category);
        this.articles="获取到的"+category
    }
    
  },
};
</script>

<style scoped>
</style>
