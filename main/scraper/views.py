from django.shortcuts import render
from .utils import scrape_website


def scrape_and_save(request):
    url = "https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8"  # ターゲットのURLを設定
    title, common_words, webimages = scrape_website(url)

    return render(request, 'frontpage.html', {'title': title, 'common_words': common_words, 'image_urls':webimages})