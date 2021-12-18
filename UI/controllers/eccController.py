from flask import request
from tinyec.ec import Point
from UI import app
from tinyec import registry
import secrets

@app.route('/ecc/generate-key', methods=['POST'])
def generate_ecc_key():
    data = {
        "public_key": {
            "x": {},
            "y": {}
        },
        "private_key": {}
    }
    if request.method == "POST":
        curve = registry.get_curve('brainpoolP256r1')
        privKey = secrets.randbelow(curve.field.n)
        pubKey = privKey * curve.g
        # Assign data
        data['private_key'] = privKey
        data['public_key']['x'] = str(pubKey.x)
        data['public_key']['y'] = str(pubKey.y)
        # Return data
        return data

