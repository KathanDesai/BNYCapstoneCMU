# User Manual For APIs

## Manually add or remove nodes
```
127.0.0.1:8000/manualProcessNode
```
A HTTP POST method to add or remove a node. The method has two fiels:
- nodeName. The name of the system user tries to manipulate
- action. "add" stands for add a system, "remove" stands for remove an existed system 

return 200 if executed successfully

## Manually add or remove edges
```
127.0.0.1:8000/manualProcessNode
```
A HTTP POST method to add or remove an edge between two nodes. The method has two fiels:
- source. The name of the source 
- dest.  The name of the destination 

return 200 if executed successfully