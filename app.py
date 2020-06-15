from flask import Flask, render_template, url_for, redirect, request, flash
from views.item import ItemForm
from views.login import LoginForm
from models.item import item
from repository.items import itemRepository
from bson.json_util import dumps
import json
from bson import objectid

app = Flask(__name__)
app.secret_key = "mysecretkey123"

repo = itemRepository()

@app.route('/', methods=['GET','POST'])
def index():
    itemsToList = repo.read()
    message = None
    if itemsToList == None:
        message = "No Item To List, Admin Can Add Items"
    if request.method == 'GET':
        return render_template('index.html', itemsToList=itemsToList, message=message)
    
@app.route('/post-item', methods=['GET','POST'])
def postitem():
    form = ItemForm()
    if request.method == 'GET':
        return render_template('post-item.html', form=form)
    if form.validate_on_submit: 
        hyip = form.hyip.data
        status = form.status_select.data
        description = form.description.data
        itemObject = item(None, hyip, status, description)  
        repo.create(itemObject)
    return render_template('post-item.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        render_template('login.html', form=form)

@app.route('/edit-item/<id>', methods=['GET','POST'])
def edititem(id):
    form = ItemForm()
    itemToEdits = repo.read(id)
    itemToEdits = dumps(itemToEdits)
    print(itemToEdits)
    itemToEdit = json.loads(itemToEdits)[0]
    hyip = itemToEdit['hyip']
    status = itemToEdit['status']
    description = itemToEdit['description']
    id = itemToEdit['_id']
    main_id = json.loads(dumps(id))
    
    print(main_id['$oid'])
    if request.method == 'GET':
        form.hyip.data = hyip
        form.description.data = description
        if status is not None:
            form.status_select.default = status
            form.process()
        return render_template('edit-item.html', form=form, hyip=hyip, description=description)
    if form.validate_on_submit:
        hyipUpdate = form.hyip.data
        statusUpdate = form.status_select.data
        descriptionUpdate = form.description.data
        itemToEdit = item(objectId(main_id['$oid']), hyipUpdate, statusUpdate, descriptionUpdate)
        repo.update(itemToEdit)
    return render_template('edit-item.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)