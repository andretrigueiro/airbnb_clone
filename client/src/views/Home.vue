<template>
  <div class="home">
    <img alt="Night Accommodation" src="../assets/outdoor_night.jpg" width="80%">
    <Locations/>
    <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Footer from '@/components/home/Footer.vue';
import Locations from '@/components/home/Locations.vue';

export default {
  name: 'Home',
  components: {
    Footer,
    Locations,
  },
};
</script>
