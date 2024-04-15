from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        file_path = 'data/rawdata2.txt'  # 파일 경로를 올바르게 설정하세요.
        try:
            data = process_file(file_path)
            # JSON serializable data를 만듭니다.
            chart_data = {
                'x_values': data['Crosshead(mm)'].tolist(),
                'y_values': data['Load(kN)'].tolist(),
                'columns': data.columns.tolist(),
                'rows': [list(row) for row in data.values]
            }
            
        except Exception as e:
            chart_data = {}  # 데이터 처리 중 오류가 발생하면 빈 데이터를 설정
            print("Error processing the file:", e)

        return render_template('index.html', data=chart_data)
    else:
        # POST 요청이 아닐 때는 빈 데이터를 전달
        return render_template('index.html', data={})

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        column_names_line = lines[6].strip()
        units_line = lines[7].strip()

    column_names = [f"{name}({unit})" for name, unit in zip(column_names_line.split(), units_line.split())]
    data = pd.read_csv(file_path, skiprows=8, sep='\t', header=None, names=column_names, encoding='utf-8')
    
    return data

if __name__ == '__main__':
    app.run(debug=True)
