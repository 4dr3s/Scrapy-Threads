import time
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import re

dict_thread_list = []
drive = webdriver.Firefox()
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
            time.sleep(3)
            div.click()
            time.sleep(3)
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
email.send_keys('vijib84329@modotso.com')
password = form.find_element(By.ID, 'pass')
password.send_keys('12345inge')
btn_login = form.find_element(By.ID, 'loginbutton')
btn_login.click()
time.sleep(20)
drive.get('https://www.threads.net/search?q=veronica%20abad%20y%20daniel%20noboa&serp_type=default&filter=recent')
time.sleep(3)
btn_recently = drive.find_elements(By.TAG_NAME, 'div')
for div in btn_recently:
    if 'x9f619 xmixu3c x78zum5 xkh2ocl xmupa6y xqmxbcd x14vqqas' == div.get_attribute('class'):
        div.find_element(By.XPATH, './a[2]').click()
        time.sleep(9)
        break
links_array = []
date_init = datetime.strptime("2023-05-24T00:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")
divs = drive.find_elements(By.TAG_NAME, 'div')
last_height = drive.execute_script("return document.body.scrollHeight")
i = 0
while True:
    time_post = drive.find_elements(By.TAG_NAME, 'time')
    for tmt in time_post:
        date_ = tmt.get_attribute('datetime')
        date_post = datetime.strptime(date_, "%Y-%m-%dT%H:%M:%S.%fZ")
        print(f'Fecha: {date_post}')
        if date_post >= date_init:
            try:
                link = tmt.find_element(By.XPATH, '..')
                if link:
                    link_profile = link.get_attribute('href')
                    links_array.append(link_profile)
                    print(f'Listado: {link_profile}')
                    i = i + 1
                    if i % 100 == 0:
                        decision = input('Continuar? Y/N')
                        if decision == 'N':
                            break
                    print(f'Publicacion N {i}')
            except:
                print(f'Continuando a la siguiente fecha')
                continue
        else:
            print(f'Saliendo del if')
            break
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
i = 0
for post in links_array:
    i = i + 1
    dict_thread = {}
    drive.get(post)
    time.sleep(5)
    html = drive.page_source
    soup = BeautifulSoup(html, 'html.parser')
    print(f'Visitando la publicación: {post}')
    dict_thread['id'] = i
    dict_thread['fuente'] = "threads"
    dict_thread['post_link'] = post
    profile_name = soup.find_all('span', class_='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xjohtrz x1s688f xp07o12 x1yc453h')
    for name_et in profile_name:
        parent = name_et.parent
        if parent.name == 'a':
            if name_et.get_text(strip=True) != 'Hilo':
                dict_thread["user_name"] = name_et.get_text(strip=True)

    profile_link = soup.find('a', class_='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xp07o12 xzmqwrg x1citr7e x1kdxza xt0b8zv')
    if profile_link:
        link = profile_link.get('href')
        dict_thread["profile_link"] = f'https://www.threads.net{link}'

    date = soup.find('time', class_='x1rg5ohu xnei2rj x2b8uid xuxw1ft')
    if date:
        date = date.get('datetime')
        fecha = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
        dict_thread["post_date"] = fecha.strftime('%Y-%m-%d')

    content = soup.find('div', class_='x1a6qonq x6ikm8r x10wlt62 xj0a0fe x126k92a x6prxxf x7r5mf7')
    if content:
        dict_thread["description"] = content.get_text(strip=True)
        try:
            hashtags = re.findall(r'#\w+', content.get_text(strip=True))
            if hashtags:
                dict_thread["hashtags"] = hashtags
            else:
                dict_thread["hashtags"] = ["None"]
        except Exception as ex:
            print(ex)
    reactions = soup.find_all('span', class_='x10l6tqk x17qophe x13vifvy')
    suma = 0
    for reaction in reactions:
        if reaction:
            suma = int(reaction.get_text(strip=True)) + suma
        else:
            suma = 0 + suma
    dict_thread["reactions"] = suma
    dict_thread_list.append(dict_thread)

with open('C:/Users/andre/Downloads/datos_threads.json', 'w', encoding='utf-8') as json_file:
    json.dump(dict_thread_list, json_file, ensure_ascii=False, indent=4)

drive.close()
