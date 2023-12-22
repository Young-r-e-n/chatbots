# from flask import Flask, request
# from twilio.rest import Client
# from twilio.twiml.messaging_response import MessagingResponse

# # Twilio credentials
# account_sid = "AC197451b9baabdde750f466174bc0c2ad"
# auth_token = "e1b023cdf6bcce8d00f8a81ff3a9a6f2"
# client = Client(account_sid, auth_token)

# # Flask app
# app = Flask(__name__)

# @app.route("/webhook", methods=["POST"])
# def webhook():
#     incoming_message = request.values.get("Body", "").lower()
#     resp = MessagingResponse()
#     msg = resp.message()

#     # Implement your bot's logic here
#     response = generate_response(incoming_message)

#     # Generate response
#     msg.body(response)

#     return str(resp)

# def generate_response(message):
#     # Implement your logic to generate appropriate responses here
#     # You can use conditionals, APIs, or databases as needed

#     response = "Thank you for your message. We will get back to you shortly."
#     return response

# if __name__ == "__main__":
#     app.run()

