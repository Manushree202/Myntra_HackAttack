from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    trend_data = pd.read_csv('identified_trends.csv')
    return render_template('dashboard.html', data=trend_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
