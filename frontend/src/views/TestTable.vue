<template>
  <div id="test-table" style="height: 800px; width:100%">
    <pl-table 
      :datas="tableData" 
      ref="pltTable"
      use-virtual>
      <pl-table-column prop="date" label="日期" width="140"></pl-table-column>
      <pl-table-column prop="name" label="姓名" width="120">
        <!-- <template slot-scope="scope">
          <el-input
            :ref="scope.row.index"
            v-model="scope.row.name"
            v-if="flag[scope.row.index]"
            @blur="loseFocus(scope.$index, scope.row)"
            v-focus
          ></el-input>
          <span style="margin-left: 10px" v-else>{{scope.row.name}}</span>
        </template> -->
      </pl-table-column>
      <pl-table-column prop="address" label="地址"></pl-table-column>
    </pl-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        {
          index: 0,
          date: "2016-05-03",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          index: 1,
          date: "2016-05-02",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          index: 2,
          date: "2016-05-04",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          index: 3,
          date: "2016-05-01",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          index: 4,
          date: "2016-05-08",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          index: 5,
          date: "2016-05-06",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          index: 6,
          date: "2016-05-07",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        }
      ],
      // headers: ['date', 'name', 'address']
      flag: Array(7).fill(false)
    };
  },

  directives: {
    focus: {
      inserted: function(el) {
        el.querySelector('input').focus()
      }
    }
  },

  methods: {
    cellClick(row, column, cell, event) {
      console.log(this.flag[row.index]);
      this.$set(this.flag, row.index, true)
      console.log(this.flag[row.index]);
      // console.log(event)
    },

    loseFocus(index, row) {
      console.log(this.flag[row.index]);
      this.$set(this.flag, row.index, false)
      console.log(this.flag[row.index]);
    }
  }
};
</script>
