from MyFantasticToyShop import db, create_app
app = create_app()
ctx = app.app_context()
ctx.push()
db.create_all()
from MyFantasticToyShop.models import Toy, Category, Order, Order_detail

c1 = Category(id=1, name='plushie')
c2 = Category(id=2, name='collection')
c3 = Category(id=3, name='boardgame')
t1 = Toy(id=1, name='HelloKitty', image='HelloKitty.jpg', price=10, category_id=1, description='This adorable Hello Kitty plushie features soft, cuddly fabric and a cute pink bow. With her friendly smile, she''s perfect for hugs, decoration, and gifting to Hello Kitty fans of all ages.')
t2 = Toy(id=2, name='Chess', image='chess.jpg', price=15, category_id=3, description='Chess is a two-player strategic board game played on an 8x8 grid. Each player controls 16 pieces with unique moves, aiming to checkmate the opponent''s king, ensuring it cannot escape capture.')
t3 = Toy(id=3, name='Mario', image='Mario.jpg', price=20, category_id=2, description='The Mario collection features classic games starring Mario, a plumber on adventures to rescue Princess Peach from Bowser. Includes Super Mario Bros, Mario Kart, and more.')
t4 = Toy(id=4, name='IronMan', image='ironMan.jpg', price=100, category_id=2, description='The Iron Man collection includes comics, movies, and merchandise about Tony Stark, a genius billionaire in a high-tech suit fighting villains and protecting the world.')
t5 = Toy(id=5, name='Bear', image='bear.jpg', price=30, category_id=1, description='The bear plushie collection offers a variety of cute, soft teddy bears in different sizes and colors, perfect for cuddling, decorating spaces, or gifting to friends and family.')
