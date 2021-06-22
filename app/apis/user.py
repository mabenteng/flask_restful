from flask.json import jsonify
from flask_restful import Resource
# 导入资源方便我们继承,一个 资源就是一个url
from flask import request

class User(Resource):
    '''这个类就是一个资源'''
    def get(self,val="成功"):
        #上面的val只是与路由的/<string:val>有关系,get请求的参数还是要用request.args.get(xx)来获取
        vk=request.args.get("vk","默认值")
        return {'msg':val,"status":"200","data":[{"objkey":vk},{"objkey2":"objvalue2"}]}
    def post(self):
        msg=request.form.get("msg")
        return jsonify({"status":msg})