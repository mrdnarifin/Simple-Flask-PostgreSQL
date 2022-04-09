from crypt import methods
from distutils.log import debug
import re
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import DB, CustomersModel
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://#@localhost:5432/#"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

DB.init_app(app)
migrate = Migrate(app, DB)

@app.route('/')
def hello():
    return {"hello": "World"}

@app.route('/customers', methods=['POST', 'GET'])
def customers():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_cust = CustomersModel(company_name=data['company_name'], contact_name=data['contact_name'], contact_title=data['contact_title'], address=data['address'], city=data['city'], region=data['region'], postal_code=data['postal_code'], country=data['country'], phone=data['phone'], fax=data['fax']
            )
            DB.session.add(new_cust)
            DB.session.commit()
            return {"message": f"customer {new_cust.company_name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
    elif request.method == 'GET':
        customers = CustomersModel.query.all()
        results = [{
            "customer_id": customer.customer_id,
            "company_name": customer.company_name,
            "contact_name": customer.contact_name,
            "contact_title": customer.contact_title,
            "address": customer.address,
            "city": customer.city,
            "region": customer.region,
            "postal_code": customer.postal_code,
            "country": customer.country,
            "phone": customer.phone,
            "fax": customer.fax,
        } for customer in customers]
        return {"count":len(customers), "customers":results}

@app.route('/customers/<id>', methods=['GET', 'PUT', 'DELETE'])
def customer(id):
    customer = CustomersModel.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "customer_id": customer.customer_id,
            "company_name": customer.company_name,
            "contact_name": customer.contact_name,
            "contact_title": customer.contact_title,
            "address": customer.address,
            "city": customer.city,
            "region": customer.region,
            "postal_code": customer.postal_code,
            "country": customer.country,
            "phone": customer.phone,
            "fax": customer.fax,
        }
        return {"message": "success", "customer": response}
    elif request.method == 'PUT':
        data = request.get_json()
        customer.company_name = data['company_name']
        customer.contact_name = data['contact_name']
        customer.contact_title = data['contact_title']
        customer.address = data['address']
        customer.city = data['city']
        customer.region = data['region']
        customer.postal_code = data['postal_code']
        customer.country = data['country']
        customer.phone = data['phone']
        customer.fax = data['fax']
        DB.session.add(customer)
        DB.session.commit()
        return {"message": f"customer {customer.company_name} has been updated successfully."}
    
    elif request.method == 'DELETE':
        DB.session.delete(customer)
        DB.session.commit()
        return {"message": f"customer {customer.company_name} has been deleted successfully."}

if __name__ == '__main__':
    
    app.run(debug=True)