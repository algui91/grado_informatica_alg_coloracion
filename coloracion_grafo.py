# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Coloracion de grafos
"""

__author__ = """Alejandro Alcalde (algui91@gmail.com)"""

try:
        import matplotlib.pyplot as plt
except:
        raise

import networkx as nx
import argparse
import pprint
from random import random

def coloracion(grafo):
	"""Devuelve la lista minima de colores a usar"""
	nodosSinColorear = grafo.nodes()
	colores = []
	colorActual = (random(), random(), random())	
	coloresAsignados = {}

	for i in nodosSinColorear:
		
		if debug_true:
			print "NodosSinColor[" + str(i) + "]:" + str(nodosSinColorear) 
		
		nodos_adyacentes = nx.all_neighbors(grafo, i)
		nodos_no_adyacentes = nx.non_neighbors(grafo, i)
		colores_adyacentes = []
		colores_no_adyacentes = []
		
		# Almacenamos todos los colores de los nodos adyacentes
		for k in nodos_adyacentes:
			if coloresAsignados.has_key(k):
				colores_adyacentes.append(coloresAsignados[k])
		# Almacenamos todos los colores de los nodos  no adyacentes
		for k in nodos_no_adyacentes:
			if coloresAsignados.has_key(k):
				colores_no_adyacentes.append(coloresAsignados[k])

		# Volvemos a generar los iteradores para nodos adyacentes, ya que
		# al iterar en los bucles de arriba se perdieron
		nodos_adyacentes = nx.all_neighbors(grafo, i)
		nodos_no_adyacentes = nx.non_neighbors(grafo, i)
		
		if debug_true:
			print "colores adyacentes a " + str(i) + str(colores_adyacentes)
			print "colores no adyacentes a " + str(i) + str(colores_no_adyacentes)
			
		aux = False
		for j in nodos_adyacentes:
			if debug_true:
				print "j=" + str(j)
				print "Color Actual=" + str(colorActual)
			if not aux and colorActual not in colores_adyacentes:
				aux = True
				#pass
			else:
				aux = True
				aux2 = False
				# Recorremos los colores no adyacentes y comparamos 
				# el color con el adyacente, usaremos un color existente
				# pero sin que coincida con alguno adyacente
				if colores_no_adyacentes:
					for t in colores_no_adyacentes:
						if debug_true:
							print t not in colores_adyacentes
						if not aux2 and not t in colores_adyacentes:
							aux2 = True
							colorActual = t
				if not aux2:
					if debug_true:
						print "Genero para " + str(i)
					colorActual = (random(), random(), random())

		coloresAsignados[i] = colorActual
		colores.append(colorActual)
		
	if (debug_true):
		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(coloresAsignados)
		for i in colores:
			print i[0]
	return colores

parser = argparse.ArgumentParser(description='Coloración de grafos')
parser.add_argument('-e','--ejemplo', help='Qué grafo usar',type=int, 
	required=True)
parser.add_argument('-d','--debug', help='Mostrar mensajes de depuración', 
	action='store_true', default=False, required=False)
args = parser.parse_args()

#Grafo a usar
ejemploNumero = args.ejemplo
debug_true = args.debug

print ("Usando el grafo número : %s" % args.ejemplo )

G = nx.Graph()
node_size = 3000

if ejemploNumero == 1:
	#Grafo 1
	G.add_nodes_from([1,2,3,4,5])
	G.add_edges_from([(1,3), (3,4), (3,5), (4,2), (5,2)])
	# explicitly set positions
	pos={1:(.4,3),
     2:(1.4,3),
     3:(.6,3),
     4:(1,3.1),
     5:(1,2.9)}

	#Diccionario con los nombres de los nodos
	labels={1:"1",#r'$\alpha$',
		2:"2",#r'$\beta$',
		3:"3",#r'$\gamma$',
		4:"4",#r'$\delta$',
		5:"5"}#r'$\sigma$'}
	nx.draw_networkx_labels(G,pos,labels=labels,font_size=20)
elif ejemploNumero == 2:
	#Grafo 2
	G=nx.house_graph()	
	# explicitly set positions
	pos={0:(0,0),
     1:(1,0),
     2:(0,1),
     3:(1,1),
     4:(0.5,2.0)}
elif ejemploNumero == 3:
	G=nx.path_graph(8)
	pos=nx.spring_layout(G,iterations=200)
elif ejemploNumero == 4:
	G=nx.cycle_graph(24)
	pos=nx.spring_layout(G,iterations=200)
elif ejemploNumero == 5:
	G=nx.complete_graph(20)
	pos=nx.spring_layout(G,iterations=200)
elif ejemploNumero == 6:
	node_size = 100
	G=nx.balanced_tree(3,5)
	pos=nx.graphviz_layout(G,prog='twopi',args='')
	plt.figure(figsize=(8,8))
	nx.draw(G,pos,node_size=20,alpha=0.5,node_color="blue", with_labels=False)
elif ejemploNumero == 7:
	G=nx.cubical_graph()
	pos=nx.spring_layout(G) # positions for all nodes

	# nodes
	nx.draw_networkx_nodes(G,pos,
						   nodelist=[0,1,2,3],
						   node_color='r',
						   node_size=500,
					   alpha=0.8)
	nx.draw_networkx_nodes(G,pos,
						   nodelist=[4,5,6,7],
						   node_color='b',
						   node_size=500,
					   alpha=0.8)

	# edges
	nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
	nx.draw_networkx_edges(G,pos,
						   edgelist=[(0,1),(1,2),(2,3),(3,0)],
						   width=8,alpha=0.5,edge_color='r')
	nx.draw_networkx_edges(G,pos,
						   edgelist=[(4,5),(5,6),(6,7),(7,4)],
						   width=8,alpha=0.5,edge_color='b')


	# some math labels
	labels={}
	labels[0]=r'$a$'
	labels[1]=r'$b$'
	labels[2]=r'$c$'
	labels[3]=r'$d$'
	labels[4]=r'$\alpha$'
	labels[5]=r'$\beta$'
	labels[6]=r'$\gamma$'
	labels[7]=r'$\delta$'
	nx.draw_networkx_labels(G,pos,labels,font_size=16)

#Generamos la lista de colores minimos a usar mediante un algorigmo voraz
colors = coloracion(G)
nx.draw_networkx_nodes(G,pos,node_size=node_size,node_color=colors)
nx.draw_networkx_edges(G,pos,alpha=0.5,width=6)

plt.axis('off')
plt.savefig("grafo" + str(ejemploNumero) + ".png") # save as png
plt.show() # display
			
