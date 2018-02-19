# -*- coding: utf-8 -*-

# how to run:
# 
# python robin.py --host=0.0.0.0 --port=29121

from flask import Flask
from flask import request, url_for
app = Flask(__name__)
import requests
import click
import pprint
import json
import glob
import os

g_l_handles = []
g_srvurl_jandi = os.getenv('SRVURL_JANDI', '')

def postit(v_body):
    """request HTTP POST."""
    hdr = {'Accept': 'application/vnd.tosslab.jandi-v2+json',
           'Content-Type': 'application/json'}
    
    url = g_srvurl_jandi
    msg = {
        "body" : v_body,
        "connectColor" : "#FAC11B",
    }
    r = requests.post(url, data = json.dumps(msg), headers = hdr)

@app.route("/jandi", methods=['GET', 'POST'])
def jandi():
    def handle(d_pkt):
        global g_l_handles
        a_text    = ''

        # probe and apply right handle
        for mhandle in g_l_handles:
            if mhandle.probe(d_pkt):
                a_text = mhandle.handle(d_pkt)
                break
        if not a_text:
            import handledefault
            a_text = handledefault.handle(d_pkt)

        # post message
        postit(a_text)
        # print(d_pkt)
        
    # import pdb; pdb.set_trace()
    handle({'text': json.loads(request.data)['text'].strip()})
    return ''

def reghandle():
    global g_l_handles

    import glob
    l = glob.glob('handle*.py')

    for m in l:
        mname = m.replace('.py', '').strip()
        if mname.endswith('default'):
            continue
        mhandle = __import__(mname)
        g_l_handles.append(mhandle)

@click.command()
@click.option('--host', default='0.0.0.0', help='ip address.')
@click.option('--port', default=29121, help='ip port.')
@click.option('--debug', default=True, help='debug mode.')
def serveforever(host, port, debug):
    if (g_srvurl_jandi == ''):
        print('ERROR: SRVURL_JANDI is empty. your need to copy setapikey.sh ')
        print('       from setapikey.sh.sample then')
        print('       source setapikey.sh')
        return
    
    reghandle()
    # run flask
    app.run(host=host, port=port, debug=debug)
        
if __name__ == "__main__":
    serveforever()
