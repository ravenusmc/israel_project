<template>
    <div>
        <h2 class="center">Examining The Data</h2>
        <yearform />
        <div class="graph-area">
            <Avgage />
            <Deathsbygroup />
            <Deathsbyregion />
            <DeathsOfPeopleInEventGraph />
        </div>
    </div>
</template>

<script>
import yearform from '@/components/datapage/Yearform.vue'
import Avgage from '@/components/graphs/Avgage.vue'
import Deathsbygroup from '@/components/graphs/Deathsbygroup.vue'
import Deathsbyregion from '@/components/graphs/Deathsbyregion.vue'
import DeathsOfPeopleInEventGraph from '@/components/graphs/Deathsofpeopleinevent.vue'

export default {
	name: "Missing",
	components: {
    yearform,
	Avgage,
    Deathsbygroup,
    Deathsbyregion,
    DeathsOfPeopleInEventGraph, 
  },
};

</script>

<style scoped>
.graph-area {
    display: grid; 
    grid-template-columns: 1fr 1fr;
    place-items: center; /* Centers items both horizontally and vertically */
}
</style>