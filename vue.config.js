/*module.exports = {
    devServer: {
      hot: false,
      liveReload: false
    }
  }
  */
  module.exports = {
    pluginOptions: {
      electronBuilder: {
        nodeIntegration: true,
        contextIsolation: false
      }
    }
  }