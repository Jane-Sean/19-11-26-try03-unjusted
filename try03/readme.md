哈哈啊哈哈

今天是2019/11/26，（一个憨憨）想要记录爬取武大新闻网的艰辛历史。

然后她发现她什么都写不出来

那就只好我代劳了嘿嘿

总体思路：使用正则和BeautifulSoup实现数据清洗。

使用框架以及依赖库：Django（2.2.6）Python（3.7.4）beatuifulsoup4（4.8.1）

FAQ:

1.分析网页结构判断使用bs4 or 正则表达式

由于正则表达式一经匹配即成为字符串，不利于后续对于标签结构的提取和处理，所以先使用正则表达式匹配url，再使用bs4，从新闻网界面的标签结构中提取出所有的新闻内容。

2.Django模板语言的使用

由于发送到前台的数据需要csrf认证以及进行迭代处理，利用以下命令：

BackEnd:

    return render(request, 'Result.html', {a:b})

FrontEnd(html):

    Result Page:
        {% for a in result %}
        {{ a }}
        {% endfor %}

    Post form:
        {% csrf_token %}
        
或者直接注释掉Django的settings.py中的csrf中间件：
    
    # 'django.middleware.csrf.CsrfViewMiddleware',

3.关于访问频率过高导致网络差条件下访问易失败以及访问时间过长的报错：

    # 在request命令中引入timeout参数：
    response = request.get(url, timeout=0.1)   


19/11/26更新