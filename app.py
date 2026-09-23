from flask import Flask, render_template, abort

app = Flask(__name__)

products = [
    {"id": 1, "name": "AeroBook Pro 15", "price": 54999, "old_price": 64999, "category": "Electronics", "rating": 4.6, "emoji": "💻", "badge": "Best Seller"},
    {"id": 2, "name": "PixelMax 5G Smartphone", "price": 24999, "old_price": 29999, "category": "Mobiles", "rating": 4.5, "emoji": "📱", "badge": "Limited Deal"},
    {"id": 3, "name": "SoundWave Wireless Headphones", "price": 1999, "old_price": 3499, "category": "Electronics", "rating": 4.4, "emoji": "🎧", "badge": "Deal"},
    {"id": 4, "name": "FitTrack Smart Watch", "price": 3999, "old_price": 5999, "category": "Accessories", "rating": 4.3, "emoji": "⌚", "badge": "Deal"},
    {"id": 5, "name": "Urban Everyday Backpack", "price": 1299, "old_price": 1999, "category": "Fashion", "rating": 4.2, "emoji": "🎒", "badge": "20% off"},
    {"id": 6, "name": "Mechanical RGB Keyboard", "price": 2799, "old_price": 3999, "category": "Computers", "rating": 4.7, "emoji": "⌨️", "badge": "Top Rated"},
    {"id": 7, "name": "HomeBrew Coffee Maker", "price": 3499, "old_price": 4999, "category": "Home", "rating": 4.1, "emoji": "☕", "badge": "Deal"},
    {"id": 8, "name": "4K Smart LED TV 43 inch", "price": 32999, "old_price": 42999, "category": "Electronics", "rating": 4.5, "emoji": "📺", "badge": "Great Deal"},
]

categories = ["Electronics", "Mobiles", "Computers", "Fashion", "Home", "Accessories"]

@app.route("/")
def home():
    return render_template("index.html", products=products[:4], categories=categories)

@app.route("/products")
def product_list():
    category = __import__("flask").request.args.get("category")
    items = [p for p in products if not category or p["category"].lower() == category.lower()]
    return render_template("products.html", products=items, categories=categories, selected_category=category)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        abort(404)
    return render_template("product.html", product=product)

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/health")
def health():
    return {"status": "UP", "application": "Amazon Python Clone"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
