import request from '@/utils/request'


// 登录方法
export function addUser(data) {
  return request({
    url: '/user/',
    method: 'post',
    data: data
  })
}

export function listAll() {
  return request({
    url: '/user/listAll',
    method: 'get',

  })
}

export function delUser(id) {
  return request({
    url: '/user/'+id,
    method: 'delete',

  })
}

export function getUser(id) {
  return request({
    url: '/user/'+id,
    method: 'get',

  })
}

//findByStudentId
//findByStudentId
export function findByStudentId(id) {
  return request({
    url: '/user/findByStudentId/'+id,
    method: 'get',

  })
}
export function updateUser(data) {
  return request({
    url: '/user/'+data.id,
    method: 'put',
    data:data
  })
}


//forget
export function forget(data){
  return request({
    url: '/user/forget',
    method: 'post',
    data:data
  })
}