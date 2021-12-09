<template>
  <div id="calendarContainer">
    <div class="event" v-for="event of this.events" :key="event">
      {{
        event.start.getDate().toString() +
        ". " +
        (event.start.getMonth() + 1).toString() +
        ". " +
        event.summary
      }}
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
</style>