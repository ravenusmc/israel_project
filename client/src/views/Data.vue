<template>
    <div>
        <h2 class="center">Examining The Data</h2>
        <div class="form-styling">
          <yearform />
        </div>
        <div class="graph-area">
          <Avgage />
          <Deathsbygroup />
          <Deathsbyregion />
          <DeathsOfPeopleInEventGraph />
        </div>
        <hr>
        <div class="form-styling">
            <InjuryForm />
          </div>
        <div class="graph-area">
          <div>
            <Injurytypegraph v-if="!hideInjuryGraph" />
            <Hideinjurygraph v-if="hideInjuryGraph"/>
          </div>
          <div>
            <Commonammo v-if="!hideInjuryGraph"/>
            <Hideinjurygraph v-if="hideInjuryGraph"/>
          </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from "vuex";
import yearform from '@/components/datapage/Yearform.vue'
import Avgage from '@/components/graphs/Avgage.vue'
import Deathsbygroup from '@/components/graphs/Deathsbygroup.vue'
import Deathsbyregion from '@/components/graphs/Deathsbyregion.vue'
import DeathsOfPeopleInEventGraph from '@/components/graphs/Deathsofpeopleinevent.vue'
import InjuryForm from '@/components/datapage/Injuryform.vue'
import Injurytypegraph from '@/components/graphs/Injurytypegraph.vue'
import Hideinjurygraph from '@/components/support/Hideinjurygraph.vue'
import Commonammo from '@/components/graphs/Commonammo.vue'

export default {
	name: "Missing",
  computed: {
    ...mapGetters("datapage", [
      "hideInjuryGraph",
    ]),
  },
	components: {
    yearform,
	  Avgage,
    Deathsbygroup,
    Deathsbyregion,
    DeathsOfPeopleInEventGraph, 
    InjuryForm,
    Injurytypegraph,
    Hideinjurygraph,
    Commonammo, 
  },
};

</script>

<style scoped>
.graph-area {
    display: grid; 
    grid-template-columns: 1fr 1fr;
    place-items: center; /* Centers items both horizontally and vertically */
}

.form-styling {
  display: flex; 
  justify-content: center;
  margin: 50px 0 50px 0;
}
</style>