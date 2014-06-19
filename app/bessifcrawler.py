from flask import Flask, jsonify
from flask import request
import scrap_bessif_launcher

from datetime import timedelta
from flask import make_response, current_app
from functools import update_wrapper

import pdb

app = Flask(__name__)

@app.route('/patentapi')
def index():
	return 'Finally api!'

@app.route('/patentapi/test')
def test():
	return 'test api!'

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


@app.route('/patentapi/crawl', methods=['POST'])
@crossdomain(origin='*')
def crawl():
    keywords = str(request.form['keywords']).split()
    export_config = str(request.form['export_config'])
    mail_addr= str(request.form['mail_to'])
    databases = str(request.form['databases'])
    base= str(request.form['base'])
    scrap_bessif_launcher.Scrap(mail_addr,export_config,keywords,databases, base )
    return "Mail send - scraped data "

@app.route('/patentapi/export', methods=['POST'])
@crossdomain(origin='*')
def export():
    export_config = str(request.form['args'])
    mail = str(request.form['mail'])
    print export_config
    print mail
    base= str(request.form['base'])
    scrap_bessif_launcher.GetGlobalDatabase(export_config,mail, base)
    return "Mail send - simple export"

@app.route('/patentapi/number', methods=['POST'])
@crossdomain(origin='*')
def getnumber():
    keywords = str(request.form['keywords']).split()
    return jsonify(count=scrap_bessif_launcher.GetNumber(keywords))

@app.route('/patentapi/keyword', methods=['POST'])
@crossdomain(origin='*')
def getKeyword():
    base= str(request.form['base'])
    keywords=scrap_bessif_launcher.GetKeywordsFromGlobalDatabase(base)
    return jsonify(key=keywords)

@app.route('/patentapi/base', methods=['GET'])
@crossdomain(origin='*')
def GetBases():
	all_bases= scrap_bessif_launcher.GetListBases()
	return jsonify(key=all_bases)

if __name__ == '__main__':
	app.run()
