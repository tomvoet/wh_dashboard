<template>
    <video autoplay="true" id="video"></video>
</template>

<script>
export default {
  name: 'webcamVideo',
  mounted() {
    var video = document.querySelector("#video");

    if (navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({
        video: true
      }).then(
        stream => (video.srcObject = stream),
        err => console.log(err)
      );
    }
  }
}
</script>

<style scoped>
    #video {
        width: 100vw;
        height: 100vh;
        transform: scaleX(-1)
    }
</style>