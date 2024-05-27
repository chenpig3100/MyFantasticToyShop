from flask import Blueprint, render_template, url_for
from .models import Toy

# This data will eventually be stored in a database
HelloKitty = Toy('1', 'HelloKitty.jpg', 'HelloKitty', '$10', 'plushi','This adorable Hello Kitty plushie features soft, cuddly fabric and a cute pink bow. With her friendly smile, she is perfect for hugs, decoration, and gifting to Hello Kitty fans of all ages.')
IronMan = Toy('2', 'ironMan.jpg', 'IronMan', '$100', 'collection', 'The Iron Man collection celebrates Tony Stark&acute;s journey from genius inventor to iconic hero, featuring his legendary suits, groundbreaking technology, and epic battles that define the Marvel Cinematic Universe.')
toys = [HelloKitty, IronMan]

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', toys = toys)