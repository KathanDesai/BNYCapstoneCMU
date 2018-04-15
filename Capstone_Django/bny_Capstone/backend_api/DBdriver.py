from backend_api.models import *

def handleJson(jsonObj):
    sourceName  = jsonObj['source']
    destName = jsonObj['destination']

    findSource = Node.objects.filter(name = sourceName)
    if findSource:
        print('found source')
        source = findSource[0]
    else:
        source = Node(name = sourceName)
        print(source)
        source.save()

    findDest = Node.objects.filter(name = destName)
    if findDest:
        print('found dest')
        dest = findDest[0]
    else:
        dest = Node(name = destName)
        dest.save()
    source.addConnection(dest)
