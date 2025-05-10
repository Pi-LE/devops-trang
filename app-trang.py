from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return (
        "Salut les amis ! Ceci est un TP DevOps avec Flask, Git et Jenkins, "
        "réalisé par Trang. Apprendre à maîtriser CI/CD. 🚀"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
