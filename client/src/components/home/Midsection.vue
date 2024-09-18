<template>
    <div>
      <div class="pic-row">
        <div class="left-image">
        </div>
        <div>
        </div>
        <div class="'right-image'">
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: "Midsection"
};
</script>

<style scoped>

.pic-row {
  display: grid; 
  grid-template-columns: 1fr 1fr 1fr;

}

.left-image {
  margin-top: 28px;
  height: 60vh;
  background: url("../../assets/images/Israel_flag.jpg") center/contain no-repeat;
  background-position: center center;
  background-size: 65%; /* Slightly increases the width */
  display: flex;
  justify-content: center;
  align-items: center;
}


</style>
