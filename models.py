from extensions import db

class Supplier(db.Model):
    __tablename__ = 'suppliers'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    name = db.Column(db.String(100), nullable=False)


class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    name = db.Column(db.String(100), nullable=False)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    name = db.Column(db.String(100), nullable=False)

# class Size(db.Model):
#     """
#     This table stores the available sizes for each product.
#     """
#     __tablename__ = 'sizes'
#     id = db.Column(db.Integer, primary_key=True)
#     size = db.Column(db.Integer, nullable=False)

class StoreProduct(db.Model):
    """
    This table handles the assignment of products and sizes to a specific store.
    """
    __tablename__ = 'store_products'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    # count = db.Column(db.Integer, nullable=False)
    sizes = db.Column(db.ARRAY(db.String), nullable=False)  # Store sizes as an array of strings

    # Foreign Key Relationships
    supplier = db.relationship('Supplier', backref='store_products')
    store = db.relationship('Store', backref='store_products')
    product = db.relationship('Product', backref='store_products')
    # size = db.relationship('Size', backref='store_products')


class Sale(db.Model):
    """
    This table records sales data reported by stores.
    """
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    size = db.Column(db.String(50), nullable=False)  # Record the specific size sold
    quantity = db.Column(db.Integer, nullable=False)
    sale_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Foreign Key Relationships
    store = db.relationship('Store', backref='sales')
    product = db.relationship('Product', backref='sales')
