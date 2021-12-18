from tinyec import registry
from Crypto.Cipher import AES
import hashlib, secrets, binascii

from tinyec.ec import Point

def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

def ecc_point_to_256_bit_key(point):
    sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
    sha.update(int.to_bytes(point.y, 32, 'big'))
    return sha.digest()

curve = registry.get_curve('brainpoolP256r1')

def encrypt_ECC(msg, pubKey):
    ciphertextPrivKey = secrets.randbelow(curve.field.n)
    sharedECCKey = ciphertextPrivKey * pubKey
    secretKey = ecc_point_to_256_bit_key(sharedECCKey)
    ciphertext, nonce, authTag = encrypt_AES_GCM(msg, secretKey)
    ciphertextPubKey = ciphertextPrivKey * curve.g
    return (ciphertext, nonce, authTag, ciphertextPubKey)

def decrypt_ECC(encryptedMsg, privKey):
    (ciphertext, nonce, authTag, ciphertextPubKey) = encryptedMsg
    sharedECCKey = privKey * ciphertextPubKey
    secretKey = ecc_point_to_256_bit_key(sharedECCKey)
    plaintext = decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey)
    return plaintext

if __name__=="__main__":
    msg = b'Text to be encrypted by ECC public key and ' \
        b'decrypted by its corresponding ECC private key'
    print("original msg:", msg.decode('utf-8'))
    print("")
    privKey = secrets.randbelow(curve.field.n)
    pubKey = privKey * curve.g

    print("Public Key:", pubKey.curve)
    print("Public Key x:", pubKey.x)
    print("Public Key y:", pubKey.y)
    print("Private Key:", privKey)
    print("")

    # print(curve)

    # print(Point(curve, 33188084935718721586253417317385556586978377471735549632597711170147876769960, 28884836925439573423809771337372983380842880381421140302938034862970615955719))

    encryptedMsg = encrypt_ECC(msg, pubKey)
    # print(encryptedMsg[3])
    print("")
    encryptedMsgObj = {
        'ciphertext': binascii.hexlify(encryptedMsg[0]),
        'nonce': binascii.hexlify(encryptedMsg[1]),
        'authTag': binascii.hexlify(encryptedMsg[2]),
        'ciphertextPubKey': hex(encryptedMsg[3].x) + hex(encryptedMsg[3].y % 2)[2:]
    }
    print("encrypted msg:", encryptedMsgObj)
    print("")
    
    decryptedMsg = decrypt_ECC(encryptedMsg, privKey)
    print("decrypted msg:", decryptedMsg.decode('utf-8'))