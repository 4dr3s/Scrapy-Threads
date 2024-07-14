import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

drive = webdriver.Firefox()
drive.get('https://www.threads.net')
time.sleep(3)
link_login = drive.find_element(By.XPATH, '/html/body/div[2]/div/div/header/div[3]/a')
drive.get(link_login.get_attribute('href'))
time.sleep(3)
form = drive.find_element(By.TAG_NAME, 'form')
inputs = form.find_elements(By.TAG_NAME, 'input')
for input in inputs:
    if 'Nombre de usuario, teléfono o correo electrónico' == input.get_attribute('placeholder'):
        time.sleep(3)
        input.send_keys('Correo')
    if 'password' == input.get_attribute('type'):
        time.sleep(3)
        input.send_keys('Password')
btn_login = form.find_elements(By.TAG_NAME, 'div')
for btn in btn_login:
    if 'button' == btn.get_attribute('role'):
        time.sleep(3)
        btn.click()
time.sleep(3)
drive.get('https://www.threads.net/search?q=veronica%20abad%2Cdaniel%20novoa&serp_type=default')
time.sleep(3)
container = drive.find_element(By.CLASS_NAME, 'xb57i2i x1q594ok x5lxg6s x78zum5 xdt5ytf x1ja2u2z x1pq812k x1rohswg xfk6m8 x1yqm8si xjx87ck xx8ngbg xwo3gff x1n2onr6 x1oyok0e x1e4zzel x1plvlek xryxfnj')
posts = container.find_elements(By.TAG_NAME, 'div')
links_array = []
for post in posts:
    if 'x78zum5 xdt5ytf' == post.get_attribute('class'):
        links = post.find_elements(By.TAG_NAME, 'a')
        for link in links:
            if 'x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1lku1pv x12rw4y6 xrkepyr x1citr7e x37wo2f' == link.get_attribute('class'):
                link_profile = link.get_attribute('href')
                links_array.append(f'https://www.threads.net{link_profile}')
for post in links_array:
    drive.get(post)
    time.sleep(5)
    html = drive.page_source
    soup = BeautifulSoup(html, 'html.parser')
    profile_name = soup.find('span', class_='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xjohtrz x1s688f xp07o12 x1yc453h')
    if profile_name:
        print(f'Nombre de usuario: {profile_name.get_text(strip=True)}')
    profile_link = soup.find('a', class_='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xp07o12 xzmqwrg x1citr7e x1kdxza xt0b8zv')
    if profile_link:
        link = profile_link.get('href')
        print(f'Perfil de usuario: https://www.threads.net{link}')
    date = soup.find('time', class_='x1rg5ohu xnei2rj x2b8uid xuxw1ft')
    if date:
        date = date.get('datetime')
        print(f'Fecha de publicación: {date}')
    content = soup.find('span', class_='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xjohtrz xo1l8bm xp07o12 x1yc453h xat24cr xdj266r')
    if content:
        print(f'Descripción de la publicación: {content.get_text(strip=True)}')
    multimedia_array = []
    image = soup.find_all('img', class_='xl1xv1r x1lq5wgf xgqcy7u x30kzoy x9jhf4c x9f619 x1lliihq xmz0i5r x193iq5w xuiwhb7 x1g40iwv x47corl x87ps6o x1ey2m1c xds687c x10l6tqk x17qophe x13vifvy x5yr21d xh8yej3')
    for img in image:
        if img:
            image = img.get('src')
            multimedia_array.append(image)
    video = soup.find_all('video', class_='x1lliihq x5yr21d xh8yej3')
    for vdo in video:
        if vdo:
            video = vdo.get('src')
            multimedia_array.append(video)

input('Esperando respuesta: ')
