from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def calculo():
    imc=0
    if request.method=='POST' and 'peso' in request.form and 'altura' in request.form:
        peso= float(request.form.get('peso'))
        altura= float(request.form.get('altura'))
        imc = round(peso/((altura/100) **2),1)
        if imc < 18.5:
            return 'magreza'
        elif imc >= 18.5 and imc <= 24.9:
            return 'sudável'
        elif imc > 24.9 and imc <= 29.9:
            return 'sobrepeso'
        else:
            return 'obesidade'
    return render_template("imc2.html",imc=imc)


if __name__ == "__main__":
    app.run(debug=True)
