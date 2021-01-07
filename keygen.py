## This file defines the generation of API keys.

import secrets
from twilio.rest import Client

def generate_key():
	generated_key = secrets.token_urlsafe(12)
	return generated_key

def deliver_key(client, to, from_):
	key = generate_key()
	body = 'Your API key is {}'.format(key)
	message = client.messages.create(to=to, from_=from_, body=body)
	return message

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
