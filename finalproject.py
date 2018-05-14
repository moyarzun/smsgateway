from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#API endpoint for GET requests
@app.route('/')

@app.route('/restaurants')
def showRestaurants():
    return "Esta pagina muestra la lista de restaurantes registrados en el sistema."

@app.route('/restaurants/new')
def newRestaurant():
    return "Esta pagina permite agregar restaurantes al sistema."

@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return "Esta pagina permite editar restaurantes en el sistema."

@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurants(restaurant_id):
    return "Esta pagina permite eliminar restaurantes del sistema."

@app.route('/restaurants/<int:restaurant_id>')
def showMenuItems(restaurant_id):
    return "Esta pagina muestra el menu de un restaurant."

@app.route('/restaurants/<int:restaurant_id>/new')
def newMenuItem(restaurant_id):
    return "Esta pagina permite agregar un elemento menu al restaurant."

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "Esta pagina permite editar un elemento menu del restaurant."

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return "Esta pagina permite eliminar un elemento menu del restaurant."

@app.route('/restaurants/<int:restaurant_id>/JSON')
def itemRestaurantJSON(restaurant_id):
    return "API para obtener un unico elemento Restaurant"

@app.route('/restaurants/JSON')
def listaRestaurantJSON():
    return "API para obtener una lista de elementos Restaurant"

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def itemMenuJSON(restaurant_id, menu_id):
    return "API para obtener un unico elemento Restaurant"

@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def listaMenuJSON(restaurant_id):
    return "API para obtener una lista de elementos Restaurant"

if __name__ == '__main__':
    app.secret_key = 'asdasda'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
