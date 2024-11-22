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

    <!-- Desktop Navigation -->
    <div class="hidden md:flex md:flex-1 md:items-center md:justify-between md:ml-8">
      <!-- Search Bar -->
      <div class="flex-1 flex justify-center max-w-3xl mx-4">
        <input
          type="text"
          placeholder="Search events..."
          class="w-full max-w-xl p-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring focus:ring-gray-400"
        />
      </div>

      <!-- Desktop Auth Buttons -->
      <div class="flex items-center gap-4">
        <template v-if="isAuthenticated">
          <span class="text-gray-800">{{ user.username }}</span>
          <button
            @click="logout"
            class="px-4 py-2 bg-gray-400 text-white font-medium rounded-md hover:bg-gray-500 whitespace-nowrap"
          >
            Logout
          </button>
        </template>
        <template v-else>
          <button
            @click="$emit('showLoginModal')"
            class="px-4 py-2 border border-gray-800 text-gray-800 font-medium rounded-md hover:bg-gray-200 whitespace-nowrap"
          >
            Log In
          </button>
          <button
            @click="$emit('showSignupModal')"
            class="px-4 py-2 bg-gray-400 text-white font-medium rounded-md hover:bg-gray-500 whitespace-nowrap"
          >
            Sign Up
          </button>
        </template>
      </div>
    </div>

    <!-- Mobile Navigation Menu -->
    <div 
      :class="[
        isMenuOpen ? 'flex flex-col' : 'hidden',
        'md:hidden',
        'absolute top-full left-0',
        'w-full bg-gray-100',
        'shadow-lg',
        'transition-all duration-300 ease-in-out'
      ]"
    >
      <!-- Mobile Search -->
      <div class="p-4">
        <input
          type="text"
          placeholder="Search events..."
          class="w-full p-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring focus:ring-gray-400"
        />
      </div>

      <!-- Mobile Auth Buttons -->
      <div class="flex flex-col gap-2 p-4 border-t border-gray-200">
        <template v-if="isAuthenticated">
          <div class="flex items-center justify-between">
            <span class="text-gray-800">{{ user.username }}</span>
            <button
              @click="logout"
              class="px-4 py-2 bg-gray-400 text-white font-medium rounded-md hover:bg-gray-500"
            >
              Logout
            </button>
          </div>
        </template>
        <template v-else>
          <button
            @click="$emit('showLoginModal')"
            class="w-full px-4 py-2 border border-gray-800 text-gray-800 font-medium rounded-md hover:bg-gray-200"
          >
            Log In
          </button>
          <button
            @click="$emit('showSignupModal')"
            class="w-full px-4 py-2 bg-gray-400 text-white font-medium rounded-md hover:bg-gray-500"
          >
            Sign Up
          </button>
        </template>
      </div>
    </div>
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
.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: all 0.3s ease;
}

.mobile-menu-enter-from,
.mobile-menu-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

/* Custom scrollbar for better mobile experience */
@media (max-width: 768px) {
  ::-webkit-scrollbar {
    width: 4px;
  }
  
  ::-webkit-scrollbar-track {
    background: #f1f1f1;
  }
  
  ::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 2px;
  }
}
</style>