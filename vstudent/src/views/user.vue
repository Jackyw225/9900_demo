<template>
  <div id="app">
    <el-row :gutter="20">
      <el-col :span="12" :offset="6">
        <div class="grid-content bg-purple font">
          User Profile
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="24">

      <el-col :span="24">
        <el-form :model="ruleForm"  ref="ruleFormRef" label-width="100px" class="demo-ruleForm">
          <el-form-item label="email" prop="email">
            <el-input disabled v-model="ruleForm.email" ></el-input>
          </el-form-item>
          <el-form-item label="name" prop="name">
            <el-input  v-model="ruleForm.name" ></el-input>
          </el-form-item>

          <el-form-item label="phone" prop="phone">
            <el-input v-model="ruleForm.phone" ></el-input>
          </el-form-item>
       
          <el-form-item label="address" prop="address">
            <el-input v-model="ruleForm.address" ></el-input>
          </el-form-item>
          <el-form-item label="Education Experience" prop="desc">
            <el-input type="textarea" v-model="ruleForm.experience"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="updateUserInfo('ruleForm')">update</el-button>
         
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>




  </div>

</template>

<script setup>
import { ref,reactive } from 'vue'
import { ElMessage as Message, ElMessageBox as MessageBox } from 'element-plus'
import {getUser,updateUser} from '../api/user'




const ruleForm = reactive({})
function resetForm() {
  Object.assign(ruleForm, {
    name: '',
    date1: '',
    date2: '',
    desc: ''
  })
}
function getUserInfo(){
  getUser(localStorage.getItem('token')).then(res=>{
    Object.assign(ruleForm, res.data)

  })
}
getUserInfo();

function updateUserInfo(){
  updateUser(ruleForm).then(res=>{
    Message.success('update success')
  })
}
</script>

<style lang="scss" scoped>
.font {
  text-align: center;
  /* 文本居中对齐 */
  font-size: 26px;
}

.el-row {
  margin-bottom: 20px;

  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

#app {
  box-sizing: border-box;
  padding: 20px;
}
</style>