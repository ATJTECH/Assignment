from flask import Flask, render_template, request

app = Flask(__name__)

# Column names for input features
column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
                'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
                'hours-per-week', 'native-country']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = {col: request.form[col] for col in column_names}
    # You can add additional processing here if needed
    return render_template('index.html', input_data=input_data)

if __name__ == '__main__':
    app.run(debug=True)
