<template>
  <div id="image-selection">
    <el-button @click="getImageData()">测试数据</el-button>
    <el-button @click="sendSelection()">发送选中</el-button>
    <pl-table 
      :datas="this.tableData"
      ref="plTable"
      fixed-columns-roll
      header-drag-style
      use-virtual
      fit
      :show-overflow-tooltip="true"
      :pagination-show="false"
      :highlight-current-row="false"
      >
      <pl-table-column v-for="(itm, index) of this.table_keys"
          :key="index"
          :prop="itm"
          :label="itm"
          :align="'center'"
          >
        <template slot-scope="scope"  >
          <div @click="cellClick(scope.$index, itm)">
            <img v-bind:src="$globals.api_url + '/' + scope.row[itm]['url'] + '?id=' + Math.random()" v-if="table_data_selection_flag[scope.$index][itm]" class="full-image"/>
            <!-- <img v-bind:src="$globals.api_url + '/' + scope.row[itm]['url'] + '?id=' + Math.random()" v-if="scope.row[itm]['sel']" class="full-image"/> -->
            <img v-bind:src="$globals.api_url + '/' + scope.row[itm]['url'] + '?id=' + Math.random()" v-else class="small-image"/>
          </div>
        </template>
      </pl-table-column>
    </pl-table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
      return {
        tableData: [],
        table_data_selection_flag:[],
        img_length: 0
      }
    },

  computed: {
    table_keys: function(){
      var keys = []
      if (this.tableData.length == 0){
        console.log('table empty')
      } else {
        console.log('table length: ', this.tableData.length)
        keys = Object.keys(this.tableData[0])
        for(var i=0;i<this.tableData.length;i++){
          var tmp_obj={}
          for(var j=0;j<keys.length;j++){
            tmp_obj[keys[j]]=false
          }
          this.table_data_selection_flag.push(tmp_obj)
        }
      }
      return keys
    },
  },

  methods: {
    getImageData() {
      axios.get(this.$globals.api_url + '/list_imgs').then(
        response=>{
          var tmp_tableData = []
          var rawData = response.data
          this.img_length = rawData.length
          // reorganize tableData
          var n_cols = 5
          for(var idx=0; idx< Math.ceil(rawData.length/n_cols); ++idx){
            var tmp_obj = {}
            for(var jdx=0; jdx<n_cols; ++jdx){
              if(idx * n_cols + jdx < rawData.length){
                tmp_obj[jdx] = rawData[4 * idx + jdx]
              } else {
                tmp_obj[jdx] = {
                  'url': 'invalid',
                  'info': 'None',
                }
              }
            }
            tmp_tableData.push(tmp_obj)
          }
          this.tableData = tmp_tableData
        }).catch(error=>{
        console.log(error)
      })
    },

    sendSelection() {
      var res = []
      for(var idx=0;idx<this.tableData.length;++idx){
        var tmp_obj = this.tableData[idx]
        for(var key in tmp_obj){
          if (this.table_data_selection_flag[idx][key]) {
            res.push(tmp_obj[key]['url'])
          }
        }
      }
      axios.post(this.$globals.api_url+'/selected',res)
    },

    cellClick(row_index, itm) {
      // console.log(row_index)
      // console.log(col_index)
      this.table_data_selection_flag[row_index][itm] = !this.table_data_selection_flag[row_index][itm]
      console.log(this.table_data_selection_flag[row_index][itm])
    },

  }
}
</script>

<style>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}
  
/* .el-aside {
  color: #333;
} */

.full-image {
  width: 100%
}

.small-image {
  width: 50%
}
</style>
