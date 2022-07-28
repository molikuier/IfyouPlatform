from django import template
register = template.Library()


@register.simple_tag
def addstr_tag(strs):
    return f"{strs}"

#注册自定义引用标签
@register.inclusion_tag('inclusion.html',takes_context=True)
#定义函数渲染模板文件 inclusion.html
def add_webname_tag(context,namestr): #使用takes_context=True此时第一个参数必须为context
    return {'inclusion':'%s %s'%(context['varible'],namestr)}