<template>
  <div id="app">

    <el-container>
      <el-header style="background-color: #1372e5; display: flex; justify-content: space-between; align-items: center;">
        <el-menu default-active="1" class="el-menu-demo" mode="horizontal" @select="handleSelect"
          background-color="#1372e5" text-color="#fff" active-text-color="#ffd04b">
          <el-menu-item index="1">
            <router-link to="/">Dashboard</router-link>
          </el-menu-item>
          <el-menu-item index="2">
            <router-link to="/course"> My Course</router-link>
          </el-menu-item>
        </el-menu>

        <div>
          <div style="float: right;line-height: 40px" @click="exit"> log out</div>
          <el-avatar icon="el-icon-user" @click="goToProfile" style="float: right;margin-right: 15px;"></el-avatar>
        </div>
      </el-header>
    </el-container>

    <el-container>
      <el-aside style="overflow: hidden; min-height: 100vh; background-color: #545c64; width: 250px">
        <el-menu default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose"
          background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
          <el-menu-item index="1" v-for="item of dataList">
            <router-link style="text-align: center;display: block;list-style: none;    width: 100%;"
              :to="'/home/' + item.id"><i class="el-icon-menu"></i>
              <span slot="title">{{ item.name }}</span></router-link>
          </el-menu-item>

          <el-menu-item index="4" v-if="user.type == 2">
            <i class="el-icon-plus"></i>
            <span slot="title">
              <router-link to="/course">Course Management</router-link>
            </span>
          </el-menu-item>

        </el-menu>
      </el-aside>
      <el-main>
        <router-view :key="$route.fullPath"></router-view>
      </el-main>
    </el-container>


  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { findByStudentId } from '../api/course';
import {listAll} from '../api/course'
import { getUser } from '../api/user'
import { ref } from 'vue';
const router = useRouter();
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

function goToProfile() {
  // localStorage.removeItem('token')
  router.push('/user')
}
const dataList = ref([])

function exit() {
  localStorage.removeItem('token')
  router.push('/login')
}


</script>

<style scoped>
.el-menu {
  border-right: none !important;
}

.el-menu-demo {
  width: 800px;
}

.icon-black {
  color: black !important;
  /* 设置图标颜色为黑色 */
}

.icon-with-text {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.full-size-icon {
  font-size: 130px !important;
  /* 调整这个值来改变图标大小 */
}

.full-size-icon {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  /* 确保按钮填满整个布局 */
  width: 100%;
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

.bg-purple {
  background: #d7d0d0;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 4px;
  min-height: 200px;
  /* 或根据需要调整 */
}

.row-bg {
  padding: 10px 0;
  background-color: #1c1ca8;
}
</style>