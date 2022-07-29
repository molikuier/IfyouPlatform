from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template,Context#调用template、以及上下文处理器方法
# Create your views here.


def test_html(request):
    a={} #创建空字典，模板必须以字典的形式进行传参
    a['name']='C语言中文网'
    a['course']=["Python","C","C++","Java"]
    a['b']={'name':'如果科技','address':'http://www.ifyou.com/'}
    a['test_hello']=test_hello
    a['class_obj']=Website()
    return render(request,'test.html',a)
def test_hello():
    return '欢迎来到如果科技'
class Website:
    def Web_name(self):
        return 'Hello，科技'

def test_if(request):
    dic={'x':2**4}
    return render(request,'test_if.html',dic)



def Hello_MyWeb(request,id):
      #调用template()方法生成模板
      t=Template("""
                        {% if web.name == 'C语言中文网' %}
                              {% if printable %}
                                     <h1>Hello myweb{{ id }}</h1>
                              {% else %}
                                      <h2>欢迎您下次访问，C语言中文网</h2>
                              {% endif %}
                        {% endif %}
                                      """)
      c= Context({'web':{'name':'C语言中文网'}, 'printable': True,'id':id }) #Context必须是字典类型的对象，用来给模板传递数据
      html=t.render(c)
      return HttpResponse(html)


def test_for(request):
    # 调用template()方法生成模板
    t1 = Template("""
                    {% for item in list %}
                     <div>
                        <p><b>{{ forloop.counter }}:{{ item }}</b></p>
                    </div>
                        <li>{{ item }}</li>
                    {% empty %}
                        <h1>如果找不到你想要，可以来C语言中文网(网址：http://c.biancheng.net/)</h1>
                    {% endfor %}
                              """)
    # 调用 Context()方法
    c1 = Context({'list': ['Python', 'Java', 'C', 'Javascript', 'C++']})
    html = t1.render(c1)
    return HttpResponse(html)

def test_sort(request):
    t=Template("""
    {% for book in books|dictsort:"author.age" %}
         {{ book.title }} ({{ book.author.name }})
     {% endfor %}
     """)
    html = t.render(Context({'books':[
        {'title': 'C语言教程', 'author': {'name': 'ycs', 'age': 14}},
         {'title': 'Python教程', 'author': {'name': 'xxw', 'age': 17}},
         {'title': 'Django教程', 'author': {'name': 'ccs', 'age': 16}},
     ]}))
    return HttpResponse(html)

def test_url(request):
    return render(request,'test_url.html')

def simple_tag(request):
    t=Template("""
    {% load index_tags %}
    {% addstr_tag 'Django BookStore' %}
    """)
    html = t.render(Context())
    return HttpResponse(html)

def inclu_tag(request):
    t=Template("""
    {% load index_tags %}
    {% add_webname_tag 'ifyou ' %}
    """)

    html = t.render(Context({'varible':'Hello'}))
    return HttpResponse(html)

def sim_tag(request):
    t=Template("""
    {% load index_tags %}
    {% test_as_tag '语言中文网欢迎你' as test %}
    <p>{{ test }}</p>
    """)

    html = t.render(Context())
    return HttpResponse(html)

def ifchanged(request):
    t=Template("""
    {% for name in webnames %}
         {% ifchanged %}
         {{name.1|add:'ioe'}}
         {% endifchanged %}
     {% endfor %}    
     """)
    html = t.render(Context({'webnames':[['Python','Flask'],'java','c语言']}))
    return HttpResponse(html)