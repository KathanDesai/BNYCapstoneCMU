from django.db import models


class Attribute(models.Model):
    name = models.TextField(default="")

class System(models.Model):
    name = models.TextField(default="")
    attributes = models.ManyToManyField(Attribute)
    #connectionsTo = models.ManyToManyField('self', symmetrical = False)
    #connectionsFrom = models.ManyToManyField('self', symmetrical = False)


    def addConnectionTo(self, otherSystem):
        self.connectionsTo.add(otherSystem)

    def addConnectionFrom(self, otherSystem):
        self.connectionsFrom.add(otherSystem)

    

 

class Relationship(models.Model):
    fromSystem = models.ForeignKey(System, related_name="relationsTo")
    toSystem =  models.ForeignKey(System, related_name="relationsFrom")
    attributes = models.ManyToManyField(Attribute, related_name="rel_attributes")