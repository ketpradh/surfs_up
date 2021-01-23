from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:/n
    /api/v1.0/precipitation/n
    /api/v1.0/stations/n
    /api/v1.0/tobs/n
    /api/v1.0/temp/start/end/n
    ''')

if __name__ == '_main_':
    app.run(debug=True, port=9999)