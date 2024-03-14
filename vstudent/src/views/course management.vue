<template>
  <div id="app">
    <el-row :gutter="20">
      <el-col :span="12" :offset="6">
        <div class="grid-content bg-purple font">
          Course Management
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="24">

      <el-col :span="24">
        <div class="grid-content bg-purple" v-if="user.type == 2">
          <el-button type="primary" @click="addRecord">ADD</el-button>
        </div>
      </el-col>
    </el-row>

    <el-dialog v-model="dialogFormVisible" title=" course" width="500">
      <el-form style="max-width: 600px" :model="form" label-width="auto" label-position="top">

        <el-form-item label="Name" prop="desc">
          <el-input :disabled="form.id" v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="Time" required>
          <el-col :span="11">
            <el-form-item prop="date1">
              <el-date-picker
        v-model="form.date1"
        type="date"
        placeholder="Date"
        format="YYYY/MM/DD"
        value-format="YYYY-MM-DD"
      />
              <!-- <el-date-picker type="date" placeholder="Date" v-model="form.date1" value-format="yyyy-MM-dd HH:mm"
                format="yyyy-MM-dd HH:mm" style="width: 100%;"></el-date-picker> -->
            </el-form-item>
          </el-col>
          <el-col class="line" :span="2">-</el-col>
          <el-col :span="11">
            <el-form-item prop="date2">
              <el-time-picker placeholder="Time" value-format="HH:mm:ss" v-model="form.date2"
                style="width: 100%;"></el-time-picker>
            </el-form-item>
          </el-col>
        </el-form-item>


        <el-form-item label="Details" prop="desc">
          <el-input type="textarea" v-model="form.description"></el-input>
        </el-form-item>

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
          <el-table :data="dataList" style="width: 100%">
            <el-table-column label="ID" prop="id">
            </el-table-column>
            <el-table-column label="name" prop="name">

            <template #default="scope">
                <router-link v-if="user.type == 2" :to="'/student/'+scope.row.id">{{ scope.row.name }}</router-link>
                <span v-else>{{ scope.row.name }}</span>
              </template>
            </el-table-column>
            <el-table-column label="date1" prop="date1">
            </el-table-column>
            <el-table-column label="date2" prop="date2">
            </el-table-column>
            <el-table-column label="description" prop="description">
            </el-table-column>
            <el-table-column v-if="user.type == 2" label="Action" prop="name">

              <template #default="scope">

                <el-button @click="getRecord(scope.row.id)">Edit</el-button>
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
import { addCourse, getCourse, updateCourse, delCourse, listAll } from '../api/course'
import { ElMessage as Message, ElMessageBox as MessageBox } from 'element-plus'
import { useRouter } from 'vue-router';
import { findByStudentId } from '../api/course';
import { getUser } from '../api/user'
const dataList = ref([])
let  form = reactive({})
const dialogFormVisible = ref(false)
function getListAll() {
  listAll().then(res => {
    dataList.value = res.data
  })
}
const user = ref({})  
getUser(localStorage.getItem('token')).then(res=>{
  user.value = res.data;
  if (user.value.type == 2) {
    getListAll()
  } else {
    findByStudentId().then(res => {
      dataList.value = res.data ? res.data : [];
    })

  }
})



function addRecord() {
  
  dialogFormVisible.value = true
}

function submit() {
  if (!form.id) {
    form.t_id = localStorage.getItem('token')
    addCourse(form).then(res => {
      if (res.code == '200') {
        Message({
          message: res.msg,
          type: 'success'
        })
        dialogFormVisible.value = false
        getListAll();
        retrun
      }

    })
  } else {
    updateCourse(form).then(res => {
      if (res.code == '200') {
        Message({
          message: res.msg,
          type: 'success'
        })
        dialogFormVisible.value = false
        getListAll();
        retrun
      }

    })
  }
}

function delRecord(id) {
  delCourse(id).then(res => {
    if (res.code == '200') {
      Message({
        message: res.msg,
        type: 'success'
      })
      getListAll();
    }
  })
}

function getRecord(id) {
  getCourse(id).then(res => {
    if (res.code == '200') {

      Object.assign(form, res.data);
      dialogFormVisible.value = true
    }
  })
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