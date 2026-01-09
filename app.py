from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------------- DATABASE ----------------
def get_db():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db()
conn.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course TEXT,
    email TEXT
)
""")
conn.close()

# ---------------- HOME ----------------
@app.route("/")
def index():
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("index.html", students=students)

# ---------------- ADD ----------------
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        email = request.form["email"]

        conn = get_db()
        conn.execute(
            "INSERT INTO students(name,course,email) VALUES (?,?,?)",
            (name, course, email)
        )
        conn.commit()
        conn.close()
        return redirect("/")
    
    return render_template("add.html")

# ---------------- DELETE ----------------
@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

# ---------------- EDIT ----------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db()

    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        email = request.form["email"]

        conn.execute(
            "UPDATE students SET name=?, course=?, email=? WHERE id=?",
            (name, course, email, id)
        )
        conn.commit()
        conn.close()
        return redirect("/")

    student = conn.execute(
        "SELECT * FROM students WHERE id=?",
        (id,)
    ).fetchone()
    conn.close()

    return render_template("edit.html", student=student)

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
