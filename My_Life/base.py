import json

from django.core.exceptions import ImproperlyConfigured

with open('static/secrets.json') as f:
    secrets = json.loads(f.read())

    def get_secret(setting, secrets=secrets):
        try:
            return secrets[setting]
        except KeyError:
            error_msg = 'Set the {} environment variable'.format(setting)
            return ImproperlyConfigured(error_msg)