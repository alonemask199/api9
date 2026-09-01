from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/send")
def send():
    phone = request.args.get("phone")
    if not phone:
        return jsonify({"error": "phone required"}), 400

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://weblogin.grameenphone.com",
        "Referer": "https://weblogin.grameenphone.com/",
        "User-Agent": "Mozilla/5.0",
        # "X-XSRF-TOKEN": "<your-token>"
    }

    # cookies = {
    #     "XSRF-TOKEN": "<your-token>",
    #     "laravel_session": "<your-session>"
    # }

    payload = {"msisdn": phone}

    try:
        r = requests.post(
            "https://weblogin.grameenphone.com/backend/api/v1/otp",
            headers=headers,
            json=payload,
            timeout=15,
            # cookies=cookies
        )
        return jsonify({
            "status_code": r.status_code,
            "response": r.text
        }), r.status_code
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
