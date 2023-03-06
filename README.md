# A ChatGPT Web App Based On OpenAI API
ChatGPT Web


![chat-screenshot](images/gpt-web-screenshot.png)

## Updates
### 2023-03-06

* Render markdown using JS lib
* Save chat history to `sessionStorage` to prevent loss after refreshing
* Fix some browser compatibility issue by rewriting some functions in highlightjs-badge.js with jQuery
* Shift + Enter (⇧+⏎) to newline in the chatbox

## Usage

* install dependecies with `pip install -r requirements.txt`
* visit https://platform.openai.com/account/api-keys to get/create your API KEY
* set env variable: `export OPENAI_API_KEY=<your_openai_key>`
* start server: `python main.py`
* visit http://127.0.0.1:8088/chat and enjoy!