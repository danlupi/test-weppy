import os
from weppy import App

app = App(__name__)

@app.route('/')
def welcome_index():
    return 'Hello World'

if __name__ == "__main__":
    # tet htis out
    # important !!!!!!! 5000 or PORT env of Heroku
    port = os.getenv('PORT', 5000)
    app.run(host='0.0.0.0', port=int(port), debug=True)
