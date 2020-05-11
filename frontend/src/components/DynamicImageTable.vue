<template>
  <div style="height: 1500px; width: 100%">
    <pl-table 
      :datas="table_data"
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
            <img v-bind:src="$globals.api_url + '/' + scope.row[itm] + '?id=' + Math.random()" v-if="table_data_attr[scope.$index][itm]" class="full-image"/>
            <img v-bind:src="$globals.api_url + '/' + scope.row[itm] + '?id=' + Math.random()" v-else class="small-image"/>
          </div>
        </template>
      </pl-table-column>
    </pl-table>
  </div>
</template>

<script>
export default {
  props:["table_data"],
  data() {
    return {
      table_data_attr:[]
    }
  },
  computed: {
    table_keys: function(){
      var keys = []
      if (this.table_data.length == 0){
        console.log('table empty')
      } else {
        console.log('table length: ', this.table_data.length)
        keys = Object.keys(this.table_data[0])
        for(var i=0;i<this.table_data.length;i++){
          var tmp_obj={}
          for(var j=0;j<keys.length;j++){
            tmp_obj[keys[j]]=false
          }
          this.table_data_attr.push(tmp_obj)
        }
        console.log(this.table_data_attr)
      }
      return keys
    },
  },
  
  methods: {
    cellClick(row_index, itm) {
      // console.log(row_index)
      // console.log(col_index)
      this.table_data_attr[row_index][itm] = !this.table_data_attr[row_index][itm]
    },
  }

}

</script>

<style scoped>
.full-image {
  width: 100%
}

.small-image {
  width: 50%
}
</style>