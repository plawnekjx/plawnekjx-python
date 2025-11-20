import { Module } from 'vuex';

interface PlawnekjxState {
  processes: Process[],
}

type Process = [number, string];

const plawnekjxModule: Module<PlawnekjxState, any> = {
  state: {
    processes: []
  },

  mutations: {
  }
};

export default plawnekjxModule;
