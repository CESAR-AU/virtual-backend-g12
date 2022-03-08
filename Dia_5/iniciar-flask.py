from datetime import date, datetime
from glob import escape
from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicial():
    print('Me llamaron!') 
    return 'Bienvenido a mi API 🔌'

@app.route('/usuarios')
def usuarios():
    print('Me llamaron!')
    return 'Bienvenido a mi API usuarios 🔌'

@app.route('/api/info')
def info_app():
    return {
        'fecha': date.today(),
        'fecha2': date.weekday(date.today()),
        'fecha3': date.strftime(date.today(), 'yyyy-MM-dd'),
        'fecha3_1': date.strftime(date.today(), '%Y-%m-%d %H:%M:%S'),
        'fecha4': datetime.now(),
        'fecha5': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }

@app.route("/usuario/<name>")
def hello(name):
    return f"Hola, {escape(name)}!"

app.run(debug=True, port='5555', host='0.0.0.0')