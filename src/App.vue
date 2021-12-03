<template>
  <webcamVideo />
  <h1 id="time">{{ this.time }}</h1>
  <button @click="testFunction()">test</button>
  <route v-bind:destination="'DHBW'" v-bind:start="'Wohnheim'" />
</template>

<script>
import webcamVideo from "@/components/video.vue";
import route from "@/components/route.vue";

export default {
  name: "App",
  components: {
    webcamVideo,
    route,
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
    }, 1000);
  },
  methods: {
    testFunction() {
      //console.log(new google.maps.DirectionsService());
      /*this.axios.get(this.api).then((res) => {
        console.log(res)
      });*/
    },
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
  position: fixed;
  left: 0;
  bottom: 0;
  background: #ffffff34;
  padding: 1em 1em 0;
  margin: 1em;
  border-radius: 9px;
  line-height: normal;
}
</style>
