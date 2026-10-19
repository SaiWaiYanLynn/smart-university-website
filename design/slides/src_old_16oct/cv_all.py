import lib, chatvs
def make():
    d = lib.Deck('CV_All','cv all')
    for k in ['visa','room','transcript','slip','record','memory','makeup']: chatvs.chat_vs(d, k)
    for k in chatvs.STAFF: chatvs.chat_vs(d, k, over='Staff and instructors')
    return d
