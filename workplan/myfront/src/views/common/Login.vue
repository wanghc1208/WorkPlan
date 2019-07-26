<template>
  <div class="homeBox">
    <ul class="tyg-div">
      <li>让</li>
      <li>
        <div style="margin-left:20px;">测</div>
      </li>
      <li>
        <div style="margin-left:40px;">试</div>
      </li>
      <li>
        <div style="margin-left:60px;">变</div>
      </li>
      <li>
        <div style="margin-left:80px;">得</div>
      </li>
      <li>
        <div style="margin-left:100px;">轻</div>
      </li>
      <li>
        <div style="margin-left:120px;">松</div>
      </li>
    </ul>
    <div style="width:32%;height: auto;margin-left: 30%">
      <div class="title0">测试平台</div>
      <div class="title1">项目管理、接口管理、用例管理、测试报告、任务设置</div>
      <div class="lun-container">
        <div class="carouse" id="carouse">
          <div class="pic1"><img src="../../assets/page1_0.png" alt="pic1"></div>
          <div class="pic2"><img src="../../assets/page1_1.png" alt="pic2"></div>
          <div class="pic3"><img src="../../assets/page1_2.png" alt="pic3"></div>
        </div>
      </div>
      <img class="img-login" src="../../assets/page1_3.jpg"/>
    </div>
    <el-form :model="loginForm" :rules="rules2" ref="loginForm" label-position="left" label-width="0px"
             class="demo-ruleForm login-container">
      <h3 class="title">用户登录</h3>
      <el-form-item prop="account">
        <el-input type="text" v-model.trim="loginForm.account" auto-complete="off" placeholder="账号"></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input type="password" v-model.trim="loginForm.password" auto-complete="off" placeholder="密码"></el-input>
      </el-form-item>
      <el-checkbox v-model="checked" checked class="remember">记住密码</el-checkbox>
      <el-form-item style="width:100%;">
        <el-button type="primary" style="width:100%;" @click.native.prevent="submitForm" :loading="logining">登录
        </el-button>
        <!--<el-button @click.native.prevent="handleReset2">重置</el-button>-->
      </el-form-item>
    </el-form>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        logining: false,
        loginForm: {
          account: '',
          password: ''
        },
        rules2: {
          account: [
            {required: true, message: '请输入账号', trigger: 'blur'}
            // { validator: validaePass }
          ],
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'}
            // { validator: validaePass2 }
          ]
        },
        checked: true
      }
    },
    methods: {
      /*提交进行判断的函数 */
      submitForm(loginFrom) {
        this.$refs[loginFrom].validate(valid => {  //vue前台的验证规则
          if (valid) {
            let data = new FormData()
            data.append('username', this.loginFrom.name)
            data.append('password', this.loginFrom.pass)
            this.$axios.post('/api/login/', data).then((res) => {
              if (res.data.code == "ok") {
                console.log(12345678)
                this.$router.push({name: "firstpage"})
              }
            })
          } else {
            console.log("error submit!!");
            return false;
          }
        });
      }
    }
  }
</script>

<!--<style lang="scss" scoped>-->
<style scoped>
  .homeBox {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0px;
    background-color: #191c2c;
  }

  .login-container {
    /*box-shadow: 0 0px 8px 0 rgba(0, 0, 0, 0.06), 0 1px 0px 0 rgba(0, 0, 0, 0.02);*/
    position: absolute;
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-border-radius: 5px;
    background-clip: padding-box;
    /*margin: 180px auto;*/
    /*margin-top: 10%;*/
    /*right: 50px;*/
    width: 300px;
    padding: 35px 35px 15px 35px;
    background: #23305a;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
    z-index: 1000;
    float: right;
    right: 4%;
    top: 25%;
  }

  .title {
    margin: 0px auto 40px auto;
    text-align: center;
    color: #2ec0f6;
  }

  .remember {
    margin: 0px 0px 35px 0px;
    color: #eaeaea;
  }

  .img-login {
    margin-top: -35%;
    width: 100%;
    height: auto;
  }

  .title0 {
    position: absolute;
    top: 10%;
    left: -41px;
    width: 100%;
    text-align: center;
    color: #2ec0f6;
    font-size: 40px;
    height: 70px;
    line-height: 70px;
    /*<!--margin: -300px 0 0 0;-->*/
    z-index: 1000;
  }

  .title1 {
    position: absolute;
    top: 16%;
    left: -41px;
    width: 100%;
    text-align: center;
    color: #eaeaea;
    font-size: 20px;
    height: 70px;
    line-height: 70px;
    /*<!--margin: -300px 0 0 0;-->*/
    z-index: 1000;
    margin-top: 25px;
  }

  .tyg-div {
    color: #2ec0f6;
    z-index: -1000;
    float: left;
    position: absolute;
    left: 5%;
    top: 20%;
    font-size: 30px;
    list-style-type: none
  }

  .lun-container {
    width: 210px;
    height: 140px;
    position: relative;
    font-size: 32px;
    color: #FFFFFF;
    text-align: center;
    line-height: 90px;
    margin: 200px auto;
    margin-bottom: 0px;
    margin-top: 48%;
    perspective: 1000px;
    z-index: 1000;
  }

  .carouse {
    transform-style: preserve-3d;

  }

  .carouse div {
    display: block;
    position: absolute;
    width: 140px;
    height: 90px;
  }

  .carouse .pic1 {
    transform: rotateY(0deg) translateZ(160px);
  }

  .carouse .pic2 {
    transform: rotateY(120deg) translateZ(160px);
  }

  .carouse .pic3 {
    transform: rotateY(240deg) translateZ(160px);
  }

  /*=== 下一个动画 ===*/
  @keyframes to-scroll1 {
    0% {
      transform: rotateY(0deg);
    }

    33% {
      transform: rotateY(-120deg);

    }
    66% {
      transform: rotateY(-240deg);

    }
    100% {
      transform: rotateY(-360deg);

    }

  }

  #carouse1 {
    animation: to-scroll1 10s ease infinite;
    /*animation-fill-mode: both;*/
  }
</style>

