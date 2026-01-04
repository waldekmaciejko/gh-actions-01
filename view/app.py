from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!"


@app.route('/secret/<ps>')
def secret(ps):
    
    if ps == 'agent123':
        return "Ok!"
    else:
        return "Access Denied"
    

if __name__ == '__main__':
    app.run(debug=True)