import lib, chatvs
def make():
    d = lib.Deck('CV3','t', theme='C', sections=['A'])
    for k in ['attend','approve','remind','room','move','makeup','slipdb','retry']: chatvs.chat_vs(d, k, section='A')
    return d
