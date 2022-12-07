from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 = 11, number2 = 22)

@app.route('/sum')
def add():
    var1, var2 = 15210, 38960
    return render_template('body.html', value1 = var1, value2 = var2, sum = var1 + var2)

@app.route('/sub')
def sub():
    var1, var2 = 20.5, 10.36
    return render_template('body2.html', value1 = var1, value2 = var2, sub = var1 - var2)

@app.route('/mult')
def star():
    var1, var2 = 20, 6
    return render_template('body3.html', value1 = var1, value2 = var2, multiplication = round(var1*var2,2))


@app.route('/div')
def div():
    var1, var2 = 5, 6
    return render_template('body4.html', value1 = var1, value2 = var2, divide = round(var1/var2,2))


@app.route('/add')
def short():
    var1, var2 = 5, 6
    return render_template('body5.html', var1=var1, var2=var2)


if __name__ == '__main__':
    app.run(debug=True)