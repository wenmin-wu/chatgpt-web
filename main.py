import markdown2
import openai

from flask import Flask, request, render_template, redirect

server = Flask(__name__, static_url_path="/static")

N = 20

class Conversation:
    def __init__(self, prompt, num_of_round):
        self.prompt = prompt
        self.num_of_round = num_of_round
        self.messages = []
        self.messages.append({"role": "system", "content": self.prompt})

    def ask(self, question):
        try:
            self.messages.append({"role": "user", "content": question})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                temperature=0.5,
                max_tokens=2048,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
        except Exception as e:
            print(e)
            return e

        message = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": message})

        if len(self.messages) > self.num_of_round * 2 + 1:
            del self.messages[1:3]
        return message

        

converstation = Conversation(prompt="You are a helpful assistant.", num_of_round=10)

@server.route("/chat")
def home():
    return render_template("chat.html")


@server.route("/chat/get")
def get_bot_response():
    user_text = request.args.get("msg")
    return markdown2.markdown(
        str(converstation.ask(user_text)), extras=["fenced-code-blocks"]
    )


if __name__ == "__main__":
    server.run(debug=False, host="0.0.0.0", port=8088)
