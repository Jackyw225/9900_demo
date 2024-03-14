import request from '@/utils/request'


// 登录方法
export function addUserCourse(data) {
  return request({
    url: '/user_course/',
    method: 'post',
    data: data
  })
}

export function listUserCourseAll() {
  return request({
    url: '/user_course/listAll',
    method: 'get',

  })
}

export function delUserCourse(sid,cid) {
  return request({
    url: '/user_course/'+sid+'?c_id='+cid,
    method: 'delete',

  })
}

export function getUserCourse(id) {
  return request({
    url: '/user_course/'+id,
    method: 'get',

  })
}


export function getTUserCourse(id) {
  return request({
    url: '/user_course/t/'+id,
    method: 'get',

  })
}

export function updateUserCourse(data) {
  return request({
    url: '/user_course/'+data.id,
    method: 'put',
    data:data
  })
}


