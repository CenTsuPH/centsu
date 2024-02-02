def clear():
	os.system('clear')
def back():
	login()
	
	import getpass

attemps = 0

while attemps < 12345677901:
    username = input(' \033[0;92mEnter Username: ')
    password = input(' \033[0;93mEnter Password: ')

    if username == 'cent' and password == '15':
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
