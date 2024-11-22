<template>
    <div class="min-h-screen flex flex-col">
      <!-- Navbar -->
      <Navbar @showLoginModal="isLoginFormVisible = true" @showSignupModal="isSignupFormVisible = true" />
      
      <!-- Featured Event -->
      <FeaturedEvent />
      
      <!-- Events Section (using Events.vue component) -->
      <Events />
    
      <!-- Modal Login Form -->
      <LoginForm 
        v-if="isLoginFormVisible" 
        @close="closeLoginForm" 
        @switchToSignup="switchToSignup"
      />
    
      <!-- Modal Sign Up Form -->
      <SignupForm 
        v-if="isSignupFormVisible" 
        @close="closeSignupForm" 
        @switchToLogin="switchToLogin"
      />
    </div>
  </template>
  
  <script>
  import Navbar from '../components/icons/navbar.vue';
  import FeaturedEvent from '../components/icons/featuredEvents.vue';
  import Events from '../components/icons/events.vue'; // Import Events.vue component
  import LoginForm from '../components/icons/Login.vue';
  import SignupForm from '../components/icons/signup.vue';
  
  export default {
    name: "Home",
    components: {
      Navbar,
      FeaturedEvent,
      Events, // Register Events component
      LoginForm,
      SignupForm
    },
    data() {
      return {
        isLoginFormVisible: false,
        isSignupFormVisible: false
      };
    },
    methods: {
      closeLoginForm() {
        this.isLoginFormVisible = false;
      },
      closeSignupForm() {
        this.isSignupFormVisible = false;
      },
      switchToSignup() {
        this.isLoginFormVisible = false;
        this.isSignupFormVisible = true;
      },
      switchToLogin() {
        this.isSignupFormVisible = false;
        this.isLoginFormVisible = true;
      }
    }
  };
  </script>
  