import requests
from bs4 import BeautifulSoup
import random
import json
def translate(text):
    source_language = 'en'
    target_language = 'fa'
    #translate section
    #remember you should write your comments in english so people from other countries could understand what you had wrote :)
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

    servers_list = ["lingva.ml", "lingva.lunar.icu"]
    random_element = random.choice(servers_list)
    print(f"server: {random_element}")

    translated_chunks = []  # New list to store translated chunks

    for i in chunks:
        url = f'https://{random_element}/api/v1/{source_language}/{target_language}/{i}'
        response = requests.get(url)
        requ_code = response.status_code
        if requ_code == 200:
            print("len requ: ", len(i))
            print(response.status_code)
            data = response.json()
            translati = data['translation']
            translated_chunks.append(translati)  # Append each translation to the list
        else:
            while requ_code != 200:
                print("error:", response.status_code)
                print("len requ: ", len(i))
                random_element = random.choice(servers_list)
                print("new server:", random_element)
                url = f'https://{random_element}/api/v1/{source_language}/{target_language}/{i}'
                response = requests.get(url)
                requ_code = response.status_code

            data = response.json()
            translati = data['translation']
            translated_chunks.append(translati)

    text = ' '.join(translated_chunks)
    return text  # Return the combined translation




def extract_content_from_url(url, n_file):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        text_ex = ""

        with open(n_file, "a", encoding="utf-8") as file:
            h1 = soup.find_all('h1')
            for h1 in h1:
                content = h1.text
                file.write(content + "\n")
                text_ex += content + "\n"

            p = soup.find_all('p')
            for paragraph in p:
                file.write(paragraph.text + "\n" + " ")
                text_ex += paragraph.text + "\n"

            h2 = soup.find_all('h2')
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
