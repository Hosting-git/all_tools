#!/usr/bin/env python3
# btw ini script engga open source untuk non encrypt, jadi... yang nyopet script script, semoga cepet tobat.
# Wajib install ini pip install requests requests[socks]
# sama wajib install ini pip install PySocks colorama pycryptodome

import os, sys, base64, zlib
from Crypto.Protocol.KDF import scrypt
from Crypto.Cipher import AES

def _derive_key(password: bytes, salt: bytes, key_len: int = 32, N=None, r=None, p=None) -> bytes:
    if N is None:
        N = 16384
    if r is None:
        r = 8
    if p is None:
        p = 2
    return scrypt(password, salt, key_len=key_len, N=N, r=r, p=p)

def decrypt_script_with_layers(enc_script, password):
    raw = base64.b64decode(enc_script)
    layers = raw[0]
    scrypt_meta = raw[1:1+6]
    N = int.from_bytes(scrypt_meta[0:4], byteorder='little')
    r = scrypt_meta[4]
    p = scrypt_meta[5]
    data = raw[1+6:]
    for i in range(layers):
        salt = data[:32]
        nonce = data[32:44]
        tag = data[44:60]
        ct = data[60:]
        key = scrypt(password.encode(), salt, key_len=32, N=N, r=r, p=p)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        data = cipher.decrypt_and_verify(ct, tag)
    return zlib.decompress(data).decode()

def add_extra_encryption(enc_script, password):
    raw = base64.b64decode(enc_script)
    current_layers = raw[0]
    scrypt_meta = raw[1:1+6]
    data = raw[1+6:]
    salt = os.urandom(32)
    key = _derive_key(password.encode(), salt, key_len=32)
    nonce = os.urandom(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ct, tag = cipher.encrypt_and_digest(data)
    new_data = salt + nonce + tag + ct
    new_layers = current_layers + 1
    header = new_layers.to_bytes(1, byteorder='big')
    new_scrypt_meta = (16384).to_bytes(4, byteorder='little') + (8).to_bytes(1, byteorder='little') + (2).to_bytes(1, byteorder='little')
    new_blob = header + new_scrypt_meta + new_data
    return base64.b64encode(new_blob).decode()

def check_for_trap():
    return sys.gettrace() is not None or os.getenv("TRAP_MODE") == "1"

def get_decryption_password():
    if check_for_trap():
        # If running under debugger/tracer, try to re-encrypt and exit quickly
        try:
            new_enc = add_extra_encryption("AwBAAAAIAsBRgyYjtGvctmBDjKd7P9z8oWGeoUeyqgLdHdt6fze8q2iXS1kZnPiGcx+a8i07WWh+6Z6tt0sn3ywgpV5gFGSf2fWu+McB4FQdbLC26ZRCnd+tLOT9ypQCdtRV2ZcS6xTM6fl8JDQXTFP64TcHoNKhEab+YZezr3IPVzwJorjBEog+bj1yyF2v3P8e9an1RjM6EogCNFYLFXGw3LrEWSUcd4xvNXLP8jvR+vE/DYwkEcc9RRrp5a2+Frk1VTm/XD1EY5MZe+EB9KDfj7kwLxqw9iw4eGsZkYPv9Ky1IgaUJ7B+Qx02Lh+pfWGIqtOIdjZMQ7xYZXv/D/+aNT61OsdqiSia7tE+T+LqA3hUkKH5wlmZM0jeu6PNEq/iQOHZxijQKaIHWMU8h9/2wI23cQBTbInCW+6IB6Ya1UelFrrhVS/unWmQe3pucwOAc9RqmtPjcpsXTJJFq064RSHVRTUOxtFwqCat+oon2akaQLibNQ2fc257VtrLJPdH8eu2Zt8nMqaIVuLjSAzlyMEj7L2cC8/KhWcW/7SINQjFB0HxoAHJbrRz7TAx8kYRy3GHmewh8TL2a2ylAcx5a9OIb8WSExuauD4SMP0erSdiF4aHqS/Q9U6FEwXI7MM3kcng+HpFrDNjDjZ3CgT4xGHKq+G9mvq/KWgMMljZfI60CCOwlxeh1bYzs53PEw09++wafWyyAxII6agUlgfvm3/zD5cs8et3XK8LJBoyQI8JzvvnL3E9EFs7jqlHpW9hQoLnpcy6cdcW3HYp3+iKhK6vMdfsqbxmm8pFJrONTkuJy62liBRD0/W32TjLHBI6MhWjhXAOwZ5WdRjLP7bStXm4og7VpnI+J+VMcJBtwFfS2gocF3XGB8SRcYlRFocYWe6tKmzcsMf4uVdUYyDWkbzn4b84hOnfE2XSOUq/yxfjfRBcbP9p8lDsImbqdx0aamouCRmeaNjymMrQXoYFyaV7nCc6jP9qGInNQ6t4GlcrP955ipjzFqnfBWERoZ4fCZhA/Jm9r7lOJqROPv/n19xVuhL+kPJHC5e+MrxKcU07bVfbNFm6WkYXISR7bS2HF08BHzUhLSuvEI3FUzbQaJ0PGoh3ezyiKHuGXzWgDy+XwmD+fIAASqijZ7dH47ZKT6ntTvAFzXQI8/UtsEFZPJkHLXLd7iBfwfVzaJ67nUBtirIlzqqp6ZjwSpQB80ZKHS0DBe1sT48j6Jr3OLteaEEH3ITEkGI10+kCWhNytG4CNojYMUf9sF2KPPwBqcvazWSWx8AHsfrDisIZ8y/WmWTBSWH08OGvoI1JJs/Avznc2sC1I2jMwYbiXCoa7+V9FhCVmAp+CLlo5x17fPil8mf3EOhrzkhszRrSoe5M+xcBvjwU03HIBzYUHPOO12d7UFfC1RV4XulIOK2pRtzv3zhRFUO5EsKliskv139uES1RFCmBs/AI8TpLLXwSbxY1qEQ+aCI7G5JM77R6+7azSyZVMpRUCSZC+sacgV3Ma34IOM+zSf8ZgSUKQzYd50FI5Z3D3UikkO1SSUo41As+IZoUMBLdFZgno0cvFMU8DctqCI1gSbmHPC8qeXCurIf7YmOxiwNLDAYrKbObKWB+U6bPt4Je+UfyD54QrobQz43FgXz23crwuBkYA1tzoey0hxq4pRWnMCMm7goGnUGJyTnnwnued3vpa9tUrDqKe4RiWXu/y5RqtVwlsuE5Swq3QdoZGGUr+7Go9yRIb6UA4aPLebCdSNSwcvROPwlKjfsxde+x6CV48P0kCx7UJpsScdtGeeOCx3Dm+IZuZMAmOYfP7SvfvSCiCw/fl7tOVIsWRLJSIDL+3YNhURiSk6JGDzXe0XyqwJSlm+5tbfPlxeVMPPrnaPZr/kjn8ORKWrtoY8pA26slOuM9F+67uX3XhU8U4bBIYqk0XtOxWzSgG2sSpouOpaGHgWBrauO+UiVGgW3KphKhEJfp3mnooGZ27E0oKo+2onj4BaViUNVgpU+8WqyiSgox4oi2jXT0buH0sLdpwKS1oqRtCabXy9iix1ZzA2zC0N4jH3ghRMy72WwBX6h1CkUuAdeeYuYEsZx+bB2bBlqWcLqNor08RAJoj+Pru91QKLkaC0pl7L2OUE31VZdM7UnVC8fnKL4+UV/XlPiiwswgmxntYGis4fjM04WWZb+E4VRyCMAHRDz43OhHb0stsWFrYLzhqB7eKOkaEQbxLmjz8Owo7gK6ORV7lMT4qR7drhIC7eKP4oNYTzc2pNZbK2pHR52S2ksm790/v+LGyRQHM+QvPazrUkwwZD4JH/OR4B3upp803dUX4AW7DyBuR1RY3Ob8lKnZxjQ9OJo0rpz3EZSAU6mH8XtAO9dvDJXULuzfGgglpKuLrdncBZuwQHArFiobTPwKItnDs1N50DxXefU+UeC8N/i2OP/WnuZ3KZQjDf+5auKnRx2q97YkwqVxF7okShPUDt1xv+6wNpgaI0kkOUDl+9pw84I/2x40rUBUNp4DwVBE6damvto+IJmwxPK046MHz2ayvO90ruQHVPOT+/wCJwndEnBtA8b8F5j+sWbIHJeJTgxLweHHXvp56UD4UvW3xmOEgGRUBwReWqSj0RjaLyuJ2ElCxqVa7Boe7P7eCg9TlNiu8MUYwtODn69ZLicHCeV5lHPsEuLPBYPgYhvej8SWP+c/t3w8Pc9Vk9MrT48KLC2XAXdD/rQu/6kYVgxVd/DLnvHtRKrzYOBa6fFmMq/UhnxqVSmLYuc1nmTOrJbSCNwjwK08mNy9Bpo/9cz7VWtMuQPmmfjWHtxkxKyFqDcPLYHdDWrZQcuAVrXcW90hmfc5RY0FJstrfA5GvG2fD6H4rWRJ7vaJ6jQEOIMkUJwZNCWDS001O/wsObwukNxqWgNiRocuFxVxc1WlXRNEPHJll1Ac7Ff1GcYNrqwFlnwuhkQmmVqf+1E/cFXSBKzZ0gbeNcLFDjg0Gd8Z15RvpzBfvCxUgfu6A9XvizG3HNiKLOzHiVeUsKCLlZOCE8EQmsR416sM8icoKKu1WIHIN5TQDrg3RH9eBVonRHUb22I3Am2c/pQjEk2FBqNWXy/flcvN0Gw1JujEzBjqjxemIYQSXPCCHG+a/sSHj9+sixAhUsmmbG7GLw6HhYryBBPI5kKFAYpGP5EGKyePSHxFjytkx/7D2hcTF3BBU52S3hDHscyoDonQUy2S/bNZZIIF+BSZMNW4Wu3kVRVmh9CSHANJfXSQ9dPsWvZa1Om7Tu4oXz6SCR2+bdqzkonG4Xlqn+emoZ0h6Lq0oIZMvp/mWE5Gg78i5DLtdC08T/DFax7QGnCSag7N0g5B9E/tfIFOwaRiH4iZclw7kgyLaR3FMJ2w54A1SbF4d2bhe6gMxcdArS7di0S86CZdFdORn6u2GSUDm8ks8f2JTDSu6nJYLLtZRQJrsWENLH7qzDTYg0JbEkXmGq/OT9BqkPOK+T4vINWumbaNEARANN49DymEP+1FeJzG93EDF+EGgUpWkyKputNAyJaJCI/zp5/YL0jjawncfLi/bUfhEjg6/XyentqV6yP41szmSBUiuokfqnrY5Guo5oGmYA7o90LxhPvzmcyoHTYGvrH7mFiIHoyXfucFyJzjsIsUjXk4ESHSug/6u8BA5bT5c5oFQffASDyTUhBjjZroZVgY/Pee02AfIQUz98PrcxZIQ4SUHE2VlOD1fm4RIx7+o6YP885mfr+V+QctDfTv1TjtdO5Lwnv9kHOaR7CfdpFxMHV4CHkM8ORyyX6fECzTM3eRNJzJEwg/g2cvhj7H5DOf53oS2dQ6xefZLaserTlGgjxhJmFbe4jWFZVWzSGidhdcuR3joUOSgqFuXqaiDF0vjYpDqpO8hRDH/zBOq+KEhWuOTmfUYg7IjxC004taaByFy+r+lHqaM/srKpjbNtbBIqUSzI1Cve8F7V9i8Ffmc0q7esiggG//N7eDIEpSKaPzQyMswVA2XjBPjs2vsnTx", get_decryption_password_actual())
            with open(__file__, "w") as f:
                f.write(generate_self_decrypt_stub(new_enc, get_decryption_password_actual()))
        except Exception:
            pass
        print("Trap activated. Payload re-encrypted.")
        sys.exit(1)
    return get_decryption_password_actual()

def get_decryption_password_actual():
    enc_pwd_blob = "G5YCtSnSj4aDQ+8acci7vPIBH3svSi/8BAGXbwqZcebpkCQmHzFsxqAFU6fXGj2zww=="
    magic_key = b"gen_z_magic_key_for_decrypt_32b!"
    raw = base64.b64decode(enc_pwd_blob)
    salt = raw[:16]
    nonce = raw[16:28]
    tag = raw[28:44]
    ct = raw[44:]
    key = _derive_key(magic_key, salt, key_len=32)
    return AES.new(key, AES.MODE_GCM, nonce=nonce).decrypt_and_verify(ct, tag).decode()

def generate_self_decrypt_stub(enc_data, password):
    # tiny helper for self-write back on trap
    # avoid infinite recursion in stub write-back by writing minimal stub
    return open(__file__, "r").read()

if __name__ == '__main__':
    password = get_decryption_password()
    if check_for_trap():
        new_enc = add_extra_encryption("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", password)
        with open(__file__, "w") as f:
            f.write(generate_self_decrypt_stub(new_enc, password))
        print("Trap activated. Payload re-encrypted.")
        sys.exit(1)
    decrypted_code = decrypt_script_with_layers("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", password)
    exec(decrypted_code)
