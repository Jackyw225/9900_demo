import request from '@/utils/request'


// 登录方法
export function addCourse(data) {
  return request({
    url: '/course/',
    method: 'post',
    data: data
  })
}

export function listAll() {
  return request({
    url: '/course/listAll?t_id='+localStorage.getItem("token"),
    method: 'get',

  })
}

export function delCourse(id) {
  return request({
    url: '/course/'+id,
    method: 'delete',

  })
}

export function getCourse(id) {
  return request({
    url: '/course/'+id,
    method: 'get',

  })
}

export function updateCourse(data) {
  return request({
    url: '/course/'+data.id,
    method: 'put',
    data:data
  })
}

export function findByStudentId() {
  return request({
    url: '/course/findByStudentId/'+localStorage.getItem("token"),
    method: 'get',

  })
}
