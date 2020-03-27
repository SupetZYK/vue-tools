<template>
  <div id="table-viewer">
    <!-- <el-table :data="tableData">
      <el-table-column v-for="(itm, index) of headers"
      :key="index"
      :prop="itm"
      :label="itm"
      >
        <template slot-scope="scope">
          <el-input v-model="scope.row[itm]"></el-input>
        </template>
      </el-table-column>
    </el-table> -->
    <el-button @click="getTestCSV()">获取测试CSV</el-button>
    <el-button @click="saveCSV()">保存CSV</el-button>
    <dynamic-table :table_data="tableData"></dynamic-table>
    <!-- <span>"{{tableData[0]}}"</span> -->
  </div>
</template>

<script>
import DynamicTable from '../components/DynamicTable'
import axios from 'axios'

export default {
  components: {
    "dynamic-table": DynamicTable
  },
  data() {
      return {
        tableData: [
        {
          // index: 0,
          date: "2016-05-03",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          // index: 1,
          date: "2016-05-02",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          // index: 2,
          date: "2016-05-04",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          // index: 3,
          date: "2016-05-01",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          // index: 4,
          date: "2016-05-08",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          // index: 5,
          date: "2016-05-06",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          // index: 6,
          date: "2016-05-07",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        }
      ],
      }
    },
  
  methods: {
     csvToObject(csvString){
        var csvarry = csvString.split("\r\n");
        var datas = [];
        var headers = csvarry[0].split(",");
        for(var i = 1;i<csvarry.length;i++){
            var data = {};
            data['index'] = i
            // if (i >=100) {
            //   break;
            // }
            var temp = csvarry[i].split(",");
                 for(var j = 0;j<temp.length;j++){
                     data[headers[j]] = temp[j];
                 }
            datas.push(data);
        }
         return datas;
    },

    getTestCSV() {
      axios.get(this.$globals.api_url + '/test_csv').then(
        response=>{
          this.tableData = this.csvToObject(response.data)
          console.log('read_csv')
          console.log(this.tableData[0])
        }
      ).catch(error=>{
        console.log(error)
      })
    },

    saveCSV() {
      console.log('save')
      var res = this.object_list2CSV(this.tableData)
      console.log(res)
      axios.post(this.$globals.api_url+'/save_csv',res)
    },

    object_list2CSV(obj_list) {
      if(obj_list.length == 0){
        return ''
      }
      //title ["","",""]
      var title = Object.keys(obj_list[0])
      //titleForKey ["","",""]
      var str = [];
      str.push(title.join(","));
      for(var i=0;i<obj_list.length;i++){
          var temp = [];
          for(var j=0;j<title.length;j++){
              temp.push(obj_list[i][title[j]]);
          }
        str.push(temp.join(","));
      }
      return str.join("\r\n")
    }
  }
}
</script>
