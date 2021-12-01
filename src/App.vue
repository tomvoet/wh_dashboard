<template>
  <webcamVideo />
</template>

<script>
import webcamVideo from '@/components/video.vue'


export default {
  name: 'App',
  components: {
    webcamVideo
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100vh;
  width: 100vw;
}

body {
  margin: 0;
  padding: 0;
}

</style>
