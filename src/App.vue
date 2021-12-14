<template>
  <webcamVideo />
  <h1 id="time">{{ this.time }}</h1>
  <temp />
  <div class="dataContainer">
    <route v-bind:destination="'DHBW'" v-bind:start="'Wohnheim'" />
    <calendar />
  </div>
  {{ this.envVals }}
  <button onclick="this.movementTrigger = !this.movementTrigger"></button>
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
      index: 0,
      envVals: null,
      sql: "SELECT * FROM daten",
      movementTrigger: false,
    };
  },
  mounted() {
    var sqlite3 = require("sqlite3").verbose();
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
