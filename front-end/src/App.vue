<template>
  <div id="app">
    <div class="map" id="map-container"></div>
  </div>
</template>

<script>
import AMap from 'AMap'
export default {
  name: 'App',
  data () {
    return {
      msg: 'hello'
    }
  },
  mounted () {
    this.init()
  },
  methods: {
    init: function () {
      let map = new AMap.Map('map-container', {
        center: [116.397, 39.90923],
        resizeEnable: true,
        zoom: 20
        // mapStyle: 'amap://styles/grey'
      })
      AMap.plugin(['AMap.ToolBar', 'AMap.Scale'], function () {
        map.addControl(new AMap.ToolBar())
        map.addControl(new AMap.Scale())
      })
    }
  }
}
</script>

<style>
#app {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#map-container {
  margin: 0;
  width: 100%;
  height: 100%;
}
</style>
