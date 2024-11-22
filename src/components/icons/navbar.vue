<template>
  <header class="flex items-center justify-between p-4 md:p-8 bg-gray-100 shadow-md sticky top-0 z-50">
    <!-- Brand -->
    <div class="flex items-center gap-4">
      <div class="flex items-center justify-center w-8 h-8 bg-gradient-to-br from-gray-300 to-gray-400 text-gray-600 font-bold rounded-full">
        A
      </div>
      <h1 class="text-lg font-semibold tracking-wider text-gray-800">AGORA</h1>
    </div>
    <!-- Menu toggle for mobile -->
    <button 
      class="md:hidden flex items-center text-gray-800 focus:outline-none"
      @click="toggleMenu"
    >
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16m-7 6h7" />
      </svg>
    </button>
    <!-- Main Navigation -->
    <nav 
      :class="[
        'md:flex items-center md:gap-8',
        isMenuOpen ? 'flex flex-col' : 'hidden',
        'absolute md:static top-16 left-0 w-full md:w-auto bg-gray-100',
        'shadow-lg md:shadow-none',
        'p-4 md:p-0',
        'space-y-4 md:space-y-0'
      ]"
      @click.away="isMenuOpen = false"
    >
      <!-- Search Bar -->
      <div class="w-full md:flex-grow md:mx-8 max-w-md">
        <input
          type="text"
          placeholder="Search events..."
          class="w-full p-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring focus:ring-gray-400"
        />
      </div>
      <!-- Auth Buttons / User Info -->
      <div class="flex flex-col md:flex-row gap-4 items-center w-full md:w-auto">
        <!-- If logged in, show profile and logout -->
        <template v-if="isAuthenticated">
          <div class="flex items-center gap-2 w-full md:w-auto justify-center">
            <span>{{ user.username }}</span>
            <button
              @click="logout"
              class="px-4 py-2 bg-gray-400 text-white font-medium rounded-md hover:bg-gray-500 w-full md:w-auto"
            >
              Logout
            </button>
          </div>
        </template>
        <!-- If not logged in, show Login and Signup buttons -->
        <template v-else>
          <button
            @click="$emit('showLoginModal')"
            class="px-4 py-2 border border-gray-800 text-gray-800 font-medium rounded-md hover:bg-gray-200 w-full md:w-auto"
          >
            Log In
          </button>
          <button
            @click="$emit('showSignupModal')"
            class="px-4 py-2 bg-gray-400 text-white font-medium rounded-md hover:bg-gray-500 w-full md:w-auto"
          >
            Sign Up
          </button>
        </template>
      </div>
    </nav>
  </header>
</template>

<script>
import { ref } from 'vue';
import { useAuthStore } from "../../store/auth.js";

export default {
  name: "Navbar",
  setup() {
    const authStore = useAuthStore();
    const { isAuthenticated, user, logout } = authStore;
    const isMenuOpen = ref(false);
    
    const toggleMenu = () => {
      isMenuOpen.value = !isMenuOpen.value;
    };

    return {
      isAuthenticated,
      user,
      logout,
      isMenuOpen,
      toggleMenu,
    };
  },
};
</script>

<style scoped>
nav {
  transition: all 0.3s ease-in-out;
}

@media (max-width: 768px) {
  nav {
    transform: translateY(-10px);
    opacity: 0;
    pointer-events: none;
  }
  
  nav.flex {
    transform: translateY(0);
    opacity: 1;
    pointer-events: auto;
  }
}
</style>