# -*- coding: utf-8 -*-

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os

g_l_handles = []

def serveforever(apikey):
    if (apikey == ''):
        print('ERROR: APIKEY_TELE is empty. your need to copy setapikey.sh ')
        print('       from setapikey.sh.sample then')
        print('       source setapikey.sh')
        return
    
    import time, pprint
    
    def handletext(bot, update):
        global g_l_handles
        
        print(update.message)
        d_pkt = {'text': update.message.text}
        a_text    = ''
        # import pdb; pdb.set_trace()
        # probe and apply right handle
        for mhandle in g_l_handles:
            if mhandle.probe(d_pkt):
                a_text = mhandle.handle(d_pkt)
                break
        if not a_text:
            import handledefault
            a_text = handledefault.handle(d_pkt)

        # post message
        update.message.reply_text(a_text)

    updater = Updater(apikey)
    mh = MessageHandler(Filters.text, handletext)
    updater.dispatcher.add_handler(mh)

    # help_handler = CommandHandler('help', help_command)
    # updater.dispatcher.add_handler(help_handler)

    # photo_handler = MessageHandler(Filters.photo, get_photo)
    # updater.dispatcher.add_handler(photo_handler)

    # file_handler = MessageHandler(Filters.document, get_file)
    # updater.dispatcher.add_handler(file_handler)

    updater.start_polling(timeout=3, clean=True)
    updater.idle()

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
    apikey = os.getenv('APIKEY_TELE', '')
    reghandle()
    serveforever(apikey)
