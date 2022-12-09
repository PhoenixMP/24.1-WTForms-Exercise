from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    """List of Pets"""
    pets = Pet.query.all()
    available_pets = [pet for pet in pets if pet.available]
    unavailable_pets = [pet for pet in pets if pet.available == False]

    return render_template("home.html", unavailable_pets=unavailable_pets, available_pets=available_pets)


@app.route('/pets/<int:id>')
def show_pet(id):
    """Show Pet details"""
    pet = Pet.query.get_or_404(id)
    return render_template("show_pet.html", pet=pet)


@app.route('/pets/add', methods=["GET", "POST"])
def add_pet():
    """Renders new pet form (GET) or handles pet form submission (POST)"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data
        if photo_url == "":
            pet = Pet(name=name, species=species,
                      notes=notes, available=available)
        else:
            pet = Pet(name=name, species=species, photo_url=photo_url,
                      notes=notes, available=available)

        db.session.add(pet)
        db.session.commit()

        flash(f"Added a new {species} named {name}!")
        return redirect('/')
    else:
        return render_template("pet_add_form.html", form=form)


@app.route('/pets/<int:id>/edit', methods=["GET", "POST"])
def edit_pet(id):
    """Renders edit pet form (GET) or handles pet form submission (POST)"""
    pet = Pet.query.get_or_404(id)
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        if form.photo_url.data != "":
            pet.photo_url = form.photo_url.data

        db.session.commit()

        return redirect('/')
    else:
        return render_template("pet_edit_form.html", pet=pet, form=form)
