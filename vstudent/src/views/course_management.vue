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
          <el-button type="primary" @click="addRecord">ADD</el-button>
        </div>
      </el-col>
    </el-row>

    <el-dialog v-model="dialogFormVisible" title="add student" width="500">
      <el-form style="max-width: 600px" :model="form" label-width="auto" label-position="top">
        <el-input placeholder="name" v-model="form.name" style="margin-bottom: 10px;"></el-input>
        <el-input placeholder="Email" v-model="form.email" style="margin-bottom: 10px;"></el-input>
        <el-input placeholder="password" type="password" v-model="form.password"
          style="margin-bottom: 10px;"></el-input>
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
            <el-table-column label="Email" prop="email">
            </el-table-column>
            <el-table-column label="Name" prop="name">
            </el-table-column>
            <el-table-column label="Action" prop="name">

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
import { listAll, addUser, delUser, getUser,updateUser } from '../api/user';
import { ElMessage as Message, ElMessageBox as MessageBox } from 'element-plus'
import { useRouter } from 'vue-router';
import { getUser } from '../api/user'
const dataList = ref([])
const form = reactive({})
const dialogFormVisible = ref(false)



function getListAll() {
  listAll().then(res => {
    dataList.value = res.data
  })
}
getListAll();
function addRecord() {
  dialogFormVisible.value = true
}

function submit() {
  if (!form.id) {
    form.type = 1;
    addUser(form).then(res => {
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
  }else{
    updateUser(form).then(res => {
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
  delUser(id).then(res => {
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
  getUser(id).then(res => {
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