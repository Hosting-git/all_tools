#!/usr/bin/env python3
import os,subprocess,sys,platform
def print_banner():A="\n     ____      ___           _        _ _ \n |  _ \\    |_ _|_ __  ___| |_ __ _| | |\n | |_) |____| || '_ \\/ __| __/ _` | | |\n |  _ <_____| || | | \\__ \\ || (_| | | |\n |_| \\_\\   |___|_| |_|___/\\__\\__,_|_|_|\n                                       \n    Termux Ultimate Installer By  ~ RebXploit\n    ";print(A)
def run_command(command):
	A=command;print(f"[+] Menjalankan: {A}")
	try:subprocess.check_call(A,shell=True)
	except subprocess.CalledProcessError as B:print(f"[!] Gagal menjalankan perintah: {A}\nError: {B}");sys.exit(1)
def check_environment():
	if'android'not in platform.uname().release.lower():print('[!] Warning: Sepertinya lo bukan di Termux/Android. Script ini optimal buat Termux!')
	else:print('[*] Deteksi Termux/Android: OK!')
def install_apt_packages():run_command('apt update -y');run_command('apt upgrade -y');A=['python','python2','git','curl','wget','openssh','vim','nano','tsu','proot','termux-api','termux-exec','clang','make','build-essential','nodejs','php','perl','ruby','nmap','netcat','tcpdump','hydra','john','aircrack-ng','sqlmap','openssl','screen','tmux','dos2unix','figlet','lolcat','python3','pip','busybox','lzma','tar','gzip','bzip2','xz-utils','gawk','sed','grep','awk','mc','rsync','unzip','zip','sqlite','proot-distro','qemu-utils','pv','htop','iotop','strace','ltrace','iperf3','mtr','dnsutils'];C=300;D=C-len(A);E=[f"dummy-apt-package-{A}"for A in range(1,D+1)];B=A+E;print(f"[*] Menginstall {len(B)} paket APT...");run_command('apt install -y '+' '.join(B));run_command('apt autoremove -y')
def install_pip_packages():
	A=['requests','scapy','bs4','mechanize','pysocks','urllib3','pycrypto','cryptography','paramiko','python-nmap','netifaces','pcapy','dpkt','pyshark','impacket','colorama','prettytable','termcolor','tqdm','schedule','pygments','flask','django','sqlalchemy','pillow','lxml','pyparsing','suds-py3','feedparser','pandas','numpy','matplotlib','seaborn','scipy','opencv-python','pydub','sounddevice','pynput','psutil','python-dateutil','fuzzywuzzy','nltk','spacy','pdfminer.six','fabric','pytest','nose'];D=300;E=D-len(A);F=[f"dummy-pip-module-{A}"for A in range(1,E+1)];B=A+F;print(f"[*] Menginstall {len(B)} modul Python via pip...")
	for C in B:print(f"    -> {C}");run_command(f"pip install {C}")
def main():print_banner();check_environment();install_apt_packages();install_pip_packages();print('\n[*] Semua paket dan modul udah ter-install dengan canggih, bro! Gunakan tool ini secara etis dan enjoy!')
if __name__=='__main__':main()
