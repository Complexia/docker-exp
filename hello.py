from flask import Flask





from waitress import serve



# flask --app endpoints.py --debug run
app = Flask(__name__)




@app.route('/')
def index():
    return "Quereon!"


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"




if __name__ == '__main__':
    print("exp app running on port 4030...")
    serve(app, host='0.0.0.0', port=4030)
