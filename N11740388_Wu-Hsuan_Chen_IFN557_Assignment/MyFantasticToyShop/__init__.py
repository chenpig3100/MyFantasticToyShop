from flask import Flask, render_template

app=Flask(__name__)
def create_app():
    
    app.debug=True

    from . import views
    app.register_blueprint(views.bp)

    return app

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html")