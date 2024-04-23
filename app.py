from flask import Flask ,render_template

app=Flask(__name__)
@app.route('/')

def welcome():
    return render_template('index.html')
@app.route('/task')
def task ():
    return render_template ('task1.html')

if __name__=='__main__':
    app.run(debug=True)
