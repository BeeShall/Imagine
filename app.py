from flask import Flask, render_template,request,redirect
from flask_bootstrap import Bootstrap
import enchant #to check if the word entered is a valid english word

app=Flask(__name__)
tags_searched=[]
dictionary=enchant.Dict("en_US")
colors=[] #it will store the list of hex-color values
Bootstrap(app)

@app.route('/', methods=['POST','GET'])
def index():
	if request.method=='POST':
		tags_searched=[]
		user_input=request.form['user_tag']
		tags_searched=user_input.split(',') #split the text using ','
		valid_word=False #Flag to check if all the words entered by the user is valid
		current_word=''

		#check if the word entered by the user is valid
		for word in tags_searched:
			valid_word=dictionary.check(word)
			current_word=word
			if(valid_word==False):
				break

		if valid_word==True:
			message='Input Received'

		else:
			message=current_word+" does not have a valid meaning!"

		
		return render_template('form.html',message=message,valid_word=valid_word)

	return render_template('form.html',valid_word=False)
		

def color_hex_values(): #this functions returns a list of hexadecimal values for colors
	hex_values=[]
	colors=open('color_hex_values.csv')
	for values in colors:
		values=values.replace('\n',"")
		hex_values.append(values)
	return hex_values

if __name__=='__main__':
	app.run(debug=True, host='0.0.0.0')
