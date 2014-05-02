from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'Finally running from inside the environment with a Flask app!'

@app.route('/scrap', methods=['POT'])
def scrap():
	keywords = request.form['keywords'].split()
	export_config = request.form['export_config'].split()
	#inventeur  demandeur  classificationinternationalle abregpour  mot_clef (k)
	mail_addr= request.form['mail_to']
	databases = request.form['databases'].split() # f pour espace.net.fr et w pour espace.net.world , faire comme pour export config 
	scrap_bessif_launcher.Scrap(mail_addr,export_config,keywords,databases)
	return 'test:)'

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)
