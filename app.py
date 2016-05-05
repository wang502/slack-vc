from flask import Flask, request, Response, redirect
import vc

app = Flask(__name__)

@app.route("/")
def hello():
    portfolio = vc.geta16zPortfilio()
    print portfolio
    return Response(str(portfolio), content_type='text/plain;charset=utf-8')

if __name__ == "__main__":
    app.run()
