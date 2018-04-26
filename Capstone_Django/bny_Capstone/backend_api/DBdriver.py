from backend_api.models import *

def handleJson(jsonObj):
    sourceName  = jsonObj['source']
    destName = jsonObj['destination']

    findSource = System.objects.filter(name = sourceName)
    if findSource:
        print('found source')
        source = findSource[0]
    else:
        source = System(name = sourceName)
        print(source)
        source.save()

    findDest = System.objects.filter(name = destName)
    if findDest:
        print('found dest')
        dest = findDest[0]
    else:
        dest = System(name = destName)
        dest.save()
    
    findRelationShip = Relationship.objects.filter(fromSystem = source, toSystem = dest)
    if findRelationShip:
        relation = findRelationShip[0]
    else:
        relation = Relationship(fromSystem = source, toSystem = dest)
        relation.save()
    
      
    fields = jsonObj['fields']
    for field in fields:
        findField = Attribute.objects.filter(name = field)
        if findField:
            attribute = findField[0]
        else:
            attribute = Attribute(name = field)
            attribute.save()
        findInRelationship = True if attribute in relation.attributes.all() else False
        if not findInRelationship:
            relation.attributes.add(attribute)




