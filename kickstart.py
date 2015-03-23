from flask import Flask, render_template
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

    random_hostname = '%s-%s' % (random.choice(adjective), random.choice(name))
    return render_template('kickstart.ks', random_hostname=random_hostname)


if __name__ == '__main__':
    app.run(debug=True)
