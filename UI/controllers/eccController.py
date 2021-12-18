import binascii
from flask import request
from tinyec.ec import Point
from UI import app
from tinyec import registry
import secrets

from ecc import encrypt_ECC

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

# @app.route('/ecc/encrypt', methods=['POST'])
# def encrypt_ecc():
#     request_data = request.get_json()
#     res = {
#         "encrypted": {}
#     }
#     if request.method == "POST":
#         curve = registry.get_curve('brainpoolP256r1')
#         public_key = Point(curve, int(request_data['public_key_x']), int(request_data['public_key_y']))
#         # private_key = int(request_data['private_key'])

#         message = request_data['plain']
        
#         encryptedMsg = encrypt_ECC(bytes(message, 'utf-8'), public_key)
#         encryptedMsgObj = {
#             'ciphertext': binascii.hexlify(encryptedMsg[0]),
#             'nonce': binascii.hexlify(encryptedMsg[1]),
#             'authTag': binascii.hexlify(encryptedMsg[2]),
#             'ciphertextPubKey': hex(encryptedMsg[3].x) + hex(encryptedMsg[3].y % 2)[2:]
#         }

#         res["encrypted"] = str(encryptedMsgObj['ciphertext'].decode('utf-8'))
#         print(res)

#         return res

# @app.route('/ecc/decrypt', methods=['POST'])
# def decrypt_ecc():
#     request_data = request.get_json()
#     res = {
#         "decrypted": {}
#     }
#     if request.method == "POST":
#         block_length = 3
#         print(request_data)

#         public_key = [int(request_data['n']), int(request_data['e'])]
#         private_key = int(request_data['private_key'])

#         message = request_data['encrypted'].split()
#         map_message = map(int, message)
#         list_message = list(map_message)
        
#         res["decrypted"] = decrypt_data(list_message, private_key, public_key[0], block_length)
#         print(res)

#         return res

