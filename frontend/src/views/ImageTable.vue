<template>
  <div id="table-viewer">
    <el-button @click="getImageData()">测试数据</el-button>
    <image-table :table_data="tableData"></image-table>
    <!-- <span>"{{tableData[0]}}"</span> -->
  </div>
</template>

<script>
import ImageTable from '../components/ImageTable'
import axios from 'axios'

export default {
  components: {
    "image-table": ImageTable
  },
  data() {
      return {
        tableData: []
      }
    },
    methods: {
      getImageData() {
        axios.get(this.$globals.api_url + '/random_imgs').then(
          response=>{
            this.tableData = response.data
            console.log(this.tableData)
          }).catch(error=>{
          console.log(error)
        })
      }
    }
}
</script>

<style>
.el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  
  .el-aside {
    color: #333;
  }
</style>
