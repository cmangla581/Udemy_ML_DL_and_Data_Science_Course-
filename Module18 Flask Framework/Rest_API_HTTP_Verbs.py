
## Put and delete -  HTTP Verbs 
## Working with the API's - JSON 

from flask import Flask, jsonify, request  

app = Flask(__name__)  

items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"}, 
    {"id": 2, "name": "Item 2", "description": "This is item 2"}, 

] 

@app.route('/') 
def home(): 
    return "Welcome to theSample of To DO List" 

@app.route('/items', methods = ['GET']) 
def get_items(): 
    return jsonify(items) 

@app.route('/items/<int:item_id>', methods = ['GET']) 
def get_items(item_id): 
    item = next((item for item in items if item["id"] == item_id), None) 
    if item is None: 
        return jsonify({"error": "error not found"}) 
    return jsonify(item)  

## Post : create a new task 
@app.route('/items'.methods['POST']) 
def create_item(): 
    if not request.json or not 'name' in request.json: 
        return jsonify({"error": "item not found"}) 
    new_items = {
        "id": items[-1]["id"] + 1  if items else 1, 
        "name": request.json['name'], 
        "description": request.json["description"]
    } 
    items.append(new_item) 
    return jsonify(new_item) 

# Put update on an existing line which takes place as: 
@app.route('/items/<int:item_id>', methods = ['PUT']) 
def update_item(item_id): 
    item = next((item for item in items if item["id"] == item_id), None) 
    return jsonify(item) 

## Delete Item  
@app.route('/items/<int:item_id>', methods = ['DELETE']) 
def delete_item(item_id): 
    global items  
    items = [item for item in items if item["ID"] != item_id] 
    return jsonify({'result': "Item deleted"})




if __name__ == '__main__': 
    app.run(debug = True)  

