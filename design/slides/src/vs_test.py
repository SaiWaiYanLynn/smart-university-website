import lib, versus
def make():
    d = lib.Deck('VS_Test','vs test')
    for k in versus.SCEN: versus.versus(d, k)
    return d
