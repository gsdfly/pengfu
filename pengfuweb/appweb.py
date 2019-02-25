from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:158269@47.75.84.250:3306/lty'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Pengfu(db.Model):
    __tablename__ = 'pengfu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    title = db.Column(db.String(500))
    content = db.Column(db.String(500))
    img = db.Column(db.String(500))

    def to_dict(self):
        a = {}
        for c in self.__table__.columns:
            a[c.name] = getattr(self, c.name, None)
            if str(type(a[c.name])) == "<class 'bytearray'>":
                a[c.name] = a[c.name].decode('utf-8')
        return a

    db.Model.to_dict = to_dict

    # results = db.session.query(Pengfu).all()
    # print(results)
def error():
    return {"error":400,"message":'参数错误'}

def pagination():
    pageIndex = request.values.get('pageIndex')
    pageSize = request.values.get('pageSize')
    if request.content_type == 'application/json':
        pageIndex = json.loads(request.data.decode()).get('pageIndex')
        pageSize = json.loads(request.data.decode()).get('pageSize')
    if pageIndex is None:
        pageIndex = 1
    if pageSize is None:
        pageSize = 20
    pageIndex = int(pageIndex)
    pageSize = int(pageSize)
    if pageIndex < 0 or pageSize < 0:
        return error()
    results = db.session.query(Pengfu).order_by('-id').limit(pageSize).offset(pageIndex*pageSize).all()
    results = [item.to_dict() for item in results]
    return {"data":results,"pageIndex":pageIndex,"pageSize":pageSize}

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    results = pagination()
    # results = session.query(Pengfu).order_by('-id').all()[0:5]
    # results = db.session.query(Pengfu).limit(10).offset(0).all()
    # print(results)
    # results = session.query(Pengfu).slice(0,10)
    # res = db.session.query(Pengfu).limit(10).offset((1) * 10).all()
    # print(res)
    # results = db.session.query(Pengfu).all()
    # app.logger.info('123')
    # return jsonify(results)

    # flask - CORS 解决跨域问题的

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': '*'
    }
    response = jsonify(results)
    response.headers = headers
    return response
    # return

if __name__ == '__main__':
    # app.debug = True
    app.run(port=2018)
