from flask import Flask
from flask import jsonify
from flask import request
import uuid

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/resourceFunction/msisdn/<msisdn>", methods=['GET'])
def number(msisdn):
    uuid_generated = uuid.uuid4()
    number_1 = msisdn

    data = {
        "id" : f"localhost:5002/resourceFunction/msisdn/{number_1}",
        "uuid" : uuid_generated,
        "features" : {"name":"joel"}
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)