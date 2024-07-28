import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
import re

dict_thread_list = []
drive = webdriver.Edge()
drive.get('https://www.threads.net')
time.sleep(3)
link_login = drive.find_element(By.XPATH, '/html/body/div[2]/div/div/header/div[3]/a')
drive.get(link_login.get_attribute('href'))
time.sleep(3)
form = drive.find_element(By.TAG_NAME, 'form')
divs = form.find_elements(By.TAG_NAME, 'div')
time.sleep(3)
for div in divs:
    try:
        if 'x1i10hfl xjbqb8w x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x6s0dn4 x6bh95i x1re03b8 x1hvtcl2 x3ug3ww xfh8nwu xoqspk4 x12v9rci x138vmkv x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x178xt8z xm81vs4 xso031l xy80clv x78zum5 xn6708d x5ib6vp x1cnzs8 xx6bls6 x12w9bfk x1g2r6go x11xpdln xk4oym4' == div.get_attribute('class'):
            time.sleep(5)
            div.click()
            time.sleep(5)
            break
    except Exception as ex:
        print(ex)
        exit(0)
form = drive.find_element(By.TAG_NAME, 'form')
btn_form = form.find_elements(By.TAG_NAME, 'button')
time.sleep(3)
for btn in btn_form:
    try:
        if ' _acan _acao _acas _aj1- _ap30' == btn.get_attribute('class'):
            time.sleep(3)
            btn.click()
            time.sleep(3)
            break
    except Exception as ex:
        print(ex)
        exit(0)
form = drive.find_element(By.TAG_NAME, 'form')
email = form.find_element(By.ID, 'email')
email.send_keys('ninet78361@tsderp.com')
password = form.find_element(By.ID, 'pass')
password.send_keys('lenin12345')
btn_login = form.find_element(By.ID, 'loginbutton')
btn_login.click()
time.sleep(20)
drive.get('https://www.threads.net/search?q=conflicto%20entre%20veronica%20abad%20y%20daniel%20noboa&serp_type=default')
time.sleep(3)
date_init = datetime(2024, 5, 17)
date_end_ = datetime(2024, 7, 26)
divs = drive.find_elements(By.TAG_NAME, 'div')
last_height = drive.execute_script("return document.body.scrollHeight")
i = 919
while True:
    time_post = drive.find_elements(By.TAG_NAME, 'time')
    for tmt in time_post:
        date_ = tmt.get_attribute('datetime')
        date_post = datetime.strptime(date_, "%Y-%m-%dT%H:%M:%S.%fZ")
        date_post = date_post.strftime('%Y-%m-%d')
        date_post = datetime.strptime(date_post, '%Y-%m-%d')
        if date_init <= date_post <= date_end_:
            try:
                link = tmt.find_element(By.XPATH, '..')
                if link:
                    dict_thread = {}
                    link_post = link.get_attribute('href')
                    i = i + 1
                    dict_thread["id"] = i
                    dict_thread["post_link"] = link_post
                    print(link_post)
                    dict_thread["fuente"] = "threads"
                    if i % 10 == 0:
                        decision = input('Continuar? Y/N: ')
                        if decision == 'N':
                            break
                    print(f'Publicacion N {i}')
                    try:
                        parent = tmt.find_element(By.XPATH, '../../../../../../../..')
                        info = parent.find_element(By.XPATH, 'div[2]')
                        name = info.find_element(By.XPATH, 'div/div/div/span[1]')
                        name_info = name.find_element(By.XPATH, 'div/div/a/span')
                        print(name_info.text)
                        dict_thread["user_name"] = name_info.text
                    except NoSuchElementException as ex:
                        i = i - 1
                        continue
                    try:
                        name_url = name.find_element(By.XPATH, 'div/div/a')
                        print(name_url.get_attribute('href'))
                    except NoSuchElementException as ex:
                        i = i - 1
                        continue
                    try:
                        dict_thread["profile_link"] = name_url.get_attribute('href')
                        print(date_post)
                    except NoSuchElementException as ex:
                        i = i - 1
                        continue
                    dict_thread["post_date"] = date_post.strftime('%Y-%m-%d')
                    try:
                        # Description
                        description = parent.find_element(By.XPATH, 'div[3]')
                        text_description = description.find_element(By.XPATH, 'div/div[1]')
                        if ('noboa' in text_description.text or 'Noboa' in text_description.text) and ('veronica' in text_description.text or 'abad' or 'Veronica' in text_description.text or 'Abad' in text_description.text):
                            print(text_description.text)
                            dict_thread["description"] = text_description.text
                        else:
                            print('El texto no concuerda con lo buscado')
                            i = i - 1
                            continue
                    except NoSuchElementException:
                        i = i - 1
                        continue
                    list_hashtags = []
                    try:
                        hashtags = re.findall(r'#\w+', text_description.text)
                        if not hashtags:
                            list_hashtags.append("None")
                        else:
                            for hash_ in hashtags:
                                list_hashtags.append(hash_)
                    except Exception as ex:
                        print(ex)
                    print(list_hashtags)
                    dict_thread["hashtags"] = list_hashtags
                    list_hashtags = []
                    try:
                        suma = 0
                        reactions = description.find_element(By.XPATH, 'div/div[3]')
                        count_reactions = reactions.find_elements(By.TAG_NAME, 'span')
                        if count_reactions:
                            for reaction in count_reactions:
                                if 'x10l6tqk x17qophe x13vifvy' == reaction.get_attribute('class'):
                                    suma = suma + int(reaction.text)
                            print(suma)
                            dict_thread["reactions"] = suma
                        else:
                            dict_thread["reactions"] = 0
                    except NoSuchElementException as ex:
                        print(f'No se encontro el elemento de las reacciones')
                        dict_thread["reactions"] = 0
                    dict_thread_list.append(dict_thread)
            except Exception as ex:
                print(ex)
                continue
        else:
            print(f'Saliendo del if, la publicacion esta fuera del rango de fechas')
            continue
    else:
        drive.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(7)
        new_height = drive.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print('Mismo tamaño')
            break
        last_height = new_height
        continue
    print('No hay mas publicaciones que concuerden')
    break

with open('C:/Users/andre/Downloads/datos_threads 17 MAY - 26 JUL.json', 'w', encoding='utf-8') as json_file:
    json.dump(dict_thread_list, json_file, ensure_ascii=False, indent=4)

drive.close()
