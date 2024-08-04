from django import template

register = template.Library()

"""
I prefer to use this filter tags in my template 
but as i said in views we can use our manager tho

"""
@register.filter
def only_active_comments(comments):
    return comments.filter(status=True)

@register.filter
def active_comments_count(comments):
    return comments.filter(status=True).count()