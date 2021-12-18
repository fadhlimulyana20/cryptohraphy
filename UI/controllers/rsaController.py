from UI import app
from flask import render_template, request

from rsa import decrypt_data, encrypt_data, generate_private_key, generate_public_key

@app.route('/rsa/generate-key', methods=['POST'])
def generate_rsa_key():
    data = {
        "public_key": {
            "n": {},
            "e": {}
        },
        "private_key": {}
    }
    if request.method == "POST":
        # Memilih 2 bilangan prima yang besar
        p = 271
        q = 173

        public_key = generate_public_key(p, q)
        private_key = generate_private_key(p, q, public_key[1])

        data["public_key"]["n"] = public_key[0]
        data["public_key"]["e"] = public_key[1]
        data["private_key"] = private_key

        return data
    
@app.route('/rsa/encrypt', methods=['POST'])
def encrypt_rsa():
    request_data = request.get_json()
    res = {
        "encrypted": {}
    }
    if request.method == "POST":
        block_length = 3
        print(request_data)

        public_key = [int(request_data['n']), int(request_data['e'])]

        message = request_data['plain']
        
        res["encrypted"] = encrypt_data(message, public_key[0], public_key[1], block_length)
        print(res)

        return res

@app.route('/rsa/decrypt', methods=['POST'])
def decrypt_rsa():
    request_data = request.get_json()
    res = {
        "decrypted": {}
    }
    if request.method == "POST":
        block_length = 3
        print(request_data)

        public_key = [int(request_data['n']), int(request_data['e'])]
        private_key = int(request_data['private_key'])

        message = request_data['encrypted'].split()
        map_message = map(int, message)
        list_message = list(map_message)
        
        res["decrypted"] = decrypt_data(list_message, private_key, public_key[0], block_length)
        print(res)

        return res