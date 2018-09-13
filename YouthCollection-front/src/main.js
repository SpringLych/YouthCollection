// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';

import axios from 'axios';
import VueAxios from 'vue-axios';
// 添加 Fastclick 移除移动端点击延迟
const FastClick = require('fastclick')
FastClick.attach(document.body)

Vue.config.productionTip = false
Vue.use(VueAxios, axios);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: {
    App
  },
  template: '<App/>',
  data: {
    eventHub: new Vue()
  }
})
