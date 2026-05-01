from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(silent=True)

    # safety check
    if not data or "marks" not in data:
        return jsonify({"error": "No marks provided"}), 400

    marks = data.get("marks")

    # remove empty or invalid values
    clean_marks = []
    for m in marks:
        try:
            clean_marks.append(float(m))
        except:
            continue

    if len(clean_marks) == 0:
        return jsonify({"error": "Enter valid marks"}), 400

    total = sum(clean_marks)
    percentage = total / len(clean_marks)

    return jsonify({
        "total": total,
        "percentage": round(percentage, 2)
    })

# test route
@app.route("/test")
def test():
    return "Server is working ✅"

# Render config
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)