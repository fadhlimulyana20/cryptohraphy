from UI import app
from flask import render_template, request

from old_ntru import *


@app.route('/ntru/generate-key', methods=['POST'])
def generate_ntru_key():
    data = {
        "public_key": {
            "n": {},
            "p": {},
            "q": {},
            "key": {}
        },
        "poli": {
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

        Bob = Ntru(n, p, q)
        Bob.genPublicKey(f, g, d)
        public_key = Bob.getPublicKey()

        data["public_key"]["key"] = public_key
        data["public_key"]["n"] = n
        data["public_key"]["p"] = p
        data["public_key"]["q"] = q
        data["poli"]["f"] = f
        data["poli"]["g"] = g

        print(data)

        return data

@app.route('/ntru/encrypt', methods=['POST'])
def encrypt_ntru():
    request_data = request.get_json()
    res = {
        "encrypted": {},
        "poli": {}
    }
    if request.method == "POST":
        n = int(request_data['n'])
        p = int(request_data['p'])
        q = int(request_data['q'])
        f = request_data['poli_f'].split(",")
        for i in range(0, len(f)):
            f[i] = int(f[i])
        g = request_data['poli_g'].split(",")
        for i in range(0, len(g)):
            g[i] = int(g[i])
        print("n: ", n)
        print("p: ", p)
        print("q: ", q)
        print("f: ", f)
        print("g: ", g)

        # Bob
        Bob = Ntru(n, p, q)
        Bob.genPublicKey(f, g, 2)
        pub_key = Bob.getPublicKey()

        print("bob created")

        # Alice
        Alice = Ntru(n, p, q)
        Alice.setPublicKey(pub_key)

        print("alice created")

        msg = request_data['plain']
        ranPol = [-1, -1, 1, 1]

        encrypt_msg = Alice.encrypt(msg, ranPol)
        
        res["encrypted"] = str(encrypt_msg["list_e"])
        res["poli"] = str(encrypt_msg["list_input"])
        print(res)

        return res

@app.route('/ntru/decrypt', methods=['POST'])
def decrypt_ntru():
    request_data = request.get_json()
    res = {
        "decrypted": {}
    }
    if request.method == "POST":
        n = int(request_data['n'])
        p = int(request_data['p'])
        q = int(request_data['q'])
        f = request_data['poli_f'].split(",")
        for i in range(0, len(f)):
            f[i] = int(f[i])
        g = request_data['poli_g'].split(",")
        for i in range(0, len(g)):
            g[i] = int(g[i])
        print("n: ", n)
        print("p: ", p)
        print("q: ", q)
        print("f: ", f)
        print("g: ", g)

        # Bob
        Bob = Ntru(n, p, q)
        Bob.genPublicKey(f, g, 2)
        pub_key = Bob.getPublicKey()

        print("bob created")

        # Alice
        Alice = Ntru(n, p, q)
        Alice.setPublicKey(pub_key)

        print("alice created")

        msg = request_data['plain']
        ranPol = [-1, -1, 1, 1]

        encrypt_msg = Alice.encrypt(msg, ranPol)
        
        # BOB
        decrypted_msg = Bob.decrypt(encrypt_msg['list_input'])
        
        res["decrypted"] = decrypted_msg
        print(res)

        return res