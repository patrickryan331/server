from flask import Flask, request
import  json
from config import db


#Global Variables
items = []
catalogItem =  []
totalReport = []
specialCatagory = []



app = Flask(__name__)

@app.get("/")
def home():
    return "Hello and Welcome to RESTfull API!"

@app.get("/test")
def test():
    return "hello from the test page"




# API endpoints
# JSON
# create an API to preform a get request at this url: /api/about
#return your name as a message
@app.get("/api/about")
def about():
    me = {"name":"Patrick Ryan"}    #me is an example of a library
    return json.dumps(me)           #convert to json so other cpus without python can read it



products = []


def fix_id(obj):
    obj["_id"]=str(obj["_id"])
    return obj



#### post request #### creates a new instance within the server
@app.post("/api/products")
def saveProduct():
    newItem = request.get_json()
    print (newItem)
    db.products.insert_one(newItem)
    #mock the save
    #products.append(newItem)
    return json.dumps(fix_id(newItem))


@app.post("/api/catalog")
def saveCatalog():
    catalogItem = request.get_json()
    print (catalogItem)
    db.products.insert_one(catalogItem)
    return json.dumps(fix_id(catalogItem))



#### this  gets/reads the product added to the server
@app.get("/api/s")
def getProducts():
    return json.dumps(items) 


@app.get("/api/catalog")
def getCatalog():
    return json.dumps(catalogItem) 


@app.get("/api/reports/total")
def getTotalReport():
    return json.dumps(totalReport)


@app.get("/api/products/category")
def getCatagory():
    return json.dumps(specialCatagory) 



app.run(debug = True )