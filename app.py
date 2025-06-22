from flask import Flask, render_template, request
from converter.logic import convert_to_test_case

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    test_case = ""
    if request.method == "POST":
        user_story = request.form.get("user_story", "")
        test_case = convert_to_test_case(user_story)
    return render_template("index.html", test_case=test_case)

if __name__ == "__main__":
    app.run(debug=True)