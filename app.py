from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<body>
    <h2>Specimen Calculator</h2>
    <form method="POST">
        Size: <input type="text" name="size"><br>
        Mag: <input type="text" name="mag"><br>
        <input type="submit" value="Calculate">
    </form>
    {% if result %} <h3>Result: {{ result }}</h3> {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            result = float(request.form['size']) / float(request.form['mag'])
        except:
            result = "Error"
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(debug=True)