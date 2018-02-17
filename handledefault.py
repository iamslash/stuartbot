# -*- coding: utf-8 -*-

def probe(d_pkt):
    return True

def handle(d_pkt):
    import random
    l = [u'무엇을 원하시나요?',
         u'그렇군요.',
         u'열심히 공부해 주세요.',
         u'그래요',
         u'아니에요',
         u'별말씀을...',
         u'맘대로해요',
         u'믿거나 말거나']
    return random.choice(l)

if __name__ == "__main__":
    print(handle({}))
