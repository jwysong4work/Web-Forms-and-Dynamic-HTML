from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

user_inputs = []

@app.route('/', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        first_name = request.form['FirstName']
        last_name = request.form['LastName']
        jersey_no = int(request.form['JerseyNo'])
        position = request.form['Position']

        user_data = {
            'FirstName': first_name,
            'LastName': last_name,
            'JerseyNo': jersey_no,
            'Position': position
        }

        user_inputs.append(user_data)

        return redirect(url_for('display_players_table'))

    return render_template('input_form.html')

@app.route('/display_players_table')
def display_players_table():
    players = [
        {'FirstName': 'Riq', 'LastName': 'Woolen', 'JerseyNo': 27, 'Position': 'Cornerback'},
        {'FirstName': 'Quandre', 'LastName': 'Diggs', 'JerseyNo': 6, 'Position': 'Free Safety'}
    ]

    players.extend(user_inputs)

    return render_template('players_table.html', Players=players)

if __name__ == '__main__':
    app.run(port=8000, debug=True, host="0.0.0.0")
