<template>
    <div>dasd</div>
    <button @click="updateFunc()">testttttt</button>
</template>

<script>
import { Loader } from '@googlemaps/js-api-loader';

export default {
  name: 'route',
  data() {
      return {
          loader: null,
          apiKey: "AIzaSyAQUU4it_YoZqtcEFOb-uREcjjWfTnC3P8",
      }
  },
  async mounted() {
    this.loader = new Loader({
        apiKey: "AIzaSyAQUU4it_YoZqtcEFOb-uREcjjWfTnC3P8",
        version: "weekly",
        libraries: ["directions"]
    });
    },
  methods: {
      updateFunc() {
        this.loader.load()
            .then((google) => {
                const directionsService = new google.maps.DirectionsService();
                directionsService
                .route({
                origin: "Pfaffenwaldring+48+70569+Stuttgart",
                destination: "Rotebühlpl.+41/1+70178+Stuttgart",
                // Note that Javascript allows us to access the constant
                // using square brackets and a string value as its
                // "property."
                travelMode: google.maps.TravelMode["TRANSIT"],
                })
                .then((response) => {
                console.log(response);
                console.log(response["routes"][0]["legs"][0]["departure_time"]);
                console.log(response["routes"][0]["legs"][0]["steps"])
                })
                .catch((e) => window.alert("Directions request failed due to " + e));
        
            })
      }  
  }
}
</script> 