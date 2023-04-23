import os
from flask import Flask, jsonify, request, render_template
import cogtran

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    print('serve path!!!')
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return app.send_static_file(path)
    else:
        return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    print('analyzing!!')
    url = request.form["url"]
    text = cogtran.extract_text(url)
    result = cogtran.analyze_article(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
