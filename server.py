from flask import Flask, render_template, request, redirect, session
import secrets
from user import User

app = Flask(__name__)
# app.secret_key =


@app.route("/users")
def display_users():
    all_users = User.get_all()
    print(all_users)
    return render_template("read_all.html", all_users=all_users)


@app.route("/users/new")
def show_new_user_page():
    return render_template("create.html")


@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    new_user_id = User.create_user(data)
    print(f"New user ID is {new_user_id}")
    return redirect(f"/users/{new_user_id}")


@app.route("/users/<int:user_id>")
def display_user(user_id):
    selected_user = User.get_user_by_id(user_id)
    return render_template("read_one.html", selected_user=selected_user)


@app.route("/users/<int:user_id>/edit")
def show_edit_page(user_id):
    # Should we store the below in session in display_user instead of recreating a class instance?
    prepopulated_user = User.get_user_by_id(user_id)
    return render_template("edit.html", prepopulated_user=prepopulated_user)


@app.route("/users/<int:user_id>/update_user", methods=["POST"])
def update_user(user_id):
    data = {
        "id": user_id,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    User.update_user(data)
    return redirect(f"/users/{user_id}")


@app.route("/users/<int:user_id>/delete_user")
def delete_user(user_id):
    User.delete_user(user_id)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5150")
