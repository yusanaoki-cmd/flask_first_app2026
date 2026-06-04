from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    print(request.method)
    if request.method == "GET":
        return """
        <form action="/login" method="POST">
            Password: <input type="text"><br>
            <input type="submit" value="Login">
        </form>
        """
    return "Logged in!"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
