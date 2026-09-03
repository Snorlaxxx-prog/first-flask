from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = [
    {
        "id": 1001,
        "name": "Juan Dela Cruz",
        "course": "BSIT",
        "age": 20
    },
    {
        "id": 1002,
        "name": "Maria Santos",
        "course": "BSCS",
        "age": 19
    }
]


# HOME
@app.route("/")
def index():
    return render_template("index.html")


# ADD STUDENT
@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        student_id = int(request.form["id"])
        name = request.form["name"]
        course = request.form["course"]
        age = int(request.form["age"])

        new_student = {
            "id": student_id,
            "name": name,
            "course": course,
            "age": age
        }

        students.append(new_student)

        return redirect(url_for("index"))

    return render_template("add_student.html")


# SEARCH STUDENT
@app.route("/search", methods=["GET", "POST"])
def search_student():

    student = None

    if request.method == "POST":

        student_id = int(request.form["id"])

        for s in students:

            if s["id"] == student_id:
                student = s
                break

    return render_template(
        "search_student.html",
        student=student
    )


# REMOVE STUDENT
@app.route("/remove", methods=["GET", "POST"])
def remove_student():

    message = ""

    if request.method == "POST":

        student_id = int(request.form["id"])

        for student in students:

            if student["id"] == student_id:

                students.remove(student)

                message = "Student successfully removed."

                break

        else:
            message = "Student not found."

    return render_template(
        "remove_student.html",
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)