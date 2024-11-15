from flask import Blueprint, jsonify, request
from models import db, Supplier, Store, Product, StoreProduct, Sale

bp = Blueprint("routes", __name__)


# Supplier CRUD
@bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the API"})


@bp.route("/suppliers", methods=["GET", "POST", "PUT", "DELETE"])
def suppliers_ep():
    if request.method == "GET":
        suppliers = Supplier.query.all()
        return jsonify([{"id": s.id, "name": s.name, "created_at": s.created_at, "updated_at": s.updated_at} for s in suppliers])

    elif request.method == "POST":

        # Ensure we only attempt to parse JSON for POST requests
        data = request.get_json()
        if not data or "name" not in data:
            return jsonify({"error": "Invalid data"}), 400

        new_supplier = Supplier(name=data["name"])
        db.session.add(new_supplier)
        db.session.commit()
        return jsonify({"id": new_supplier.id, "name": new_supplier.name}), 201

    elif request.method == "PUT":

        data = request.get_json()
        if not data or "id" not in data or "name" not in data:
            return jsonify({"error": "Invalid data"}), 400

        supplier = Supplier.query.get(data["id"])
        if not supplier:
            return jsonify({"error": "Supplier not found"}), 404

        supplier.name = data["name"]
        db.session.commit()

        return jsonify({"id": supplier.id, "name": supplier.name}), 200

    elif request.method == "DELETE":

        data = request.get_json()
        if not data or "id" not in data:
            return jsonify({"error": "Invalid data"}), 400

        supplier = Supplier.query.get(data["id"])
        if not supplier:
            return jsonify({"error": "Supplier not found"}), 404

        db.session.delete(supplier)
        db.session.commit()

        return jsonify({"message": "Supplier deleted successfully"}), 200


# Store CRUD
@bp.route("/stores", methods=["GET", "POST", "PUT", "DELETE"])
def stores_ep():
    if request.method == "GET":
        stores = Store.query.all()
        return jsonify([{"id": s.id, "name": s.name, "created_at": s.created_at, "updated_at": s.updated_at} for s in stores])
    elif request.method == "POST":
        data = request.json
        new_store = Store(name=data["name"])
        db.session.add(new_store)
        db.session.commit()
        return jsonify({"id": new_store.id, "name": new_store.name}), 201
    elif request.method == "PUT":
        data = request.json
        store = Store.query.get(data["id"])
        if not store:
            return jsonify({"error": "Store not found"}), 404
        store.name = data["name"]
        db.session.commit()
        return jsonify({"id": store.id, "name": store.name}), 200
    elif request.method == "DELETE":
        data = request.json
        store = Store.query.get(data["id"])
        if not store:
            return jsonify({"error": "Store not found"}), 404
        db.session.delete(store)
        db.session.commit()
        return jsonify({"message": "Store deleted successfully"}), 200


# Product CRUD
@bp.route("/products", methods=["GET", "POST", "PUT", "DELETE"])
def products_ep():
    if request.method == "GET":
        products = Product.query.all()
        return jsonify([{"id": p.id, "name": p.name, "created_at": p.created_at, "updated_at": p.updated_at} for p in products])
    elif request.method == "POST":
        data = request.json
        new_product = Product(name=data["name"])
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"id": new_product.id, "name": new_product.name}), 201
    elif request.method == "PUT":
        data = request.json
        product = Product.query.get(data["id"])
        if not product:
            return jsonify({"error": "Product not found"}), 404
        product.name = data["name"]
        db.session.commit()
        return jsonify({"id": product.id, "name": product.name}), 200
    elif request.method == "DELETE":
        data = request.json
        product = Product.query.get(data["id"])
        if not product:
            return jsonify({"error": "Product not found"}), 404
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 200


@bp.route("/sales", methods=["POST"])
def sales_ep():
    data = request.json
    new_sale = Sale(store_id=data["store_id"], product_id=data["product_id"], size=data["size"], quantity=data["quantity"])
    db.session.add(new_sale)
    db.session.commit()
    return jsonify({"id": new_sale.id, "store_id": new_sale.store_id, "product_id": new_sale.product_id, "size": new_sale.size, "quantity": new_sale.quantity}), 201


@bp.route("/sales-report", methods=["POST"])
def sales_report():
    data = request.json
    store_id = data.get("store")
    product_id = data.get("product")
    size = data.get("size")

    query = Sale.query

    if store_id:
        query = query.filter(Sale.store_id == store_id)
    if product_id:
        query = query.filter(Sale.product_id == product_id)
    if size:
        query = query.filter(Sale.size == size)

    sales = query.all()
    
    return jsonify([
        {
            "store_name": s.store.name,
            "product_name": s.product.name,
            "size": s.size,
            "quantity": s.quantity,
            "sale_date": s.sale_date
        } for s in sales
    ])


@bp.route("/store-products", methods=["GET"])
def store_products_ep():
    store_products = StoreProduct.query.all()
    
    # Fetching names using relationships
    result = [{
        "id": sp.id,
        "supplier_id": sp.supplier_id,
        "supplier_name": sp.supplier.name if sp.supplier else None,
        "store_id": sp.store_id,
        "store_name": sp.store.name if sp.store else None,
        "product_id": sp.product_id,
        "product_name": sp.product.name if sp.product else None,
        "sizes": sp.sizes,
        "created_at": sp.created_at,
    } for sp in store_products]

    return jsonify(result)

# Assigning Products to Stores
@bp.route("/assign-product", methods=["POST"])
def assign_product():
    data = request.json
    store_product = StoreProduct(
        supplier_id=data["supplier_id"],
        store_id=data["store_id"],
        product_id=data["product_id"],
        sizes=data["sizes"]
    )
    db.session.add(store_product)
    db.session.commit()
    return jsonify({"message": "Product assigned successfully"}), 201
