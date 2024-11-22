<template>
    <div 
      class="featured-event flex flex-col sm:flex-row p-6 sm:p-8 shadow-lg bg-gray-300 rounded-lg">
      <!-- Featured Content -->
      <div class="featured-content sm:flex-1 p-4 sm:p-8 pt-6 pb-6">
        <h2 class="text-2xl sm:text-4xl font-bold mb-2">Community Clean-up Drive</h2>
        <p class="text-gray-600 text-sm sm:text-lg mb-4">Saturday, December 15, 2024</p>
        <p class="text-gray-800 text-sm sm:text-base mb-4">
          Join us for our biggest community clean-up event of the year! We're
          gathering volunteers to help clean and beautify our local parks and
          streets. This is a great opportunity to make a real difference in our
          community.
        </p>
        <a href="#" class="text-blue-500 hover:text-blue-400 text-sm sm:text-lg">Read More →</a>
      </div>
      
      <!-- Featured Image -->
      <div 
        class="featured-image h-48 sm:h-auto sm:w-1/3 bg-cover bg-center rounded-lg sm:rounded-none"
        :style="`background-image: url(${featuredImage})`">
      </div>
    </div>
  </template>
  
  <script>
  import featuredImage from '../../assets/feature2.png';
  
  export default {
    name: 'FeaturedEvent',
    data() {
      return {
        featuredImage,
      };
    },
  };
  </script>
  