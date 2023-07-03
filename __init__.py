import pickle
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
dataset = pd.DataFrame(pickle.load(open('exported-df.pkl', 'rb')))
model = pickle.load(open('ExtraTreesRegressor.pkl', 'rb'))
education = dataset['Education Level'].unique()
jobs = sorted(dataset['Job Title'].unique())
@app.route('/')
def index():
    return render_template('index.html', education = education, jobs = jobs)
@app.route('/api/predict')
def predict():
    education = request.args.get('educ')
    job = request.args.get('job')
    exp = int(request.args.get('exp'))
    age = int(request.args.get('age'))
    gender = int(request.args.get('gender'))
    salary = model.predict(pd.DataFrame({"Education Level": [education],"Job Title": [job],"Years of Experience": [exp],"Age": [age],"Gender": [gender]}))
    return jsonify({"salary":round(salary[0])})

if __name__ == '__main__':
    app.run(debug=True)