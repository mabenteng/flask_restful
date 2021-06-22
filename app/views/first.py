from flask import Blueprint,request,session,url_for,render_template,redirect
from werkzeug.security import generate_password_hash,check_password_hash



first=Blueprint("first",__name__)


@first.route("/")
def index():
    return "返回index页面"