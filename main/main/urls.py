from django.contrib import admin
from django.urls import path
from scraper.views import scrape_and_save

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scrape_and_save, name='frontpage')
]
