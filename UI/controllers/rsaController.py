from UI import app
from flask import render_template, request

from rsa import generate_private_key, generate_public_key

@app.route('/rsa/generate-key', methods=['POST'])
def generateKey():
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
    