from datetime import datetime

from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship

from app import db, app


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False, unique=True)
    active = Column(Boolean, default=True)


class TimestampMixin(db.Model):
    __abstract__ = True

    created_date = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_date = Column(DateTime, onupdate=datetime.utcnow())


class Category(BaseModel, TimestampMixin):
    __tablename__ = 'category'

    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(BaseModel, TimestampMixin):
    __tablename__ = 'product'

    description = Column(String(125), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(255))
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    def __str__(self):
        return self.name


with app.app_context():
    db.create_all()

    # c1 = Category(name='Mobile')
    # c2 = Category(name='Tablet')
    # c3 = Category(name='Watch')

    # db.session.add(c1)
    # db.session.add(c2)
    # db.session.add(c3)

    # products = [{
    #     "id": "1",
    #     "name": "Samsung Galaxy S22 Ultra 5G 128GB",
    #     "description": "Samsung 5G, 128GB",
    #     "price": 17990000,
    #     "image": "https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/235838/Galaxy-S22-Ultra-Burgundy-600x600.jpg",
    #     "category_id": 1
    # }, {
    #     "id": "2",
    #     "name": "iPhone 14 Pro Max 128GB",
    #     "description": "iPhone 5G, 128GB",
    #     "price": 37990000,
    #     "image": "https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/235838/Galaxy-S22-Ultra-Burgundy-600x600.jpg",
    #     "category_id": 2
    # }, {
    #     "id": "3",
    #     "name": "realme C53",
    #     "description": "Samsung 5G, 128GB",
    #     "price": 26990000,
    #     "image": "https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/235838/Galaxy-S22-Ultra-Burgundy-600x600.jpg",
    #     "category_id": 1
    # }]
    
    # for p in products:
    #     pro = Product(name=p['name'], description=p['description'], price=p['price']
    #                   , image=p['image'], category_id=p['category_id'])
        
    #     db.session.add(pro)

    db.session.commit()
