# -*- coding: utf-8 -*-

from slacker import Slacker
import os

def serveforever(apikey):
    if (apikey == ''):
        print('APIKEY_SLACK is empty. source setapikey.sh...')
        return
    
    import time, pprint
    from slackclient import SlackClient
    sc = SlackClient(apikey)
    
    def handle(a_channel):
        if a_channel == None:
            return
        print('...')
        import random
        ANS = [u'응',u'알았어',u'그래',u'아니야',u'그럼 안돼',u'맘대로해',u'믿거나 말거나']
        a_text = ANS[random.randrange(0, len(ANS))]
        sc.api_call(
            "chat.postMessage",
            channel=a_channel,
            text=a_text
        )
        
    def parse(l):
        # import pdb; pdb.set_trace()
        if l is None or len(l) is 0:
            return None
        pprint.pprint(l)
        for d in l:
            if 'channel' in d and 'text' in d and 'user' in d:
                if d['user'] is not 'awesomeboy':
                    return d['channel']
        return None

    if sc.rtm_connect(with_team_state=False):
        while True:
            pkt = sc.rtm_read()
            if pkt == None:
                time.sleep(10)
            else:
                handle(parse(pkt))
                time.sleep(1)
    else:
        print("Connection Failed")
        
if __name__ == "__main__":
    apikey = os.getenv('APIKEY_SLACK', '')
    serveforever(apikey)
