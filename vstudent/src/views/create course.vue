<template>
  <div id="app">
    <el-row :gutter="20">
      <el-col :span="12" :offset="6">
        <div class="grid-content bg-purple font">
           Course details
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="24">

      <el-col :span="24">
        <el-button @click="gouBack">return</el-button>
        <el-form :model="ruleForm"  ref="ruleFormRef" label-width="100px" class="demo-ruleForm">
          <el-form-item label="Name" prop="name">
            <el-input v-model="ruleForm.name" disabled></el-input>
          </el-form-item>

          <el-form-item label="Time" required>
            <el-col :span="11">
              <el-form-item prop="date1">
                <el-date-picker
        v-model="ruleForm.date1"
        type="date"
        placeholder="Date" disabled
        format="YYYY/MM/DD"
        value-format="YYYY-MM-DD"
      />
              </el-form-item>
            </el-col>
            <el-col class="line" :span="2">-</el-col>
            <el-col :span="11">
              <el-form-item prop="date2">
                <el-time-picker placeholder="Time" disabled value-format="HH:mm:ss" v-model="ruleForm.date2"
                style="width: 100%;"></el-time-picker>
              </el-form-item>
            </el-col>
          </el-form-item>


          <el-form-item label="Details" prop="desc">
            <el-input type="textarea" disabled  v-model="ruleForm.description"></el-input>
          </el-form-item>
          
        </el-form>
      </el-col>
    </el-row>




  </div>

</template>

<script setup>
import { ref,reactive } from 'vue'
import { ElMessage as Message, ElMessageBox as MessageBox } from 'element-plus'
import{ addCourse,getCourse,updateCourse, } from '../api/course'
import { useRoute,useRouter } from 'vue-router';
const router = useRouter();
const route = useRoute();
let ruleForm = ref({})
console.log(666)
getCourse(route.params.id).then(res=>{

 ruleForm.value = res.data;
});
function gouBack(){
  router.go(-1)
}
function  submitForm(){
  if(!ruleForm.id){
    addCourse(ruleForm).then(res=>{
      if(res.code==200){
        Message({
          message: res.msg,
          type: 'success'
        })
        resetForm();
      }
    })
  }else{

  }
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