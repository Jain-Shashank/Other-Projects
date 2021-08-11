import pyautogui,subprocess,os
from time import sleep
def Search():
    ask_browser=pyautogui.confirm('Browser',buttons=['chrome','msedge'])
    def YouTubeVideo():
        from youtube_search import YoutubeSearch
        name_search=pyautogui.prompt('enter search and we will play first video of it..')
        results = YoutubeSearch(name_search, max_results=10).to_json()
        results = YoutubeSearch(name_search, max_results=10).to_dict()
        first_result=results[0]
        link=first_result['url_suffix']
        return f'https://www.youtube.com{link}'
    def Search_Query():
        search_query=pyautogui.prompt('Enter Your query')
        search_query=search_query.replace(' ','+')
        search_query='https://www.google.com/search?q='+search_query
        return search_query
    def Send_Null():
    	return ' '
    ask_method=pyautogui.confirm('What you want',buttons=['Send_Null','YouTubeVideo','Search_Query'])
    ask_method=eval(ask_method+"()")
    subprocess.call(f'start {ask_browser} {ask_method}',shell=True)

def Shutdown():
    subprocess.call('shutdown /h /f',shell=True)
    exit()

def start():
    program_name={1:["bluetooth","ms-settings:bluetooth"],2:["Chrome","chrome.exe"],3:["cmd","cmd.exe"],4:["Admin CMD",f'powershell "start cmd \\"/k cd /d {os.getcwd()}" -v runAs"'],5:['This Pc','explorer file:']}
    for x,y in program_name.items():
        print(f'{x}.{y[0]}')
    input_name=input("Enter number of program or new program name:")
    if input_name.isdigit():
        give_str=program_name[int(input_name)][1]
    else:
        give_str=input_name
    subprocess.call(f'start {give_str}',shell=True)

def close_cmd():
	ask=input('press Y to close or N for cancel:')
	if ask=='Y' or ask=='y':
		pyautogui.hotkey('alt','f4')
	else:
		pass
		
def clean(seconds_clear=0):
    for x in range(seconds_clear):
        print(f'Clear screen in {seconds_clear-x}',end=' \r')
        sleep(1)
    subprocess.call('cls',shell=True)

def run():    
    print('press enter to exit from function')
    str_create='1.Search\n2.Shutdown\n3.start\n4.close_cmd\n5.clean'
    print(str_create)
    dic_fun={1:"Search",2:"Shutdown",3:"start",4:"close_cmd",5:"clean"}
    ask=int(input("Please enter number of function you want to call:"))
    eval(dic_fun[ask]+'()')

run()