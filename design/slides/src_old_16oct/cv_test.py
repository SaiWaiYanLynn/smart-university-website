import lib, chatvs
def make():
    d = lib.Deck('CV_Test','cv test')
    for k in chatvs.SCEN: chatvs.chat_vs(d, k)
    return d
