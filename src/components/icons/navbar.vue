<template>
  <header class="flex items-center justify-between p-4 md:p-8 bg-gray-100 shadow-md sticky top-0 z-50">
    <!-- Brand -->
    <div class="flex items-center gap-4">
      <div class="flex items-center justify-center w-8 h-8 bg-gradient-to-br from-gray-300 to-gray-400 text-gray-600 font-bold rounded-full">
        A
      </div>
      <h1 class="text-lg font-semibold tracking-wider text-gray-800">AGORA</h1>
    </div>

    <!-- Search Bar -->
    <div class="flex-grow mx-8 max-w-md">
      <input type="text" placeholder="Search events..." class="w-full p-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring focus:ring-gray-400" />
    </div>

    <!-- Auth Buttons / User Info -->
    <div class="flex gap-4">
      <!-- Jika sudah login, tampilkan profil dan logout -->
      <template v-if="isAuthenticated">
        <div class="flex items-center gap-2">
          <span>{{ user.username }}</span> <!-- Tampilkan nama user -->
          <button @click="logout" class="px-4 py-2 bg-gray-400 text-white font-medium rounded-md hover:bg-gray-500">
            Logout
          </button>
        </div>
      </template>

      <!-- Jika belum login, tampilkan tombol Login dan Signup -->
      <template v-else>
       <!-- Navbar.vue -->
        <button @click="$emit('showLoginModal')" class="px-4 py-2 border border-gray-800 text-gray-800 font-medium rounded-md hover:bg-gray-200">
          Log In
        </button>
        <button @click="$emit('showSignupModal')" class="px-4 py-2 bg-gray-400 text-white font-medium rounded-md hover:bg-gray-500">
          Sign Up
        </button>

      </template>
    </div>
  </header>
</template>

<script>
import { useAuthStore } from '../../store/auth.js'; // Import store Pinia

export default {
  name: "Navbar",
  setup() {
    const authStore = useAuthStore(); // Mengakses store Pinia

    const { isAuthenticated, user, logout } = authStore; // Mendapatkan status login dan data user

    return {
      isAuthenticated,
      user,
      logout,
    };
  },
};
</script>
