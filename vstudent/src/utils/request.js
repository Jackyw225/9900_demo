import axios from 'axios'
import { ElMessage as Message, ElMessageBox as MessageBox } from 'element-plus'



let downloadLoadingInstance;
// 是否显示重新登录
export let isRelogin = { show: false };

axios.defaults.headers['Content-Type'] = 'application/json;charset=utf-8'
// 创建axios实例
const service = axios.create({
  // axios中请求配置有baseURL选项，表示请求URL公共部分
  baseURL: import.meta.env.VITE_APP_BASE_API,
  // 超时
  timeout: 60000
})

// request拦截器
service.interceptors.request.use(config => {
  // 是否需要设置 token
  const isToken = (config.headers || {}).isToken === false
  // 是否需要防止数据重复提交,repeatSubmit为true表示需要进行重复提交检查,即isRepeatSubmit为false时需要进行重复提交检查
  const isRepeatSubmit = (config.headers || {}).repeatSubmit === false
      if (getToken()) {
        config.headers['Authorization'] = getToken() // 让每个请求携带自定义token 请根据实际情况自行修改
      }
  // get请求映射params参数
  // if (config.method === 'get' && config.params) {
  //   let url = config.url + '?' + tansParams(config.params);
  //   url = url.slice(0, -1);
  //   config.params = {};
  //   config.url = url;
  // }
  // if (!isRepeatSubmit && (config.method === 'post' || config.method === 'put')) {
  //   const requestObj = {
  //     url: config.url,
  //     data: typeof config.data === 'object' ? JSON.stringify(config.data) : config.data,
  //     time: new Date().getTime()
  //   }
  //   // const sessionObj = cache.session.getJSON('sessionObj')
  //   // if (sessionObj === undefined || sessionObj === null || sessionObj === '') {
  //   //   cache.session.setJSON('sessionObj', requestObj)
  //   // } else {

  //   // }
  //   const s_url = sessionObj.url;                  // 请求地址
  //   const s_data = sessionObj.data;                // 请求数据
  //   const s_time = sessionObj.time;                // 请求时间
  //   const interval = 1000;                         // 间隔时间(ms)，小于此时间视为重复提交
  //   if (s_data === requestObj.data && requestObj.time - s_time < interval && s_url === requestObj.url) {
  //     const message = '数据正在处理，请勿重复提交';
  //     console.warn(`[${s_url}]: ` + message)
  //     return Promise.reject(new Error(message))
  //   } else {
  //     cache.session.setJSON('sessionObj', requestObj)
  //   }
  // }


  return config
}, error => {

  Promise.reject(error)
})

function getToken() {
  return ( localStorage.getItem('token') && localStorage.getItem('token') !== 'undefined')  ?  localStorage.getItem('token') : null
}

// 响应拦截器
service.interceptors.response.use(res => {

  const code = res.data.code;
 const msg = res.data.msg;
  if (code === 600) {
    if (!isRelogin.show) {
      location.href = '/login';
    }
    return Promise.reject('Invalid session, or session has expired, please log in again.')
  } else if (code === 500) {
    Message({
      message: msg,
      type: 'error'
    })
    return Promise.reject(new Error(msg))
  } else if (code !== 200) {
    Notification.error({
      title: msg
    })
    return Promise.reject('error')
  } else {
    return res.data
  }
},
  error => {
    console.log('err' + error)
    let { message } = error;
    if (message == "Network Error") {
      message = "后端接口连接异常";
    }
    else if (message.includes("timeout")) {
      message = "系统接口请求超时";
    }
    else if (message.includes("Request failed with status code")) {
      message = "Invaild" + message.substr(message.length - 3);
    }
    Message({
      message: message,
      type: 'error',
      duration: 5 * 1000
    })
    return Promise.reject(error)
  }
)

// 通用下载方法
export function download(url, params, filename) {
  downloadLoadingInstance = Loading.service({ text: "正在下载数据，请稍候", spinner: "el-icon-loading", background: "rgba(0, 0, 0, 0.7)", })
  return service.post(url, params, {
    transformRequest: [(params) => { return tansParams(params) }],
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    responseType: 'blob'
  }).then(async (data) => {
    const isLogin = await blobValidate(data);
    if (isLogin) {
      const blob = new Blob([data])
      saveAs(blob, filename)
    } else {
      const resText = await data.text();
      const rspObj = JSON.parse(resText);
      const errMsg = errorCode[rspObj.code] || rspObj.msg || errorCode['default']
      Message.error(errMsg);
    }
    downloadLoadingInstance.close();
  }).catch((r) => {
    console.error(r)
    Message.error('There is an error downloading the file, please contact the administrator!')
    downloadLoadingInstance.close();
  })
}

// 通用下载方法
export function downloadForGet(url, filename) {
  downloadLoadingInstance = Loading.service({ text: "Downloading", spinner: "el-icon-loading", background: "rgba(0, 0, 0, 0.7)", })
  return service.get(url, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    responseType: 'blob',
    // `timeout` 指定请求超时的毫秒数。
    // 如果请求时间超过 `timeout` 的值，则请求会被中断
    timeout: 0, // 默认值是 `0` (永不超时)
    // `maxContentLength` 定义了node.js中允许的HTTP响应内容的最大字节数 Infinity
    maxContentLength: Infinity,
    // `maxBodyLength`（仅Node）定义允许的http请求内容的最大字节数 Infinity
    maxBodyLength: Infinity,
  }).then(async (data) => {
    const isLogin = await blobValidate(data);
    if (isLogin) {
      const blob = new Blob([data])
      saveAs(blob, filename)
    } else {
      const resText = await data.text();
      const rspObj = JSON.parse(resText);
      const errMsg = errorCode[rspObj.code] || rspObj.msg || errorCode['default']
      Message.error(errMsg);
    }
    downloadLoadingInstance.close();
  }).catch((r) => {
    console.log(r)
    Message.error('下载文件出现错误，请联系管理员！')
    downloadLoadingInstance.close();
  })
}

export default service
