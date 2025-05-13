from flask import Flask, render_template,request,redirect, url_for
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("06.05.1.html")
@app.route("/about")
def about():
    return render_template("06.05.2.html")
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(f"Имя: {name}, SMS: {message}\n")   
        return redirect("/thank-you")
    return render_template("06.05.3.html")

@app.route("/thank-you")
def thank_you():
    return render_template("06.05.4.html")

if __name__ == "__main__":
    app.run(debug=True,port=8082)