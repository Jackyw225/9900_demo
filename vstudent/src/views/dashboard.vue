<template>
  <div class="navbar">
      <div>
        <span class="nav-item">Dashboard</span>
        <span class="nav-item selected">My course</span>
      </div>
      <div>
        <span class="nav-item">icon</span>
      </div>
    </div>

    <div class="main-content">
      <div class="card">
        <div class="card-header">Timeline</div>
        <div class="card-content" v-for="item of dataList">{{item.date2}}</div>
      </div>

      <div class="card">
        <div class="card-header">Course overview</div>
        <div class="card-content" v-for="item of dataList">{{item.name}}</div>
      </div>
    </div>

</template>

<script setup>
import { ref,reactive } from 'vue'
import { ElMessage as Message, ElMessageBox as MessageBox } from 'element-plus'
import {getUser,updateUser} from '../api/user'
import { findByStudentId } from '../api/course';
import {listAll} from '../api/course'
const dataList = ref([]);
const user = ref({})
getUser(localStorage.getItem('token')).then(res => {
  user.value = res.data;
  if (user.value.type == 2) {
    listAll().then(res => {
      dataList.value = res.data ? res.data : [];
    })
  } else {
    findByStudentId().then(res => {
      dataList.value = res.data ? res.data : [];
    })

  }
})

</script>

<style lang="scss" scoped>
   .navbar {
        display: flex;
        justify-content: space-between;
        padding: 10px;
        background-color: #296bef;
      }

      .main-content {
        display: flex;
        justify-content: space-around;
        padding: 20px;
      }

      .card {
        width: 40%;
        border: 1px solid #ccc;
        padding: 20px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
      }

      .card-header {
        background-color: #4caf50; /* 绿色背景 */
        color: white; /* 白色文本 */
        padding: 10px;
        margin-bottom: 15px; /* 添加一些底部边距 */
      }

      .card-content {
        background-color: #f8f8f8; /* 浅灰色背景 */
        color: black; /* 黑色文本 */
        padding: 10px;
      }

      .nav-item {
        margin-right: 10px;
        cursor: pointer;
      }
</style>