<template>
    <div class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
      <div class="bg-white p-6 rounded-lg shadow-lg w-96">
        <h3 class="text-xl font-semibold mb-4">Add New Event</h3>
  
        <form @submit.prevent="submitEventForm">
          <div class="mb-4">
            <label for="title" class="block text-sm font-medium text-gray-700">Event Title</label>
            <input type="text" v-model="newEvent.title" id="title" class="w-full p-2 border border-gray-300 rounded-md" required />
          </div>
          <div class="mb-4">
            <label for="description" class="block text-sm font-medium text-gray-700">Event Description</label>
            <textarea v-model="newEvent.description" id="description" rows="4" class="w-full p-2 border border-gray-300 rounded-md" required></textarea>
          </div>
          <div class="mb-4">
            <label for="category" class="block text-sm font-medium text-gray-700">Event Category</label>
            <select v-model="newEvent.category" id="category" class="w-full p-2 border border-gray-300 rounded-md">
              <option value="Charity">Charity</option>
              <option value="Volunteer">Volunteer</option>
              <option value="Uncategorized">Uncategorized</option>
            </select>
          </div>
          <div class="mb-4">
            <label for="image" class="block text-sm font-medium text-gray-700">Event Banner Image URL</label>
            <input type="url" v-model="newEvent.image" id="image" class="w-full p-2 border border-gray-300 rounded-md" required />
          </div>
          <div class="mb-4">
            <label for="proposal" class="block text-sm font-medium text-gray-700">Event Proposal (PDF)</label>
            <input type="file" @change="handleFileUpload" id="proposal" class="w-full p-2 border border-gray-300 rounded-md" accept=".pdf" />
            <p v-if="newEvent.proposalFile" class="text-sm text-gray-600 mt-2">Proposal File: {{ newEvent.proposalFile.name }}</p>
          </div>
          <div class="mb-4">
            <label for="date" class="block text-sm font-medium text-gray-700">Event Date</label>
            <input type="date" v-model="newEvent.date" id="date" class="w-full p-2 border border-gray-300 rounded-md" required :min="minDate" />
          </div>
  
          <div class="flex justify-between items-center">
            <button @click="$emit('close')" type="button" class="bg-gray-300 px-4 py-2 rounded-md text-gray-700">Cancel</button>
            <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded-md">Add Event</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        minDate: new Date().toISOString().split("T")[0], // Set today's date as minimum
        newEvent: {
          title: "",
          description: "",
          category: "Charity",
          image: "",
          date: "",
          proposalFile: null,
        },
      };
    },
    methods: {
      submitEventForm() {
        this.$emit('submit', this.newEvent); // Emit the form data to the parent
        this.newEvent = { title: "", description: "", category: "Charity", image: "", date: "", proposalFile: null }; // Reset form
      },
      handleFileUpload(event) {
        const file = event.target.files[0];
        if (file && file.type === 'application/pdf') {
          this.newEvent.proposalFile = file;
        } else {
          alert("Please upload a valid PDF file.");
        }
      },
    },
  };
  </script>
  