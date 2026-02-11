from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------------- DB Connection ----------------
def get_db():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- Create Table ----------------
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

# ---------------- Home Page ----------------
@app.route("/")
def index():
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("index.html", students=students)

# ---------------- Add Student ----------------
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    course = request.form["course"]
    email = request.form["email"]

    conn = get_db()
    conn.execute(
        "INSERT INTO students(name, course, email) VALUES (?, ?, ?)",
        (name, course, email)
    )
    conn.commit()
    conn.close()
    return redirect("/")

# ---------------- Delete Student ----------------
@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

# ---------------- Edit Page ----------------
@app.route("/edit/<int:id>")
def edit(id):
    conn = get_db()
    student = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("edit.html", student=student)

# ---------------- Update Student ----------------
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    course = request.form["course"]
    email = request.form["email"]

    conn = get_db()
    conn.execute("""
        UPDATE students 
        SET name=?, course=?, email=? 
        WHERE id=?
    """, (name, course, email, id))
    conn.commit()
    conn.close()
    return redirect("/")

# ---------------- Run App ----------------
if __name__ == "__main__":
    app.run(debug=True)
