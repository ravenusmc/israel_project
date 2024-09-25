<template>
    <div>
      <div class="pic-row">
        <div class="generic-pic-styling left-image">
        </div>
        <div class="paragraph-div">
          <h1 class="title center">Purpose</h1>
          <p>As I write these words it appears that a war may erupt between Israel and Lebannon.
            I've built quite a few data science projects and some of them look at wars. I've always
            been fascinated with the Israeli-Palestinian conflict. 
          </p>
          <p>
            Weeks ago, I was going through Kaggle and I found a dataset on the conflict. I started 
            to look through it and decided that I'd be using it for this project. I have quite a few 
            graphs built for this and please enter and review them. 
          </p>
          <p>
            Finally, I will say that I'll stay fairly neutral on this conflict and let the data 
            speak for itself. Yet, I find that the data can only tell so much of a story. These 
            were real people who were killed. They had lives, families and so much to live for in 
            the future.
          </p>
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
  align-items: center;
}

.title {
  text-transform: uppercase;
}

.generic-pic-styling {
  height: 80vh;
  background-position: center center;
  margin: 0 7% 0 7%;
}

.left-image {
  background: url("../../assets/images/Israel_flag.jpg") center/contain no-repeat
}

.right-image {
  background: url("../../assets/images/Palestinain_flag.jpg") center/contain no-repeat;
}

@media only screen and (max-width: 950px) {

  .pic-row { 
    grid-template-columns: 1fr;
  }

  .paragraph-div {
    margin: 0 10% 0 10%;
  }

}

</style>
