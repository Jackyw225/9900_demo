<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <div class="icon-with-text">
            <el-button type="text" icon="el-icon-document" class="full-size-icon icon-black"></el-button>
            <div>Assignment</div>
          </div>
        </div>
      </el-col>

      <el-col :span="6">
        <div class="grid-content bg-purple">
          <div class="icon-with-text">
            <el-button type="text" icon="el-icon-edit" class="full-size-icon icon-black"></el-button>
            <div>Exam</div>
          </div>
        </div>
      </el-col>

      <el-col :span="6">
        <div class="grid-content bg-purple">
          <div class="icon-with-text">
            <el-button type="text" icon="el-icon-chat-dot-round" class="full-size-icon icon-black"></el-button>
            <div>Forum</div>
          </div>
        </div>
      </el-col>

      <el-col :span="6">
        <div class="grid-content bg-purple">
          <div class="icon-with-text">
            <el-button type="text" icon="el-icon-folder" class="full-size-icon icon-black"></el-button>
            <div>Material</div>
          </div>
        </div>
      </el-col>
    </el-row>

    <el-row :gutter="20">
      <el-col :span="6">
        <div class="grid-content bg-purple" @click="openHtml('/createcourse')">
          <div class="icon-with-text">
            <el-button type="text" icon="el-icon-suitcase" class="full-size-icon icon-black"></el-button>
            <div>Course Details</div>
          </div>
        </div>
      </el-col>

      <el-col :span="6">
        <div class="grid-content bg-purple" @click="openHtml('/student')">
          <div class="icon-with-text">
            <el-button type="text" icon="el-icon-user" class="full-size-icon icon-black"></el-button>
            <div>Student Management</div>
          </div>
        </div>
      </el-col>

      <el-col :span="6">
        <div class="grid-content bg-purple">
          <div class="icon-with-text">
            <el-button type="text" icon="el-icon-monitor" class="full-size-icon icon-black"></el-button>
            <div>Online Course</div>
          </div>
        </div>
      </el-col>

    </el-row>

  </div>
</template>

<script setup>
import { useRouter,useRoute } from 'vue-router'
import { getUser } from '../api/user'
import {ref} from 'vue'
import { ElMessage as Message, ElMessageBox as MessageBox } from 'element-plus'
const router = useRouter()
const user = ref({})
const route = useRoute();
getUser(localStorage.getItem('token')).then(res => {
  user.value = res.data;
  
})


function openHtml(url) {
  if (url == '/student' && user.value.type != 2) {
    Message({
      message: 'No permission',
      type: 'error'
    })
    return 
  }

  router.push(url+'/'+route.params.id)
}

</script>

<style scoped>
.el-menu {
  border-right: none !important;
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