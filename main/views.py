from django.shortcuts import render

import os

def main(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATICFILES_DIRS = os.path.join(BASE_DIR, "/static/css")
    # print(STATICFILES_DIRS, '   ', BASE_DIR)
    current_day = '03/01/2018'
    return render(request, 'main.html', locals())