<template>
  <div
    v-show="showForm"
    class="fixed inset-0 z-50 flex items-center justify-center bg-gray-900 bg-opacity-50"
  >
    <div class="bg-gradient-to-r from-gray-700 via-gray-600 to-gray-500 rounded-lg shadow-lg p-8 w-full max-w-md relative">
      <button @click="closeForm" class="absolute top-4 right-4 text-gray-600 hover:text-gray-800" aria-label="Close">
        <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <h2 class="text-3xl font-extrabold text-center text-[#94a3b8] mb-6 font-catchy">Login to Your Account</h2>

      <form @submit.prevent="handleLogin">
        <div class="mb-4">
          <input
            id="email"
            type="email"
            v-model="email"
            placeholder="Email address"
            class="w-full text-lg py-3 px-4 rounded-md bg-gray-200 text-gray-700 placeholder-gray-500 focus:bg-white focus:border-gray-400 focus:outline-none"
            required
          />
        </div>

        <div class="mb-4">
          <input
            id="password"
            :type="showPassword ? 'text' : 'password'"
            v-model="password"
            placeholder="Password"
            class="w-full text-lg py-3 px-4 rounded-md bg-gray-200 text-gray-700 placeholder-gray-500 focus:bg-white focus:border-gray-400 focus:outline-none"
            required
          />
        </div>

        <div class="mb-4 flex items-center">
          <input
            id="showPassword"
            type="checkbox"
            v-model="showPassword"
            class="mr-2"
          />
          <label for="showPassword" class="text-white">Show password</label> <!-- Text color changed to white -->
        </div>

        <button
          type="submit"
          class="bg-[#a1a1aa] text-white font-medium py-3 px-4 rounded-md hover:bg-[#8f8f97] w-full text-lg"
        >
          Log In
        </button>

        <div class="mt-4 text-center">
          <span @click="switchToSignup" class="text-[#a1a1aa] hover:text-[#8f8f97] text-lg cursor-pointer">Don't have an account? Sign Up</span>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from '../../store/auth.js'; // Pinia store for authentication
import { ref } from 'vue'; // Import ref for reactivity
import { useRouter } from 'vue-router'; // Import useRouter for routing

export default {
  data() {
    return {
      email: '',
      password: '',
      showPassword: false,
      showForm: true,
    };
  },
  methods: {
    async handleLogin() {
  try {
    const authStore = useAuthStore(); // Access Pinia store instance here

    const response = await authStore.login({
      email: this.email,
      password: this.password,
    });

    if (response && response.data && response.data.token) {
      localStorage.setItem('token', response.data.token);

      // Store the username and token in the auth store
      authStore.setUser({
        username: response.data.username,
        token: response.data.token,
      });

      this.closeForm();
      this.$router.push({ name: 'home' }); // Redirect to the home page
    } else {
      // Handle cases where token is not returned
      alert(response && response.data && response.data.error
        ? response.data.error
        : 'Login failed: No token returned');
    }
  } catch (error) {
    console.error('Error during login:', error);
    
    // Check if error.response exists before accessing its properties
    if (error.response && error.response.data) {
      alert(`Backend error: ${error.response.data.error || 'Unknown error'}`);
    } else if (error.message) {
      // Handle other errors (like network issues)
      alert(`Login error: ${error.message}`);
    } else {
      alert('An unexpected error occurred.');
    }
  }
},


    closeForm() {
      this.showForm = false;
      this.$emit('close');
    },
    switchToSignup() {
      this.$emit('switchToSignup');
    },
  },
};
</script>

<style scoped>
/* Add custom styles here if needed */
</style>
