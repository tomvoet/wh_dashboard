<template>
    <video autoplay="true" id="video"></video>
    <div id="filter"></div>
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
        transform: scaleX(-1);
        position: fixed;
        top: 0;
        left: 0;
    }

    #filter {
        width: 100vw;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        backdrop-filter: brightness(.1);
    }
</style>