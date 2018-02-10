from django import template

registre = template.Library()

@registre.filter
def bootstrap3(value):
    return value
