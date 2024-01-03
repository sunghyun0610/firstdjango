from django.shortcuts import render, HttpResponse

topics=[
    {'id':1,'title':'routing', 'body': 'Routing is..'},
    {'id':2,'title':'view', 'body': 'View is..'},
    {'id':3,'title':'routing', 'body': 'Model is..'}
]

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
    <h1><a href="/">Django</a></h1>
    <ul>
        {ol}
    </ul>
    {articleTag}
    
    <ul>
        <li><a href="/create/">Create</a></li>
    </ul>
    </body>
    </html>

    '''


def index(request):
    article='''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def create(request):
    article='''
    <form action="/create/">
        <p><input type="text" name="title" placeholder="write title"></p> 
        <p><textarea name="body" placeholder="body"></textarea></p>
        <p><input type="submit" value="제출"></p>
    </form>
    '''
    # title : 입력한 데이터를 서버로 전송할때 title이라는 이름으로 감
    # placeholder : 칸안에 도움말이다
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article=f'<h2>{topic["title"]}</h2>{topic["body"]}'

    return HttpResponse(HTMLTemplate(article))