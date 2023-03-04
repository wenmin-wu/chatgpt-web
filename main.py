import markdown2
import openai

from flask import Flask, request, render_template, redirect

server = Flask(__name__, static_url_path="/static")

messages = []

N = 20


def generate_response(prompt):
    global messages
    try:
        messages.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
        )
    except Exception as e:

        print(e)
        return e
    message = response["choices"][0]["message"]["content"]
    messages.append({"role": "system", "content": message})
    if len(messages) > N:
        messages = messages[-N:]
    return message


@server.route("/chat")
def home():
    return render_template("chat.html")


@server.route("/chat/get")
def get_bot_response():
    user_text = request.args.get("msg")
    return markdown2.markdown(
        str(generate_response(user_text)),
        extras=["fenced-code-blocks"] 
    )



if __name__ == "__main__":
    server.run(debug=False, host="0.0.0.0", port=8088)
