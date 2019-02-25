from flask import Flask,jsonify,request
from  pengfuweb.model import session,Pengfu
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    # results = session.query(Pengfu).order_by('-id').all()[0:5]
    results = session.query(Pengfu).limit(10).offset(0)
    # results = session.query(Pengfu).slice(0,10)
    results = [item.to_dict() for item in results]
    # app.logger.info('123')
    print(request.args)
    return jsonify({"data":results})

if __name__ == '__main__':
    app.debug = True
    app.run()