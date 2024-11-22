// stores/auth.js
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: null,
    isAuthenticated: false
  }),

  actions: {
    setUser(userData) {
      this.user = userData;
      this.isAuthenticated = true;
    },

    setToken(token) {
      this.token = token;
      // Opsional: Simpan token di localStorage
      localStorage.setItem('token', token);
    },

    logout() {
      this.user = null;
      this.token = null;
      this.isAuthenticated = false;
      localStorage.removeItem('token');
    },

    // Action untuk login
    async login(credentials) {
      try {
        const response = await fetch('http://localhost:5000/api/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(credentials)
        });

        const data = await response.json();

        if (!response.ok) {
          throw new Error(data.error || 'Login failed');
        }

        // Set user data dan token ke store
        this.setUser({
          username: data.username,
          // tambahkan data user lain yang diperlukan
        });
        this.setToken(data.token);

        return { success: true };
      } catch (error) {
        console.error('Login error:', error);
        return { success: false, error: error.message };
      }
    }
  },

  getters: {
    getUserName: (state) => state.user?.username,
    isLoggedIn: (state) => state.isAuthenticated
  }
})