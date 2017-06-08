import os
import urllib

#Networkx
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import random
import csv
import nx2tikz

class Patient(object):

    #print(dict_ages['APOE-4-01'])

    def __init__(self, p_name=None):

        dict_ages = {
                    'APOE-3_01': 75.95,
                    'APOE-3_02': 50.88,
                    'APOE-3_03': 69.41,
                    'APOE-3_04': 67.51,
                    'APOE-3_05': 78.62,
                    'APOE-3_06': 65.49,
                    'APOE-3_07': 64.99,
                    'APOE-3_08': 53.95,
                    'APOE-3_09': 56.53,
                    'APOE-3_10': 67.00,
                    'APOE-3_11': 54.65,
                    'APOE-3_12': 66.52,
                    'APOE-3_13': 65.19,
                    'APOE-3_14': 73.07,
                    'APOE-3_15': 70.56,
                    'APOE-3_16': 61.82,
                    'APOE-3_17': 68.22,
                    'APOE-3_18': 45.96,
                    'APOE-3_19': 68.06,
                    'APOE-3_20': 69.75,
                    'APOE-3_21': 64.26,
                    'APOE-3_22': 78.73,
                    'APOE-3_23': 59.84,
                    'APOE-3_24': 53.97,
                    'APOE-3_25': 55.84,
                    'APOE-3_26': 65.14,
                    'APOE-3_27': 52.27,
                    'APOE-3_28': 56.67,
                    'APOE-3_29': 63.92,
                    'APOE-3_30': 69.43,
                    'APOE-4_01': 67.75,
                    'APOE-4_02': 62.11,
                    'APOE-4_03': 46.59,
                    'APOE-4_04': 72.08,
                    'APOE-4_05': 72.39,
                    'APOE-4_06': 45.83,
                    'APOE-4_07': 60.54,
                    'APOE-4_08': 68.41,
                    'APOE-4_09': 59.05,
                    'APOE-4_10': 61.75,
                    'APOE-4_11': 78.27,
                    'APOE-4_12': 65.94,
                    'APOE-4_13': 53.23,
                    'APOE-4_14': 59.41,
                    'APOE-4_15': 69.84,
                    'APOE-4_16': 42.80,
                    'APOE-4_17': 50.00,
                    'APOE-4_18': 67.33,
                    'APOE-4_19': 50.50,
                    'APOE-4_20': 70.86,
                    'APOE-4_21': 65.39,
                    'APOE-4_22': 61.33,
                    'APOE-4_23': 49.18,
                    'APOE-4_24': 68.27,
                    'APOE-4_25': 51.58
                    }

        if p_name is None:
            print('Using deffault patient')
            self.id = 'APOE-4_01'
        else:
            self.id = p_name

        try:
            self.age = dict_ages[self.id]
            #UCLA_CCN_APOE_DTI_APOE-4_1_connectmat.txt
            #printing patient info:
            
            if os.path.exists('data/connectivity'):
                if not os.path.exists('data/connectivity/UCLA_CCN_APOE_DTI_'+self.id+'_connectmat.txt'):
                    file = urllib.URLopener()
                    file.retrieve('https://raw.githubusercontent.com/pabloruiziba/aging_oscillators/master/data/connectivity/UCLA_CCN_APOE_DTI_'+self.id+'_connectmat.txt',
                                  'data/connectivity/UCLA_CCN_APOE_DTI_'+self.id+'_connectmat.txt')
            else:
                os.makedirs('data/connectivity')
                file = urllib.URLopener()
                file.retrieve('https://raw.githubusercontent.com/pabloruiziba/aging_oscillators/master/data/connectivity/UCLA_CCN_APOE_DTI_'+self.id+'_connectmat.txt',
                              'data/connectivity/UCLA_CCN_APOE_DTI_'+self.id+'_connectmat.txt')

            self.connectivity_path = 'data/connectivity/UCLA_CCN_APOE_DTI_'+self.id+'_connectmat.txt'

            print('##################################################')
            print('Id: '+self.id+', Age:'+str(self.age))        
            print('##################################################')


        except KeyError:
            print('##################################################')
            print('Patient id does not exist or was misspelled!!!')
            print('##################################################')
            quit()

    def draw_graph(self):
        with open(self.connectivity_path) as f:
            C = [map(float, line.split()) for line in f]      
        C = C/np.max(C) 
        G=nx.from_numpy_matrix(C)
        pos = nx.circular_layout(G)
        elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
        emedium=[(u,v) for (u,v,d) in G.edges(data=True) if (d['weight'] <=0.5 and d['weight'] >0.1)]
        esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.1]
        # nodes
        nx.draw_networkx_nodes(G,pos,node_size=30)
        # edges
        nx.draw_networkx_edges(G,pos,edgelist=elarge,
                            width=1.5)
        nx.draw_networkx_edges(G,pos,edgelist=emedium,
                            width=0.8,alpha=0.5,edge_color='b')
        nx.draw_networkx_edges(G,pos,edgelist=esmall,
                            width=0.8,alpha=0.2,edge_color='g')
        #nx.draw(G)
        plt.axis('off')
        plt.show()

    def graph_statistics(self):
        with open(self.connectivity_path) as f:
            C = [map(float, line.split()) for line in f]      
        C = C/np.max(C)
        G=nx.from_numpy_matrix(C)

        print("Radius (minimum excentricity): %d" % nx.radius(G))
        print("Diameter (shortes distance between most distant nodes): %d" % nx.diameter(G))
        print("Density: %s" % nx.density(G))
        print("Number of edges: %s" % G.number_of_edges())
        print("Avg. path length: %s" % nx.average_shortest_path_length(G))
        print("Avg. degree: %s" % str(sum(G.degree().values())/float(len(G))))
        print("Avg. clustering: %f" % nx.average_clustering(G))






model = Patient('APOE-3_02')


model.draw_graph()
#model.graph_statistics()


