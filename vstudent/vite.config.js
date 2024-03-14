import { fileURLToPath, URL } from 'node:url'

import { defineConfig ,loadEnv} from 'vite'

import vue from '@vitejs/plugin-vue'


// https://vitejs.dev/config/
// export default defineConfig({
  export default defineConfig(({mode}) => {
    //mode 模式字符串  process.cwd()项目  根目录
    //返回值  import.meta.env
    const env =  loadEnv(mode, process.cwd());
    return {
  // base:'mxg',
    //开发环境有效，生产环境无效
    server: 
    {
      port: 8888,// 端口号
      open: true,//启动项目自动打开浏览器
      host: '0.0.0.0',//'0.0.0.0'（开放给所有ip访问此项目）
      proxy: {
          [env.VITE_APP_BASE_API] :{ //key变量要加中括号 []
          target: 'http://127.0.0.1:5000',
          rewrite: path => path.replace(new RegExp(`^${env.VITE_APP_BASE_API}`), ''),
          //开启代理
          changeOrigin:true,
        }
      }
    },
    plugins: [
      vue(),
    ],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    }
    }
   
    
  })
// https://vitejs.dev/config/
// export default defineConfig({
//   plugins: [
//     vue(),
//   ],
//   resolve: {
//     alias: {
//       '@': fileURLToPath(new URL('./src', import.meta.url)),

//     },
    
//   },
  
// })

