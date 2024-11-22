<template>
    <div class="featured-event flex p-8 shadow-lg bg-gray-300">
      <!-- Featured Content -->
      <div class="featured-content flex-1 p-8 pt-10 pb-10">
        <h2 class="text-4xl font-bold mb-2">Community Clean-up Drive</h2>
        <p class="text-gray-600 text-lg mb-4">Saturday, December 15, 2024</p>
        <p class="text-gray-800 mb-4">
          Join us for our biggest community clean-up event of the year! We're
          gathering volunteers to help clean and beautify our local parks and
          streets. This is a great opportunity to make a real difference in our
          community.
        </p>
        <a href="#" class="text-blue-500 hover:text-blue-400 text-lg">Read More →</a>
      </div>
      <!-- Featured Image -->
      <div
         class="featured-image w-1/4 bg-cover bg-center"
         :style="`background-image: url(${featuredImage})`"
            ></div>

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
  