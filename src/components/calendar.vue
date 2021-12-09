<template>
  <div id="calendarContainer">
    <div id="calendarWrapper">
    <div class="event" v-for="event of this.events" :key="event" :style="{backgroundColor: this.colors[this.events.indexOf(event) % this.colors.length] }">
      <div class="date">
        <div>
          <div>
            {{ this.weekday[event.start.getDay()] }} 
          </div>
          <!-- https://mythemeshop.com/wp-content/uploads/2020/01/EventON-.png -->
          <div style="font-size: 1.5em; font-weight: 900;"> 
            {{ event.start.getDate().toString() + "." }}
          </div>
          <div>
            {{ this.months[event.start.getMonth()] }}
          </div>
        </div>
      </div>
      <div class="dateText">
      <span>{{event.summary}}</span>
      </div>
    </div>
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
      weekday: ["So","Mo","Di","Mi","Do","Fr","Sa"],
      colors: ["#17EBA0", "#F740FF", "#00C8FF", "#FC6161", "#FFBC44", "#FFEB59"],
      months: ["Jan.", "Febr.", "März", "Apr.", "Mai", "Juni", "Juli", "Aug.", "Sep.", "Okt.", "Nov.", "Dez."]
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
      /*setInterval(() => {

      }, )*/
    });
  },
};
</script>

<style scoped>
.date {
  width: 14%;
  float: left;
  padding: auto 0;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  padding-top: 4px;
}

.date > div > div {
  width: max-content;
  margin: 0 auto;
}


.event {
  display: flex;
  flex-direction: row;
  color: rgb(36, 36, 36);
}

.dateText {
  flex: 1;
  padding: 1em 1em 1em .1em;
  font-size: 1.5em;
  font-weight: 600;
  display: flex;
  flex-direction: row;
  align-items: center;
}

.dateText > span {
  margin-top: .1em;
}

#calendarWrapper {
  overflow: hidden;
  height: 100%;
  width: 100%;
}
</style>