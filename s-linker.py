import requests
from bs4 import BeautifulSoup
import random
import json
def translate(text):
    source_language = 'en'
    target_language = 'fa'
    #بخش بندی متن برای ترجمه
    chunks = []
    current_chunk = ""
    max_chunk_size = 5000
    for sentence in text.split(". "):
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + ""
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + "."
    if current_chunk:
        chunks.append(current_chunk)

    servers_list = ["lingva.ml", "translate.plausibility.cloud", "lingva.lunar.icu"]
    random_element = random.choice(servers_list)
    print(f"server: {random_element}")

    for i in chunks:
        url = f'https://{random_element}/api/v1/{source_language}/{target_language}/{i}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            translati = data['translation']
            data_i_terans =[]
            data_i_terans.append(translati)
            text = ' '.join(data_i_terans)
            return text
        else:
            print(response.status_code)



def extract_content_from_url(url, n_file):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        text_ex = ""
        h1 = soup.find_all('h1')
        for h1 in h1:
            content = h1.text
            with open(n_file, "w", encoding="utf-8") as file:
                file.write(content + "\n")
                text_ex += content + "\n"

        p = soup.find_all('p')
        with open(n_file, "a", encoding="utf-8") as file:
            for paragraph in p:
                file.write(paragraph.text + "\n" + " ")
                text_ex += paragraph.text + "\n"

        h2 = soup.find_all('h2')
        with open(n_file, "a", encoding="utf-8") as file:
            for header in h2:
                file.write(header.text + "\n" + " ")
                text_ex += header.text + "\n"
    else:
        print("Error: نمیتوان به این صفحه دسترسی داشت.")
    return text_ex


def writer(text):
    with open("e.txt", "a", encoding="utf-8") as file:
        file.write(text)


def run():
    with open("url.txt", "r", encoding="utf-8") as file:
        url_list = file.read().splitlines()
    for url in url_list :
        en_text = extract_content_from_url(url, file_surese_name)
        fa_text = translate(en_text)
        writer(fa_text)

file_surese_name = "s.txt"
run()



