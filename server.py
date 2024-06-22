from flask import Flask, request
import  json

#Global Variables
items = []
#


app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"

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






#### post request #### creates a new instance within the server
@app.post("/api/product")
def saveProduct():
    product = request.get_json()
    print (product)
    #mock the save
    items.append(product)
    return json.dumps(product)


#### this  gets/reads the product added to the server
@app.get("/api/product")
def getProducts():
    return json.dumps(items) 





app.run(debug = True )