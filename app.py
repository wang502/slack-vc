from flask import Flask, request, Response, redirect
import vc
import os

app = Flask(__name__)

@app.route("/", methods=['post'])
def hello():
    '''
    Example message:
    /vc a16z portfolio
    '''
    message = request.values.get('text')

    arr = message.split(" ")
    result = vc.getPortfolio(arr[0]) if arr[1] == "portfolio" else vc.getKhoslaPortfolio()
    response = ""
    for k, v in result.iteritems():
        response += "<" + v.strip() + "|" + k.strip() + ">\n"
    return Response(response, content_type='text/plain;charset=utf-8')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
