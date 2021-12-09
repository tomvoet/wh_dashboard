<template>
    <iframe id="video" src="http://localhost:8081"></iframe>
    <div id="filter"></div>
</template>

<script>
export default {
  name: 'webcamVideo',
  mounted() {
    //console.log(require ("python-shell"))
    //test
    /*
    var video = document.querySelector("#video");

    if (navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({
        video: true
      }).then(
        stream => (video.srcObject = stream),
        err => console.log(err)
      );
    }
    */
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
        object-fit: cover;
        object-position: center;
        z-index: -5;
    }

    #filter {
        width: 100vw;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        backdrop-filter: brightness(1);
        z-index: -5;
    }
</style>