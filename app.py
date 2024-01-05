from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open('my_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input values from the form
        marketing = float(request.form['marketing'])
        administration = float(request.form['administration'])
        rd_spending = float(request.form['rd_spending'])

        # Make prediction using the loaded model
        prediction = model.predict([[marketing, administration, rd_spending]])

        return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
