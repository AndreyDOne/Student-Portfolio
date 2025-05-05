from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
app = Flask(__name__)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_port"
)

cursor = db.cursor()

@app.route('/')
def home():
    cursor = db.cursor(dictionary=True)  
    
    cursor.execute("SELECT * FROM student_info")
    students = cursor.fetchall()
    
    return render_template('home.html', students =students)

@app.route('/about/<int:student_id>') 
def about(student_id):
    
    cursor = db.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM student_info WHERE id = %s", (student_id,))
    student = cursor.fetchone()
    
    return render_template('about.html', student=student)

@app.route('/projects/<int:student_id>')
def project(student_id):
    
    cursor = db.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM student_info WHERE id = %s", (student_id,))
    student = cursor.fetchone()
    
    cursor.execute("SELECT * FROM projects WHERE student_id = %s", (student['student_id'],))
    projects = cursor.fetchall()
    
    print(f"Projects: {projects}")

    return render_template('project.html', projects=projects, student=student)


if __name__ == '__main__':
    app.run(debug=True)