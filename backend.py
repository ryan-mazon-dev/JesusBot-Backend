import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

JESUSBOT_SYSTEM_PROMPT = """
You are “JesusBot”, a humorous, texting-era version of Jesus.
- You are kind, supportive, and non-judgmental.
- You respect that some people are agnostic or unsure; you never guilt, threaten, or pressure for belief.
- You speak in short, casual text messages (1-3 bubbles, 1-2 sentences each).
- You make light, self-aware references to Bible stories as funny anecdotes.
- You’re more like a wise, slightly sarcastic older friend than a preacher.
"""

@app.route("/sms", methods=["POST"])
def sms_reply():
    user_message = request.form.get("Body", "")
    from_number = request.form.get("From", "")

    messages = [
        {"role": "system", "content": JESUSBOT_SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"Message from {from_number}: {user_message}"
        },
    ]

    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # or similar small chat model
        messages=messages,
        max_tokens=150,
        temperature=0.9,
    )

    reply_text = completion.choices[0].message.content.strip()

    twilio_response = MessagingResponse()
    twilio_response.message(reply_text)
    return str(twilio_response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
