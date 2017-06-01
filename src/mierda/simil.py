'''
Created on 31/05/2017

@author: ernesto
'''
import logging
import sys

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

kaka = 0

class NodoMierda:
    def __init__(self, iave):
        self.iave = iave
        self.intervalo_inicio = iave - kaka
        if(self.intervalo_inicio <= 0):
            self.intervalo_inicio = 1
        self.intervalo_fin = iave + kaka
        self.simios = 0
        self.otros_pendejos = []
    def __str__(self):
        return "iave %u, otros pendejos %s, intervalo %u-%u" % (self.iave, self.otros_pendejos, self.intervalo_inicio, self.intervalo_fin)
    
    def __repr__(self):
        return self.__str__()

def mierda_simil_bit_ch_modifica(shits, inter_ini, inter_fin, valor):
    shits_tam = len(shits)
    logger_cagada.debug("el ini %u el fin %u el tam %u" % (inter_ini, inter_fin, shits_tam))
    
    idx = inter_ini
    while(idx < shits_tam):
        shits[idx] += valor
        idx += (idx & (-idx))
        logger_cagada.debug("el puto idx %u" % idx)
        
    idx = inter_fin + 1
    while(idx < shits_tam):
        shits[idx] -= valor
        idx += (idx & (-idx))
        
def mierda_simil_bit_ch_consulta_puto(shits, idx_query):
    idx = idx_query
    resu = 0
    while(idx > 0):
        resu += shits[idx]
        idx -= (idx & (-idx))
    
    return resu

def mierda_simil_dfs(raiz, nodos):
    cacas = []
    ia_visitados = set()
    simios_totales = 0
    
    bit_ch_array = [0] * (len(nodos.keys()) + 2)
    
    cacas.append(raiz)
    
    while(cacas):
        caca_actual = cacas.pop()
        if(caca_actual.iave in ia_visitados):
            logger_cagada.debug("ia c visitaron todos los ijos de perra %s" % caca_actual)
            mierda_simil_bit_ch_modifica(bit_ch_array, caca_actual.intervalo_inicio, caca_actual.intervalo_fin, -1)
        else:
            caca_actual.simios = mierda_simil_bit_ch_consulta_puto(bit_ch_array, caca_actual.iave)
            simios_totales += caca_actual.simios
            logger_cagada.debug("el nodo %u tiene %u simios", caca_actual.iave, caca_actual.simios)
            llaves_chidoris = sorted(caca_actual.otros_pendejos, reverse=True)
            cacas += ([caca_actual] + list(map(lambda x: nodos[x], llaves_chidoris)))
            ia_visitados.add(caca_actual.iave)
            mierda_simil_bit_ch_modifica(bit_ch_array, caca_actual.intervalo_inicio, caca_actual.intervalo_fin, 1)
    
    return simios_totales


def mierda_simil_core(raiz, nodos):
    logger_cagada.debug("la raiz %s, los nodos %s la kaka %u" % (raiz, nodos, kaka))
    
    asshit = mierda_simil_dfs(raiz, nodos)
    print(asshit)
    
def mierda_simil_main():
    lineas = list(sys.stdin)
    
    num_nodos, asshole = [int(x) for x in lineas[0].strip().split(" ")]
    nodos = {}
    ensartados = set()
    
    global kaka
    kaka = asshole
    
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
