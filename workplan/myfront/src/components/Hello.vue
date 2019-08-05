<template >
  <el-button value="click me" @click.native="getData">click me</el-button>
  <p>welecome you  come here!</p>
  <span>{{testData}}</span>

  <!--<el-tag>{{ getData }}</el-tag>-->

</template>

<script>
export default{
  data () {
    return {
      testData: []
    }
  },
  created () {
    this.getData()
  },
  methods: {
    getData () {
      this.$http.get('/plan/showplan').then(response => {
        this.testData = response.data.body
        console.log(response.data.body)
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>
