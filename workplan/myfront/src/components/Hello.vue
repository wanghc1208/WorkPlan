<template>
  <el-button value="click me" @click.native="getData">click me</el-button>
  <!--<h1>welecome you come here!</h1>-->
  <!--<h2>{{testData}}</h2>-->

</template>

<script>
  export default {
    data() {
      return {
        testData: [],
        // info: {
        //   user: [],
        //   plan: []
        // },
      }
    },
    created() {
      this.getData()
    },
    methods: {
      getData() {
        this.$http.get('/plan/showplan').then(response => {

          data = eval(response.data)
          console.log(data)
          this.testData = data
          // this.info = data
        }).catch(error => {
          console.log(error)
        })
      }
    }
  }
</script>

<style scoped>

</style>
