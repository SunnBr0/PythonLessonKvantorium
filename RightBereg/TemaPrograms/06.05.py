from flask import Flask, render_template
from flask import redirect, url_for,request
app = Flask(__name__)
# py -m pip install flask 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        age = request.form.get('age')
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(f"Имя: {name}, Возраст: {age}\n")
        return redirect(url_for('index'))
    return render_template('06.05.html')
if __name__ == '__main__':
    app.run(debug=True, port=8082)