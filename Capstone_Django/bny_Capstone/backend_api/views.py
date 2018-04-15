from django.shortcuts import render, redirect, get_object_or_404

import json

from django.http import HttpResponse, Http404, JsonResponse

from backend_api.DBdriver import *

from backend_api.models import *

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
    

def getModels(request):
    result = {}
    systems = []
    result['systems'] = systems
    seen = set()
    for node in Node.objects.all():
        obj = {}
        innerObj = {}
        innerObj['id'] = node.name
        obj['data'] = innerObj
        systems.append(obj)
        if not node.connections:
            continue
        for connection in node.connections.all():
            innerObj = {}
            innerObj['source'] = node.name
            innerObj['target'] = connection.name
            innerObj['id'] = node.name + connection.name
            obj = {}
            obj['data'] = innerObj
            systems.append(obj)

    return JsonResponse(result)
