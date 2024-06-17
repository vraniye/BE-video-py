from flask import Flask, render_template, request, send_from_directory, make_response

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH')
    return response


@app.route('/', methods=['GET', 'POST'])
def input():
    return render_template("home.html")


@app.route('/entr', methods=['POST'])
def entr():
    prompt = request.form['input']
    model_id = request.form['model_names']
    if model_id == "mistral":
        print(1)
        response = generate(model_id, prompt)
        print(response)
        return render_template('home.html', prompt=prompt, response=response)
    elif model_id == "mistral_ru":
        print(1)
        response = generate_ru(model_id, prompt)
        print(response)
        return render_template('home.html', prompt=prompt, response=response)
    elif model_id == "sdxlturbo":
        print(11)
        full_name = generate_pic(model_id, prompt)
        print(full_name)
        return render_template('home.html', prompt=prompt, full_name=full_name)
    elif model_id == "sound_ru":
        print(22)
        full_name = generate_sound_ru(model_id, prompt)
        print(full_name)
        return render_template('home.html', prompt=prompt, full_name=full_name)
    elif model_id == "sound":
        print(22)
        full_name = generate_sound(model_id, prompt)
        print(full_name)
        return render_template('home.html', prompt=prompt, full_name=full_name)
    elif model_id == "s2t":
        print(22)
        full_name = generate_text(model_id, prompt)
        print(full_name)
        return render_template('home.html', prompt=prompt, full_name=full_name)
    elif model_id == "ru_en":
        print(22)
        full_name = translate_text(model_id, prompt)
        print(full_name)
        return render_template('home.html', prompt=prompt, full_name=full_name)
    elif model_id == "en_ru":
        print(22)
        full_name = translate_text1(model_id, prompt)
        print(full_name)
        return render_template('home.html', prompt=prompt, full_name=full_name)
    print(111)
    return render_template('home.html')


@app.route('/clr', methods=['POST'])
def clr():
    clear = " "
    print(2)
    return render_template("home.html", clear=clear)


@app.route('/generate', methods=['POST'])
def generate(model_id=None, prompt=None):
    print(model_id, prompt)
    if request.method == "POST":
        print(3)
        # Получаем данные из формы, если они не были переданы явно
        if prompt is None:
            print(4)
            prompt = request.args.get('prompt')
        if model_id is None:
            print(5)
            model_id = request.args.get('model_id')
    print(model_id, prompt)
    print(6)
    response = run_model(model_id, prompt)
    print(response)
    return response.get("response")


@app.route('/generate1', methods=['POST'])
def generate_ru(model_id=None, prompt=None):
    print(model_id, prompt)
    if request.method == "POST":
        print(3)
        # Получаем данные из формы, если они не были переданы явно
        if prompt is None:
            print(4)
            prompt = request.args.get('prompt')
        if model_id is None:
            print(5)
            model_id = request.args.get('model_id')
    print(model_id, prompt)
    print(6)
    model_id = "aboba/saiga_mistral_13b"
    print(model_id, model_id, prompt)
    response = run_model(model_id, prompt)
    print(response)
    return response.get("response")


@app.route('/generate_pic', methods=['POST'])
def generate_pic(model_id=None, prompt=None):
    print(model_id, prompt)
    if request.method == "POST":
        print(7)
        # Получаем данные из формы, если они не были переданы явно
        if prompt is None:
            print(8)
            prompt = request.args.get('prompt')
        if model_id is None:
            print(9)
            model_id = request.args.get('model_id')
    print(model_id, prompt)
    print(10)
    full_name = run_sec_model(prompt)
    print(full_name)
    return full_name


@app.route('/generate_sound', methods=['POST'])
def generate_sound_ru(model_id=None, prompt=None):
    print(model_id, prompt)
    if request.method == "POST":
        print(7)
        # Получаем данные из формы, если они не были переданы явно
        if prompt is None:
            print(8)
            prompt = request.args.get('prompt')
        if model_id is None:
            print(9)
            model_id = request.args.get('model_id')
    print(model_id, prompt)
    print(10)
    full_name = run_third_model(prompt)
    print(full_name)
    return full_name


@app.route('/generate_sound', methods=['POST'])
def generate_sound(model_id=None, prompt=None):
    print(model_id, prompt)
    if request.method == "POST":
        print(7)
        # Получаем данные из формы, если они не были переданы явно
        if prompt is None:
            print(8)
            prompt = request.args.get('prompt')
        if model_id is None:
            print(9)
            model_id = request.args.get('model_id')
    print(model_id, prompt)
    print(10)
    full_name = run_third_model_en(prompt)
    print(full_name)
    return full_name


@app.route('/generate_text', methods=['POST'])
def generate_text(model_id=None, prompt=None):
    print(model_id, prompt)
    if request.method == "POST":
        print(3)
        # Получаем данные из формы, если они не были переданы явно
        if prompt is None:
            print(4)
            prompt = request.args.get('prompt')
        if model_id is None:
            print(5)
            model_id = request.args.get('model_id')
    print(model_id, prompt)
    print(6)
    response = run_fourth_model(prompt)
    print(response)
    return response


@app.route('/generate_translate', methods=['POST'])
def translate_text(model_id=None, prompt=None):
    print(model_id, prompt)
    if request.method == "POST":
        print(3)
        # Получаем данные из формы, если они не были переданы явно
        if prompt is None:
            print(4)
            prompt = request.args.get('prompt')
        if model_id is None:
            print(5)
            model_id = request.args.get('model_id')
    print(model_id, prompt)
    print(6)
    response = run_translate_ru_en(prompt)
    print(response)
    return response


@app.route('/generate_translate1', methods=['POST'])
def translate_text1(model_id=None, prompt=None):
    print(model_id, prompt)
    if request.method == "POST":
        print(3)
        # Получаем данные из формы, если они не были переданы явно
        if prompt is None:
            print(4)
            prompt = request.args.get('prompt')
        if model_id is None:
            print(5)
            model_id = request.args.get('model_id')
    print(model_id, prompt)
    print(6)
    response = run_translate_en_ru(prompt)
    print(response)
    return response


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080', debug=True, threaded=True)
