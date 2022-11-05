import requests

token = "xoxb-4296737263574-4320693496581-hCRlm9L6p9kyyxDtnzVG2i1p"
channel = "#doge_upbit"
text = "Slack Connect"

requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text})
