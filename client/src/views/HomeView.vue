<template>
  <div>
    <Jumbotron />
    <hr/>
    <Midsection />
    <hr/>
    <Bottom />
  </div>
</template>

<script>
// @ is an alias to /src
import Jumbotron from '@/components/home/Jumbotron.vue';
import Midsection from '@/components/home/Midsection.vue';
import Bottom from '@/components/home/Bottom.vue';

export default {
  name: 'HomeView',
  components: {
    Jumbotron, 
    Midsection, 
    Bottom,
  }
}
</script>
