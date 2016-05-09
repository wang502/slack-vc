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

    result1 = {}
    result2 = []
    option = ""
    response = ""
    if arr[1] == "p":
        result1 = vc.getPortfolio(arr[0].lower())
        option = "portfolio"
        response = ":innocent: This is " + vc.getVCName(arr[0].lower()) + "'s portfolio: \n\n"
    else:
        result2 = vc.getInvestors(arr[0].lower())
        option = "investors"
        response = ":innocent: This is " + arr[0].lower() + "'s investors: \n"
    if option == "portfolio":
        i = 1
        for k, v in result1.items():
            response += "<" + v.strip() + "|" + str(i) + ". " + utils.extract_name_from_string(k.strip()) + ">\n"
            i += 1
    elif option == "investors":
        #for serie in result2:
        #    response += " " + str(serie["round"]).strip() + "(" + str(serie["year"]) +")\n"
        #    for investor in serie["investors"]:
        #        response += "  <" + str(investor["link"]) + "|" + str(investor["name"]) + ">\n"
        response += str(result2)
    return Response(response, content_type='text/plain;charset=utf-8')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
