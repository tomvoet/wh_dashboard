<template>
  <div @click="test()">testttt</div>
</template>

<script>
export default {
  name: "spotify",
  data() {
    return {};
  },
  methods: {
    /*async*/ test() {
      /*
      var SpotifyWebApi = require("spotify-web-api-node");
      var spotifyApi = new SpotifyWebApi();
      spotifyApi.setAccessToken(
        "BQBC8jsN2QMVW1y2o1EXykObTCo_91H85h_mPJ4_Zmu5jRrPSeNcSuVf8-KbIfHw6EFvrmF7IGnFfD6tDvuofTcIzgvbwTzX_Wli4WP_IYUDWeqPu0_oQw85n3ZM8NYsG5-rX9QK5N026icA8OeMiJ0wbr3W0FQKZips"
      );
      spotifyApi.getMyDevices().then((res) => {
        console.log(res.body);
      });
      */
      /*
      const { SpotifyPlaybackSDK } = require("spotify-playback-sdk-node");
      const spotify = new SpotifyPlaybackSDK();
      await spotify.init().then();

      const player = await spotify.createPlayer({
        name: "Web",
        getOAuthToken() {
          // get your Access token here: https://developer.spotify.com/documentation/web-playback-sdk/quick-start/
          return "BQCeY1Jo5rrLEnpJpMHylMHt4d_g-DqeA_7uGy6WeW61OJOKe-kHAIVYzm_qJEirLlqnUzVlxx2W5a3VMc7F6KR--hudJKMJCenuTaoiDtR954wy56m3PYfJgenyYEgX5eY2k5Izz52vgSK0_e_VTvf6sroive_Feusz";
        },
      });
      player.on("player_state_changed", console.log);

      const stream = await player.getAudio();
      const connected = await player.connect();
      if (!connected) throw "couldn't connect";

      console.log("connected", stream);
      */
    },
  },
};
</script>

<style scoped>
</style>