from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Sayalijadhav@2316@localhost:3306/foodie_haven'

db = SQLAlchemy(app)

# Define your database models (e.g., MenuItem) here, above db.create_all()

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    availability = db.Column(db.Boolean, nullable=False)

# Move the db.create_all() call inside a Flask route or function
@app.route('/')
def create_tables():
    db.create_all()
    return 'Database tables created!'

# Now, you can add data to the database and interact with it within your routes/functions

if __name__ == '__main__':
    app.run(debug=True)
