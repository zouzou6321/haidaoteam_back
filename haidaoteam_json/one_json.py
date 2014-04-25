# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.utils import simplejson
from haidaoteam_json.models import *
import string
from django.core.exceptions import ObjectDoesNotExist

def getlist(request):
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
        row_list = one_list.objects.get(home_id=home_row)
    except ObjectDoesNotExist:
        print('ObjectDoesNotExist')
        return HttpResponse(simplejson.dumps({}))
    data = {'data':row_list.toJSON().decode('utf8'),
            'type':'list',
            'id':one_id}
    json=simplejson.dumps(data,ensure_ascii = False)
    return json

def getQA(request):
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
    except ObjectDoesNotExist:
        print('ObjectDoesNotExist')
        return HttpResponse(simplejson.dumps({}))
    data = {'data':row_qa.toJSON().decode('utf8'),
            'type':'QA',
            'id':one_id}
    json=simplejson.dumps(data,ensure_ascii = False)
    return json

def gethome(request):
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
    except ObjectDoesNotExist:
        print('ObjectDoesNotExist')
        return HttpResponse(simplejson.dumps({}))
    data = {'data':home_row.toJSON().decode('utf8'),
            'type':'home',
            'id':one_id}
    json=simplejson.dumps(data,ensure_ascii = False)
    return json
def one_json(request):
    if request.method != 'GET' or 'datatype' not in request.GET:
        return HttpResponse('this is not a crructly json GET request')
    data_type = request.REQUEST.get('datatype')
    if data_type != 'json':
        return HttpResponse('not json request but in json func')
    if 'type' in request.GET:
        type = request.REQUEST.get('type')
        if type == 'home':
            return HttpResponse(gethome(request))
        if type == 'QA':
            return HttpResponse(getQA(request))
        if type == 'list':
            return HttpResponse(getlist(request))
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
        return HttpResponse(simplejson.dumps({}))
    data = {'id':one_id,
            'home':home_row.toJSON().decode('utf8'),
            'QA':row_qa.toJSON().decode('utf8'),
            'list':row_list.toJSON().decode('utf8')}
    json=simplejson.dumps(data,ensure_ascii = False)
    return HttpResponse(json)

def feedback(request):
    if request.method == 'POST' and 'email' in request.POST and 'phone' in request.POST and 'text' in request.POST:
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['text']
        feedback = one_feedback(email=email, phone=phone, content=content)
        feedback.save()
        return HttpResponse('succ')
    return HttpResponse('fail')
