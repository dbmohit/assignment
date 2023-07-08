from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbmks:2001@localhost/Housing'
db = SQLAlchemy(app)

# Define the House model
class House(db.Model):
    __tablename__ = 'houses'

    id = db.Column(db.Integer, primary_key=True)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    square_footage = db.Column(db.Integer)
    location = db.Column(db.String)
    sale_price = db.Column(db.Integer)

    def __init__(self, bedrooms, bathrooms, square_footage, location, sale_price):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.square_footage = square_footage
        self.location = location
        self.sale_price = sale_price


db.create_all()


@app.route('/houses', methods=['POST'])
def add_houses():
    data = request.get_json()

    if not data:
        return jsonify({'message': 'No data provided.'}), 400

    try:
        for house_data in data:
            house = House(
                bedrooms=house_data['Bedrooms'],
                bathrooms=house_data['Bathrooms'],
                square_footage=house_data['SquareFootage'],
                location=house_data['Location'],
                sale_price=house_data['SalePrice']
            )
            db.session.add(house)
        db.session.commit()
        return jsonify({'message': 'Data stored successfully.'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error occurred while storing data.', 'error': str(e)}), 500


@app.route('/statistics', methods=['GET'])
def get_statistics():
   
    avg_sale_price_overall = db.session.query(func.avg(House.sale_price)).scalar()

    avg_sale_price_per_location = db.session.query(House.location, func.avg(House.sale_price)).group_by(House.location).all()

    max_sale_price = db.session.query(func.max(House.sale_price)).scalar()

    min_sale_price = db.session.query(func.min(House.sale_price)).scalar()

    statistics = {
        'average_sale_price_overall': avg_sale_price_overall,
        'average_sale_price_per_location': dict(avg_sale_price_per_location),
        'max_sale_price': max_sale_price,
        'min_sale_price': min_sale_price
    }

    return jsonify(statistics), 200

if __name__ == '__main__':
    app.run(debug=True)
