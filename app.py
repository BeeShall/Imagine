from flask import Flask, render_template,request,redirect
from flask_bootstrap import Bootstrap

app=Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['POST','GET'])
def index():
	if request.method=='POST':
		user_input=request.form['user_tag']
		return render_template('form.html',message='Input Received')

	return render_template('form.html')
		



if __name__=='__main__':
	app.run(debug=True)
