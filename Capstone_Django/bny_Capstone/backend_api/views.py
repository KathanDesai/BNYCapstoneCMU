from django.shortcuts import render, redirect, get_object_or_404

import json

from backend_api.models import *

from django.http import HttpResponse, Http404, JsonResponse

from backend_api.DBdriver import *

# Create your views here.
def handle(request):

    return HttpResponse("")


def BNYBackEndPost(request):
    if request.method != 'POST' or not request.POST.get('JsonData'):
        raise Http404
    jsonString = request.POST['JsonData']
    jsonObj = json.loads(jsonString)
    # {'source': 's1name', 'destination': 's2name', 'fields': [{'fname1': 'fval1'}, {'fname2': 'fval2'}]}
    print(jsonObj)
    handleJson(jsonObj)
    return HttpResponse()

def getData(request):
    context_json = {}
    if request.method == 'GET':
        nodes = Node.objects.all()
        for node in nodes:
            print (node.name)
            for neighour in node.connections.all():
                print (neighour.name)

    context_json['system'] = ['a'
    ]
    print (context_json)

    return HttpResponse(context_json, content_type='application/json')
