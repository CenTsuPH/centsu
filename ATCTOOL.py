import os,sys,re,time,json
import requests,bs4,string
import faker,fake_email,random
from faker import Faker
from fake_email import Email
from bs4 import BeautifulSoup
import secrets  # added
#_________|LOOP|_________#
oks = [];cps = [];loop = 0
#_________|COLOR|_________#
G = '\x1b[1;32m';W = '\x1b[1;97m';R = '\x1b[38;5;160m';B = '\x1b[1;90m';Y = '\x1b[1;33m';T = '\x1b[1;34m';E = '\x1b[38;5;205m';O = '\x1b[38;5;81m'
#_________|STYLE|_________#
xd = f''' {W}[{G}={W}]{W}''';xd1 = f''' {W}[{G}1{W}]{W}''';xd2 = f''' {W}[{G}2{W}]{W}''';xd0 = f''' {W}[{G}0{W}]{W}''';xdx = f''' {W}[{G}?{W}]{W}'''
#_________|CLEAR|_________#
def clear():os.system('clear');print(logo)
#_________|LINE|_________#
def linex():print(f'''{W}{'‚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'}''')
try:
    msgUPdate = requests.get('https://raw.githubusercontent.com/CenTsuPH/update/main/RNDM.txt', timeout=10).text.splitlines()
except Exception:
    msgUPdate = []
#_________|UA|_________#

def ____useragent____():
    version = random.choice(['14','15','10','13','7.0.0','7.1.1','9','12','11','9.0','8.0.0','7.1.2','7.0','4','5','4.4.2','5.1.1','6.0.1','9.0.1'])
    model = random.choice(['1105','1107','15','3T','62A','6779','6833','7273','9A','A1','A1 5G','A1 Pro','A11','A11k','A11x','A12','A15','A15s','A16','A16e','A16k','A16s','A17','A17k','A18','A1i 5G','A1k','A1s','A1x','A2 5G','A25','A2x 5G','A3','A3 5G','A3 Pro 5G','A30','A31','A31c','A32','A33','A33m','A33t','A34','A35','A36','A37','A37t','A38','A39','A3s','A3x 5G','A4','A40','A400','A41','A42','A43','A44','A45','A46','A47','A48','A49','A5','A5 (2020)','A50','A51','A52','A53','A53 5G','A53m','A53s','A53s 5G','A54','A54 5G','A54s','A55','A55 5G','A55s 5G','A56','A56 5G','A57','A57 (2016)','A57 (2022)','A58','A58 5G','A59','A59 5G','A59m','A59s','A59t','A5S','A60','A7','A71','A71 (2018)','A71A','A72','A72n 5G','A73','A73 5G','A73t','A74','A74 5G','A76','A77','A77 5G','A77s','A77t','A78','A78 5G','A79','A79 5G','A79k','A79t','A7n','A7x','A8','A83','A83 (2018)','A83PRO','A83t','A85T','A9','A9 (2020)','A91','A92','A92s','A93','A93s','A94','A95','A96','A96 5G','A97','A98','A98 5G','A9x','AX5','AX5s','AX7','C1','CNM632','CNM652','CPH1114','CPH1235','CPH1427','CPH1451','CPH1615','CPH1664','CPH1869','CPH1927','CPH1929','CPH1985','CPH2048','CPH2068','CPH2107','CPH2238','CPH2261','CPH2331','CPH2332','CPH2351','CPH2381','CPH2389','CPH2399','CPH2401','CPH2409','CPH2411','CPH2413','CPH2415','CPH2417','CPH2419','CPH2423','CPH2447','CPH2449','CPH2451','CPH2459','CPH2465','CPH2467','CPH2469','CPH2487','CPH2491','CPH2493','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2535','CPH2551','CPH2553','CPH2557','CPH2569','CPH2573','CPH2579','CPH2581','CPH2583','CPH2585','CPH2589','CPH2591','CPH2599','CPH2603','CPH2605','CPH2607','CPH2609','CPH2611','CPH2613','CPH2617','CPH2619','CPH2621','CPH2625','CPH2629','CPH2631','CPH2637','CPH2639','CPH2641','CPH2643','CPH2661','CPH2663','CPH2665','CPH2667','CPH2669','CPH2681','CPH2683','CPH2687','CPH2843','CPH2931','CPH3475','CPH3669','CPH3682','CPH3731','CPH3776','CPH3785','CPH4125','CPH4275','CPH4299','CPH4395','CPH4473','CPH4987','CPH5286','CPH5841','CPH5947','CPH6178','CPH6244','CPH6271','CPH6316','CPH6519','CPH6528','CPH6697','CPH7338','CPH7364','CPH7382','CPH7532','CPH7577','CPH7948','CPH7991','CPH8153','CPH8346','CPH8347','CPH8363','CPH8393','CPH8467','CPH8472','CPH8534','CPH8686','CPH8893','CPH9177','CPH9226','CPH9659','CPH9667','CPH9716','CPH9763','CPH9839','CPH9929','CPH9977','f','F1','F1 Plus','F10','F11','F11 Pro','F11Pro','F15','F17','F17 Pro','F19','F19 Pro','F19 Pro Plus','F19s','F1s','F21 Pro','F21s Pro','F23 5G','F25 Pro 5G','F27 Pro+ 5G','F3','F3 Plus','F5','F5 Youth','F51','F61','F7','F9','F9 Pro','Find','Find 5','Find 5 Mini','Find 7','Find 7a','Find Clover','Find Melody','Find Muse','Find N','Find N 5G','Find N2','lFind N2 Flip','Find N3','Find N3 Flip','Find Way S','Find X','Find X Lamborghini','Find X2','Find X2 Lite','Find X2 Pro','Find X3','Find X3 Lite','Find X3 Neo','Find X3 Pro','Find X5','Find X5 Pro','Find X6','Find X6 Pro','Find X7','Find X7 Ultra','Find X7 Ultra SE','JLAJH6','Joy Plus','K1','K10','K10 5G','K10 Pro 5G','K10x','K11 5G','K11x 5G','K12 5G','K3','K5','K7','K7x','K9 5G','K9 Pro 5G','K9s','K9x','N1 Mini','N1T','N3','Neo','Neo 3','Neo 5','Neo 7','Neo 7s','Pad 2','Pad Air','Pad Air 2','Pad Neo','Pad WiFi','R10','R1001','R11','R11 Plus','R11plus','R11s','R11s Plus','R15','R15 Dream Mirror','R15 Neo','R15 Pro','R15x','R17','R17 Neo','R17 Pro','R1K','R1L','R1S','R1x','R2001','R2010','R2017','R3006','R5','R53','R6007','R7','R7 Lite','R7 Plus','R7 Plus F','R7005','R7007','R7s','R7s Plus','R7sm','R7st','R7t','R801','R805','R807','R811','R819','R819T','R8205','R8207','R823T','R829','R829T','R830','R830S','R833T','R9','R9 Plus','R9km','R9s','R9s Plus','R9t','R9tm','Real','Reno','Reno 10','Reno 10 5G','Reno 10 Pro 5G','Reno 10 Pro+ 5G','Reno 10X','Reno 10X Zoom','Reno 11','Reno 11 Pro','Reno 12','Reno 12 5G','Reno 12 F 4G','Reno 12 F 5G','Reno 12 Pro 5G','Reno 2','Reno 2F','Reno 2Z','Reno 3','Reno 3 5G','Reno 3 Lite','Reno 3 Pro','Reno 3A','Reno 4 4G','Reno 4 5G','Reno 4 Lite','Reno 4 Pro 4G','Reno 4 Pro 5G','Reno 4 SE 5G','Reno 4F','Reno 4Z 5G','Reno 5','Reno 5 5G','Reno 5 Lite','Reno 5 Pro 5G','Reno 5 Pro Plus 5G','Reno 5A','Reno 5F','Reno 5G','Reno 5K','Reno 5K 5G','Reno 5Z','Reno 6','Reno 6 Pro','Reno 6 Pro 5G','Reno 6 Pro Plus','Reno 6 Z 5G','Reno 7','Reno 7 Pro','Reno 7 SE','Reno 7A','Reno 7Z','Reno 8','Reno 8 Pro','Reno 8 Pro+','Reno 8 Z','Reno 8T','Reno 9','Reno 9 A','Reno 9 Pro','Reno 9 Pro+','Reno A','Reno Ace','Reno Ace 2','Reno K3','Reno Z','Reno10','Reno11','Reno2','RENO3','Reno4','Reno5','Reno8','Reno9','RX17 Neo','S1','S17','S3','S4','T29','Ulike 2','V5','V8821','Watch 2 46mm','Watch 41mm','Watch 46mm','X','x20','x22','X50Pro','X54','X9017','X907','Y15','Y21','Y3','Z1'])
    build = random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''
#_________|EXTRACTOR|_________#
def extractor(data):
    try:
        soup = BeautifulSoup(data,"html.parser")
        data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {"error":str(e)}
#_________|FAKE EMAIL|_________#
def GetEmail():
    try:
        response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new', timeout=15).json()
        return response.get('email')
    except Exception:
        return None
#_________|FAKE EMAIL CODE|_________#
def GetCode(email):
    try:
        response = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages', timeout=15).text
        m = re.search(r'FB-(\d+)', response)
        if m: return m.group(1)
        return None
    except Exception:
        return None
        
def gen_password(length: int = 12) -> str:
    import string as _s
    symbols = "!@#$%^&*()-_=+"
    alphabet = _s.ascii_lowercase + _s.ascii_uppercase + _s.digits + symbols
    mandatory = [
        secrets.choice(_s.ascii_lowercase),
        secrets.choice(_s.ascii_uppercase),
        secrets.choice(_s.digits),
        secrets.choice(symbols),
    ]
    remaining = [secrets.choice(alphabet) for _ in range(max(0, length - len(mandatory)))]
    pwd = mandatory + remaining
    secrets.SystemRandom().shuffle(pwd)
    return "".join(pwd)

#_________|LOGO|_________#
logo = """            
\033[97;1m           █████╗ ███████╗███╗  ██╗████████╗
\033[97;1m          ██╔══██╗██╔════╝████╗░██║╚══██╔══╝
\033[97;1m          ██║░░╚═╝█████╗░░██╔██╗██║░░░██║░░░
\033[97;1m          ██║░░██╗██╔══╝░░██║╚████║░░░██║░░░
\033[97;1m          ╚█████╔╝███████╗██║░╚███║░░░██║░░░                                                                         
     ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
     ║      \033[97;1m[ F U C K Y O U B Y P A S S E R ]     \033[97;1m ║
     ╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[97;1m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
for line in msgUPdate:
    logo += f"{line}\n"

logo += """\033[97;1m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[§] AUTHOR       :      cent
[§] TOOLS        :      AUTOCREATE 
[§] TYPE         :      PAID
[§] FACEBOOK     :      cent
[§] VERSION.     :      PRIVATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[97;1m"""

#================= RANDOM NAME LISTS =================#
MALE_NAMES = [
    "James","John","Robert","Michael","William","David","Richard","Joseph","Thomas","Charles",
    "Christopher","Daniel","Matthew","Anthony","Mark","Donald","Steven","Paul","Andrew","Joshua",
    "Kenneth","Kevin","Brian","George","Edward","Ronald","Timothy","Jason","Jeffrey","Ryan",
    "Jacob","Gary","Nicholas","Eric","Stephen","Jonathan","Larry","Justin","Scott","Brandon",
    "Benjamin","Samuel","Gregory","Alexander","Frank","Patrick","Raymond","Jack","Dennis","Jerry",
    "Tyler","Aaron","Jose","Henry","Adam","Douglas","Nathan","Peter","Zachary","Kyle",
    "Walter","Harold","Jeremy","Ethan","Carl","Keith","Roger","Gerald","Christian","Terry",
    "Bryan","Shawn","Bruce","Jordan","Austin","Joe","Jesse","Albert","Billy","Willie",
    "Logan","Arthur","Ralph","Roy","Vincent","Wayne","Alan","Russell","Louis","Philip"
]

FEMALE_NAMES = [
    "Mary","Patricia","Jennifer","Linda","Elizabeth","Barbara","Susan","Jessica","Sarah","Karen",
    "Nancy","Lisa","Margaret","Betty","Sandra","Ashley","Dorothy","Kimberly","Emily","Donna",
    "Michelle","Carol","Amanda","Melissa","Deborah","Stephanie","Rebecca","Sharon","Laura","Cynthia",
    "Kathleen","Amy","Shirley","Angela","Helen","Anna","Brenda","Pamela","Nicole","Emma",
    "Samantha","Katherine","Christine","Debra","Rachel","Catherine","Carolyn","Janet","Ruth","Maria",
    "Heather","Diane","Virginia","Julie","Joyce","Victoria","Olivia","Kelly","Christina","Lauren",
    "Joan","Evelyn","Judith","Megan","Cheryl","Andrea","Hannah","Martha","Jacqueline","Frances",
    "Sophia","Isabella","Madison","Abigail","Chloe","Ella","Avery","Grace","Natalie","Lily",
    "Hailey","Brooklyn","Zoe","Stella","Mila","Aurora","Savannah","Leah","Lucy","Aria"
]

LAST_NAMES = [
    "Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez",
    "Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin",
    "Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson",
    "Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores",
    "Green","Adams","Nelson","Baker","Hall","Rivera","Campbell","Mitchell","Carter","Roberts",
    "Gomez","Phillips","Evans","Turner","Diaz","Parker","Cruz","Edwards","Collins","Reyes",
    "Stewart","Morris","Morales","Murphy","Cook","Rogers","Gutierrez","Ortiz","Morgan","Cooper",
    "Peterson","Bailey","Reed","Kelly","Howard","Ramos","Kim","Cox","Ward","Richardson",
    "Price","Barnes","Sanders","Ross","Henderson","Coleman","Powell","Long","Patterson","Hughes",
    "Flores","Washington","Butler","Simmons","Foster","Gonzales","Bryant","Alexander","Russell","Griffin"
]

#_________|MENU|_________#
def CNT():
    clear();print(f'''{xd1} START AUTO CREATE ''');print(f'''{xd0} EXIT CLONE ''');linex();mr = input(f'''{xdx} SELECT : ''')
    if mr in ('1',):____create____()
    elif mr in ('0',):exit()
    else:linex();print(f'''{xd} OPTION NOT FOUND ''');linex();time.sleep(1);print(f'''{xd} TRY AGAIN ''');time.sleep(1);CNT()

#_________|MODULE|_________#
def progres(current, num_accounts, delay):
    # Standout progress with animated bar and percentage
    try:
        cols = os.get_terminal_size().columns
    except Exception:
        cols = 80

    # Header showing overall status
    header = (
        f"{W}[{G}CNT | CREATE{W}] "
        f"[{G}{current}{W}/{G}{num_accounts}{W}] "
        f"[{G}OK:{len(oks)}{W}] "
        f"[{R}CP:{len(cps)}{W}]"
    )

    # Strip ANSI when estimating width for bar size
    ansi_re = re.compile(r'\x1b\[[0-9;]*m')
    plain_header_len = len(ansi_re.sub('', header))
    bar_max_width = max(10, min(50, cols - plain_header_len - 12))

    total_ticks = max(1, int(delay))
    for tick in range(total_ticks):
        pct = int(((tick + 1) / total_ticks) * 100)
        filled = int((pct / 100) * bar_max_width)
        bar = f"{G}{'█' * filled}{W}{'░' * (bar_max_width - filled)}"
        line = f"\r{E}»{W} {header} {E}|{W} {bar} {G}{pct:3d}%{W}"
        print(line, end='', flush=True)
        time.sleep(1)
        print()
        clear()


# Helper to pick random names (missing in original; adding)
def pick_random_name(gender="male"):
    first = random.choice(MALE_NAMES if gender == "male" else FEMALE_NAMES)
    last = random.choice(LAST_NAMES)
    return first, last

#_________|CREATE|_________#
def ____create____():
    global num_accounts,delay
    clear()
    print(f'''{xd1} MANUAL NAMES''')
    print(f'''{xd2} RANDOM MALE NAMES''')
    print(f''' {W}[{G}3{W}]{W} RANDOM FEMALE NAMES''')
    print(f'''{xd0} BACK''');linex()
    mode = input(f'''{xdx} SELECT NAME MODE : ''').strip()

    firstname = ""; lastname = ""
    gender_mode = None

    if mode == '1':
        clear();print(f'''{xd} EXAMPLE {R}:{W} James {R}|{W} Nicole {R}|{W} Mark {R}|{W} Samantha ''');linex()
        firstname = input(f'''{xdx} ENTER FIRST NAME : ''').strip() or random.choice(MALE_NAMES+FEMALE_NAMES)
        linex();print(f'''{xd} EXAMPLE {R}:{W} Smith {R}|{W} hanna {R}|{W} Viel {R}|{W} Kim ''');linex()
        lastname = input(f'''{xdx} ENTER LAST NAME : ''').strip() or random.choice(LAST_NAMES)
    elif mode == '2':
        gender_mode = "male"
    elif mode == '3':
        gender_mode = "female"
    elif mode == '0':
        return CNT()
    else:
        print(f'''{xd} INVALID OPTION''');time.sleep(1);return ____create____()

    linex();print(f'''{xd} EXAMPLE {R}:{W} 5000 {R}|{W} 1000 {R}|{W} 7777 {R}|{W} 9999 ''');linex()
    try:
        num_accounts = int(input(f'''{xdx} ENTER LIMIT : ''').strip())
    except Exception:
        num_accounts = 10
    linex();print(f'''{xd} EXAMPLE {R}:{W} 1 {R}|{W} 2 {R}|{W} 3 {R}|{W} 4 {R}|{W} 5 {R}|{W} 6 {R}|{W} 7 {R}|{W} 8 ''');linex()
    try:
        delay = int(input(f'''{xdx} ENTER BETWEEN TIME : ''').strip())
    except Exception:
        delay = 1

    clear();print(f'''{xd} TOTAL CREATE LIMIT {R}:{G} {num_accounts} ''');print(f'''{xd} IF NO RESULT ON{R}|{W}OFF AIRPLANE MODE''');linex()
    for make in range(int(num_accounts)):
        # choose names per account if random mode
        if gender_mode:
            firstname, lastname = pick_random_name(gender=gender_mode)
        elif not firstname or not lastname:
            # fallback manual defaults
            firstname = firstname or random.choice(MALE_NAMES+FEMALE_NAMES)
            lastname = lastname or random.choice(LAST_NAMES)

        progres(make + 1, num_accounts, delay)
        ses = requests.Session()
        try:
            response = ses.get(
                url='https://x.facebook.com/reg',
                params={"_rdc":"1","_rdr":"","wtsid":"rdr_0t3qOXoIHbMS6isLw","refsrc":"deprecated"},
                timeout=20
            )
        except Exception:
            continue

        try:
            mts = ses.get('https://x.facebook.com', timeout=20).text
            m_ts_match = re.search(r'name="m_ts" value="(.*?)"', str(mts))
            m_ts = m_ts_match.group(1) if m_ts_match else ""
        except Exception:
            m_ts = ""

        formula = extractor(response.text) if response and response.text else {}

        email2 = GetEmail()
        if not email2:
            continue
        rand_password = gen_password(12)
        payload = {
            'ccp': "2",
            'reg_instance': str(formula.get("reg_instance","")),
            'submission_request': "true",
            'helper': "",
            'reg_impression_id': str(formula.get("reg_impression_id","")),
            'ns': "1",
            'zero_header_af_client': "",
            'app_id': "103",
            'logger_id': str(formula.get("logger_id","")),
            'field_names[0]': "firstname",
            'firstname': firstname,
            'lastname': lastname,
            'field_names[1]': "birthday_wrapper",
            'birthday_day': str(random.randint(1,28)),
            'birthday_month': str(random.randint(1,12)),
            'birthday_year': str(random.randint(1992,2009)),
            'age_step_input': "",
            'did_use_age': "false",
            'field_names[2]': "reg_email__",
            'reg_email__': email2,
            'field_names[3]': "sex",
            'sex': "2",
            'preferred_pronoun': "",
            'custom_gender': "",
            'field_names[4]': "reg_passwd__",
            'name_suggest_elig': "false",
            'was_shown_name_suggestions': "false",
            'did_use_suggested_name': "false",
            'use_custom_gender': "false",
            'guid': "",
            'pre_form_step': "",
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0], rand_password),
            'submit': "Sign Up",
            'fb_dtsg': formula.get("fb_dtsg","NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0"),
            'jazoest': str(formula.get("jazoest","")),
            'lsd': str(formula.get("lsd","")),
            '__dyn': "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",
            '__csr': "",
            '__req': "p",
            '__fmt': "1",
            '__a': "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",
            '__user': "0"
        }
        header1 = {
            "Host":"m.facebook.com",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":____useragent____(),
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "dnt":"1",
            "X-Requested-With":"mark.via.gp",
            "Sec-Fetch-Site":"none",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-User":"?1",
            "Sec-Fetch-Dest":"document",
            "dpr":"1.75",
            "viewport-width":"980",
            "sec-ch-ua":"\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile":"?1",
            "sec-ch-ua-platform":"\"Android\"",
            "sec-ch-ua-platform-version":"\"\"",
            "sec-ch-ua-model":"\"\"",
            "sec-ch-ua-full-version-list":"",
            "sec-ch-prefers-color-scheme":"dark",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
        }
        reg_url = 'https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1'
        try:
            py_submit = ses.post(reg_url, data = payload, headers = header1, timeout=25)
        except Exception:
            continue

        if py_submit is not None and 'c_user' in py_submit.cookies:
            first_cok = ses.cookies.get_dict()
            uid = str(first_cok.get('c_user',''))
            header2 = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '2',
                'referer': 'https://m.facebook.com/login/save-device/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ____useragent____(),
                'viewport-width': '980',      
            }
            params = {
                'next': 'https://m.facebook.com/?deoia=1',
                'soft': 'hjk',
            }
            try:
                con_sub = ses.get('https://x.facebook.com/confirmemail.php', params=params, headers=header2, timeout=20).text
            except Exception:
                con_sub = ""

            valid = GetCode(email2)
            if valid:
                print(f'''\n{xd}-{W}[{G}ACCOUNTS-NAME{W}]{G} {firstname} {lastname} ''')
                print(f'''{xd}-{W}[{G}VERIFY-CODE{W}]{G} {valid} ''')
                confirm_id(email2,uid,valid,con_sub,ses,rand_password)
            cps.append(uid)

#_________|CONFIRM ID|_________#
def confirm_id(mail,uid,otp,data,ses,rand_password):
    try:
        url = "https://m.facebook.com/confirmation_cliff/"
        params = {
        'contact': mail,
        'type': "submit",
        'is_soft_cliff': "false",
        'medium': "email",
        'code': otp}
        jazo_match = re.search(r'"\d+"', data or "")
        lsd_match = re.search(r'"LSD",\[\],{"token":"([^"]+)"}', str(data or ""))
        payload = {
        'fb_dtsg': 'NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0',
        'jazoest': jazo_match.group().strip('"') if jazo_match else "",
        'lsd': lsd_match.group(1) if lsd_match else "",
        '__dyn': "",
        '__csr': "",
        '__req': "4",
        '__fmt': "1",
        '__a': "",
        '__user': uid}
        headers = {
        'User-Agent': ____useragent____(),
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'sec-ch-ua-full-version-list': "",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-mobile': "?1",
        'x-asbd-id': "129477",
        'x-fb-lsd': "KnpjLz-YdSXR3zBqds98cK",
        'sec-ch-prefers-color-scheme': "light",
        'sec-ch-ua-platform-version': "\"\"",
        'origin': "https://m.facebook.com",
        'x-requested-with': "mark.via.gp",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'priority': "u=1, i"}
        response = ses.post(url, params=params, data=payload, headers=headers, timeout=25)
        if response is not None and "checkpoint" in str(getattr(response,'url','')):
            cps.append(uid)
        else:
            cookie = (";").join([ "%s=%s" % (key,value) for key,value in ses.cookies.get_dict().items()])
            print(f'\r{xd}-{W}[{G}CENT-OK{W}]{G} {uid} | {otp} | {rand_password} | ')
            print(f'''\r{xd}-{cookie} ''');linex()
            try:
                with open('/sdcard/CENTSU-CRATE-OK-ID.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{uid}|{otp}|{rand_password}|{cookie}\n')
            except Exception:
                pass
            oks.append(uid)
    except Exception as e:
        pass

#_________|END|_________#
if __name__ == '__main__':
    CNT()
