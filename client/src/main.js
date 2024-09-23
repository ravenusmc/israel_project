import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import {
  faUserSecret, faHashtag, faPencilAlt, faCodeBranch, faNetworkWired,
} from '@fortawesome/free-solid-svg-icons';

Vue.config.productionTip = false

library.add(faUserSecret,
  faHashtag,
  faPencilAlt,
  faCodeBranch,
  faNetworkWired);

Vue.component('fa-icon', FontAwesomeIcon);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
