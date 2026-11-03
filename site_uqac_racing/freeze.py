from flask_frozen import Freezer
from interface import app

app.config["FREEZER_DESTINATION"] = "build"
app.config["FREEZER_REDIRECT_POLICY"] = "ignore"
freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
    with open("build/_redirects", "w") as f:
        f.write("/ /acceuil.html 302\n")