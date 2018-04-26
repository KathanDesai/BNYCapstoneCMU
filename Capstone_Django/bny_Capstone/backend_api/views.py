import json

from backend_api.models import *

from django.http import HttpResponse, Http404, JsonResponse

from backend_api.DBdriver import *

from backend_api.models import *
from django.shortcuts import get_object_or_404


# Create your views here.
def handle(request):
    return HttpResponse("")


def BNYBackEndPost(request):
    if request.method != 'POST' or not request.POST.get('JsonData'):
        raise Http404
    jsonString = request.POST['JsonData']
    jsonObj = json.loads(jsonString)
    # {'source': 's1name', 'destination': 's2name', 'fields': ['fname1', 'fname2']}
    # print(jsonObj)
    handleJson(jsonObj)
    return HttpResponse()


def getOverlaps(request):
    result = {}
    result['overlaps'] = []
    # for every target system
    for dest in Relationship.objects.values_list("toSystem_id",flat=True).distinct():
        obj = {}
        obj['dest'] = get_object_or_404(System, id=dest).name
        #
        obj['overlap'] = []
        # find all the source systems whose destination is dest
        sources = Relationship.objects.filter(toSystem_id=dest)

        for i in range(len(sources)):
            # print (sources[i].fromSystem.name)
            # fields involves message from i to dest
            relation1 =get_object_or_404(Relationship, toSystem_id=dest, fromSystem_id=sources[i].fromSystem.id)
            # print (relation1.attributes.all())
            for j in range(i + 1, len(sources)):
                # fields involves message from j to dest
                relation2 = get_object_or_404(Relationship, toSystem_id=dest, fromSystem_id=sources[j].fromSystem.id)
                # find intersect if any
                intersect = list(set(relation1.attributes.all()) & set(relation2.attributes.all()))

                # if intersect detected
                if len(intersect) > 0:
                    for field in intersect:
                        innerObj = {}
                        innerObj['field'] = field.name
                        innerObj['sources'] = [sources[i].fromSystem.name, sources[j].fromSystem.name]
                        obj['overlap'].append(innerObj)

                        # print(dest.fromSystem.name + ' -> ' + dest.toSystem.name)
        result['overlaps'].append(obj)
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
