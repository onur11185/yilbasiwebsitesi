from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "veilwood-secret"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        reason = request.form.get("type", "")
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        message = request.form.get("message", "")

        with open("feedbacks.txt", "a", encoding="utf-8") as f:
            f.write("---- NEW SUBMISSION ----\n")
            f.write(f"Neden: {reason}\n")
            f.write(f"Ad: {name}\n")
            f.write(f"E-posta: {email}\n")
            f.write(f"Mesaj: {message}\n\n")

        return redirect(url_for("feedback"))

    return render_template("feedback.html")






@app.route("/product-tree")
def tree():
    return render_template("product-tree.html")

@app.route("/product-candle")
def candle():
    return render_template("product-candle.html")

@app.route("/product-snow")
def snow():
    return render_template("product-snow.html")

@app.route("/product-light")
def lights():
    return render_template("product-light.html")

@app.route("/product-gift")
def gift():
    return render_template("product-gift.html")

@app.route("/product-cookie")
def cookie():
    return render_template("product-cookie.html")

@app.route("/product-ribbon")
def ribbon():
    return render_template("product-ribbon.html")

@app.route("/product-socks")
def socks():
    return render_template("product-socks.html")

@app.route("/product-accs")
def accs():
    return render_template("product-accs.html")

@app.route("/product-LED")
def LED():
    return render_template("product-LED.html")



PRODUCTS = {
    "1": {"name": "Çam Ağacı", "price": 650},
    "2": {"name": "Orman Mumları", "price": 120},
    "3": {"name": "Kar Küresi", "price": 200},
    "4": {"name": "Işıklı Zincir", "price": 90},
    "5": {"name": "Hediye Kutusu", "price": 300},
    "6": {"name": "Noel Kurabiye Seti", "price": 150},
    "7": {"name": "Yılbaşı Kurdele Seti", "price": 50},
    "8": {"name": "Noel Çorapları", "price": 80},
    "9": {"name": "Kar Taneleri Asma Süsleri", "price": 70},
    "10": {"name": "LED Noel Yıldızı", "price": 150},
}


@app.route("/add-to-cart/<product_id>")
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(product_id)
    session.modified = True
    return redirect(url_for("sepet"))


@app.route("/sepet")
def sepet():
    cart = session.get("cart", [])
    items = [PRODUCTS[id] for id in cart if id in PRODUCTS]
    total = sum(item["price"] for item in items)
    return render_template("sepet.html", items=items, total=total)

@app.route("/clear-cart")
def clear_cart():
    session.pop("cart", None)
    return redirect(url_for("sepet"))


if __name__ == "__main__":
    app.run(debug=True)
