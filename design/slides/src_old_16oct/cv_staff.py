import lib, chatvs
def make():
    d = lib.Deck('CV_Staff','cv staff')
    for k in chatvs.STAFF: chatvs.chat_vs(d, k, over='Staff and instructors')
    return d
