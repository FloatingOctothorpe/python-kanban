#/usr/bin/env python

"""A simple Kanban board application using Flask and SQLLite"""

from flask import Flask, send_from_directory, request, abort
from flask.json import jsonify

from database import db
import cards

def setup_app(kanban_db):
    """Create a new instance of the flask app"""
    kanban_app = Flask(__name__)
    kanban_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban.db'
    kanban_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    kanban_app.config['kanban.columns'] = ['To Do', 'Doing', 'Done']
    kanban_db.init_app(kanban_app)
    kanban_app.app_context().push()
    kanban_db.create_all()
    return kanban_app

app = setup_app(db) # pylint: disable=invalid-name

@app.route('/')
def index():
    """Serve the main index page"""
    return send_from_directory('static', 'index.html')

@app.route('/static/<path:path>')
def static_file(path):
    """Serve files from the static directory"""
    return send_from_directory('static', path)

@app.route('/cards')
def get_cards():
    """Get an order list of cards"""
    return jsonify(cards.all_cards())

@app.route('/columns')
def get_columns():
    """Get all valid columns"""
    return jsonify(app.config.get('kanban.columns'))

@app.route('/card', methods=['POST'])
def create_card():
    """Create a new card"""

    # TODO: validation
    cards.create_card(
        text=request.form.get('text'),
        column=request.form.get('column', app.config.get('kanban.columns')[0]),
        color=request.form.get('color', None),
    )

    # TODO: handle errors
    return 'Success'

@app.route('/card/reorder', methods=["POST"])
def order_cards():
    """Reorder cards by moving a single card

    The JSON payload should have a 'card' and 'before' attributes where card is
    the card ID to move and before is the card id it should be moved in front
    of. For example:

      {
        "card": 3,
        "before": 5,
      }

    "before" may also be "all" or null to move the card to the beginning or end
    of the list.
    """

    if not request.is_json:
        abort(400)
    cards.order_cards(request.get_json())
    return 'Success'


@app.route('/card/<int:card_id>', methods=['PUT'])
def update_card(card_id):
    """Update an existing card, the JSON payload may be partial"""
    if not request.is_json:
        abort(400)

    # TODO: handle errors
    cards.update_card(card_id, request.get_json(), app.config.get('kanban.columns'))

    return 'Success'

@app.route('/card/<int:card_id>', methods=['DELETE'])
def delete_card(card_id):
    """Delete a card by ID"""

    # TODO: handle errors
    cards.delete_card(card_id)
    return 'Success'

if __name__ == '__main__':
    app.run(debug=True)
