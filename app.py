from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def api():
    key = request.args.get("key")
    num = request.args.get("num")

    if key != "demo-testing":
        return jsonify({
            "status": "error",
            "message": "Invalid API key"
        })

    if not num or not num.isdigit() or len(num) != 10:
        return jsonify({
            "status": "error",
            "message": "Invalid mobile number"
        })

    return jsonify({
        "status": "success",
        "number": num,
        "country": "India",
        "operator": "Demo Telecom",
        "api_by": "Soumyadip Sahoo"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
