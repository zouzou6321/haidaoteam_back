# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.utils import simplejson
from haidaoteam_json.models import *
import string
from django.core.exceptions import ObjectDoesNotExist
from haidaoteam_json.one_json import one_json,feedback
from django.shortcuts import render_to_response
def webroot(request):
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