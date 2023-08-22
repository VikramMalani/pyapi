from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/get_data', methods=['GET'])
def get_data():
    try:
        data = pd.read_csv('data.csv')
        return jsonify(data.to_dict(orient='records'))
    except Exception as e:
        return jsonify(error=str(e))


@app.route('/api/download_csv', methods=['GET'])
def download_csv():
    api_key = request.args.get('api_key')
    
    # Validate the API key (replace 'customapibyvikram#21m' with the actual API key)
    if api_key == 'customapibyvikram#21m':
        try:
            data = pd.read_csv('data.csv')
            response = make_response(data.to_csv(index=False))
            response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
            response.headers['Content-Type'] = 'text/csv'
            return response
        except Exception as e:
            return jsonify(error=str(e))
    else:
        return jsonify(error='Invalid API Key')

if __name__ == '__main__':
    app.run(debug=True)