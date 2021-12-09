<template>
  <div id="calendarContainer">
    <div class="event" v-for="event of this.events" :key="event">
      <div class="date">
        <div>
        {{ event.start.getDate().toString() + "." }}
        </div>
        <!-- https://mythemeshop.com/wp-content/uploads/2020/01/EventON-.png -->
        <div> 
          {{ (event.start.getMonth() + 1).toString() + "." }}
        </div>
        <div>
          {{ this.weekday[event.start.getDay()] }}
        </div>
      </div>
      {{event.summary}}
    </div>
  </div>
</template>

<script>
import calendar from "raw-loader!../assets/basic.ics";
window.setImmediate = window.setTimeout;

export default {
  name: "calendar",
  data() {
    return {
      events: [],
      weekday: ["So","Mo","Di","Mi","Do","Fr","Sa"]
    };
  },
  methods: {
    parseCalendar() {
      const ical = require("node-ical");
      //var toString = require("stream-to-string");
      this.events = [];
      var heute = new Date();
      ical.async.parseICS(calendar).then((res) => {
        for (var item in res) {
          if (res[item].type == "VEVENT") {
            if (res[item].start >= heute || res[item].rrule != undefined)
              this.events.push(res[item]);
          }
        }
        for (var event of this.events) {
          if (event.rrule != undefined) {
            if (event.start < heute) {
              event.start.setFullYear(heute.getFullYear());
              if (event.start < heute) {
                event.start.setFullYear(heute.getFullYear() + 1);
              }
            }
          }
        }

        this.events.sort((a, b) => {
          return a["start"] - b["start"];
        });
        this.events = this.events.splice(0, 10);
        console.log(this.events);
      });
    },
  },
  mounted() {
    this.$nextTick(() => {
      this.parseCalendar();
      setInterval(() => {
        this.parseCalendar();
      }, 5000 * 60);
    });
  },
};
</script>

<style scoped>
div {
  color: white;
}
.date {
  width: 10%;
  float: left;
}
.event {
  display: flex;
  flex-direction: row;
}
</style>