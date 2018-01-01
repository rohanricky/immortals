from flask import *
import configparser
from python.kumu import main

app = Flask(__name__)

@app.route("/api",methods=["POST"])
def api():
    data=request.form['data']
    print(data)
    data=data.lower()
    link=data.split()
    x=main(data)
    return x

if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000)
#host='0.0.0.0'
'''
config = configparser.ConfigParser()
config.read('config.ini')
host=config['HOST']
'''
