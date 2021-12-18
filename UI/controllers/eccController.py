import binascii
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
        data['private_key'] = str(privKey)
        data['public_key']['x'] = str(pubKey.x)
        data['public_key']['y'] = str(pubKey.y)
        # Return data
        return data

@app.route('/ecc/encrypt', methods=['POST'])
def encrypt_ecc():
    request_data = request.get_json()
    res = {
        'ciphertext': {},
        'nonce': {},
        'authTag': {},
        'ciphertextPubKey': {}
    }
    
    if request.method == "POST":
        curve = registry.get_curve('brainpoolP256r1')
        pubKey = Point(curve, int(request_data['x']), int(request_data['y']))
        print(request_data)

        message = request_data['plain']

        encryptedMsg = encrypt_ECC(bytes(message, 'utf-8'), pubKey)
        encryptedMsgObj = {
            'ciphertext': binascii.hexlify(encryptedMsg[0]),
            'nonce': binascii.hexlify(encryptedMsg[1]),
            'authTag': binascii.hexlify(encryptedMsg[2]),
            'ciphertextPubKey': hex(encryptedMsg[3].x) + hex(encryptedMsg[3].y % 2)[2:]
        }

        res['ciphertext'] = str(encryptedMsgObj['ciphertext'].decode('utf-8'))
        res['nonce'] = str(encryptedMsgObj['nonce'].decode('utf-8'))
        res['authTag'] = str(encryptedMsgObj['authTag'].decode('utf-8'))
        res['ciphertextPubKey'] = {
            'x': str(encryptedMsg[3].x),
            'y': str(encryptedMsg[3].y)
        }
        print(res)

        return res

@app.route('/ecc/decrypt', methods=['POST'])
def decrypt_ecc():
    request_data = request.get_json()
    res = {
        "decrypted": {}
    }
    if request.method == "POST":
        # print(request_data)

        # ciphertext = request_data['ciphertext']
        # nonce = request_data['nonce']
        # authTag = request_data['authTag']
        # ciphertextPubKey = request_data['ciphertextPubKey']

        # curve = registry.get_curve('brainpoolP256r1')
        # pubKey = Point(curve, int(request_data['x']), int(request_data['y']))

        # encryptedMsgObj = (
        #     bytes(ciphertext, 'utf-8'),
        #     bytes(nonce, 'utf-8'),
        #     bytes(authTag, 'utf-8'),
        #     pubKey
        # )

        private_key = int(request_data['private_key'])
        # decryptedMsg = decrypt_ECC(encryptedMsgObj, private_key)
        
        # res["decrypted"] = str(decryptedMsg.decode('utf-8'))
        # print(res)

        curve = registry.get_curve('brainpoolP256r1')
        pubKey = Point(curve, int(request_data['x']), int(request_data['y']))
        print(request_data)

        message = request_data['plain']

        encryptedMsg = encrypt_ECC(bytes(message, 'utf-8'), pubKey)
        decryptedMsg = decrypt_ECC(encryptedMsg, private_key)
        res['decrypted'] = decryptedMsg.decode('utf-8')
        return res
