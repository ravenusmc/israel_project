<template>
    <div>
        <div class="main-image">
        <div class="title-div">
            <h1 class="center">Israel and Palestine</h1>
            <hr />
            <h3 class="center">A Study of People Killed</h3>
        </div>
        </div>
    </div>
</template>

<script>
export default {
  name: "Jumbotron"
};
</script>

<style scoped>
.main-image {
  margin-top: 28px;
  height: 80vh;
  background: url("../../assets/images/destruction.gif") center/contain no-repeat;
  background-position: center center;
  background-size: 65%; /* Slightly increases the width */
  display: flex;
  justify-content: center;
  align-items: center;
}

.title-div {
  background-color: rgba(0, 0, 0, 0.6);
  border-radius: 15px;
  color: white;
  padding: 20px;
}

.center {
  text-align: center;
}
</style>

