from flask import Flask, render_template, request,redirect,url_for
app = Flask(__name__,template_folder='templates')

@app.route('/')#an app instance
def home():
    return render_template("index.html")

@app.route('/add_task',methods=['post'])
def create_task():
    task=request.form.get('task')
    task.append(task)
    return redirect(url_for('home'))

if __name__ == "__main__":#activating the debug mode
    app.run(debug=True)