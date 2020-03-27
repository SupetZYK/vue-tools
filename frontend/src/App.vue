<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <el-container>
      <el-header style="text-align: right; font-size: 12px"></el-header>
      <el-container>
        <el-aside width="200px">
          <el-menu router :default-active="$route.path">
            <el-menu-item index="/">Home</el-menu-item>
            <el-menu-item index="/table">Table</el-menu-item>
            <el-menu-item index="/test_table">TestTable</el-menu-item>
            <el-menu-item index="/image_table">Images</el-menu-item>
            <el-menu-item index="/api">API</el-menu-item>
            <el-menu-item index="/about">About</el-menu-item>
          </el-menu>
        </el-aside>
        <el-main>
          <keep-alive>
            <router-view v-if="$route.meta.keepAlive"></router-view>
          </keep-alive>
          <router-view v-if="!$route.meta.keepAlive"></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import Home from './components/Home.vue'
// import About from './components/About.vue'

export default {
  name: "App",
  components: {}
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
}

.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
  border-bottom: 0;
}

/* .el-container {
  border-bottom: 2px solid red;
} */

.el-main {
  position: absolute;
  left: 200px;
  right: 0;
  top: 75px;
  bottom: 0;
  overflow-y: scroll;
  border-bottom: 0;
}
</style>
