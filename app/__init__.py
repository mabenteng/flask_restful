from app.ext import init_ext
# from app.views import init_view  #这里不用视图函数了
from app.apis import init_api
from app.settings import envs
from flask import Flask


# 这里还可以引入缓存和其他第三方

def create_app(env):
    app=Flask(__name__)
    app.config.from_object(envs.get(env))
    init_ext(app)
    # init_view(app)
    init_api(app)
    return app
