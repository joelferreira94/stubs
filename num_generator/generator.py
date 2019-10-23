from flask import Flask
from flask import jsonify
import uuid

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/", methods=['POST'])
def number():
    uuid_generated = uuid.uuid4()
    data = jsonify(
        data = "UUID Value",
        uuid = uuid_generated,
    )
    return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)