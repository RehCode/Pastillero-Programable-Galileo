from bottle import Bottle, template, static_file

app = Bottle()

@app.route('/personas')
def personas():
    """Home page"""
    info = {'title': 'Welcome Home!',
            'names': ['John', 'Paul', 'George', 'Ringo']
            }
    return template('views/simple.tpl', info)

@app.route('/home')
@app.route('/')
def home():
    return template('index.tpl', variable='variable')

@app.route('/static/css/<filename>')
def server_static(filename):
    return static_file(filename, root='static/css/')

def main():
    app.run()

if __name__ == '__main__':
    main()
