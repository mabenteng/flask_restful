from flask_restful import Api
from app.apis.user import User
def init_api(app):
    api=Api(app)
    api.add_resource(User,"/<val>","/kk")