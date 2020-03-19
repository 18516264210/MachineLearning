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
        print(key)

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


pwd = '99ba136891a15506c95788651de6744e'
msg = "iPmyWg2r2YfxpcggGzCulM7y+USVEQSS6RSX3Co1qGImrfzBVE3DS0AD5LmW58on89E3K53sXUNWljFy1CikxqcW3RRBnZ7+b+R6snhk8kNgndrt08AJ7z6NzynxYe4C/v9eDnqSffSi/AC9nCTYnTrLvt0xcCGIWLgS7EupEDGG4Fv3wIXfOPVRZiEWIuP/ZbJwElbqxI8N5R+gKP4R2v7Xtp6iuOmDzqqchSF3JhM0WRUIArEChw4mNtgV+tR031DBybDal4qrkvdxKruCeOCGMr0lKX8Ag/1fP4z/Vkpsn6nfHuBBcTsLacPaxH+2SqC3I1m2s0Y6O508FIdgduC/TGOaUHxNGNyX+DkvOcMOD2Fdr7q5gFuLPtPBVlxKStsXdsVzeU4pu49e9BueyEJWdiYn1jE4Zd72XiZ/wVzcCbud4NJ8io8QHx1zcrfgWzt04EHG5IMFVatpzLnvFEK1SsFP9I1Fh93LtYQNXuTOAykFDre/VdwKlciDCQQ3IXgtG9Ua6Wze1i8dYQAft4y0huceYvKhcE5Z4yWmZ95bePpnPLfYq12zHxFzi8utXXeQnUgjXwnqBgv0PdDuLCScD0WtHy7BqbMCNmVDvu7aJFL2gAiknRfz2fJKM58WRS7hipL/Ogeu+km2I9L2XsAzYjwZ8KL7OMpuzC6d319X8/xR6UVEo0l7mvEwBiqBFUyU3hORdJoh1DMUh19KDzqHdsaTMEghOsFE05LMctesGdgCXeOT70m8AtdG3Q1Y5Y3IeZwWEWkpPMfp2ywq10RVGFj79dx/K8utNNjrodSMiBR3nkhJmDiuB8Bu4Yto37BV0UliLnvJwGfLpj8iRg+UcX9thjVAdc3Ql82Zn1u+RplO34k6Hppoz0WM3IX1DBduQHl3MX8KdsYCTg5AD4AlmLDTaAvz2foucPorqza72xOutc/HQkPRGVOCcc+i8/BLpMr2a8knrC8iPAtjldDBvXiIFeK9usXQS7GrZ1d8/9Xbup5sF9WK3hLXs0ZikDlAAfdtUvP/9l6qd0p+ssoeY7DWCG4suz0jOzsiIXk="
print(AESCipher(pwd).decrypt(msg))