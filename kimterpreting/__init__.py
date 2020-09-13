from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f85ad43eacb9177969e56c73270c5907298c64e6ab96c74a9d7c8f3a264b7f3a'

from kimterpreting import routes