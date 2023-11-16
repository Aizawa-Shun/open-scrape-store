import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
from .models import WebData


# ウェブスクレイピング
def scrape_website(url):
    # データを取得
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # タイトルタグのテキストを取得
    title_text = soup.title.string

    # ページの全テキストを取得
    text = soup.get_text()

    # テキストを単語に分割
    words = re.findall(r'\w+', text)

    # 出現頻度の高い単語をカウント
    word_freq = Counter(words)

    # 最も出現頻度の高い10単語を取得
    common_words = word_freq.most_common(10)

    # 画像のURLを取得
    images = get_images_from_website(soup)


    # 特定のタグ（例: 'a'タグ）をすべて取得
    # tags = soup.find_all('a')
    # # タグの情報を表示
    # for tag in tags:
    #     print(tag)

    # 例: 'a'タグのテキストとhref属性の値を取得
    # for tag in tags:
    #     print(tag.text)  # タグのテキスト
    #     print(tag['href'])  # href属性の値

    # 例: class="sample-class"を持つdivタグを取得
    # divs = soup.find_all('div', class_='sample-class')
    # for div in divs:
    #     print(div)


    # データをDjangoのモデルに保存
    web_data = WebData(title=title_text, keywords=str(common_words), images=str(images))
    web_data.save()

    return title_text, common_words, images  # タイトル, 頻出単語, 画像


# 指定したBeautifulSoupオブジェクトから画像のURLを取得
def get_images_from_website(soup):

    img_tags = soup.find_all('img')  # imgタグを探す
    img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]  # 画像のurlを取得
    
    return img_urls