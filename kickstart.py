from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def kickstart():

    adjective = [
        'sleepy',
        'dopey',
        'bashful',
        'grumpy',
        'sneezy',
        'sleepy',
        'happy',
        'doc'
    ]

    name = [
        'fozzie',
        'kermit',
        'rizzo',
        'beaker',
        'bunsen',
        'animal',
        'scooter',
        'piggy',
        'rowllf'
    ]

    return '%s_%s' % (random.choice(adjective), random.choice(name))


if __name__ == '__main__':
    app.run()
