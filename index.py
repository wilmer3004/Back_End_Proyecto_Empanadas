from config import config 
from flask import Flask

configuration = config['development']
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=configuration.DEBUG)
    
