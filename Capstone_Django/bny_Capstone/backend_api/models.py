from django.db import models

class Node(models.Model):
    name = models.TextField(default="")
    fields = models.TextField(default="")
    connections = models.ManyToManyField('self')



    def addConnection(self, otherNode):
        self.connections.add(otherNode)

    
