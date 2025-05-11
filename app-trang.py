from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return """
      <h3 style="color:green;">Trang</h3>
      <h2 style="color:red;">Salut les amis ! Ceci est un TP DevOps. CI/CD validé par TRang 🚀  !</h2>
    """
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

