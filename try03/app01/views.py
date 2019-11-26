# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def choose(request):
    return render(request, "Homepage.html")


def command(request):
    return render(request, 'Command.html')


def crawler(request):
    import re
    import requests
    # request.method = 'post'
    # if request.method =="POST":
    required_num = request.POST.get("required_num")
    b = int(required_num)
    keyword = request.POST.get("keyword")

    url01 = 'https://news.whu.edu.cn/wdyw.htm'
    response = requests.get(url01)
    response.encoding = 'utf-8'
    html01 = response.text
    news_part_url_list = re.findall(r' <div class="infotitle"><a href="info(.*?)" title=', html01, re.S)

    news_url_list = []
    news_title_list = []
    news_content_list = []
    result_list = []
    search_result_list = []
    # get whole news urls
    from bs4 import BeautifulSoup
    for news_part_url in news_part_url_list:
        news_url = 'https://news.whu.edu.cn/info%s' % news_part_url
        news_url_list.append(news_url)
        print(news_url)

    # crawler function
    for f in news_url_list:
        news_response = requests.get(f)
        news_response.encoding = 'utf-8'
        news_html = news_response.text
        soup01 = BeautifulSoup(news_html, 'html.parser')
        title_tags = soup01.find('div', 'news_title')
        if title_tags:
            news_title = title_tags.text
            news_title_list.append(news_title)
            print(news_title)
            content_tags01 = soup01.find('div', 'v_news_content')
            content_part = content_tags01.text
            news_content_list.append(content_part)

            result = f + news_title + content_part
            result_list.append(result)

    if keyword:
            # for news_s_url in news_url_list:
            #     news_s_response = requests.get(news_s_url)
            #     news_s_response.encoding = 'utf-8'
            #     news_s_html = news_s_response.text
            #     soup01 = BeautifulSoup(news_s_html, 'html.parser')
            #     title_s_tags = soup01.find('div', 'news_title')
            #     if title_s_tags:
            #         news_s_title = title_s_tags.text
            #         print(news_title)
            #         content_tags01 = soup01.find('div', 'v_news_content')
            #         content_part = content_tags01.text
            #         news_content_list.append(content_part)

        for c in result_list:
            search_result = re.findall(keyword, c, re.S)
            print(search_result)
            if search_result:
                search_result_list.append(c)
                if len(search_result_list) == b:
                    break
                else:
                    return HttpResponse("Not enough")
            # sorry = 1
            # search_result_list.append(sorry)
        h = search_result_list
        return render(request, 'search_result.html', {'result': h})

    else:
        g = result_list[:b]

        return render(request, 'result.html', {'result': g})




