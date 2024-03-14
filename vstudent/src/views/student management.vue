<template>
  <div id="app">
    <el-row :gutter="20">
      <el-col :span="12" :offset="6">
        <div class="grid-content bg-purple font">
          Student Management
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="24">

      <el-col :span="24">
        <div class="grid-content bg-purple">
          <!-- <el-button type="primary" style="margin-right: 15px;" @click="addRecord">ADD</el-button> -->

          <el-button @click="gouBack">return</el-button>

          <el-button @click="getRecord()">ADD</el-button>
        </div>
      </el-col>
    </el-row>

    <el-dialog v-model="dialogFormVisible" title="course relation" width="800">
      <el-form style="max-width: 600px" :model="form" label-width="auto" label-position="top">
        <el-transfer v-model="value" :data="dataList" :titles="['Source', 'Target']" :right-default-checked="right">
          <template #left-footer>
            <el-button class="transfer-footer" size="small">all course</el-button>
          </template>
          <template #right-footer>
            <el-button class="transfer-footer" size="small">selected course</el-button>
          </template>
        </el-transfer>
      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogFormVisible = false">Cancel</el-button>
          <el-button type="primary" @click="submit">
            Confirm
          </el-button>
        </div>
      </template>
    </el-dialog>

    <el-row :gutter="24">
      <el-col :span="24">
        <div class="grid-content bg-purple">
          <el-table :data="userList" style="width: 100%">
            <el-table-column label="ID" prop="id">
            </el-table-column>
            <el-table-column label="Email" prop="email">
            </el-table-column>
            <el-table-column label="Name" prop="name">
            </el-table-column>
            <el-table-column label="Action" prop="name">

              <template #default="scope">


                <el-button type="danger" @click="delRecord(scope.row.id)">Delete</el-button>
              </template>
            </el-table-column>
          </el-table>

        </div>
      </el-col>

    </el-row>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { listAll, findByStudentId } from '../api/user';
import { listAll as courseListAll } from '../api/course';
import { listUserCourseAll, addUserCourse, delUserCourse, getUserCourse, getTUserCourse } from '../api/user_course';
import { ElMessage as Message, ElMessageBox as MessageBox } from 'element-plus'
import { useRoute, useRouter } from 'vue-router';
const router = useRouter();
const dataList = ref([])
const userList = ref([])
const form = reactive({})
const right = ref({});
const value = ref([])
const dialogFormVisible = ref(false)
const route = useRoute();
onLoadList();
function getListAll() {
  // courseListAll().then(res => {
  //   dataList.value = res.data.map(item => {
  //     return {
  //       key: item.id,
  //       label: item.name,
  //       disabled: false,
  //     }
  //   })
  // })
  // if (route.params.id != 'all') {
  //   return
  // }
  listAll().then(res => {
    dataList.value = res.data.map(item => {
      return {
        key: item.id,
        label: item.name,
        disabled: false,
      }
    })
  })
}

function gouBack() {
  router.go(-1)
}

function onLoadList() {
  findByStudentId(route.params.id).then(res => {
    userList.value = res.data
  });
}

// const user = ref({})  
// getUser(localStorage.getItem('token')).then(res=>{
//   user.value = res.data;
//   if(user.value.type == 2){

//   }else{

//   }
// })



getListAll();
function addRecord() {
  dialogFormVisible.value = true
}




function submit() {

  value.value.forEach(item => {
    form.student_id = item;
    addUserCourse(form).then(res => {
      if (res.code == '200') {
        if (dialogFormVisible.value) {
          Message({
            message: res.msg,
            type: 'success'
          })
          dialogFormVisible.value = false
        }
        onLoadList();

        retrun
      }

    })
  })


}

function delRecord(id) {
  delUserCourse(id, route.params.id).then(res => {
    Message({
      message: res.msg,
      type: 'success'
    })
    dialogFormVisible.value = false
    onLoadList();
  })
}

function getRecord() {
  form.c_id = route.params.id;
  value.value = [];
  right.value = [];
  getTUserCourse(route.params.id).then(res => {
    if (res.code == '200') {
      value.value = res.data.map(item => item.student_id - 0)
      right.value = value.value

    }

  })



  dialogFormVisible.value = true

}



// export default {
//   data() {
//     return {
//       tableData: [{
//         ID: '1',
//         Email:'1@123.com',
//         name: 'A',

//       }, {
//         ID: '2',
//         Email:'2@123.com',
//         name: 'B',

//       }, {
//         ID: '3',
//         Email:'3@123.com',
//         name: 'C',

//       }, {
//         ID: '4',
//         Email:'4@123.com',
//         name: 'D',

//       }],
//       search: ''
//     }
//   },
//   methods: {
//     handleEdit(index, row) {
//       console.log(index, row);
//     },
//     handleDelete(index, row) {
//       console.log(index, row);
//     }
//   },
// }
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