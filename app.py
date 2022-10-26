# from flask import Flask, render_template, request

# app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True

# @app.route('/', methods=["GET", "POST"])
# def hello_world():  # put application's code here
#     if request.method == "POST":
#         stockInfo = request.form.get("symbol")
#     return render_template("testPage.html")

# if __name__ == '__main__':
#     app.run()


from flask import Flask, request, render_template
from uploadFiles import selectQuery
  
app = Flask(__name__)
  
  
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
          
        return render_template("Coordinadora Envío de mensajería y mercancía nacional e internacional.html", valorText=request.form.get("myInput"))
    return render_template("Coordinadora Envío de mensajería y mercancía nacional e internacional.html", valorText="")


@app.route("/hola", methods=["POST", "GET"])
def hola():
    if request.method == "POST":
        return "Hola2"
    language = request.args.get("texto")
    language = language.lower()
    language = language.replace(".", "")
    language = language.replace("calle", "cl ")
    language = language.replace("calla", "cl ")
    language = language.replace("call", "cl ")
    language = language.replace("cll", "cl ")
    language = language.replace("carrera", "cra ")
    language = language.replace("carr", "cra ")
    language = language.replace("cr ", "cra ")
    language = language.replace("kra ", "cra ")
    language = language.replace("kr ", "cra ")
    language = language.replace("  ", " ")
    language = language + "%"
    print(language)
    query = f"SELECT address, count FROM bogotacount WHERE address LIKE '{language}' order by count DESC LIMIT 5"
    resultado = selectQuery(query)
    str = []
    for i in resultado:
        str.append(i[0])
    resultado = ",".join(str)
    print(resultado)
    return resultado
  
if __name__ == '__main__':
    app.run(debug=True)