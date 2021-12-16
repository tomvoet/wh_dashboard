<template>
  <div @click="test()">
    {{ this.data.temp + "&deg;C " + this.data.humid + "%" }}
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "temp",
  data() {
    return {
      data: { temp: null, humid: null },
    };
  },
  methods: {
    test() {
      axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";

      axios.get("http://192.168.0.103/").then((res) => {
        this.data = res.data;
      });
    },
  },
};
</script>

<style scoped>
div {
  color: black;
}
</style>