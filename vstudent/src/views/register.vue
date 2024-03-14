<template>

    <div class="body">
        <div class="container">
            <h1 class="title">LMS</h1>
            <div class="login-form">
                <el-form style="max-width: 600px" :model="form" label-width="auto" label-position="top">
                    <el-input placeholder="name" v-model="form.name" style="margin-bottom: 10px;"></el-input>
                    <el-input placeholder="Email" v-model="form.email" style="margin-bottom: 10px;"></el-input>
                    <el-input placeholder="password" type="password" v-model="form.password"
                        style="margin-bottom: 10px;"></el-input>

                    <el-radio-group v-model="form.type" class="ml-4">
                        <el-radio :label="1" size="large">Student</el-radio>
                        <el-radio :label="2" size="large">Teacher</el-radio>
                    </el-radio-group>

                    <el-form-item label="Where is your birth place？">
                        <el-input v-model="form.address" />
                    </el-form-item>
                </el-form>

                <button class="login-button register-button" @click="submit">Register</button>

                <router-link to="/login" class="login-link">Already have an account? Login</router-link>

            </div>

        </div>

    </div>
</template>
<script setup>
import { ref, reactive } from 'vue';
import { addUser } from '../api/user';
import { ElMessage as Message, ElMessageBox as MessageBox } from 'element-plus'
import { useRouter   } from 'vue-router';
const router = useRouter();
const form = reactive({
    type: 1,
});

const submit = () => {
    addUser(form).then(res => {
        if (res.code == '200') {
            Message({
                message: res.msg,
                type: 'success'
            })
            router.push('/login')
            retrun 
        }
    })

}

const options = [
    {
        value: '1',
        label: '学生',
    },
    {
        value: '2',
        label: '教师',
    },

]


const email = ref('');

</script>
<style lang="scss" scoped>
.body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f5f5f5;
}

.container {
    text-align: center;
}

.title {
    color: blue;
    font-size: 32px;
    margin-bottom: 20px;
}

.login-form {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.login-form input {
    width: calc(100% - 22px);
    /* 减去边框和内边距的宽度 */
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-sizing: border-box;
    /* 确保边框和内边距包含在宽度内 */
}

button,
.register-button {
    width: 100%;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-bottom: 10px;
    text-align: center;
    display: inline-block;
    box-sizing: border-box;
    /* 确保边框和内边距包含在宽度内 */
}

.login-button {
    background-color: #007bff;
    color: white;
}

.register-button {
    background-color: #ffc107;
    color: white;
    text-decoration: none;
    /* 移除链接的下划线 */
}

.register-button:hover {
    background-color: darkorange;
    color: white;
}

.forgot-password {
    display: block;
    margin-top: 10px;
    color: #007bff;
    text-decoration: none;
}
</style>