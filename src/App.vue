<template>
  <webcamVideo />
  <h1 id="time">{{ this.time }}</h1>
  <temp />
  <div class="dataContainer">
    <route v-bind:destination="'DHBW'" v-bind:start="'Wohnheim'" />
    <calendar />
  </div>
</template>

<script>
import webcamVideo from "@/components/video.vue";
import route from "@/components/route.vue";
import temp from "@/components/temp.vue";
import calendar from "@/components/calendar.vue";

export default {
  name: "App",
  components: {
    webcamVideo,
    route,
    temp,
    calendar,
  },
  data() {
    return {
      time: null,
      interval: null,
    };
  },
  mounted() {
    this.interval = setInterval(() => {
      this.time = new Date().toLocaleTimeString();
      document.getElementById('calendarContainer').style.height = document.getElementById('routeContainer').offsetHeight + 'px'
    }, 1000);
  },
};
</script>

<style>
#app {
  font-family: "MetricHPE", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
}

#time {
  color: white;
  text-align: center;
  font-size: 5em;
  font-weight: 300;
}

#routeContainer {
  background: #ffffff34;
  padding: 1em 1em 0;
  margin: 1em;
  border-radius: 9px;
  height: max-content;
}

#calendarContainer {
  background: #ffffff34;
  width: 40%;
  margin: 1em;
  border-radius: 9px;
  overflow: hidden;
}

.dataContainer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
}
</style>
