# -*- coding: utf-8 -*-

import sys
import datetime
import hashlib
import urllib.request
from lxml import html
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import JsonResponse

from cms.models import Web_Page



def index(request):
    context = {}
    return render(request, 'cms/index.html', context)


class HtmlPage:
    def __init__(self, path, __type=1):
        self.status = True
        try:
            fp = urllib.request.urlopen(path)
            self.__raw_text = fp.read().decode('utf-8')
            self.lxml = BeautifulSoup(self.__raw_text, 'lxml')
            self.html = BeautifulSoup(self.__raw_text, 'html.parser')
        except Exception:
            self.status = False
            self.exception = sys.exc_info()[1]


def parse_html(myHeap):
    resp = {}
    if myHeap.status:
        total_list = myHeap.html.recursiveChildGenerator()
        total_list_clean = [el for el in total_list if el.name]
        for el in total_list_clean:
            _ch = len([foo for foo in list(el.children) if foo.name])
            if el.name in resp.keys():
                resp[el.name]['count'] += 1
                resp[el.name]['nested'] += _ch
            else:
                print(el.name, _ch)
                resp[el.name] = {'count': 1, 'nested': _ch}
    else:
        resp['error'] = myHeap.exception
    return str(resp)


def get_token(__url):
    string_to_encode = (__url+str(datetime.datetime.now())).encode()
    return hashlib.sha256(string_to_encode).hexdigest()[:10]


def variant_1(request):
    context = {}
    if request.GET:
        __url = request.GET.get('url', None)
        __token = request.GET.get('token', None)
        context['get_url'] = f'url={__url}, token={__token}'
        if __token:
            page_by_token = Web_Page.objects.filter(token=__token)
            if not page_by_token:
                context['token'] = __token
                context['response'] = 'Token wasn\'t found'
            else:
                context['token'] = __token
                context['response'] = page_by_token[0].results

        else:
            context['response'] = parse_html(HtmlPage(__url))
            myToken = get_token(__url)
            context['token'] = myToken
            newWebPage = Web_Page(
                url = __url,
                token = myToken,
                status = 1,
                results = str(context)
                )
            newWebPage.save()
        return JsonResponse(context)
    return render(request, 'cms/variant_1.html', context)
