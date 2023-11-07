import requests
import json
web_hook_url = 'https://hooks.slack.com/services/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'
slack_msg ={'text':'i got you buddy'}
requests.post(web_hook_url, data=json.dumps(slack_msg))