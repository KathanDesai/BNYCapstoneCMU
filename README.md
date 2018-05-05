# User Manual For APIs

## Manually add or remove nodes
```
127.0.0.1:8000/manualProcessNode
```
A HTTP POST method to add or remove a node. The method expects two fiedls:
- nodeName. The name of the system user tries to manipulate
- action. "add" stands for add a system, "remove" stands for remove an existed system 

return 200 if executed successfully, or 403

## Manually add or remove edges
```
127.0.0.1:8000/manualProcessNode
```
A HTTP POST method to add or remove an edge between two nodes. The method expects two fiedls:
- source The name of the source 
- dest  The name of the destination 
- action "add" stands for add a relationship, "remove" stands for remove an relationship 

return 200 if executed successfully, or 403