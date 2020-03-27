<template>
  <div style="height: 800px; width: 100%">
    <pl-table 
      :datas="table_data"
      ref="plTable"
      fixed-columns-roll
      header-drag-style
      use-virtual
      fit
      :show-overflow-tooltip="true"
      :pagination-show="false"
      :align="'center'"
      >
      <pl-table-column v-for="(itm, index) of this.table_keys"
          :key="index"
          :prop="itm"
          :label="itm"
          :min-width="100"
          >
        <template slot-scope="scope">
          <el-input
          v-model="scope.row[itm]" v-if="row_editable_flags[scope.$index] && col_editable_flags[index]" @blur="loseFocus(scope.$index, index)" v-focus></el-input>
          <span style="margin-left: 10px" v-else @click="cellClick(scope.$index, index)">{{scope.row[itm]}}</span>
        </template>
      </pl-table-column>
    </pl-table>
  </div>
</template>

<script>
export default {
  props:["table_data"],
  computed: {
    table_keys: function(){
      this.row_editable_flags = Array(this.table_data.length).fill(false)
      // init editable_flags
      // for(i=0; i < this.table_data.length; i++) {
      //   this.editable_flags.push(Array(this.))
      // }
      var keys = []
      if (this.table_data.length == 0){
        console.log('table empty')
      } else {
        console.log('table length: ', this.table_data.length)
        keys = Object.keys(this.table_data[0])
        this.col_editable_flags = Array(keys.length).fill(false)
      }


      // for (var jdx = 0; jdx < keys.length; ++jdx) {
      //   this.col_width[keys[jdx]] = 0;
      // }

      // var len_sum = 0;
      // var sample_number = Math.min(50, this.table_data.length);
      // for (var idx = 0; idx < sample_number; idx++) {
      //   for (var jdx = 0; jdx < keys.length; ++jdx) {
      //     var tmp_len = this.getStrLength(
      //       String(this.table_data[idx][keys[jdx]])
      //     );
      //     this.col_width[keys[jdx]] += tmp_len;
      //     len_sum += tmp_len;
      //   }
      // }

      // var final_total_length = Math.min(
      //   parseInt(len_sum / sample_number) * 15,
      //   5000
      // );

      // for (var jdx = 0; jdx < keys.length; ++jdx) {
      //   this.col_width[keys[jdx]] = parseInt(
      //     (this.col_width[keys[jdx]] / len_sum) * final_total_length
      //   );
      //   console.log("width of ", keys[jdx], this.col_width[keys[jdx]]);
      // }

      return keys
    },

  },


  data() {
    return {
      row_editable_flags: [],
      col_editable_flags: [],
      col_width: {}
    }
  },

  methods: {
    
    // tableRowClassName({row, rowIndex}) {
    //   row.index = rowIndex
    // },
    cellClick(row_index, col_index) {
      // console.log(row_index)
      // console.log(col_index)
      this.$set(this.row_editable_flags, row_index, true)
      this.$set(this.col_editable_flags, col_index, true)
    },

    loseFocus(row_index, col_index) {
      // this.$set(this.editable_flags[key], index, false)
      this.$set(this.row_editable_flags, row_index, false)
      this.$set(this.col_editable_flags, col_index, false)
    },

    getStrLength(str) {
      var cArr = str.match(/[^\x00-\xff]/gi);
      return str.length + (cArr == null ? 0 : cArr.length);
    }

    // cellClick(row, column, cell, event) {
    //   this.$set(this.editable_flags, row.index, true)
    // },

    // loseFocus(index, row) {
    //   this.$set(this.editable_flags, row.index, false)
    // }
  },

  directives: {
    focus: {
      inserted: function(el) {
        el.querySelector('input').focus()
        // el.focus()
      }
    }
},

}

</script>

<style scoped>

</style>