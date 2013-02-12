""" Rest endpoints
    
"""
import json

import bottle
import testapp

app = testapp.app #get app from myapp package.

@app.route('/backend')
@app.route('/backend/tryme') 
def trymeGet():
    return dict(result='success')

