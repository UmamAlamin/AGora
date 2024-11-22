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
    
        <h2 class="text-3xl font-extrabold text-center text-[#94a3b8] mb-6 font-catchy">Create a New Account</h2>
    
        <form @submit.prevent="handleSignup">
          <div class="mb-4">
            <input id="username" type="text" v-model="username" placeholder="Username" class="w-full text-lg py-3 px-4 rounded-md bg-gray-200 text-gray-700 placeholder-gray-500 focus:bg-white focus:border-gray-400 focus:outline-none" required />
          </div>
    
          <div class="mb-4">
            <input id="email" type="email" v-model="email" placeholder="Email address" class="w-full text-lg py-3 px-4 rounded-md bg-gray-200 text-gray-700 placeholder-gray-500 focus:bg-white focus:border-gray-400 focus:outline-none" required />
          </div>
    
          <div class="mb-4">
            <input id="password" :type="showPassword ? 'text' : 'password'" v-model="password" placeholder="Password" class="w-full text-lg py-3 px-4 rounded-md bg-gray-200 text-gray-700 placeholder-gray-500 focus:bg-white focus:border-gray-400 focus:outline-none" required />
          </div>
    
          <div class="mb-6">
            <input id="confirmPassword" :type="showPassword ? 'text' : 'password'" v-model="confirmPassword" placeholder="Confirm Password" class="w-full text-lg py-3 px-4 rounded-md bg-gray-200 text-gray-700 placeholder-gray-500 focus:bg-white focus:border-gray-400 focus:outline-none" required />
          </div>
    
          <button type="submit" class="bg-[#a1a1aa] text-white font-medium py-3 px-4 rounded-md hover:bg-[#8f8f97] w-full text-lg">
            Sign up
          </button>
    
          <div class="mt-4 text-center">
            <span @click="switchToLogin" class="text-[#a1a1aa] hover:text-[#8f8f97] text-lg cursor-pointer">Already have an account? Login</span>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>

import { useUserStore } from '../../store/user.js';

  export default {
    data() {
      return {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
        showPassword: false,
        showForm: true,
      };
    },
    methods: {
      async handleSignup() {
        if (this.password !== this.confirmPassword) {
          alert('Passwords do not match!');
          return;
        }
  
        const userData = { username: this.username, email: this.email, password: this.password };
  
        try {
          const response = await fetch('http://localhost:5000/api/auth/signup', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userData),
          });
  
          const result = await response.json();
          
          if (response.ok) {
            alert(result.message);
            this.closeForm();
          } else {
            alert(result.error || 'Signup failed');
          }
        } catch (error) {
          console.error('Error during signup:', error);
          alert('Something went wrong!');
        }
      },
      closeForm() {
        this.showForm = false;
        this.$emit('close');
      },
      switchToLogin() {
        this.$emit('switchToLogin');
      },
    },
  };
  </script>
  