from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model (adjust the path if necessary)
with open('/home/rohan/Desktop/Ai/projects/experience-portal/wheat_kernel_classification/web_app/wheat_kernel_classfier.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def Home():
    prediction = None  # Initialize prediction variable
    error = None  # To store error messages
    
    if request.method == 'POST':
        try:
            # Retrieve and convert form data to float
            c1 = float(request.form.get('c1'))
            c2 = float(request.form.get('c2'))
            c3 = float(request.form.get('c3'))
            c4 = float(request.form.get('c4'))
            c5 = float(request.form.get('c5'))
            c6 = float(request.form.get('c6'))
            c7 = float(request.form.get('c7'))
        except ValueError:
            error = "Invalid input. Please enter valid numbers for all fields."

        if not error:
            # Prepare the data as a 2D array (model usually expects 2D data for prediction)
            input_data = np.array([[c1, c2, c3, c4, c5, c6, c7]])

            # Make the prediction
            prediction = model.predict(input_data)[0]  # Get the first prediction

            # Convert prediction to a regular Python type (int or float)
            prediction = int(prediction) if isinstance(prediction, np.int64) else float(prediction)

        # Return the prediction as JSON
        return jsonify({'prediction': prediction, 'error': error})

    return render_template('index.html', prediction=prediction, error=error)

if __name__ == '__main__':
    app.run(debug=True)
