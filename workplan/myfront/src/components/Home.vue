<template>

  <el-table
    :data="tableData"
    height
    style="width: 100%">
    <el-table-column prop="group" label="小组" width="120"></el-table-column>
    <el-table-column prop="name" label="姓名" width="120"></el-table-column>

    <el-table-column :label=data.time v-for=" data in tableData" :key="key">
      <el-table-column prop="planlist" label="上午" width="120">
        <template slot-scope="scope"  v-for="i in (0,1)">
          {{scope.row.planlist[0].planname.split("@@@")[0]}}
          <!--{{tableData[scope.$index][i]}}-->
          <!--{{tableData[scope.$index][i].planname.split("@@@")[0]}}-->
        </template>
      </el-table-column>
      <el-table-column
        prop="planlist"
        label="下午"
        width="120">
        <template slot-scope="scope" >
          {{scope.row.planlist[0].planname.split("@@@")[1]}}
          <!--{{tableData[scope.$index][i]}}-->
          <!--{{tableData[scope.$index][i].row.planname.split("@@@")[1]}}-->
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
        tableHeader: ["2018-09-08", "2018-09-09", "2018-09-10", "2018-09-11"],
        tableData: [
          {
            group: '错题本',
            name: '王小虎',
            // planlist:[{date:"2018-09-08",planname:"测试1@@@测试2"},{date:"2018-09-09",planname:"测试3@@@测试4"}],
            planlist:[{date:"2018-09-08",planname:"测试1@@@测试2"}],
            time: "2018-09-08",
            // planname: "测试1@@@测试2"
          },
          // {
          //   group: '错题本',
          //   name: '王小虎',
          //   time: "2018-09-09",
          //   planname: "测试3@@@测试4"
          // },
          // {
          //   group: '错题本',
          //   name: '王小虎',
          //   time: "2018-09-09",
          //   planname: "测试5@@@测试6"
          // },
          // {
          //   group: '错题本',
          //   name: '王小虎',
          //   time: "2018-09-09",
          //   planname: "测试7@@@测试8"
          // },

        ]
      }
    },
    methods: {
      show() {
        axios.Get({
          url: '/plan/showplan/',
          params: {},
          callback: (res) => {
            console.log(res);
            let data = res.data;
            console.log(data);
          }
        })
      },
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
