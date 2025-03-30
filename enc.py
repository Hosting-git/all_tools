#!/usr/bin/env python3
_A=b'gen_z_magic_key_for_decrypt_32b!'
import os,sys,base64,getpass,zlib
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
try:from colorama import init,Fore,Style;init(autoreset=True)
except ImportError:
	class Dummy:
		def __getattr__(A,attr):return''
	Fore=Dummy();Style=Dummy()
def encrypt_script_with_layers(script,password,layers=3):
	'\n    Compress dan encrypt script secara berlapis.\n    ';B=layers;A=zlib.compress(script.encode())
	for K in range(B):C=os.urandom(32);E=scrypt(password,C,key_len=32,N=131072,r=8,p=2);D=os.urandom(12);F=AES.new(E,AES.MODE_GCM,nonce=D);G,H=F.encrypt_and_digest(A);A=C+D+H+G
	I=B.to_bytes(1,byteorder='big');J=I+A;return base64.b64encode(J).decode()
def decrypt_script_with_layers(enc_script,password):
	'\n    Decrypt dan decompress script yang terenkripsi.\n    ';B=base64.b64decode(enc_script);C=B[0];A=B[1:]
	for J in range(C):D=A[:32];E=A[32:44];F=A[44:60];G=A[60:];H=scrypt(password,D,key_len=32,N=131072,r=8,p=2);I=AES.new(H,AES.MODE_GCM,nonce=E);A=I.decrypt_and_verify(G,F)
	return zlib.decompress(A).decode()
def add_extra_encryption(enc_script,password):'\n    Tambahkan satu lapisan enkripsi ekstra.\n    ';A=base64.b64decode(enc_script);D=A[0];E=A[1:];B=os.urandom(32);F=scrypt(password,B,key_len=32,N=131072,r=8,p=2);C=os.urandom(12);G=AES.new(F,AES.MODE_GCM,nonce=C);H,I=G.encrypt_and_digest(E);J=B+C+I+H;K=D+1;L=K.to_bytes(1,byteorder='big');M=L+J;return base64.b64encode(M).decode()
def generate_self_decrypt_stub(enc_data,password):'\n    Buat stub executable Python untuk dekripsi otomatis.\n    ';C=_A;A=os.urandom(16);D=scrypt(C,A,key_len=32,N=131072,r=8,p=2);B=os.urandom(12);E=AES.new(D,AES.MODE_GCM,nonce=B);F,G=E.encrypt_and_digest(password.encode());H=base64.b64encode(A+B+G+F).decode();I=f'''#!/usr/bin/env python3
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
    header = new_layers.to_bytes(1, byteorder=\'big\')
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
    enc_pwd_blob = "{H}"
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
    decrypted_code = decrypt_script_with_layers("{enc_data}", password)
    exec(decrypted_code)
''';return I
def generate_self_decrypt_stub_bash(enc_data,password):'\n    Buat stub executable Bash yang nge-run Python untuk dekripsi otomatis.\n    Perubahan: Menghilangkan trap agar file tidak dihapus setelah dieksekusi.\n    ';C=_A;A=os.urandom(16);D=scrypt(C,A,key_len=32,N=131072,r=8,p=2);B=os.urandom(12);E=AES.new(D,AES.MODE_GCM,nonce=B);F,G=E.encrypt_and_digest(password.encode());H=base64.b64encode(A+B+G+F).decode();I=f'''#!/bin/bash
# File tidak akan dihapus otomatis setelah dijalankan
decrypted=$(python3 - << \'EOF\'
import base64, sys, zlib, os
from Crypto.Protocol.KDF import scrypt
from Crypto.Cipher import AES

def get_decryption_password():
    enc_pwd_blob = "{H}"
    magic_key = b"gen_z_magic_key_for_decrypt_32b!"
    raw = base64.b64decode(enc_pwd_blob)
    salt = raw[:16]
    nonce = raw[16:28]
    tag = raw[28:44]
    ct = raw[44:]
    return AES.new(scrypt(magic_key, salt, key_len=32, N=131072, r=8, p=2),
                   AES.MODE_GCM, nonce=nonce).decrypt_and_verify(ct, tag).decode()

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

password = get_decryption_password()
print(decrypt_script_with_layers("{enc_data}", password))
EOF
)
if [ $? -ne 0 ]; then
    echo "Eh, lo kenapa di sini?"
    exit 1
fi
bash -c "$decrypted"
''';return I
def main():
	L='w';K='Masukin password enkripsi: ';I='r';print(f"{Fore.CYAN}{Style.BRIGHT} ____            _             _        _   _       _");print('|  _ \\ __ _  ___| | ____ _  __| |   ___| |_| |__   (_) ___');print("| |_) / _` |/ __| |/ / _` |/ _` |  / __| __| '_ \\  | |/ _ \\");print('|  __/ (_| | (__|   < (_| | (_| |  \\__ \\ |_| | | | | |  __/');print('|_|   \\__,_|\\___|_|\\_\\__,_|\\__,_|  |___/\\__|_| |_| |_|\\___|');print(f"\npassword(ObfusCation_tripel_encrypt) - Advanced Multi-Layer Encryption Edition");print(' Python & Bash/Shell Script Encryption & Obfuscation Tool with Trap Mechanisms'+Style.RESET_ALL);print(f"{Fore.YELLOW}Pilih opsi:");print('1. Enkripsi script Python');print('2. Dekripsi script Python (Output plaintext)');print('3. Enkripsi script Python dengan stub executable (trap & re-encrypt on access)');print('4. Enkripsi script Bash/Shell dengan stub executable (tanpa prompt input)');H=input(f"{Fore.GREEN}Masukin pilihan (1/2/3/4): {Style.RESET_ALL}").strip()
	if H=='1':
		B=input(f"{Fore.BLUE}Masukin nama file script Python yang mau dienkripsi: {Style.RESET_ALL}").strip()
		if not os.path.isfile(B):print(f"{Fore.RED}File gak ketemu, bro!{Style.RESET_ALL}");sys.exit(1)
		D=getpass.getpass(K)
		try:
			with open(B,I)as A:F=A.read()
			G=encrypt_script_with_layers(F,D,layers=3);C=input(f"{Fore.BLUE}Masukin nama file output buat hasil encrypt: {Style.RESET_ALL}").strip()
			with open(C,L)as A:A.write(G);A.flush()
			print(f"{Fore.MAGENTA}Enkripsi selesai, bro! File terenkripsi udah disimpen di: {C}{Style.RESET_ALL}")
		except Exception as E:print(f"{Fore.RED}Error saat enkripsi: {str(E)}{Style.RESET_ALL}")
	elif H=='2':
		B=input(f"{Fore.BLUE}Masukin nama file terenkripsi: {Style.RESET_ALL}").strip()
		if not os.path.isfile(B):print(f"{Fore.RED}File gak ketemu, bro!{Style.RESET_ALL}");sys.exit(1)
		D=getpass.getpass('Masukin password dekripsi: ')
		try:
			with open(B,I)as A:M=A.read()
			N=decrypt_script_with_layers(M,D);print(f"{Fore.GREEN}Dekripsi berhasil! Nih, script aslinya:{Style.RESET_ALL}");print('-'*50);print(N);print('-'*50)
		except Exception as E:print(f"{Fore.RED}Gagal mendekripsi script. Periksa password atau file terenkripsi, bro. ({str(E)}){Style.RESET_ALL}");sys.exit(1)
	elif H=='3':
		B=input(f"{Fore.BLUE}Masukin nama file script Python yang mau dienkripsi: {Style.RESET_ALL}").strip()
		if not os.path.isfile(B):print(f"{Fore.RED}File gak ketemu, bro!{Style.RESET_ALL}");sys.exit(1)
		D=getpass.getpass(K)
		try:
			with open(B,I)as A:F=A.read()
			G=encrypt_script_with_layers(F,D,layers=3);C=input(f"{Fore.BLUE}Masukin nama file output buat hasil encrypt dengan stub: {Style.RESET_ALL}").strip();J=generate_self_decrypt_stub(G,D)
			with open(C,L)as A:A.write(J);A.flush()
			os.chmod(C,493);print(f"{Fore.MAGENTA}Enkripsi dengan stub selesai! File executable udah disimpen di: {C}{Style.RESET_ALL}")
		except Exception as E:print(f"{Fore.RED}Error saat membuat stub executable: {str(E)}{Style.RESET_ALL}")
	elif H=='4':
		B=input(f"{Fore.BLUE}Masukin nama file script Bash/Shell yang mau dienkripsi: {Style.RESET_ALL}").strip()
		if not os.path.isfile(B):print(f"{Fore.RED}File gak ketemu, bro!{Style.RESET_ALL}");sys.exit(1)
		D=getpass.getpass(K)
		try:
			with open(B,I)as A:F=A.read()
			G=encrypt_script_with_layers(F,D,layers=3);C=input(f"{Fore.BLUE}Masukin nama file output buat hasil encrypt dengan stub Bash: {Style.RESET_ALL}").strip();J=generate_self_decrypt_stub_bash(G,D)
			with open(C,L)as A:A.write(J);A.flush()
			os.chmod(C,493);print(f"{Fore.MAGENTA}Enkripsi dengan stub Bash selesai! File executable udah disimpen di: {C}{Style.RESET_ALL}")
		except Exception as E:print(f"{Fore.RED}Error saat membuat stub Bash: {str(E)}{Style.RESET_ALL}")
	else:print(f"{Fore.RED}Pilihan gak valid, bro. Bye.{Style.RESET_ALL}");sys.exit(1)
if __name__=='__main__':main()
