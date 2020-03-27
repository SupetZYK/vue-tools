<template>
  <div>
    <el-table :data="this.table_data">
      <el-table-column v-for="(itm, index) of this.table_keys"
          :key="index"
          :prop="itm"
          :label="itm"
          >
        <template slot-scope="scope">
          <img v-bind:src="$globals.api_url + '/' + scope.row[itm] + '?id=' + Math.random()"/>
          <!-- <el-input v-model="scope.row[itm]"></el-input> -->
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  props:["table_data"],
  computed: {
    table_keys: function(){
      if (this.table_data.length == 0){
        return []
      } else {
        return Object.keys(this.table_data[0])
      }
    },
  }
}

</script>

<style scoped>

</style>