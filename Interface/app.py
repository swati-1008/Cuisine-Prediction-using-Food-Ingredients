from flask import Flask, render_template, request, redirect, url_for
import pickle
import sklearn
import warnings

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def first():
    if request.method == 'GET':
        return render_template('first_page.html')
    return render_template('prediction.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        input_ingredients = request.form.get('ingredients')
        # print ([input_ingredients])
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            file = open('cuisine_prediction.pickle', 'rb')
            data = pickle.load(file)
            cv = pickle.load(open("CountVect.pkl", "rb"))
            enc = pickle.load(open("LabelEncoder.pkl", "rb"))
            file.close()
            lis = [input_ingredients]
            inp = cv.transform(lis)
            # while len(lis) != 3010:
                # lis.append(None)
            # print(lis)
            var = enc.inverse_transform(data.predict(inp))
            return render_template('result.html', var1 = var)
            # return f"The cuisine is of {(enc.inverse_transform(data.predict(inp)))} origin."
            # print(data.predict([[lis]]))
            # return redirect(url_for('first'))
    return render_template('prediction.html')

if __name__ == "__main__":
    app.run(debug = True)





# Dictionary >> list >> sparse matrix >> predict