import lib, chatvs
def make():
    d = lib.Deck('CV_T2','t', theme='B', sections=['Gap','Student','Staff','Plan'])
    for k in ['visa','slipdb','remind','record']: chatvs.chat_vs(d, k, section='Student')
    return d
