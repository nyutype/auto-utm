from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        width = float(request.form['width'])
        thickness = float(request.form['thickness'])

        measured_area = width * thickness

        calculations = {
            'width' : width,
            'thickness' : thickness,
            'measured_area' : measured_area
        }
        return render_template('index.html', calculations=calculations)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)