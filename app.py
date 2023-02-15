from flask import Flask, render_template
from escpos.printer import Network
import datetime

senha = 0
kitchen = Network("192.168.10.31")

app = Flask(__name__)
@app.route("/")
def homepage():

    return render_template("homepage.html")

@app.route("/rodar", methods=["post","get"])
def rodar():

    global senha

    senha += 1
    senhaP = str('%03d'% senha)
    now = datetime.datetime.now()
    nowP = str(now.strftime("%d-%m-%Y %H:%M:%S"))

    # style
    kitchen.text("\x1b\x61\x01EXAMES\n")

    # style
    kitchen.text("\x1b!\x32\x01\n")

    kitchen.text("SENHA\n")
    kitchen.text(senhaP)
    kitchen.text("\n")

    # style
    kitchen.text("\x1b!\x00\x00\n")
    kitchen.text(nowP)
    kitchen.cut()
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run()
