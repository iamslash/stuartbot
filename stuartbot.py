# -*- coding: utf-8 -*-

from slacker import Slacker
import os

g_l_handles = []

def serveforever(apikey):
    if (apikey == ''):
        print('ERROR: APIKEY_SLACK is empty. your need to copy setapikey.sh ')
        print('       from setapikey.sh.sample then')
        print('       source setapikey.sh')
        return
    
    import time, pprint
    from slackclient import SlackClient
    sc = SlackClient(apikey)
    
    def handle(l_pkts):
        def _handle(d_pkt):
            global g_l_handles
            a_channel = d_pkt['channel']
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
            sc.api_call(
                "chat.postMessage",
                channel=a_channel,
                text=a_text
            )
        
        for d_pkt in l_pkts:
            # hand shake packet
            if 'type' in d_pkt and d_pkt['type'] == 'hello':
                print(d_pkt)
                return
            if 'channel' in d_pkt and 'text' in d_pkt and 'user' in d_pkt:
                if d_pkt['user'] is not 'awesomeboy':
                    _handle(d_pkt)

    if sc.rtm_connect(with_team_state=False):
        while True:
            l_pkts = sc.rtm_read()
            if l_pkts == None or len(l_pkts) == 0:
                time.sleep(1)
            else:
                handle(l_pkts)
    else:
        print("Connection Failed")

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
    
if __name__ == "__main__":
    apikey = os.getenv('APIKEY_SLACK', '')
    reghandle()
    serveforever(apikey)
