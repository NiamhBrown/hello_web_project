import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
pre_defined_names = ['Julia', 'Alice', 'Karim']
@app.route('/names', methods=['GET'])
def add_name():
    # new_name = request.args.get('add','')
    new_names = request.args.get('add', '').split(',')
    print(f'new names={new_names}')
    new_names = [name.strip() for name in new_names if name.strip()]

    if new_names:
        for name in new_names:
            print(f"pre_defined_names={pre_defined_names}")
            pre_defined_names.append(name)
            print(f"pre_defined_names={pre_defined_names}")
        sorted_pre_defined_names= sorted(pre_defined_names)
        names_string = ', '.join(sorted_pre_defined_names)
        print(f"names_string={names_string}")
        return names_string
    else:
        return 'Please enter a name to add.', 400


# == Example Code Below ==
# @app.route('/count_vowels', methods=['POST'])
# def count_vowels():
#     text = request.form['text']
#     vowel_count = sum(1 for char in text if char.lower() in 'aeiou')
#     return f'There are {vowel_count} vowels in "{text}"'

# @app.route('/hello', methods=['GET'])
# def hello():
#     name = request.args['name'] # The value is 'David'

#     # Send back a friendly greeting with the name
#     return f"Hello {name}!"

# To make a request, run:
# curl "http://localhost:5000/hello?name=David"

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

