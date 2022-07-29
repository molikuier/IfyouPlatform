from django import template
register = template.Library()


@register.simple_tag
def addstr_tag(strs):
    return f"{strs}"

#注册自定义引用标签
@register.inclusion_tag('inclusion.html',takes_context=True)
def add_webname_tag(context,namestr):
    return {'inclusion':'%s %s'%(context['varible'],namestr),
            'inclusion2':'inclu2'}


@register.simple_tag
def test_as_tag(strs):
    return 'Hello Test Tag-%s'%strs