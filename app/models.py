from app.ext import db


class basemodel(db.Model):
    '''定义一个继承的基类'''
    __abstract__=True
    id=db.Column(db.Integer,primary_key=True)
    def save(self):
        db.session.add(self)
        db.session.commit()