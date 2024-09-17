<template>
  <div>
    <Jumbotron />
    <hr/>
    <Midsection />
  </div>
</template>

<script>
// @ is an alias to /src
import Jumbotron from '@/components/home/Jumbotron.vue';
import Midsection from '@/components/home/Midsection.vue';

export default {
  name: 'HomeView',
  components: {
    Jumbotron, 
    Midsection, 
  }
}
</script>
