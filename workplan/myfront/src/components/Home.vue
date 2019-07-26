<template>
  <el-table
    :data="tableData"
    height
    style="width: 100%">
    <el-table-column prop="group" label="小组" width="120"></el-table-column>
    <el-table-column prop="name" label="姓名" width="120"></el-table-column>
    <el-table-column :label=title[key] v-for="(item,key) in title" :key="key">
      <el-table-column
        prop="morning"
        label="上午"
        width="120">
        <template slot-scope="scope">
          {{scope.row[key*3]}}
        </template>
      </el-table-column>
      <el-table-column
        prop="afternoon"
        label="下午"
        width="120">
        <template slot-scope="scope">
          {{scope.row[key*3+1]}}
        </template>
      </el-table-column>
    </el-table-column>
  </el-table>
</template>

<script>
  export default {
    name: "Home",
    data() {
      return {
        title: ["周一", "周二", "周三", "周四"],
        tableData: [
          {
            group: '错题本',
            name: '王小虎',
            // data:[{morning: "测试1", afternoon: '测试2'},{morning: "测试3", afternoon: '测试4'}]
            // morning: ["测试1", '测试2'],
            // afternoon: ["测试3", '测试4']
            list: [3, 5, 1, 2, 6, 3, 4, 5, 7, 8, 9, 5, 4, 1, 2, 3, 6, 5, 4, 1]

          },

        ]
      }
    },
    methods: {
      change_days() {
        let that = this;
        that.base_title = [];
        let Max_length = that.value;
        console.log(Max_length)
        for (let i = 0; i < Max_length; i++) {
          that.value_date = that.value_dateVal;
          let param = {
            label: that.getDay(i) + "" + (that.getWeek(that.getDay(i).toString())),
            prop: that.getDay(i)
          };
          that.base_title.push(param);
        }
        console.info(that.base_title);
      },
      /**
       * @getDay 获取日期
       * @doHandleMonth
       * @getWeek 获取当前星期
       */
      getDay(day) {
        let that = this;
        let value_day = new Date();
        let target_day_milliseconds = value_day.getTime() + 1000 * 60 * 60 * 24 * day;
        value_day.setTime(target_day_milliseconds); //注意，这行是关键代码
        let tYear = value_day.getFullYear();
        let tMonth = value_day.getMonth();
        let tDate = value_day.getDate();
        tMonth = that.doHandleMonth(tMonth + 1);
        tDate = that.doHandleMonth(tDate);
        return tYear + "-" + tMonth + "-" + tDate;
      },
      getWeek(dateString) {
        let weekArray = ["(星期日)", "(星期一)", "(星期二)", "(星期三)", "(星期四)", "(星期五)", "(星期六)"];
        return weekArray[new Date(dateString).getDay()];
      },
      doHandleMonth(month) {
        let m = month;
        if (month.toString().length === 1) {
          m = "0" + month;
        }
        return m;
      },
    }
  }
</script>

<style scoped>

</style>
