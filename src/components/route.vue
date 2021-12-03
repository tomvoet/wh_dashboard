<template>
    <button @click="updateFunc()">testttttt</button>
    <div id="routeContainer" v-if="this.route != {}">
        <div id="routeHeader">
            <div id="start">
            {{this.start}}<br><b>{{this.route["departure_time"]}}</b>
            </div>
            <div>
            {{this.route["distance"]}}<br>{{this.route["duration"]}}
            </div>
            <div id="end">
            {{this.destination}}<br><b>{{this.route["arrival_time"]}}</b>
            </div>
        </div>
        <div class="stepContainer" v-for="step in this.route['steps']" :key="step['instructions']">
            <div class="stepArrowContainer">
                <div></div>
                <div v-if="this.route['steps'].indexOf(step) != this.route['steps'].length - 1"></div>
            </div>
            <div class="step sbahn" v-if="step['type'] == 'TRANSIT'">
                <span class="stepMain" v-if="this.route['steps'].indexOf(step) != this.route['steps'].length - 1">{{step.instructions}}</span>
                <span class="stepMain" v-else>{{this.destination}}</span>
                <br>
                <span class="stepData">{{step.duration + " | " + step.distance}}</span>            
                <div>dasd</div>
            </div>
            <div class="step" v-else>
                <span class="stepMain" v-if="this.route['steps'].indexOf(step) != this.route['steps'].length - 1">{{step.instructions}}</span>
                <span class="stepMain" v-else>{{this.destination}}</span>
                <br>
                <span class="stepData">{{step.duration + " | " + step.distance}}</span>
            </div>
        </div>
    </div>
</template>

<script>
import { Loader } from '@googlemaps/js-api-loader';
import keys from '../../keys.json'

export default {
  name: 'route',
  data() {
      return {
          loader: null,
          route: {},
          addresses: {
              "DHBW": "DHBW Rotebühlpl. 41/1 Stuttgart",
              "Wohnheim": "Pfaffenwaldring 48 Stuttgart"
          }
      }
  },
  props: {
    destination: String,
    start: String
  },
  async mounted() {
    this.loader = new Loader({
        apiKey: keys["api"], //insert google-cloud api key
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
                origin: this.addresses[this.start],
                destination: this.addresses[this.destination],
                travelMode: google.maps.TravelMode["TRANSIT"],
                })
                .then((response) => {
                this.route["arrival_time"] = response["routes"][0]["legs"][0]["arrival_time"]["text"]
                this.route["departure_time"] = response["routes"][0]["legs"][0]["departure_time"]["text"]
                this.route["duration"] = response["routes"][0]["legs"][0]["duration"]["text"]
                this.route["distance"] = response["routes"][0]["legs"][0]["distance"]["text"]
                this.route["start_address"] = response["routes"][0]["legs"][0]["start_address"]
                this.route["end_address"] = response["routes"][0]["legs"][0]["end_address"]
                this.route["steps"] = []

                for(var step of response["routes"][0]["legs"][0]["steps"]) {
                    var obj = {};
                    obj["instructions"] = step["instructions"]
                    obj["distance"] = step["distance"]["text"]
                    obj["duration"] = step["duration"]["text"]
                    if (step["travel_mode"] == "TRANSIT") {
                        obj["type"] = "TRANSIT"
                        obj["arrival_stop"] = step["transit"]["arrival_stop"]["name"]
                        obj["arrival_time"] = step["transit"]["arrival_time"]["text"]
                        obj["departure_stop"] = step["transit"]["departure_stop"]["name"]
                        obj["departure_time"] = step["transit"]["departure_time"]["text"]
                        obj["headsign"] = step["transit"]["headsign"]
                        obj["short_name"] = step["transit"]["line"]["short_name"]
                    }
                    this.route["steps"].push(obj)
                }
                console.log(this.route)
                })
                .catch((e) => window.alert("Directions request failed due to " + e));
        
            })
      }  
  }
}
</script> 

<style scoped>
#routeHeader {
    background: #FFBC44;
    padding: 1em;
    width: 100%;
    border-radius: 9px;
    display: flex;
    justify-content: space-around;
    align-items: center;
}

#routeHeader>div {
    width: max-content;
    flex-basis: 100%;
    text-align: center;
}

#routeContainer {
    width: 40%;
}

.stepContainer {
    width: 100%;
    flex-direction: row;
    display: flex;
    align-items: stretch;
}

.step {
    background-color: #00C8FF;
    border-radius: 9px;    
    padding: 1em;
    margin: 1em 0;
    width: 80%;
}

.sbahn {
    background-color: #17EBA0;
}

.stepArrowContainer {
    width: 20%;
}

.stepArrowContainer>div:first-child {
    height: 50%;
    border-left: 2px solid white;
    border-bottom: 2px solid white;
    width: 50%;
    margin-left: 50%;
}

.stepArrowContainer>div:last-child {
    height: 50%;
    border-left: 2px solid white;
    width: 50%;
    margin-left: 50%;
}

#start, #end {
    font-size: 1.2em;
}

.stepMain {
    font-weight: 600;
    font-size: 1.1em;
}

</style>