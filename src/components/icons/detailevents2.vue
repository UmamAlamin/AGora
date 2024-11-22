<template>
    <div class="content mx-auto max-w-screen-xl px-4 py-6">
      <!-- Main Content Section -->
      <div class="main-content bg-gradient-to-r from-gray-400 to-blue-300 rounded-xl shadow-lg mb-6 overflow-hidden">
        <img
          alt="Group of volunteers smiling and holding hands"
          src="https://storage.googleapis.com/a1aa/image/d6L00i9SAA4NB5ysjiWdIdBHrb5WL84fMduBnBefxe47FVGPB.jpg"
          class="w-full h-72 object-cover"
        />
        <div class="text p-6">
          <h2 class="text-3xl font-semibold text-white mb-4">Food Drive</h2>
          <p class="text-white text-lg leading-relaxed">
            Teaching Program refers to an organized initiative or activity designed to facilitate education and skill development.
            It typically involves trained educators delivering lessons or training sessions to a specific group of learners.
            These programs aim to enhance knowledge, promote critical thinking, and foster personal or professional growth.
          </p>
        </div>
      </div>
  
      <!-- Info and Action Section -->
      <div class="info-action-container grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Info Section -->
        <div class="info bg-white p-6 rounded-xl shadow-md">
          <div class="info-item flex items-start gap-4 p-4 bg-gray-100 rounded-lg mb-4 hover:shadow-lg transition duration-300 ease-in-out">
            <i class="fas fa-calendar-alt text-blue-500 text-2xl"></i>
            <p class="font-semibold text-gray-800">WHEN <span class="block text-sm text-gray-600">Wednesday, 2nd October 2024</span></p>
          </div>
          <div class="info-item flex items-start gap-4 p-4 bg-gray-100 rounded-lg mb-4 hover:shadow-lg transition duration-300 ease-in-out">
            <i class="fas fa-map-marker-alt text-blue-500 text-2xl"></i>
            <p class="font-semibold text-gray-800">WHERE <span class="block text-sm text-gray-600">Jl. Kebon Jeruk 20, Jakarta Barat, Indonesia</span></p>
          </div>
          <div class="info-item flex items-start gap-4 p-4 bg-gray-100 rounded-lg mb-4 hover:shadow-lg transition duration-300 ease-in-out">
            <i class="fas fa-clock text-blue-500 text-2xl"></i>
            <p class="font-semibold text-gray-800">TIME <span class="block text-sm text-gray-600">08:00 - 12:00 WIB</span></p>
          </div>
          <div class="info-item flex items-start gap-4 p-4 bg-gray-100 rounded-lg mb-4 hover:shadow-lg transition duration-300 ease-in-out">
            <i class="fas fa-users text-blue-500 text-2xl"></i>
            <p class="font-semibold text-gray-800">VOLUNTEER <span class="block text-sm text-gray-600">60 People</span></p>
          </div>
        </div>
  
        <!-- Action Section -->
        <div class="actions flex flex-col gap-4">
          <div class="action join bg-green-500 hover:bg-green-600 text-white py-3 rounded-xl flex items-center justify-center gap-2 shadow-lg hover:shadow-xl transition duration-300 ease-in-out">
            <i class="fas fa-hand-paper text-lg"></i>
            <span class="font-semibold">JOIN VOLUNTEER</span>
          </div>
          <div class="action donate bg-yellow-500 hover:bg-yellow-600 text-white py-3 rounded-xl flex items-center justify-center gap-2 shadow-lg hover:shadow-xl transition duration-300 ease-in-out">
            <i class="fas fa-hand-holding-usd text-lg"></i>
            <span class="font-semibold">DONATE</span>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "VolunteerProgram",
  };
  </script>
  
  <style scoped>
  /* Custom styling */
  .content {
    max-width: 1200px;
    margin: auto;
  }
  
  .main-content img {
    width: 100%;
    height: 300px;
    object-fit: cover;
  }
  
  .info-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
  
  .actions .action:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
  </style>
  