from flask import Flask, request, jsonify
import pickle


app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/', methods=['POST'])
def predict():

    data = request.get_json()

    sepal_length = float(data.get("sepal length (cm)"))
    sepal_width = float(data.get("sepal width (cm)"))
    petal_length = float(data.get("petal length (cm)"))
    petal_width = float(data.get("petal width (cm)"))

    predict = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    return str(predict[0])

    





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)