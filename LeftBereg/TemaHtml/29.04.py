from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
# py -m pip install flask 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        age = request.form.get('age')
        # Можно обработать данные (например, сохранить в базу данных)
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(f"Имя: {name}, Возраст: {age}\n")
        # Перенаправляем на ту же страницу (можно изменить)
        return redirect(url_for('index'))
    # Если GET-запрос, просто отображаем страницу
    return render_template('29.04.html')
if __name__ == '__main__':
    app.run(debug=True, port=8082)  # Запуск сервера в режиме отладки