<template>
  <el-button value="click me" @click.native="getdata">click me</el-button>
</template>

<script>
  export default {
    name: "Hello",
    data() {
      abc = 'hello  world'
    },
    methods() {
      function mounted() {
        this.getdata()
      }

      function getdata() {
        // return 111
        axios
          .post('https://127.0.0.1:8000/plan/showplan')
          .then(response => (this.abc = response))
          .catch(function (error) { // 请求失败处理
            console.log(error);
          });
      }
    }
  }
</script>

<style scoped>

</style>
