'''
Created on 31/05/2017

@author: ernesto
'''
import logging
import sys

nivel_log = logging.ERROR
nivel_log = logging.DEBUG
logger_cagada = None

class NodoMierda:
    def __init__(self, iave):
        self.iave = iave
        self.otros_pendejos = []
    def __str__(self):
        return "iave %u, otros pendejos %s" % (self.iave, self.otros_pendejos)
    
    def __repr__(self):
        return self.__str__()

def mierda_simil_dfs(raiz, nodos):
    cacas = []
    ia_visitados = set()
    
    cacas.append(raiz)
    
    while(cacas):
        caca_actual = cacas.pop()
        if(caca_actual.iave in ia_visitados):
            logger_cagada.debug("ia c visitaron todos los ijos de perra %s" % caca_actual)
        else:
            llaves_chidoris = sorted(caca_actual.otros_pendejos, reverse=True)
            cacas += ([caca_actual] + list(map(lambda x: nodos[x], llaves_chidoris)))
            ia_visitados.add(caca_actual.iave)


def mierda_simil_core(raiz, nodos):
    logger_cagada.debug("la raiz %s, los nodos %s" % (raiz, nodos))
    
    mierda_simil_dfs(raiz, nodos)
    
def mierda_simil_main():
    lineas = list(sys.stdin)
    
    num_nodos, asshole = [int(x) for x in lineas[0].strip().split(" ")]
    nodos = {}
    ensartados = set()
    
    logger_cagada.debug("nodos %u asshol %u" % (num_nodos, asshole))
    
    for linea in lineas[1:]:
        puto, caca = [int(x) for x in linea.strip().split(" ")]
        logger_cagada.debug("puto %u caca %u" % (puto, caca))
        nodos.setdefault(puto, NodoMierda(puto)).otros_pendejos.append(caca)
        if(caca not in nodos.keys()):
            nodos[caca] = NodoMierda(caca)
        ensartados.add(caca)
    
    padres = set(nodos.keys()) - ensartados
    assert len(padres) == 1, "la puta madre %s - %s %s" % (set(nodos.keys()), ensartados, padres)
    
    padre = list(padres)[0]
    logger_cagada.debug("raiz %s" % padre)
    mierda_simil_core(nodos[padre], nodos)
            

if __name__ == '__main__':
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)
    
    mierda_simil_main()
