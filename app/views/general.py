from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort

mod = Blueprint('general', __name__)

@mod.route('/', methods=['GET'])
def login():
    return render_template('general/login.html', warning=request.args.get('warning', 'none'))

@mod.route('/dashboard', methods=['POST'])
def index():
    user = request.form.get('account')
    password = request.form.get('password')
    if user != '@dmin' and password != "P@ssword":
        return redirect(url_for("general.login", warning="block"))
    else:
        return render_template('general/index.html')
