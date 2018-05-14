# User Manual For APIs

## Dependencies

Install Python 3.x if not present

## Start the application

Go to the directory Capstone_Django/bny_Capstone and run the below command

```
python manage.py runserver
```

## Sending system interactions via JSON Request

Maka a HTTP POST request with content type as application/json

form-data key: "JsonData"
form-data value: A Json string in below format

JSON Format: 

{
    "source": "System 1",
    "destination": "System 2",
    "fields": ["field-1 name", "field-2 name"]
}

```
127.0.0.1:8000/processRequest
``` 

## File upload URL

Send a HTTP POST request to the below URL. The form-data should have a key: 'csv_file' and the value should be a '.csv' file of format specified in report.

```
127.0.0.1:8000/fileUpload
```

## Getting the lineage model

The Lineage model will be returned as JSON String by making a HTTP GET request: 

```
127.0.0.1:8000/getModels
```

## Getting the Overlaps

The Overlaps in Lineage model will be returned as JSON String by making a HTTP GET request: 

```
127.0.0.1:8000/getOverlaps
```

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
127.0.0.1:8000/manualProcessRelationship
```
A HTTP POST method to add or remove an edge between two nodes. The method expects two fiedls:
- source The name of the source 
- dest  The name of the destination 
- action "add" stands for add a relationship, "remove" stands for remove an relationship 

return 200 if executed successfully, or 400

## Clearing the Database for a fresh start

The entire database can be cleared by making a HTTP GET request to the below URL

```
127.0.0.1:8000/clearDB
```