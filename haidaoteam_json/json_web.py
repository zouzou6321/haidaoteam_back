# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.utils import simplejson
from haidaoteam_json.models import *
import string
from django.core.exceptions import ObjectDoesNotExist
from haidaoteam_json.one_json import one_json,feedback
from django.shortcuts import render_to_response
from haidaoteam import settings
import datetime
def webroot(request):
    if request.method == 'GET' and 'editor' in request.GET:
        return editor(request)
    if request.method == 'POST' and 'sub' in request.POST:
        return editor(request)
    if request.method == 'GET' and 'datatype' in request.GET:
        return one_json(request)
    if 'feedback' in request.GET:# and request.method == 'POST':
        return feedback(request)
    one_id = -1
    try:
        if 'id' not in request.GET:
            home_rows = home.objects.all().order_by('-id')[0:1]
            if home_rows.count() == 0:
                return HttpResponse(simplejson.dumps({}))
            home_row = home_rows[0]
            one_id = home_row.id
        else:
            str_id = request.REQUEST.get('id')
            one_id = string.atoi(str_id)
            if one_id < 0:
                return HttpResponse('the id can not be smaller than 0')
            home_row = home.objects.get(id=one_id)
        row_qa = QA.objects.get(home_id=home_row)
        row_list = one_list.objects.get(home_id=home_row)
    except ObjectDoesNotExist:
        print('ObjectDoesNotExist')
        return HttpResponse('ObjectDoesNotExist')
    return render_to_response('haidao_one.htm',{'home_row':home_row,'row_qa':row_qa,'row_list':row_list})

def webholdon(request,path):
    return HttpResponse('hold on')

def etitor_submit(request):
    if "image" in request.POST:
        try:
            home_new = home(new_tView = request.POST['content'],
                            home_share_url = "",
                            fPage_tView = request.POST['vol'],
                            imageView1 = request.POST['image'],
                            imageBelow_tView = request.POST['below_view'],
                            imageBelow_tView1 = request.POST['below_view1'],
                            date_tView = str(datetime.date.today())[8:10],
                            date1_tView = (datetime.datetime.now()).time(),
                            )
            home_new.save()
            home_new.home_share_url = settings.ROOT_URL + "?id=" + (home_new.id).__str__()
            home_new.save()
            print('33333')
        except NameError:
            HttpResponse("ONE 首页数据存在异常，请检查！")
        
        try:
            one_list_new = one_list(home_id = home_new,
                                    list_share_url = "",
                                    content_publish_time = datetime.datetime.isoformat(datetime.datetime.now()),
                                    one_content_title = request.POST['in_list_title'],
                                    one_content_author = request.POST['in_list_author'],
                                    one_content_article = request.POST['in_list_article'],
                                    one_content_author_novel = request.POST['in_list_author_novel'],
                                    )
            print('00000')
            one_list_new.save()
            print('11111')
            one_list_new.list_share_url = settings.ROOT_URL + "?id=" + (one_list_new.id).__str__() + "#articulo"
            print('22222')
            one_list_new.save()
            print('44444')
        except NameError:
            HttpResponse("ONE 文章数据存在异常，请检查！")
        
        try:
            QA_new = QA(home_id = home_new,
                        qa_share_url = "",
                        question_title = request.POST['in_qa_title'],
                        question_publish_time = datetime.datetime.isoformat(datetime.datetime.now()),
                        question_content = request.POST['in_qa_content'],
                        question_answer_title = request.POST['in_qa_answer_title'],
                        question_answer_content = request.POST['in_qa_answer_content'],
                        )
            QA_new.save()
            QA_new.qa_share_url = settings.ROOT_URL + "?id=" + (QA_new.id).__str__() + "#cuestion"
            QA_new.save()
        except NameError:
            HttpResponse("ONE 问答数据存在异常，请检查！")
        return HttpResponse("true")
    return HttpResponse("首页图片不存在!")

def editor_main(request):
    return render_to_response('editor.htm')

def editor_login_response(request):
    name = request.REQUEST.get('username')
    passd = request.REQUEST.get('userpassd')
    try:
        editor_user.objects.get(name=name,passd=passd)
    except ObjectDoesNotExist:
        print('ObjectDoesNotExist')
        return HttpResponse('username or password error!')
    request.session['admin'] = 'true'
    return editor_main(request)

def editor(request):
    if request.method == 'GET' and 'username' in request.GET and 'userpassd' in request.GET:
        return editor_login_response(request)
    try:
        if (request.session['admin'] != 'true'):
            return render_to_response('editor_login.htm')
    except:
        return render_to_response('editor_login.htm')
    if request.method == 'POST' and 'sub' in request.POST:
        print("sub mit")
        return etitor_submit(request)
    return editor_main(request)