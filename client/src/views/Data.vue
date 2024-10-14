<template>
    <div>
        <h2>Examining The Data</h2>

        <div class="graph-area">
            <Avgage />
        </div>

    </div>
</template>

<script>
import Avgage from '@/components/graphs/Avgage.vue'

export default {
	name: "Missing",
	components: {
		Avgage,
  },
};

</script>

<style scoped>
</style>