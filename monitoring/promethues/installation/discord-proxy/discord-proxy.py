# this code is a little bit buggy, you can use this one instead : https://github.com/arezoomohammadi22/DevOPs-Engineering/blob/main/Prometheus/Alert-manager/discord-proxy-webhook/discord-webhook.py

from flask import Flask, request, jsonify
import requests
import os
import json

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "PUT-YOUR-WEBHOOK-HERE"

@app.route("/webhook", methods=["POST"])
def webhook():
        # Print a message at the very beginning of the function
    print("LOG: Webhook endpoint was hit!")

    try:
        data = request.json
        print(f"LOG: Received data: {json.dumps(data, indent=2)}") # Log the full JSON payload
    except Exception as e:
        print(f"LOG: Error parsing JSON: {e}")
        return jsonify({"error": "Invalid data"}), 400

    if not data or "alerts" not in data:
        print("LOG: No alerts found in payload.")
        return jsonify({"error": "Invalid data"}), 400
    data = request.json
    if not data or "alerts" not in data:
        return jsonify({"error": "Invalid data"}), 400

    messages = []
    for alert in data["alerts"]:
        status = alert["status"].upper()  # "firing" or "resolved"
        color = "🟢 RESOLVED" if status == "RESOLVED" else "🔴 FIRING"

        message = f"**🔥 ALERT {color} 🔥**\n"
        message += f"**🚨 Alert Name:** {alert['labels'].get('alertname', 'N/A')}\n"
        message += f"**📍 Instance:** {alert['labels'].get('instance', 'N/A')}\n"
        message += f"**📝 Description:** {alert['annotations'].get('summary', 'No description')}\n"
        message += f"**⏰ Starts At:** {alert.get('startsAt', 'Unknown')}\n"

        if status == "RESOLVED":
            message += f"✅ **Alert Resolved** at {alert.get('endsAt', 'Unknown')}\n"

        messages.append(message)

    payload = {"content": "\n\n".join(messages)}
    print(f"LOG: Sending payload to Discord: {json.dumps(payload)}")
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
    print(f"LOG: Received response from Discord: Status={response.status_code}, Body={response.text}")

    if response.status_code != 204:
        return jsonify({"error": "Failed to send message", "discord_response": response.text}), response.status_code

    return jsonify({"success": True}), 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
