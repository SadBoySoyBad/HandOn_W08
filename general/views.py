from django.shortcuts import render
from django.http import HttpResponse


def ecommerce_index_view(request):
    '''This function render index page of ecommerce view'''

    return HttpResponse('Wellcome to CN334 kittipon View!')