<template>
    <div class="events-container p-6 bg-gray-50 min-h-screen">
      <div class="events-header flex justify-between items-center mb-6">
        <h2 class="text-2xl font-semibold">Upcoming Events</h2>
        <select v-model="sortOption" class="p-2 border rounded-md">
          <option value="newest">Newest First</option>
          <option value="oldest">Oldest First</option>
        </select>
      </div>
  
      <div class="events-grid grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        <div v-for="event in sortedEvents" :key="event.id" class="event-card bg-white rounded-lg shadow-md p-4">
          <div :class="`event-category ${event.category.toLowerCase()} font-bold text-gray-700`">
            {{ event.category }}
          </div>
          <div class="event-image-container mb-4">
            <img :src="event.image" alt="Event Image" class="event-image w-full h-40 object-cover rounded-lg" />
          </div>
          <div class="event-details">
            <h4 class="text-lg font-semibold">{{ event.title }}</h4>
            <p class="text-sm text-gray-600">{{ event.date }}</p>
            <!-- Use router-link to navigate to event details page -->
            <router-link :to="'/event/' + event.id" class="text-blue-600 hover:underline">Read More →</router-link>
          </div>
          <div class="event-description">
            <p>{{ event.description }}</p>
          </div>
        </div>
      </div>
  
      <button @click="openAddEventModal" class="add-event-btn fixed bottom-6 right-6 bg-blue-600 text-white p-4 rounded-full shadow-xl hover:bg-blue-700 transition">+</button>
  
      <!-- Event Form Modal -->
      <FormModal v-if="showAddEventModal" @close="closeAddEventModal" @submit="submitEventForm" />
    </div>
  </template>
  
  <script>
  import FormModal from '../icons/planner.vue';
  
  export default {
    components: {
      FormModal,
    },
    data() {
      return {
        sortOption: "newest",
        showAddEventModal: false,
        events: [
          { id: 1, title: 'Teaching Program', description: 'Volunteer to teach basic computer skills...', category: 'Volunteer', image: 'https://storage.googleapis.com/a1aa/image/d6L00i9SAA4NB5ysjiWdIdBHrb5WL84fMduBnBefxe47FVGPB.jpg', date: '2024-12-02' },
        ],
      };
    },
    computed: {
      sortedEvents() {
        return this.sortOption === "newest"
          ? [...this.events].sort((a, b) => new Date(b.date) - new Date(a.date))
          : [...this.events].sort((a, b) => new Date(a.date) - new Date(b.date));
      },
    },
    methods: {
      openAddEventModal() {
        this.showAddEventModal = true;
      },
      closeAddEventModal() {
        this.showAddEventModal = false;
      },
      submitEventForm(newEvent) {
        const eventCount = this.events.length;
        this.events.push({ ...newEvent, id: eventCount + 1 });
        this.closeAddEventModal();
      },
    },
  };
  </script>
  
  <style scoped>
  /* Event Category Styling - Bold gray text without background or border */
  .event-category {
    font-weight: bold;
    color: #4A4A4A; /* Dark gray color */
    font-size: 1.1rem;
    text-align: center;
  }
  </style>
  