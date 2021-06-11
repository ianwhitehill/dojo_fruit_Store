from types import resolve_bases
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print("*" * 80)
    print(request.form)
    count = int(request.form['apple']) + int(request.form['banana']) + int(request.form['orange'])
    print(count)
    return render_template("checkout.html", store_data = request.form, count = count)

if __name__ == "__main__":
    app.run(debug=True)