from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return """
      <h3 style="color:Red;">Trang</h3>
      <h2 style="color:blue;">Salut les amis ! Ceci est un TP DevOps avec Flask, Git et Jenkins, réalisé par Trang. Apprendre à maîtriser CI/CD. 🚀 !</h2>
    """
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

