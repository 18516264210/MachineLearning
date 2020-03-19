# -*- coding:utf-8 -*-


from flask import Flask,request
import base64, hashlib
from Crypto.Cipher import AES

class AESCipher():
    """
    Usage:
        c = AESCipher('password').encrypt('message')
        m = AESCipher('password').decrypt(c)
    Tested under Python 3 and PyCrypto 2.6.1.
    """

    def __init__(self, key):
        self.key = hashlib.md5(key.encode('utf8')).hexdigest()
        print("key:%s"%(key))

        # Padding for the input string --not
        # related to encryption itself.
        self.BLOCK_SIZE = 32  # Bytes
        self.pad = lambda s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * chr(self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE)
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    # 加密
    def encrypt(self, raw):
        raw = self.pad(raw)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(raw))

    # 解密，针对微信用此方法即可
    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return self.unpad(cipher.decrypt(enc)).decode('utf8')

app = Flask(__name__)

@app.route("/decode",methods=["GET","POST"])
def decode():
    mt = request.method
    print("请求方法：%s" % (mt))

    req_info = request.form.get("req_info")
    print("解密数据：%s" % (req_info))

    key = "99ba136891a15506c95788651de6744e"
    v = AESCipher(key).decrypt(req_info)
    print("解密结果：%s" % (v))

    return v

@app.route("/encode",methods=["GET","POST"])
def encode():
    mt = request.method
    print("请求方法：%s" % (mt))

    req_info = request.form.get("req_info")
    print("加密数据：%s" % (req_info))

    key = "99ba136891a15506c95788651de6744e"
    v = AESCipher(key).encrypt(req_info)
    print("加密结果：%s" % (v))

    return v

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9999, debug=True)