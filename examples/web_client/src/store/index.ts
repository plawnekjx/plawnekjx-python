import Vue from 'vue';
import Vuex from 'vuex';

import plawnekjx from './modules/plawnekjx';
import plawnekjxBus from './plugins/plawnekjx';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    plawnekjx
  },
  plugins: [
    plawnekjxBus()
  ]
});
