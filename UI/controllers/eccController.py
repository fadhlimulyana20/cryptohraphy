from flask import request
from tinyec.ec import Point
from UI import app
from tinyec import registry
import secrets

from ecc import decrypt_ECC, encrypt_ECC

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

@app.route('/ecc/encrypt', methods=['POST'])
def encrypt_ecc():
    request_data = request.get_json()
    res = {
        "encrypted": {}
    }
    if request.method == "POST":
        print(request_data)

        public_key = {
            "x": int(request_data['x']), 
            "y": int(request_data['y'])
        }

        message = request_data['plain']
        
        res["encrypted"] = encrypt_ECC(message, public_key)
        print(res)

        return res

@app.route('/ecc/decrypt', methods=['POST'])
def decrypt_ecc():
    request_data = request.get_json()
    res = {
        "decrypted": {}
    }
    if request.method == "POST":
        print(request_data)

        public_key = {
            "x": int(request_data['x']), 
            "y": int(request_data['y'])
        }
        private_key = int(request_data['private_key'])

        message = request_data['encrypted'].split()
        map_message = map(int, message)
        list_message = list(map_message)
        
        res["decrypted"] = decrypt_ECC(list_message, private_key, public_key)
        print(res)

        return res