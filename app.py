from flask import Flask,request, url_for, redirect, render_template
import pickle

app = Flask(__name__)

# model=pickle.load(open('model.pkl','rb'))


@app.route("/", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:
            image = request.files["image"]
            image.save("uploaded_image." + image.filename.split('.')[-1])

            return redirect(request.url)


    return render_template("add_image_file.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
