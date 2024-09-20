<template>
    <div>
      <div class="pic-row">
        <div class="generic-pic-styling left-image">
        </div>
        <div>
        </div>
        <div class="generic-pic-styling right-image">
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
  margin-top: 50px;
}

.generic-pic-styling {
  height: 60vh;
  background-size: 65%; /* Slightly increases the width */
  background-position: center center;
}

.left-image {
  background: url("../../assets/images/Israel_flag.jpg") center/contain no-repeat
}

.right-image {
  background: url("../../assets/images/Palestinain_flag.jpg") center/contain no-repeat;
}

</style>
