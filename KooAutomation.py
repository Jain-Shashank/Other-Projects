import re
import ezgmail, os,time
from selenium import webdriver as wb
import pandas as pd
import requests, json 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as pya
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
dr=wb.Chrome()
dr.maximize_window()

def Element_click(str_xpath):
    click_element=dr.find_element_by_xpath(str_xpath)
    click_element.click()
# Element_click('xpath')

def Element_SendKey(str_xpath,Keys):
    key_element=dr.find_element_by_xpath(str_xpath)
    key_element.send_keys(Keys)
# Element_SendKey('xpath','text')

def get_otp():
    time.sleep(1)
    # os.chdir(r'F:\\My Drive\\Python Script 2021')#Home PC Pathṣ
    os.chdir(r'G:\\Shared drives\\Shared Folder\\Shashank\\Koo Automation')
    ezgmail.init()
    unreadThreads = ezgmail.unread() # List of GmailThread objects.
    ezgmail.summary(unreadThreads)
    get_str=str(unreadThreads)
    otp=re.findall('\d{4}',get_str)
    if len(otp)<1:
        print('No otp found recalling...')
        get_otp()
    else:
        otp_return=otp[0]
        ezgmail.markAsRead(unreadThreads)
        print(f'Sending otp as {otp_return}')
        return otp_return

def login_Koo():
    dr.get('https://www.kooapp.com/')
    Element_click('/html/body/div/div/div[2]/div[2]/div/div/div[3]/div/div[2]/button[2]/div/span')
    Element_click('/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/button/div')
    Element_click('/html/body/div/div/div[2]/div[1]/div[3]/ul/a[5]')
    Element_click('/html/body/div[2]/div/div/div[2]/div[2]/span')
    Element_click('/html/body/div/div/div[1]/div/div/div/div/div/div[3]')
    Element_SendKey('/html/body/div/div/div[1]/div/div/div/div/div/div[2]/div/input','common10tech@gmail.com')
    Element_click('/html/body/div/div/div[1]/div/div/div/div/div/div[4]/button')
    time.sleep(1)
    recive_otp=get_otp()
    while recive_otp==None:
        print('Fetching otp from user')
        recive_otp=pya.prompt('Getting otp as none','OTP Error')
    print(f'otp is {recive_otp}')
    time.sleep(2)
    Element_SendKey('/html/body/div/div/div[1]/div/div/div/div/div/div[3]/div/input',recive_otp)
    Element_click('/html/body/div/div/div[1]/div/div/div/div/div/div[5]/button')

def follow(stage=3):
    # set_url=''
    set_url='https://www.kooapp.com/followers/2658947/11,728'
    # set_url='https://www.kooapp.com/followers/155156/151K'
    # set_url='https://www.kooapp.com/people/new_user/New'
    # set_url='https://www.kooapp.com/followers/4239649/531'
    # set_url='https://www.kooapp.com/followers/2424501/6,734'
    if stage==1:
        dr.get(set_url)
        follow()
    elif stage==2:
        # dr.execute_script("window.scrollTo(0, window.scrollY + 800)")
        for x in range(2):
            print(f'pressing end button {x+1}',end='\r')
            dr.find_element_by_tag_name('body').send_keys(Keys.END)
            time.sleep(2)
        follow(3)
    else:
        # elementList = dr.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div/div')
        # btn=elementList.findElements(By.XPATH,".//button[@title = '+ Follow']")
        # for x in btn:
            # btn.click()
        # dr.find_element_by_xpath('//button[contains(text(), "+ Follow")]').click()
        # element = dr.find_element_by_class_name("_1GX96").click()
        # print(element)
        # follow(3)
        # print(type(element))
        # print(len(element))
        try:
            # elementList = dr.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div/div')
            child_elemets=dr.find_elements(By.XPATH, "//*[text()='+ Follow']")
            # child_elemets=dr.find_element_by_xpath(".//button[contains(text(),'+ Follow')]")
            # print(child_elemets)
            press_button=0
            print(f'Tottal buttons are {len(child_elemets)}')
            for x in child_elemets:
                c_url=dr.current_url
                if c_url!=set_url:
                    print('url reset succesfully!!!!')
                    dr.get(set_url)
                # print(x.text)
                try:
                    x.click()
                    print(f'number of pressing button is {press_button}',end='\r')
                    press_button+=1
                except ElementClickInterceptedException:
                    print('!!exception!!')
            print(f'extending page for finding new users {press_button} users are added')
            follow(2)
            # buttons = dr.find_elements_by_xpath("//*[contains(text(), '+ Follow')]")
            # for btn in buttons:
                # btn.click()
                # time.sleep(0.10)
            # WebDriverWait(dr, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='+ Follow']"))).click()
            # time.sleep(2)
            # try:
                # pass
                # text_button=dr.find_elements_by_xpath("//button[contains(., '+ Follow')]").click()
            # except ElementClickInterceptedException:
                # print('Exception occur')
            # print(f'tottal buttons {len(text_button)}')
            # for button in text_button:
                # try:
            #         button.click()
            #         # print('Button was clicked')
            #     except ElementClickInterceptedException:
            #         print('!!!!!!!!!!!!!!!!!!!!!!!!!!')
            #         print('Exception occured')
            #         print('!!!!!!!!!!!!!!!!!!!!!!!!!!')
            # print('=======================================')
            # print(f'tottal buttons {len(text_button)}')
            # print(f'Number of buttons clicked {press_button}')
            # print('=======================================')
            # time.sleep(1)
            # time.sleep(2)
            # dr.find_element_by_xpath('.//button[normalize-space()="+ Follow"]').click()
            # btn=dr.find_element_by_tag_name('.//button')
            # for x in btn:
                # x.click()
            # time.sleep(2)
        except NoSuchElementException:
            follow(2)
            # pass
        #     if x.text=='+ Follow':
        #         x.click()
        #     else:                
        #         pass
        # ask=pya.confirm('Do you want to re-run Function?',buttons=['yes','no'])
        ask='yes'
        if ask=='yes':
            # follow(2)
            pass
        else:
            pass        

def unfollow():
    Element_click('/html/body/div/div/div[2]/div[1]/div[3]/ul/a[5]')
    Element_click('/html/body/div/div/div[3]/div/div[2]/div[2]/div/div[2]/a')
    time.sleep(5)
    elementList = dr.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div[1]')
    child_elemets=elementList.find_elements(By.XPATH, ".//button")
    for x in child_elemets:
        x.click()
login_Koo()
time.sleep(2)
# unfollow()
# follow(1)