<template>
    <div class="body">
        <div class="container">
            <h1 class="title">LMS</h1>
            <div class="login-form">
                <el-input  placeholder="Email" v-model="form.username" style="margin-bottom: 10px;"></el-input>
                <el-input  placeholder="password"  type="password" v-model="form.password" style="margin-bottom: 10px;"></el-input>
                <button @click="submit" class="login-button">Login</button>
                <router-link to="/register" class="register-button">Register</router-link>
                <router-link to="/forgot" class="forgot-password">Forgot Password?</router-link>

            </div>

        </div>

    </div>
</template>
<script setup>
import { reactive, ref } from 'vue';
import {login} from '../api/login'
const form = reactive({})


function submit(){
    login(form).then(res=>{
        if(res.code==200){
            localStorage.setItem('token',res.data)
         
            location.href='/'
        }
    })
}

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