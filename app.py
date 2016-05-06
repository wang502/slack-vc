from flask import Flask, request, Response, redirect
import vc
import os
import utils
import collections

app = Flask(__name__)

@app.route("/", methods=['post'])
def hello():
    '''
    Example message:
    /vc a16z p
    '''
    message = request.values.get('text')

    arr = message.split(" ")
    result = vc.getPortfolio(arr[0]) if arr[1] == "p" else vc.getKhoslaPortfolio()
    result = collections.OrderedDict(sorted(result.items()))

    response = ":innocent: This is " + arr[0] + "'s portfolio: \n\n"
    i = 1
    for k, v in result.items():
        response += "<" + v.strip() + "|" + str(i) + ". " + utils.extract_name_from_string(k.strip()) + ">\n"
        i += 1
    return Response(response, content_type='text/plain;charset=utf-8')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
