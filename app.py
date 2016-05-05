from flask import Flask, request, Response, redirect
import vc
import os

app = Flask(__name__)

@app.route("/", methods=['post'])
def hello():
    '''
    /vc a16z portfolio
    '''
    message = request.values.get('text')

    arr = message.split(" ")
    portfolio = {}
    if arr[1] == "portfolio":
        print arr[0]
        portfolio = vc.getPortfolio(arr[0])
    else:
        portfolio = vc.getKhoslaPortfolio()
    print portfolio
    return Response(str(portfolio), content_type='text/plain;charset=utf-8')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
