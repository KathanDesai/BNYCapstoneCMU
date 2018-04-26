
import json

from backend_api.models import *

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
    # {'source': 's1name', 'destination': 's2name', 'fields': ['fname1', 'fname2']}
    #print(jsonObj)
    handleJson(jsonObj)
    return HttpResponse()

<<<<<<< HEAD
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
=======

def getOverlaps(request):
    result = {}
    for sys in System.objects.all():
        for rel in sys.relationsFrom.all():
            print(rel.fromSystem.name + ' -> ' + rel.toSystem.name)
    return JsonResponse(result, status=200)




def getModels(request):
    result = {}
    systems = []
    result['systems'] = systems
    seen = set()
    if not System.objects.all():
        return JsonResponse(result, status=400)

    for system in System.objects.all():
        obj = {}
        innerObj = {}
        innerObj['id'] = system.name
        obj['data'] = innerObj
        systems.append(obj)

    for relation in Relationship.objects.all():
        innerObj = {}
        innerObj['source'] = relation.fromSystem.name
        innerObj['target'] = relation.toSystem.name
        innerObj['id'] = innerObj['source'] + innerObj['target']
        obj = {}
        obj['data'] = innerObj
        systems.append(obj) 

    return JsonResponse(result, status=200)
>>>>>>> 3e5edaf6947aaa5d130a05bcea820e9279aa6779
