#!/bin/bash
# Enhanced Telegram Bot Spammer Tool - Gen Z Edition!

# Cek apakah terminal mendukung warna
if test -t 1; then
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    CYAN='\033[0;36m'
    NC='\033[0m'
else
    RED=''
    GREEN=''
    YELLOW=''
    BLUE=''
    CYAN=''
    NC=''
fi

# Function: Banner tampilan
function banner() {
    clear
    echo -e "${CYAN}"
    cat << 'EOF'
 ___  ____   __    __  __    ____  ____  __    ____
/ __)(  _ \ /__\  (  \/  )  (_  _)( ___)(  )  ( ___)
\__ \ )___//(__)\  )    (     )(   )__)  )(__  )__)
(___/(__) (__)(__)(_/\/\_)   (__) (____)(____)(____)
EOF
    echo -e "${NC}"
    echo -e "${BLUE}   Telegram Bot Spammer Tool By ~ RenXploit${NC}"
    echo -e "${BLUE}            Spam terus brooo 🗿👍 ${NC}"
    echo -e "${CYAN}============================================${NC}"
}

# Function: Validasi input bilangan bulat positif
function validate_integer() {
    local input="$1"
    if [[ "$input" =~ ^[1-9][0-9]*$ ]]; then
        echo 1
    else
        echo 0
    fi
}

# Fungsi prompt untuk input token
function prompt_token() {
    while true; do
        read -p "Token Bot: " token
        if [[ -z "$token" ]]; then
            echo -e "${RED}Token tidak boleh kosong! Coba lagi.${NC}"
        else
            break
        fi
    done
}

# Fungsi prompt untuk input chat id
function prompt_chat_id() {
    while true; do
        read -p "Chat ID: " chat_id
        if [[ -z "$chat_id" ]]; then
            echo -e "${RED}Chat ID tidak boleh kosong! Coba lagi.${NC}"
        elif ! [[ "$chat_id" =~ ^-?[0-9]+$ ]]; then
            echo -e "${RED}Chat ID harus berupa angka! Coba lagi.${NC}"
        else
            break
        fi
    done
}

# Fungsi prompt untuk input threads
function prompt_threads() {
    while true; do
        read -p "Jumlah Threads (misal 1/detik): " threads
        valid=$(validate_integer "$threads")
        if [[ "$valid" -eq 1 ]]; then
            break
        else
            echo -e "${RED}Jumlah Threads harus berupa bilangan bulat positif! Coba lagi.${NC}"
        fi
    done
}

# Fungsi prompt untuk input pesan dan jumlah pesan
function prompt_pesan_jumlah() {
    while true; do
        read -p "Pesan: " message
        if [[ -z "$message" ]]; then
            echo -e "${RED}Pesan tidak boleh kosong! Coba lagi.${NC}"
        else
            break
        fi
    done

    while true; do
        read -p "Jumlah Pesan (angka): " jumlah
        valid=$(validate_integer "$jumlah")
        if [[ "$valid" -eq 1 ]]; then
            break
        else
            echo -e "${RED}Jumlah Pesan harus berupa bilangan bulat positif! Coba lagi.${NC}"
        fi
    done
}

# Fungsi untuk mengirim pesan via Telegram API
function send_message() {
    local token="$1"
    local chat_id="$2"
    local message="$3"
    curl -s -X POST "https://api.telegram.org/bot${token}/sendMessage" \
         -d "chat_id=${chat_id}" \
         -d "text=${message}" > /dev/null
}

# Fungsi untuk mengirim pesan secara concurrent
function send_messages_concurrent() {
    local token="$1"
    local chat_id="$2"
    local message="$3"
    local jumlah="$4"
    local threads="$5"
    local count=0

    echo -e "\n${YELLOW}Mengirim ${jumlah} pesan dengan ${threads} thread...${NC}"
    for (( i=1; i<=jumlah; i++ )); do
        send_message "$token" "$chat_id" "$message" &
        echo -e "${GREEN}[${i}/${jumlah}] Pesan terkirim!${NC}"
        ((count++))
        if (( count % threads == 0 )); then
            wait
        fi
    done
    wait
    echo -e "\n${CYAN}Selesai mengirim ${jumlah} pesan.${NC}"
}

# Global variables untuk menyimpan data token, chat_id, dan threads
global_token=""
global_chat_id=""
global_threads=""

# Main loop
while true; do
    banner

    # Jika global data belum ada, minta input data lengkap
    if [[ -z "$global_token" || -z "$global_chat_id" || -z "$global_threads" ]]; then
        echo -e "${BLUE}Input data lengkap terlebih dahulu:${NC}"
        prompt_token
        global_token="$token"
        prompt_chat_id
        global_chat_id="$chat_id"
        prompt_threads
        global_threads="$threads"
    fi

    prompt_pesan_jumlah

    # Kirim pesan secara concurrent
    send_messages_concurrent "$global_token" "$global_chat_id" "$message" "$jumlah" "$global_threads"

    # Menu opsi selanjutnya
    echo -e "\n${CYAN}Pilih opsi selanjutnya:${NC}"
    echo -e "${CYAN}[u] Input ulang data lengkap (token, chat id, threads)${NC}"
    echo -e "${CYAN}[y] Kirim ulang pesan dengan data sebelumnya (gunakan token, chat id, threads yang sama)${NC}"
    echo -e "${CYAN}[n] Keluar dari script${NC}"

    while true; do
        read -p "Opsi (u/y/n): " opsi
        if [[ "$opsi" == "n" ]]; then
            echo -e "${RED}Script dihentikan. Sampai jumpa!${NC}"
            exit 0
        elif [[ "$opsi" == "u" ]]; then
            # Reset data global agar bisa input ulang
            global_token=""
            global_chat_id=""
            global_threads=""
            break
        elif [[ "$opsi" == "y" ]]; then
            # Gunakan data yang sama, cukup input pesan dan jumlah pesan saja
            break
        else
            echo -e "${RED}Opsi tidak valid! Masukkan u, y, atau n.${NC}"
        fi
    done
done





