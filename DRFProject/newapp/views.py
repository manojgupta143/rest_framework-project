from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import TemplateView
from django.shortcuts import render
import requests
from rest_framework.throttling import UserRateThrottle


# Create your views here.
import json
def get_url(*args,**kwargs):
        BASE_URL='https://api.stackexchange.com/'
        ENDPOINT='/2.3/search/advanced?order=desc&sort=activity&site=stackoverflow&run=true'
        url=BASE_URL+ENDPOINT
        r=requests.get(url)
        data=r.json()
        return data
class Home_pageView(TemplateView):
    throttle_classes = [UserRateThrottle]
    def get_url(self,*args,**kwargs):
        BASE_URL='https://api.stackexchange.com/'
        ENDPOINT='/2.3/search/advanced?order=desc&sort=activity&site=stackoverflow&run=true'
        url=BASE_URL+ENDPOINT
        r=requests.get(url)
        data=r.json()
        return data
      # <view logic>
    def get(self,request, *args, **kwargs):
        data=(get_url())
        data=data['items']
        post_list=data
        paginator=Paginator(data,4)
        page_number=request.GET.get('page')
        try:
            post_list=paginator.page(page_number)
        except PageNotAnInteger:
           post_list=paginator.page(1)
        except EmptyPage:
            post_list=paginator.page(paginator.num_pages)  
        if request.GET.get('pageno'):
            pageno=request.GET.get('pageno')
            ENDPOINT=f'/2.3/search/advanced?{pageno}order=desc&sort=activity&site=stackoverflow&run=true'
            url=requests.get(ENDPOINT)
            data=url
        elif request.GET.get('pagesize'):
            pagesize=request.GET.get('pagesize')
            pagesize=request.GET.get('pagesize')
            ENDPOINT=f'/2.3/search/advanced?{pagesize}order=desc&sort=activity&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('fromdate'):
            fromdate=request.GET.get('fromdate')
            url=f'/2.3/questions?{fromdate}/order=desc&sort=activity&site=stackoverflow&run=true'
            url=requests.get(url)
            data=url
        elif request.GET.get('todate'):
            todate=request.GET.get('todate')
            url=f'/2.3/questions?{todate}/order=desc&sort=activity&site=stackoverflow&run=true'
            url=requests.get(url)
            data=url
        elif request.GET.get('order'):
            order=request.GET.get('order')
            ENDPOINT=f'/2.3/search/advanced?{order}order=desc&sort=activity&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('min'):
            min=request.GET.get('min')
            url=f'/2.3/search/advanced?{min}order=desc&sort=activity&site=stackoverflow&run=true'
            url=requests.get(url)
            data=url
            #2nd row
        elif request.GET.get('max'):
            max=request.GET.get('max')
            url=f'/2.3/search/advanced?{max}order=desc&sort=activity&site=stackoverflow&run=true'
            url=requests.get(url)
            data=url
        elif request.GET.get('q'):
            q=request.GET.get('q')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{q}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('accepted'):
            accepted=request.GET.get('accepted')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{accepted}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
            #4th row
        elif request.GET.get('body'):
            body=request.GET.get('body')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{body}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('closed'):
            closed=request.GET.get('closed')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{closed}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('migrated'):
            migrated=request.GET.get('migrated')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{migrated}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('notice'):
            notice=request.GET.get('notice')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{notice}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('user'):
            user=request.GET.get('user')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{user}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('url'):
            url=request.GET.get('url')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{url}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('views'):
            views=request.GET.get('views')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{views}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('wiki'):
            wiki=request.GET.get('wiki')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{wiki}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('answers'):
            answers=request.GET.get('answers')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{answers}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('page'):
            page=request.GET.get('page')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{page}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('sort'):
            sort=request.GET.get('sort')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{sort}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('tagged'):
            tagged=request.GET.get('tagged')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{tagged}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('notagged'):
            notagged=request.GET.get('notagged')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{notagged}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url
        elif request.GET.get('title'):
            title=request.GET.get('title')
            ENDPOINT=f'/2.3/search/advanced?order=desc&sort=activity&{title}&site=stackoverflow&run=true'
            url=get_url(ENDPOINT=ENDPOINT)
            data=url       
        return render(request, 'data.html',{'post':post_list,'status': 'request was permitted'})