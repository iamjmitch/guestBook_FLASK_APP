from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

class GuestBookEntry:
    def __init__(self, name, comment):
        self.name = name
        self.comment = comment

guestbook = []

@main.route('/')
def index():
    return render_template('index.html', guestbook=guestbook)


@main.route('/sign')
def sign():
    return render_template('sign.html')

@main.route('/sign', methods=['POST'])
def sign_post():
    name = request.form.get('name')
    comment = request.form.get('comment')
    new_comment = GuestBookEntry(name, comment)
    guestbook.append(new_comment)
    
    
    return redirect(url_for('main.index'))
