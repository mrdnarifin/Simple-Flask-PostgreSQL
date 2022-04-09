
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class CustomersModel(DB.Model):
    __tablename__ = 'customers'

    customer_id = DB.Column(DB.Integer(), primary_key=True)
    company_name = DB.Column(DB.String())
    contact_name = DB.Column(DB.String())
    contact_title = DB.Column(DB.String())
    address = DB.Column(DB.String())
    city = DB.Column(DB.String())
    region = DB.Column(DB.String())
    postal_code = DB.Column(DB.String())
    country = DB.Column(DB.String())
    phone = DB.Column(DB.String())
    fax = DB.Column(DB.String())

    def __init__(self, company_name, contact_name, contact_title, address, city, region, postal_code, country, phone, fax):
        self.company_name = company_name
        self.contact_name = contact_name
        self.contact_title = contact_title
        self.address = address
        self.city = city
        self.region = region
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.fax = fax

    def __repr__(self):
        return f"<Customer {self.company_name}>"
