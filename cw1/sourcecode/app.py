from flask import Flask, render_template
from flask import Flask, request
from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def root():  
    return render_template('index.html')


@app.route ('/stars/sun/')
def sun():
    return render_template('/stars/sun.html')

@app.route('/planets/mercury/')
def mercury():
    return render_template('/planets/mercury.html')

@app.route('/moons/moon.html/')
def moon():
    return render_template('/moons/moon.html')

@app.route("/moonlist/", methods=['POST','GET'])
def moonlist():
	if request.method == 'GET':
	   return render_template ('moonlist.html')

@app.route("/planetlist/", methods=['POST','GET'])
def planetlist():
        if request.method == 'GET':
           return render_template ('planetlist.html')

@app.errorhandler(404)
def page_not_found(error):
    return "Couldn't find the page you requested or page may not exist, please check the URL in  address bar and try again.", 404

@app.errorhandler(403)
def forbidden(error):
    return "You do not have permission to access this resource, contact system administator for access rights", 403

@app.errorhandler(500)
def Internal_Server_Error(error):
    return "There has been an internal error, please try again", 500

@app.errorhandler(503)
def Service_Unavailable(error):
    return "Web server unavailable, please contact system administrator", 503

@app.errorhandler(504)
def Gateway_Timeout(error):
    return "Gateway has timed out, possible DNS error, please try again.", 504

@app.route("/themoon")
def themoon_redirect():
	return redirect("http://set09103.napier.ac.uk:9135/moons/moon.html/")

@app.route("/thesun")
def thesun_redirect():
        return redirect("http://set09103.napier.ac.uk:9135/stars/sun.html/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
