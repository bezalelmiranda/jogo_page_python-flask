from views import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# instância d aplicação
app = Flask(__name__)
app.config.from_pyfile('config.py')

# instância do SQLAlchemy
db = SQLAlchemy(app)
# pontes com as tabelas do banco de dados

csrf = CSRFProtect(app)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)
