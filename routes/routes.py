from controllers import user_control, pokemon_control, backpack_control, location_control
from apps import app, jwt_requerid
from flask import jsonify, request


@app.route('/auth/register', methods=["POST"])
def register():
    try:
        user = user_control.create_user(request.form.get('username'), request.form.get(
            'email'), request.form.get('password'))
        user_control.insert(user)
        token = user_control.create_token(user)
        return jsonify({'token': token, 'id': user.id}), 201
    except:
        return jsonify({'failed': 'create user'}), 403


@app.route('/user/<int:id>', methods=['PUT', 'GET'])
@jwt_requerid
def _user(current_user, id):
    if request.method == 'GET':
        try:
            return jsonify(user_control.return_user(id)), 200
        except:
            return jsonify({'error': 'not found'}), 404

    elif request.method == 'PUT':
        try:
            new_data = user_control.create_user(request.form.get(
                'username'), request.form.get('email'), request.form.get('password'))
            user_control.update(new_data, id)
            return jsonify(), 200
        except:
            return jsonify({'error': 'not found'}), 404


@app.route('/auth/login', methods=["POST"])
def login():
    try:
        user = user_control.return_object(username=request.form.get('username'))
    except:
        try:
            user = user_control.return_object(email=request.form.get('email'))
        except:
            return jsonify({'error': 'your credentials are wrong!'}), 403

    if not user.verify_password(request.form.get('password')):
        return jsonify({'error': 'your credentials are wrong!'}), 403

    token = user_control.create_token(user)

    return jsonify({'token': token, 'id': user.id}), 200


@app.route('/backpack')
@jwt_requerid
def backpack(current_user):
    try:
        user_backpack = backpack_control.get_backpack(current_user)
        count = pokemon_control.count()
        unsighted_amount = count - (user_backpack[1] + user_backpack[2])
        return jsonify({'pokemon_amount': count, 'pokemon': user_backpack[0], 'captured_amount': user_backpack[1], 
        'sighted_amount': user_backpack[2], 'unsighted_amount': unsighted_amount}), 200
    except:
        return jsonify({'error': 'unauthorized access'}), 403


@app.route('/sorted/<int:id>/')
@jwt_requerid
def random_pokemon(current_user, id):
    try:
        return jsonify(pokemon_control.sorted_pokemon(current_user, id)), 200
    except:
        return jsonify({'error': 'not found'}), 404


@app.route('/attempt-capture/<int:id>/')
@jwt_requerid
def attempt_capture(current_user, id):
    backpack_control.sighted(current_user, id)
    if pokemon_control.attempt_capture(id):
        backpack_control.capture_for_current_backpack(current_user, id)
        return jsonify(), 200
    return jsonify({'capture': 'failed'}), 404


@app.route('/backpack/pokemon/<int:id>', methods=['PUT'])
@jwt_requerid
def backpack_pokemon(current_user, id):
    if backpack_control.auth_nickname(current_user, id, request.form.get('nickname')):
        return jsonify(), 200
    return jsonify({'error': 'not found'}), 404


@app.route('/pokemon/<int:id>/', methods=['GET'])
@jwt_requerid
def pokemon(current_user, id):
    try:
        return jsonify(pokemon_control.search_pokemon(id)), 200
    except:
        return jsonify({'error': 'not found'}), 404


@app.route('/locations/', methods=['GET'])
@jwt_requerid
def locations(current_user):
    try:
        return jsonify(location_control.get_all_locations()), 200
    except:
        return jsonify({'error': 'not found'}), 404
