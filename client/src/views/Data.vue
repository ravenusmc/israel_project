<template>
    <div>
        <h2 class="center">Examining The Data</h2>

        <div class="graph-area">
            <Avgage />
            <Deathsbygroup />
        </div>

    </div>
</template>

<script>
import Avgage from '@/components/graphs/Avgage.vue'
import Deathsbygroup from '@/components/graphs/Deathsbygroup.vue'

export default {
	name: "Missing",
	components: {
		Avgage,
        Deathsbygroup,
  },
};

</script>

<style scoped>
.graph-area {
    display: grid; 
    grid-template-columns: 1fr 1fr;
}
</style>