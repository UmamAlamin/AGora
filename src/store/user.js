import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    username: null,
    email: null,
  }),
  actions: {
    setUserData(userData) {
      this.username = userData.username;
      this.email = userData.email;
    },
    clearUserData() {
      this.username = null;
      this.email = null;
    },
  },
});
