from flask import Flask, request, Response, redirect
import vc
import os

app = Flask(__name__)

@app.route("/")
def hello():
    #portfolio = vc.getKhoslaPortfolio()
    #print portfolio
    #return Response(str(portfolio), content_type='text/plain;charset=utf-8')
    return "hello world"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
