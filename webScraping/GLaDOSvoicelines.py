import requests
from bs4 import BeautifulSoup
import wget

url = 'https://theportalwiki.com/wiki/GLaDOS_voice_lines'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


def get_voiceline_text():
    voicelines = [[voiceline.text.strip(), link['href']] for voiceline in soup.find_all('i') if "[" not in voiceline.text and (span := voiceline.find_next_sibling('span')) != None and (link := span.find('a'))]
    return voicelines


def save_files(i, j):
    # save to txt
    file = open(f"{i+1}.txt", 'w', encoding='utf-8')
    file.write(j[0])
    # save to wav
    wget.download(j[1], f"{i+1}.wav")


if __name__ == "__main__":
    voicelines = get_voiceline_text()
    for i, j in enumerate(voicelines):
        save_files(i, j)
