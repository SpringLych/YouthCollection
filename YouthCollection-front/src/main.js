// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';

import axios from 'axios';
import VueAxios from 'vue-axios';

// import MuseUI from 'muse-ui';
// import 'muse-ui/dist/muse-ui.css';
// import 'muse-ui-message/dist/muse-ui-message.css';


// 按需引入muse-ui
import 'muse-ui/lib/styles/base.less';
import {
  // Avatar,
  AppBar,
  Carousel,
  Tabs,
  Button,
  Card,
  Dialog,
  Divider,
  ExpansionPanel,
  Icon,
  List,
  LoadMore,
  Menu,
  Paper,
} from 'muse-ui';
import 'muse-ui/lib/styles/theme.less';


import 'muse-ui-message/dist/muse-ui-message.css';
import Message from 'muse-ui-message';
Vue.use(Message)
// import {Button}

// import Message from 'muse-ui-message';

Vue.config.productionTip = false
// Vue.use(Message)
// Vue.use(MuseUI)
Vue.use(VueAxios, axios);
Vue.use(AppBar);
Vue.use(Carousel);
Vue.use(Tabs);
Vue.use(Button)
Vue.use(Card);
Vue.use(Dialog);
Vue.use(Divider);
Vue.use(ExpansionPanel);
Vue.use(Icon);
Vue.use(List);
Vue.use(LoadMore);
Vue.use(Menu);
Vue.use(Paper);



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
