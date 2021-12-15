<template>
  <webcamVideo />

  <div id="filter" :class="{ active: this.movementTrigger }">
    <button @click="this.movementTrigger = !this.movementTrigger" style="z-index: 1000">test</button>
  </div>

  <h1 id="time" :class="{ active: this.movementTrigger }">{{ this.time }}</h1>
  <temp />
  <div class="dataContainer">
    <route v-bind:destination="'DHBW'" v-bind:start="'Wohnheim'" />
    <calendar />
  </div>
  {{ this.envVals }}<br />
  <button @click="this.movementTrigger = !this.movementTrigger" style="z-index: 1000">test</button>
  <spotify />
</template>

<script>
import webcamVideo from "@/components/video.vue";
import route from "@/components/route.vue";
import temp from "@/components/temp.vue";
import calendar from "@/components/calendar.vue";
import spotify from "@/components/spotify.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    webcamVideo,
    route,
    temp,
    calendar,
    spotify,
  },
  data() {
    return {
      time: null,
      interval: null,
      index: 0,
      envVals: null,
      sql: "SELECT * FROM daten",
      movementTrigger: false,
    };
  },
  mounted() {
    /*
    var db = new sqlite3.Database("C:/wh_smartmirror/db/data.db", (err) => {
      if (err) {
        console.error(err);
      }
    });

    setInterval(() => {
      db.all(this.sql, [], (err, data) => {
        if (err) throw err;
        this.envVals = data[0];
      });
    }, 100);
    */
    setInterval(() => {
      axios.get("http://localhost:8081/get_data").then((res) => {
        this.envVals = res.data;
      });
    }, 200);

    this.interval = setInterval(() => {
      this.time = new Date().toLocaleTimeString();
      document.getElementById("calendarContainer").style.height =
        document.getElementById("routeContainer").offsetHeight + "px";
    }, 1000);
    setInterval(() => {
      document.querySelectorAll(".event")[this.index % 10].scrollIntoView({ behavior: "smooth", block: "end" });
      this.index++;
    }, 5000);
  },
};
</script>

<style>
:root {
  --active-transition-time: 2s;
}

#app {
  font-family: "MetricHPE", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
  background: #474747;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
}

#filter {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  backdrop-filter: brightness(20%);
  z-index: 50;
  transition: backdrop-filter ease-in-out var(--active-transition-time);
}

#filter.active {
  transition: backdrop-filter var(--active-transition-time), z-index ease-in-out calc(var(--active-transition-time) * 2);
  z-index: -50;
  backdrop-filter: brightness(100%);
}

#time {
  color: white;
  width: max-content;
  font-size: 8em;
  font-weight: 300;
  position: fixed;
  top: 20%;
  right: 50%;
  transform: translateX(50%);
  margin: 0;
  padding: 0.25em;
  transition: all var(--active-transition-time);
}

#time.active {
  font-size: 5em;
  top: 0;
  right: 0;
  transform: translateX(0);
}

#routeContainer {
  background: #ffffff10;
  padding: 1em 1em 0;
  margin: 1em;
  border-radius: 9px;
  height: max-content;
}

#calendarContainer {
  background: #ffffff10;
  width: 40%;
  margin: 1em;
  border-radius: 9px;
  overflow: hidden;
  padding: 1em 1em;
}

.dataContainer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.event {
  border-radius: 5px;
  margin-bottom: 1em;
}
</style>
