from UI import app
from flask import render_template, request

from ntru import *


@app.route('/ntru/generate-key', methods=['POST'])
def generate_ntru_key():
    data = {
        "public_key": {
            "n": {},
            "p": {},
            "q": {}
        },
        "rand_poli": {
            "f": {},
            "g": {}
        }
    }
    if request.method == "POST":
        n = 7
        p = 29
        q = 491531
        f = [1, 1, -1, 0, -1, 1]
        g = [-1, 0, 1, 1, 0, 0, -1]
        d = 2

        # public_key = generate_public_key(p, q)
        # private_key = generate_private_key(p, q, public_key[1])

        # data["public_key"]["n"] = public_key[0]
        # data["public_key"]["e"] = public_key[1]
        # data["private_key"] = private_key

        return data
