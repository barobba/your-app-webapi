
from flask import Flask, jsonify, request
from your_app.services.AccountDirectory import AccountDirectory
from your_app.services.AccountServices import AccountServices


app = Flask(__name__)

"""
Web API requests:

    OPERATION   METHOD  PATH                    BODY
    ------------------------------------------------------------------------------------------------
    Base        GET     /

    DIRECTORY:
    
    Create      POST    /account                { first: 'Kim', last: 'Brown', balance: 6543.21 }
    List        GET     /account        
    Retrieve    GET     /account/<id>
    Update      PATCH   /account/<id>           { first: 'Kim', last: 'Brown' }
    Delete      DELETE  /account/<id>

    SERVICES:
    
    Credit      POST    /account/<id>/credit    { amount: 234.56 }
    Debit       POST    /account/<id>/debit     { amount: 100 }
    Lock        POST    /account/<id>/lock
    Unlock      POST    /account/<id>/unlock

"""


@app.route('/')
def base_path():

    return 'Your Web API'


@app.route('/account', methods=['POST'])
def account_create():

    try:

        # Load your library
        directory = AccountDirectory()

        # Run your operations
        account = directory.create(**request.json)

        # Return result
        return jsonify(account.__dict__)

    except RuntimeError as error:
        return error, 500


@app.route('/account', methods=['GET'])
def account_readlist():

    try:

        # Load your library
        directory = AccountDirectory()

        # Run your operations
        account_list = directory.read_list()

        # Return result
        return jsonify([account.__dict__ for account in account_list])

    except RuntimeError as error:
        return error, 500


@app.route('/account/<account_id>', methods=['GET'])
def account_read(account_id):

    try:

        # Load your library
        directory = AccountDirectory()

        # Run your operations
        account = directory.read(account_id)

        # Return result
        return jsonify(account.__dict__)

    except RuntimeError as error:
        return error, 500


@app.route('/account/<account_id>', methods=['PUT'])
def account_update(account_id):
    raise NotImplementedError


@app.route('/account/<account_id>', methods=['DELETE'])
def account_delete(account_id):
    raise NotImplementedError


@app.route('/account/<account_id>/credit', methods=['POST'])
def account_credit(account_id):

    try:

        # Load your library
        directory = AccountDirectory()
        services = AccountServices()

        # Run your operations
        account = directory.read(account_id)
        services.credit(account, request.json['amount'])

    except RuntimeError as error:
        return error, 500


@app.route('/account/<account_id>/debit', methods=['POST'])
def account_debit(account_id):

    try:

        # Load your library
        directory = AccountDirectory()
        services = AccountServices()

        # Run your operations
        account = directory.read(account_id)
        services.debit(account, request.json['amount'])

    except RuntimeError as error:
        return error, 500


@app.route('/account/<account_id>/lock', methods=['POST'])
def account_lock(account_id):
    raise NotImplementedError


@app.route('/account/<account_id>/unlock', methods=['POST'])
def account_unlock(account_id):
    raise NotImplementedError


if __name__ == '__main__':

    app.run(host='127.0.0.1', debug=True)
