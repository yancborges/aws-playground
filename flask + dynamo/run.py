from flask import Flask
from routes import routes

# db.Table('test_table').put_item({'name': 'Yan'})

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == '__main__':
    app.secret_key = 'hiddenpassword'
    app.run(debug=True)
