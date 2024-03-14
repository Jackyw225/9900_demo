from flask import Flask,session,request,jsonify
from models.result_entity import ResultEntity
def interceptor(func):
    def wrapper(*args, **kwargs):
        # 获取 Authorization 头中的 Token
        token = request.headers.get('Authorization')

        # 检查是否存在 Token
        if not token:
            result_entity = ResultEntity(code=600, msg='no login')
            return jsonify(result_entity.__dict__)

        # 在实际应用中，可能需要进行更复杂的 Token 验证逻辑
        # 这里简单返回 Token 信息
        try:
            return func(token, *args, **kwargs)
        except Exception as e:
            return func( *args, **kwargs)
    # 为每个装饰的路由使用唯一的端点名
    wrapper.__name__ = func.__name__ + '_intercepted'
    wrapper.__doc__ = func.__doc__
    return wrapper