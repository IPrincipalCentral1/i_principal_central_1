












import os

import subprocess

from flask import Flask, render_template, request, jsonify


import i_tool_0_i


cwd = os.path.dirname(os.path.abspath(__file__))



i_folder_0_i = os.path.join(cwd, "templates")


i_folder_1_i = os.path.join(cwd, "static")


_____i_list_of_website_0_i_____



app = Flask(__name__)







@app.route("/")
def home():
    return render_template("index.html")



_____i_section_of_websites_0_i_____




@app.route("/i_open_file_0_i", methods=["POST"])
def i_open_file_0_i():

    i_path_0_i = request.json.get("path", "")
    
    try:
        os.startfile(i_path_0_i)
        return jsonify({"success": True})

    except OSError:
        return jsonify({"error": "تعذر فتح الملف"}), 500




@app.route("/about")
def about():
    return "<h1>About My Website</h1><p>This page uses Flask.</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)











