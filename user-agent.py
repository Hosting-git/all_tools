#!/usr/bin/env python3
import random
import os
import time

# Cek modul 'rich' untuk tampilan yang makin kece
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Prompt, Confirm
    console = Console()
    use_rich = True
except ImportError:
    use_rich = False

def generate_random_user_agent():
    """
    Menghasilkan user-agent secara random dari berbagai browser dengan format yang valid.
    Pilihan browser:
      - win_chrome, win_firefox, win_edge, mac_safari, linux_chrome,
      - android_chrome, iphone_safari, opera
    """
    browser_type = random.choice([
        "win_chrome", "win_firefox", "win_edge", "mac_safari",
        "linux_chrome", "android_chrome", "iphone_safari", "opera"
    ])
    
    if browser_type == "win_chrome":
        nt = random.choice(["10.0", "6.1", "6.3"])
        chrome_version = f"{random.randint(70,100)}.0.{random.randint(1000,5000)}.{random.randint(10,150)}"
        ua = f"Mozilla/5.0 (Windows NT {nt}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"
    elif browser_type == "win_firefox":
        nt = random.choice(["10.0", "6.1", "6.3"])
        firefox_version = f"{random.randint(70,100)}.0"
        ua = f"Mozilla/5.0 (Windows NT {nt}; Win64; x64; rv:{firefox_version}) Gecko/20100101 Firefox/{firefox_version}"
    elif browser_type == "win_edge":
        nt = random.choice(["10.0", "6.1", "6.3"])
        chrome_version = f"{random.randint(70,100)}.0.{random.randint(1000,5000)}.{random.randint(10,150)}"
        # Edge biasanya pakai versi Chrome yang sama di stringnya, tapi ada "Edg/" di akhir.
        ua = f"Mozilla/5.0 (Windows NT {nt}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 Edg/{chrome_version}"
    elif browser_type == "mac_safari":
        x = random.randint(10,15)
        y = random.randint(0,9)
        version = f"{x}.{y}"
        ua = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{x}_{y}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15"
    elif browser_type == "linux_chrome":
        chrome_version = f"{random.randint(70,100)}.0.{random.randint(1000,5000)}.{random.randint(10,150)}"
        ua = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"
    elif browser_type == "android_chrome":
        android_version = random.choice(["9", "10", "11", "12"])
        device = random.choice(["SM-G973F", "Pixel 4", "OnePlus 8", "Mi 9"])
        chrome_version = f"{random.randint(70,100)}.0.{random.randint(1000,5000)}.{random.randint(10,150)}"
        ua = f"Mozilla/5.0 (Linux; Android {android_version}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36"
    elif browser_type == "iphone_safari":
        ios_version = f"{random.randint(12,15)}_{random.randint(0,5)}"
        version = f"{random.randint(12,15)}.{random.randint(0,5)}"
        ua = f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Mobile/15E148 Safari/604.1"
    elif browser_type == "opera":
        nt = random.choice(["10.0", "6.1", "6.3"])
        chrome_version = f"{random.randint(70,100)}.0.{random.randint(1000,5000)}.{random.randint(10,150)}"
        opera_version = f"{random.randint(50,70)}.0.{random.randint(2000,4000)}.{random.randint(50,150)}"
        ua = f"Mozilla/5.0 (Windows NT {nt}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 OPR/{opera_version}"
    else:
        ua = "Mozilla/5.0"
    return ua

def generate_user_agents(count: int):
    """
    Generate sejumlah 'count' user-agent random yang semuanya unik.
    """
    user_agents = set()
    # Loop sampai jumlah unik terpenuhi
    while len(user_agents) < count:
        ua = generate_random_user_agent()
        user_agents.add(ua)
    return list(user_agents)

def save_to_file(user_agents, filename):
    try:
        with open(filename, 'w') as f:
            for ua in user_agents:
                f.write(ua + "\n")
        if use_rich:
            console.print(Panel(f"Hasil berhasil disimpan ke [yellow]{filename}[/yellow]", style="bold green"))
        else:
            print(f"\nBerhasil! Hasil disimpan ke {filename}")
    except Exception as e:
        if use_rich:
            console.print(Panel(f"Error: {str(e)}", style="bold red"))
        else:
            print(f"\nError: {str(e)}")

def main():
    header_text = r"""
                  _                                                _   
  __ _ _ ___ __ _| |_ ___   _  _ ___ ___ _ _ ___ __ _ __ _ ___ _ _| |_ 
 / _| '_/ -_) _` |  _/ -_) | || (_-</ -_) '_|___/ _` / _` / -_) ' \  _|
 \__|_| \___\__,_|\__\___|  \_,_/__/\___|_|     \__,_\__, \___|_||_\__|
                                                     |___/             
𝖲𝖼𝗋𝗂𝗉𝗍 𝖡𝗒 ~ 𝖱𝖾𝗇𝖷𝗉𝗅𝗈𝗂𝗍 | github.com/THEOYS123 | www.tiktok.com/@sisten9999

    if use_rich:
        console.print(Panel(header_text, title="Random User-Agent Generator", style="bold cyan"))
    else:
        print(header_text)
        print("=== Random User-Agent Generator ===\n")
    
    try:
        jumlah = int(Prompt.ask("[bold magenta]Masukkan jumlah user-agent yang mau digenerate[/]"))
    except ValueError:
        if use_rich:
            console.print(Panel("Input harus berupa angka! Bye!", style="bold red"))
        else:
            print("Input harus berupa angka! Bye!")
        return

    if use_rich:
        console.print("[bold green]Sedang generate user-agent...[/bold green]")
    else:
        print("Sedang generate user-agent...")
    time.sleep(0.5)  # simulasi proses cepat

    hasil = generate_user_agents(jumlah)
    
    # Langsung prompt apakah mau simpan hasilnya (hasil berupa user-agent murni)
    if Confirm.ask("[bold yellow]Mau simpan hasilnya? (hasil berupa user-agent murni)[/]"):
        filename = Prompt.ask("[bold blue]Masukkan nama file untuk menyimpan (misal: hasil.txt)[/]")
        if os.path.exists(filename):
            if not Confirm.ask(f"File [yellow]{filename}[/yellow] sudah ada, overwrite?"):
                if use_rich:
                    console.print(Panel("Gak jadi disimpan.", style="bold red"))
                else:
                    print("Gak jadi disimpan.")
                return
        save_to_file(hasil, filename)
    else:
        if use_rich:
            console.print(Panel("Oke bro, hasil tidak disimpan.", style="bold cyan"))
        else:
            print("Oke bro, hasil tidak disimpan.")

    # Opsional: Tampilkan hasil ke layar (murni user-agent)
    if Confirm.ask("[bold yellow]Mau tampilkan hasil ke layar?[/]"):
        if use_rich:
            console.print(Panel("Hasil User-Agent", style="bold green"))
        for ua in hasil:
            print(ua)
    else:
        if use_rich:
            console.print(Panel("Sip, bro. Script selesai.", style="bold cyan"))
        else:
            print("Sip, bro. Script selesai.")

if __name__ == '__main__':
    main()
