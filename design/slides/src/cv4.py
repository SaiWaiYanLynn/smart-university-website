import lib, chatvs
def make():
    d = lib.Deck('CV4','t', theme='C', sections=['A'])
    for k in ['watch','advisor','cross','handoff','gap','conflict','query','blocked']: chatvs.chat_vs(d, k, section='A')
    return d
