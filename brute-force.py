#!/usr/bin/env python3
# Nanti kalo gacoor repositori ini lu kasih gw bintang ya oke, heheheheheheh
# jangan reqode mekkk bocah puqiii

import os, sys, base64, zlib, getpass
from Crypto.Protocol.KDF import scrypt
from Crypto.Cipher import AES

def decrypt_script_with_layers(enc_script, password):
    raw = base64.b64decode(enc_script)
    layers = raw[0]
    data = raw[1:]
    for _ in range(layers):
        salt = data[:32]
        nonce = data[32:44]
        tag = data[44:60]
        ct = data[60:]
        key = scrypt(password, salt, key_len=32, N=131072, r=8, p=2)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        data = cipher.decrypt_and_verify(ct, tag)
    return zlib.decompress(data).decode()

def add_extra_encryption(enc_script, password):
    raw = base64.b64decode(enc_script)
    current_layers = raw[0]
    data = raw[1:]
    salt = os.urandom(32)
    key = scrypt(password, salt, key_len=32, N=131072, r=8, p=2)
    nonce = os.urandom(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ct, tag = cipher.encrypt_and_digest(data)
    new_data = salt + nonce + tag + ct
    new_layers = current_layers + 1
    header = new_layers.to_bytes(1, byteorder='big')
    new_blob = header + new_data
    return base64.b64encode(new_blob).decode()

def check_for_trap():
    return sys.gettrace() is not None or os.getenv("TRAP_MODE")=="1" or os.getenv("PYTHONDEBUG")=="1" or os.getenv("HACKER_MODE")=="1"

def trigger_decoy():
    print("Waduh, kamu kena jebakan decoy! Gak ada apa-apa di sini, bro!")
    try:
        with open("decoy_payload.txt", "w") as f:
            f.write("Decoy data: jangan main-main!")
    except Exception:
        pass
    sys.exit(1)

def get_decryption_password():
    if check_for_trap():
        trigger_decoy()
    return get_decryption_password_actual()

def get_decryption_password_actual():
    enc_pwd_blob = "jlQ72D0iwZ0nDwHmjAMZJkRCKs3Hu6R1+aBcN4J8YO+NsgNoDHNT+H95ITvqQb5gfwGGZZaGcQ=="
    magic_key = b"gen_z_magic_key_for_decrypt_32b!"
    raw = base64.b64decode(enc_pwd_blob)
    salt = raw[:16]
    nonce = raw[16:28]
    tag = raw[28:44]
    ct = raw[44:]
    return AES.new(scrypt(magic_key, salt, key_len=32, N=131072, r=8, p=2),
                   AES.MODE_GCM, nonce=nonce).decrypt_and_verify(ct, tag).decode()

if __name__ == "__main__":
    password = get_decryption_password()
    if check_for_trap():
        trigger_decoy()
    decrypted_code = decrypt_script_with_layers("A96fXq1YpFZQFAFfKe3z2WSng0LrDuGF5kVQDD1qYWDX0G60PH67TUZwwHrkvQ3+5zDlqRz72AIcshv8iJf8F1bZ2kQwEUNbJQcsfqwlHSdgVaCFYFqCjQWzJ2lXyZkxPXXrsZxYzSvIp+/g9LRpmZ7aNh7imU9/BeC8vplS2vVhvZWHkO+ozzXQzZ+Z+8BTpJ3Y9ICY+D93mGg6mAUE3kUgNFFNGlRTVml/Yy/b/2ZK59Wup3by1YahVGXnanoFJDl7iSL8tODQn3WpaI34WlD7N4/S16J3Kkp0jBQ5hye+KlJ9Sj77u+nsLJV8pgFITDac2S34cyBV7M3aycZN2lsQpONOBVux8TX+ruJsv4FiZy215Lkm8IxATI2s/Z44N64N4c2eMtB7VqmdV8tulxp9OIYUG6Afn3HQGsJhHU/oxmFiYgXOHzwddkDgncamz01UAsXCL6KUwuDnBFri2yKB9v7lAI/OyW72pDjyj0kg74NrUud88uEyof6yxmeHYONmMXz9zbGYBnmnhD8K3BrW/tJTFKSy8O5wwLpkQsT6zEpiwXNs4l1NjUes/for7ZN9Bo2BrzEl0FEUIq4mgigo9BZ9doO5+fOqkiaflZqBVeTij086H0gCNzhYVnByKlFiIf01ZqfrjXcYlXyOiLkUl2WVOUyq6Gl3tlzoNo/NUpPEL5ftq5W1Vl0+9yoqXkTrJaVFnBuuaeCSooYDW3nTmg4qR382eCINN7hADpSg1gc0a47fTLmDSSa/7Oymw0KqBgIPOgvT+9TBm9T8mP7Iz0iliiiWlZFfkcx8UGmr6f++y+bOJF9STFdRkj8C+ta5mQKdiIdoV5Oel3zc7hYS9RbrrpQc6Ckp90odNY7s2/93//GE4ydgn3BFmFrDvZHwOAMfgYQSaTYSFTY3lmK80BNr8+Mv4ZTMg30rZrJ2dcaGVGIoWSwsERtfvHr71JbT0wV3KfM3lvMgnEP2Ry+9VFuY2WKqkYzByzOuHuLs7NcWrjTYsQIaJxDNB2iDjabJYTnM7ZQlOVTE7cq4RS9/tHqoJvuKcY+xtKsw+sEb0IzwjapcawiYc9oDWTCx/4BWBoGozvWGsIae4Pv/ntYfm2SEVpiNZaNVYW0M+kRJ6ER2wAj5z+x9c6SVQ1nwWks95p6lwxZHL4tDb9DZNGOc582VrtwOISyguQVeSb5C5EkBhbVpBVxmazUwAOSLRdTC9q5NdEjIGWhd+i1n/tw9xUpvpTh4+EXCMN1yfDY+JlJKGfnqLHRkncN+EtrVm2nJcGM87jJ4Xl08WlZJxzcJDr2NgCsarp3tUTuQT3W7wcYBZTDUyou7x47/w5P2wMrvF6TBTZnBfk8M4vVy/woE9k0N/G8k0o1wzK7sPPYwPFwjGldj30FG/LoUX05CVdMC5nEjMGxxhg==", password)
    exec(decrypted_code)
