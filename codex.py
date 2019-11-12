#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtWidgets import QGraphicsScene, QFileDialog, QMessageBox
import networkx as nx
import numpy as np
import copy
import scipy as sp
import operator
sys.setrecursionlimit(1000)

class st:
    def __init__(self,x,y,fl,pcolor,color):
        self.x = x
        self.y = y
        self.fl = fl
        self.pcolor = pcolor
        self.color = color

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 20, 741, 511))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdge_color = QtWidgets.QMenu(self.menubar)
        self.menuEdge_color.setObjectName("menuEdge_color")
        self.menuNode_color = QtWidgets.QMenu(self.menubar)
        self.menuNode_color.setObjectName("menuNode_color")
        self.menuAlgorithms = QtWidgets.QMenu(self.menubar)
        self.menuAlgorithms.setObjectName("menuAlgorithms")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_node = QtWidgets.QAction(MainWindow)
        #self.actionAdd_node.setCheckable(True)
        self.actionAdd_node.setObjectName("actionAdd_node")
        self.actionAdd_edge = QtWidgets.QAction(MainWindow)
        #self.actionAdd_edge.setCheckable(True)
        self.actionAdd_edge.setObjectName("actionAdd_edge")
        self.actionDelete_node = QtWidgets.QAction(MainWindow)
        #self.actionDelete_node.setCheckable(True)
        self.actionDelete_node.setObjectName("actionDelete_node")
        self.actionDelete_edge = QtWidgets.QAction(MainWindow)
        #self.actionDelete_edge.setCheckable(True)
        self.actionDelete_edge.setObjectName("actionDelete_edge")
        self.actionMax_matching = QtWidgets.QAction(MainWindow)
        self.actionMax_matching.setObjectName("actionMax_matching")
        self.actionEdge_3_color = QtWidgets.QAction(MainWindow)
        self.actionEdge_3_color.setObjectName("actionEdge_3_color")
        self.actionVertex_cover = QtWidgets.QAction(MainWindow)
        self.actionVertex_cover.setObjectName("actionVertex_cover")
        self.actionIndependent_Set = QtWidgets.QAction(MainWindow)
        self.actionIndependent_Set.setObjectName("actionIndependent_Set")
        self.actionHamiltonian_Path = QtWidgets.QAction(MainWindow)
        self.actionHamiltonian_Path.setObjectName("actionHamiltonian_Path")
        self.actionMove_node = QtWidgets.QAction(MainWindow)
        self.actionMove_node.setObjectName("actionMove_node")
        self.actionSave_File = QtWidgets.QAction(MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionSave_File.setShortcut("Ctrl+S")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionOpen_File.setShortcut("Ctrl+O")
        self.actionClear_Scene = QtWidgets.QAction(MainWindow)
        self.actionClear_Scene.setObjectName("actionClear_Scene")
        self.actionBlack = QtWidgets.QAction(MainWindow)
        self.actionBlack.setObjectName("actionBlack")
        self.actionRed = QtWidgets.QAction(MainWindow)
        self.actionRed.setObjectName("actionRed")
        self.actionGreen = QtWidgets.QAction(MainWindow)
        self.actionGreen.setObjectName("actionGreen")
        self.actionBlue = QtWidgets.QAction(MainWindow)
        self.actionBlue.setObjectName("actionBlue")
        self.actionBlack_2 = QtWidgets.QAction(MainWindow)
        self.actionBlack_2.setObjectName("actionBlack_2")
        self.actionRed_2 = QtWidgets.QAction(MainWindow)
        self.actionRed_2.setObjectName("actionRed_2")
        self.actionGreen_2 = QtWidgets.QAction(MainWindow)
        self.actionGreen_2.setObjectName("actionGreen_2")
        self.actionBlue_2 = QtWidgets.QAction(MainWindow)
        self.actionBlue_2.setObjectName("actionBlue_2")
        self.actionBlack_3 = QtWidgets.QAction(MainWindow)
        self.actionBlack_3.setObjectName("actionBlack_3")
        self.actionYellow_3 = QtWidgets.QAction(MainWindow)
        self.actionYellow_3.setObjectName("actionYellow_3")
        self.actionGreen_3 = QtWidgets.QAction(MainWindow)
        self.actionGreen_3.setObjectName("actionGreen_3")
        self.actionBlue_3 = QtWidgets.QAction(MainWindow)
        self.actionBlue_3.setObjectName("actionBlue_3")
        self.actionBlack_4 = QtWidgets.QAction(MainWindow)
        self.actionBlack_4.setObjectName("actionBlack_4")
        self.actionYellow_4 = QtWidgets.QAction(MainWindow)
        self.actionYellow_4.setObjectName("actionYellow_4")
        self.actionGreen_4 = QtWidgets.QAction(MainWindow)
        self.actionGreen_4.setObjectName("actionGreen_4")
        self.actionBlue_4 = QtWidgets.QAction(MainWindow)
        self.actionBlue_4.setObjectName("actionBlue_4")
        self.menuFile.addAction(self.actionAdd_node)
        self.menuFile.addAction(self.actionAdd_edge)
        self.menuFile.addAction(self.actionDelete_node)
        self.menuFile.addAction(self.actionDelete_edge)
        self.menuFile.addAction(self.actionMove_node)
        self.menuAlgorithms.addAction(self.actionMax_matching)
        self.menuAlgorithms.addAction(self.actionEdge_3_color)
        self.menuAlgorithms.addAction(self.actionVertex_cover)
        self.menuAlgorithms.addAction(self.actionIndependent_Set)
        self.menuAlgorithms.addAction(self.actionHamiltonian_Path)
        self.menuFile.addAction(self.actionSave_File)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionClear_Scene)
        self.menuEdge_color.addAction(self.actionBlack_3)
        self.menuEdge_color.addAction(self.actionYellow_3)
        self.menuEdge_color.addAction(self.actionGreen_3)
        self.menuEdge_color.addAction(self.actionBlue_3)
        self.menuNode_color.addAction(self.actionBlack_4)
        self.menuNode_color.addAction(self.actionYellow_4)
        self.menuNode_color.addAction(self.actionGreen_4)
        self.menuNode_color.addAction(self.actionBlue_4)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdge_color.menuAction())
        self.menubar.addAction(self.menuNode_color.menuAction())
        self.menubar.addAction(self.menuAlgorithms.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdge_color.setTitle(_translate("MainWindow", "Edge color"))
        self.menuNode_color.setTitle(_translate("MainWindow", "Node color"))
        self.menuAlgorithms.setTitle(_translate("MainWindow", "Algorithms"))
        self.actionAdd_node.setText(_translate("MainWindow", "Add node"))
        self.actionAdd_edge.setText(_translate("MainWindow", "Add edge"))
        self.actionDelete_node.setText(_translate("MainWindow", "Delete node"))
        self.actionDelete_edge.setText(_translate("MainWindow", "Delete edge"))
        self.actionMove_node.setText(_translate("MainWindow", "Move node"))
        self.actionMax_matching.setText(_translate("MainWindow", "Max matching"))
        self.actionEdge_3_color.setText(_translate("MainWindow","Minimum Vertex color"))
        self.actionVertex_cover.setText(_translate("MainWindow","Vertex Cover"))
        self.actionIndependent_Set.setText(_translate("MainWindow", "Independent Set"))
        self.actionHamiltonian_Path.setText(_translate("MainWindow", "Hamiltonian Path"))
        self.actionSave_File.setText(_translate("MainWindow", "Save File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionClear_Scene.setText(_translate("MainWindow", "Clear Scene"))
        self.actionDelete_edge.setStatusTip(_translate("MainWindow", "Click on the 2 corresponding nodes"))
        self.actionBlack.setText(_translate("MainWindow", "Black"))
        self.actionRed.setText(_translate("MainWindow", "Red"))
        self.actionGreen.setText(_translate("MainWindow", "Green"))
        self.actionBlue.setText(_translate("MainWindow", "Blue"))
        self.actionBlack_2.setText(_translate("MainWindow", "Black"))
        self.actionRed_2.setText(_translate("MainWindow", "Red"))
        self.actionGreen_2.setText(_translate("MainWindow", "Green"))
        self.actionBlue_2.setText(_translate("MainWindow", "Blue"))
        self.actionBlack_3.setText(_translate("MainWindow", "Black"))
        self.actionBlack_3.setToolTip(_translate("MainWindow", "eBlack"))
        self.actionYellow_3.setText(_translate("MainWindow", "Yellow"))
        self.actionYellow_3.setToolTip(_translate("MainWindow", "eYellow"))
        self.actionGreen_3.setText(_translate("MainWindow", "Green"))
        self.actionGreen_3.setToolTip(_translate("MainWindow", "eGreen"))
        self.actionBlue_3.setText(_translate("MainWindow", "Blue"))
        self.actionBlue_3.setToolTip(_translate("MainWindow", "eBlue"))
        self.actionBlack_4.setText(_translate("MainWindow", "Black"))
        self.actionBlack_4.setToolTip(_translate("MainWindow", "nBlack"))
        self.actionYellow_4.setText(_translate("MainWindow", "Yellow"))
        self.actionYellow_4.setToolTip(_translate("MainWindow", "nYellow"))
        self.actionGreen_4.setText(_translate("MainWindow", "Green"))
        self.actionGreen_4.setToolTip(_translate("MainWindow", "nGreen"))
        self.actionBlue_4.setText(_translate("MainWindow", "Blue"))
        self.actionBlue_4.setToolTip(_translate("MainWindow", "nBlue"))
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.function = 0
        self.node = []
        self.edge = []
        self.index = 0
        self.eindex = 0
        self.s1 = -1
        self.s2 = -1
        self.graphicsView.scene = QGraphicsScene()
        self.graphicsView.setScene(self.graphicsView.scene)
        self.graphicsView.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        pen = QPen(QtCore.Qt.white)
        brush = QBrush(QtCore.Qt.white)
        self.graphicsView.scene.addEllipse(5,5,10,10,pen,brush)
        self.epen = QPen(QtCore.Qt.black,5)
        self.ebrush = QBrush(QtCore.Qt.black)
        self.npen = QPen(QtCore.Qt.black,5)
        self.nbrush = QBrush(QtCore.Qt.black)
        self.psel = QPen(QtCore.Qt.red,5)
        self.bsel = QBrush(QtCore.Qt.red)
        self.ecolour = 1
        self.ncolour = 1
        self.menuFile.triggered[QtWidgets.QAction].connect(self.processtrigger)
        self.menuEdge_color.triggered[QtWidgets.QAction].connect(self.processtrigger)
        self.menuNode_color.triggered[QtWidgets.QAction].connect(self.processtrigger)
        self.menuAlgorithms.triggered[QtWidgets.QAction].connect(self.processtrigger)

    def find_maximum_matching(self,G,M):
        P = self.finding_aug_path(G,M)
        if P == []:#Base Case
            return M
        else: #Augment P to M
            ##Add the alternating edges of P to M
            for i in range(0,len(P)-2,2): 
                M.add_edge(P[i],P[i+1])
                M.remove_edge(P[i+1],P[i+2])
            M.add_edge(P[-2],P[-1])
            return self.find_maximum_matching(G,M)
    
    def dist_to_root(self,point,root,Graph):
        path = nx.shortest_path(Graph, source = point, target = root)
        return (len(path)-1)
     
        
    def finding_aug_path(self,G,M,Blossom_stack=[]):
        Forest = [] #Storing the Forests
        Path = [] # The final path 
    
        unmarked_edges = list(set(G.edges()) - set(M.edges()))
        unmarked_nodes = list(G.nodes())
        Forest_nodes = []
        ## we need a map from v to the tree
        tree_to_root = {} # key=idx of tree in forest, val=root
        root_to_tree = {} # key=root, val=idx of tree in forest
            
        ##List of exposed vertices - ROOTS OF TREES
        exp_vertex = list(set(G.nodes()) - set(M.nodes()))
        
        counter = 0
        #List of trees with the exposed vertices as the roots
        for v in exp_vertex:  
            temp = nx.Graph()
            temp.add_node(v)
            Forest.append(temp)
            Forest_nodes.append(v)
    
            #link each root to its tree
            tree_to_root[counter] = v
            root_to_tree[v] = counter
            counter = counter + 1
    
        
        for v in Forest_nodes:  
            root_of_v = None
            tree_num_of_v = None
            for tree_number in range(len(Forest)): 
                tree_in = Forest[tree_number]
                if tree_in.has_node(v) == True:
                    root_of_v = tree_to_root[tree_number]
                    tree_num_of_v = tree_number
                    break #Break out of the for loop
            edges_v = list(G.edges(v))
            for edge_number in range(len(edges_v)): 
                e = edges_v[edge_number]
                e2 = (e[1],e[0]) #the edge in the other order
                if ((e in unmarked_edges or e2 in unmarked_edges) and e!=[]):
                    w = e[1] # the other vertex of the unmarked edge
                    w_in_Forest = 0; ##Indicator for w in F or not
    
                    ##Go through all the trees in the forest to check if w in F
                    tree_of_w = None
                    tree_num_of_w = None
                    for tree_number in range(len(Forest)):
                        tree = Forest[tree_number]
                        if tree.has_node(w) == True:
                            w_in_Forest = 1
                            root_of_w = tree_to_root[tree_number]
                            tree_num_of_w = tree_number
                            tree_of_w = Forest[tree_num_of_w]
                            break #Break the outer for loop
                    
                    if w_in_Forest == 0:
                        ## w is matched, so add e and w's matched edge to F
                        Forest[tree_num_of_v].add_edge(e[0],e[1]) # edge {v,w}
                        # Note: we don't add w to forest nodes b/c it's odd dist from root
                        #assert(M.has_node(w))
                        edge_w = list(M.edges(w))[0] # get edge {w,x}
                        Forest[tree_num_of_v].add_edge(edge_w[0],edge_w[1]) # add edge{w,x}
                        Forest_nodes.append(edge_w[1]) ## add {x} to the list of forest nodes
    
                    else: ## w is in Forest
                        # if odd, do nothing.
                        if self.dist_to_root(w,root_of_w,Forest[tree_num_of_w])%2 == 0:
                            if (tree_num_of_v != tree_num_of_w):
                                ##Shortest path from root(v)--->v-->w---->root(w)
                                path_in_v = nx.shortest_path(Forest[tree_num_of_v], source = root_of_v, target = v)
                                path_in_w = nx.shortest_path(Forest[tree_num_of_w], source = w, target = root_of_w)
    
                                return path_in_v + path_in_w
                            else: ##Contract the blossom
                                # create blossom
                                blossom = nx.shortest_path(tree_of_w, source=v, target=w)
                                blossom.append(v)
                                #assert(len(blossom)%2 == 0)
                                # contract blossom into single node w
                                contracted_G = copy.deepcopy(G)
                                contracted_M = copy.deepcopy(M)
                                for node in blossom[0:len(blossom)-1]:
                                    if node != w:
                                        contracted_G = nx.contracted_nodes(contracted_G, w, node, self_loops=False)
                                        if node in contracted_M.nodes(): 
                                           edge_rm = list(M.edges(node))[0] #this will be exactly one edge
                                           contracted_M.remove_node(node)
                                           contracted_M.remove_node(edge_rm[1])
                                           #assert(len(list(contracted_M.nodes()))%2 == 0)
                                # add blossom to our stack
                                Blossom_stack.append(w)
    
                                # recurse
                                aug_path = self.finding_aug_path(contracted_G, contracted_M, Blossom_stack)
    
                                # check if blossom exists in aug_path 
                                v_B = Blossom_stack.pop()
                                if (v_B in aug_path):
                                    ##Define the L_stem and R_stem
                                    L_stem = aug_path[0:aug_path.index(v_B)]
                                    R_stem = aug_path[aug_path.index(v_B)+1:]
                                    lifted_blossom = [] #stores the path within the blossom to take
                                    # Find base of blossom
                                    i = 0
                                    base = None
                                    base_idx = -1
                                    blossom_ext = blossom + [blossom[1]] 
                                    while base == None and i < len(blossom) - 1:
                                        if not(M.has_edge(blossom[i],blossom[i+1])):
                                            if not(M.has_edge(blossom[i+1],blossom_ext[i+2])): 
                                                base = blossom[i+1]
                                                base_idx = i+1
                                            else:
                                                i += 2
                                        else:
                                            i += 1
                                    # if needed, create list of blossom nodes starting at base
                                    if blossom[0] != base:
                                        based_blossom = []
                                        base_idx = blossom.index(base)
                                        for i in range(base_idx,len(blossom)-1):
                                            based_blossom.append(blossom[i])
                                        for i in range(0,base_idx):
                                            based_blossom.append(blossom[i])
                                        based_blossom.append(base)
                                    else:
                                        based_blossom = blossom
    
                                    # CHECK IF BLOSSOM IS ENDPT
                                    if L_stem == [] or R_stem == []:
                                        if L_stem != []:
                                            if G.has_edge(base, L_stem[-1]):
                                                # CASE 1:
                                                # Chuck the blossom
                                                return L_stem + [base]
                                            else:
                                                # CASE 2:
                                                # find where Lstem is connected
                                                i = 1
                                                while (lifted_blossom == []):
                                                    #assert(i < len(based_blossom)-1)
                                                    if G.has_edge(based_blossom[i],L_stem[-1]):
                                                        # make sure we're adding the even part to lifted path
                                                        if i%2 == 0: # same dir path
                                                            lifted_blossom = list(reversed(based_blossom))[-i-1:] ####################
                                                        else: # opposite dir path
                                                            lifted_blossom = based_blossom[i:]##########################
                                                    i += 1
                                                return L_stem + lifted_blossom
    
                                        else:
                                            if G.has_edge(base, R_stem[0]):
                                                # CASE 1:
                                                # Chuck the blossom. 
                                                return [base] + R_stem
                                            else:
                                                # CASE 2:
                                                # find where R_stem is connected
                                                i = 1
                                                while (lifted_blossom == []):
                                                    #assert(i < len(based_blossom)-1)
                                                    if G.has_edge(based_blossom[i],R_stem[0]):
                                                        # make sure we're adding the even part to lifted path
                                                        if i%2 == 0: # same dir path
                                                            lifted_blossom = based_blossom[:i+1]
                                                            #print lifted_blossom
                                                        else: # opposite dir path
                                                            lifted_blossom = list(reversed(based_blossom))[:-i]
                                                    i += 1
                                                return lifted_blossom + R_stem
    
                                    else: # blossom is in the middle
                                        # LIFT the blossom
                                        # check if L_stem attaches to base
                                        if M.has_edge(base, L_stem[-1]):
                                            # find where right stem attaches
                                            if G.has_edge(base, R_stem[0]):
                                                # blossom is useless
                                                return L_stem + [base] + R_stem
                                            else:
                                                # blossom needs to be lifted
                                                i = 1
                                                while (lifted_blossom == []):
                                                    # assert(i < len(based_blossom)-1)
                                                    if G.has_edge(based_blossom[i],R_stem[0]):
                                                        # make sure we're adding the even part to lifted path
                                                        if i%2 == 0: # same dir path
                                                            lifted_blossom = based_blossom[:i+1] 
                                                            # print lifted_blossom
                                                        else: # opposite dir path
                                                            lifted_blossom = list(reversed(based_blossom))[:-i]
                                                            # print lifted_blossom
                                                    i += 1
                                                return L_stem + lifted_blossom + R_stem
                                        else: 
                                            # R stem to base is in matching
                                            # assert(M.has_edge(base, R_stem[0]))
                                            # check where left stem attaches
                                            if G.has_edge(base, L_stem[-1]):
                                                # blossom is useless
                                                return L_stem + [base] + R_stem
                                            else:
                                                # blossom needs to be lifted
                                                i = 1
                                                while (lifted_blossom == []):
                                                    # assert(i < len(based_blossom)-1)
                                                    if G.has_edge(based_blossom[i],L_stem[-1]):
                                                        # make sure we're adding the even part to lifted path
                                                        if i%2 == 0: # same dir path
                                                            lifted_blossom = list(reversed(based_blossom))[-i-1:] 
                                                        else: # opposite dir path
                                                            lifted_blossom = based_blossom[i:] 
                                                    i += 1
                                                return L_stem + list((lifted_blossom)) + R_stem
                                else: # blossom is not in aug_path
                                    return aug_path
        ##IF Nothing is Found
        return Path ##Empty Path
    
           
           



    def pixelselect(self,event):
        self.a = event.localPos()
        self.x1 = int(self.a.x())
        self.y1 = int(self.a.y())
        if self.function == 1:
            self.graphicsView.scene.addEllipse(self.x1, self.y1, 10, 10, self.npen,self.nbrush)
            self.node.append(st(self.x1,self.y1,1,1,self.ncolour))
        if self.function == 3:
            self.f2=0
            for i in range(len(self.node)):
                self.ni1 = abs(self.x1-self.node[i].x)
                self.ni2 = abs(self.y1-self.node[i].y)
                if self.ni1<10:
                    if self.ni2<10:
                        self.i1 = i
                        self.f2= 1
                        self.node[i].fl = 0

            for i in range(len(self.edge)):
                if self.edge[i].x == self.i1:
                    self.edge[i].fl = 0
                if self.edge[i].y == self.i1:
                    self.edge[i].fl = 0

            if self.f2==1:
                self.graphicsView.scene.clear()
                for i in range(len(self.node)):
                    if self.node[i].fl == 1:
                        if self.node[i].color == 1:
                            self.pen = QPen(QtCore.Qt.black,5)
                            self.brush = QBrush(QtCore.Qt.black)
                        if self.node[i].color == 2:
                            self.pen = QPen(QtCore.Qt.yellow,5)
                            self.brush = QBrush(QtCore.Qt.yellow)
                        if self.node[i].color == 3:
                            self.pen = QPen(QtCore.Qt.green,5)
                            self.brush = QBrush(QtCore.Qt.green)
                        if self.node[i].color == 4:
                            self.pen = QPen(QtCore.Qt.blue,5)
                            self.brush = QBrush(QtCore.Qt.blue)
                        if self.node[i].color == 5:
                            self.pen = QPen(QtCore.Qt.red,5)
                            self.brush = QBrush(QtCore.Qt.red)
                        if self.node[i].color == 6:
                            self.color = QColor(205, 22, 212)
                            self.pen = QPen(self.color,5)
                            self.brush = QBrush(self.color)
                        if self.node[i].color == 7:
                            self.color = QColor(255, 161, 73)
                            self.pen = QPen(self.color,5)
                            self.brush = QBrush(self.color)
                        self.graphicsView.scene.addEllipse(self.node[i].x,self.node[i].y,10,10,self.pen,self.brush)
                for i in range(len(self.edge)):
                    if self.edge[i].fl == 1:
                        if self.edge[i].color == 1:
                            self.pen = QPen(QtCore.Qt.black,5)
                            self.brush = QBrush(QtCore.Qt.black)
                        if self.edge[i].color == 2:
                            self.pen = QPen(QtCore.Qt.yellow,5)
                            self.brush = QBrush(QtCore.Qt.yellow)
                        if self.edge[i].color == 3:
                            self.pen = QPen(QtCore.Qt.green,5)
                            self.brush = QBrush(QtCore.Qt.green)
                        if self.edge[i].color == 4:
                            self.pen = QPen(QtCore.Qt.blue,5)
                            self.brush = QBrush(QtCore.Qt.blue)
                        if self.edge[i].color == 5:
                            self.pen = QPen(QtCore.Qt.red,5)
                            self.brush = QBrush(QtCore.Qt.red)
                        if self.edge[i].color == 6:
                            self.color = QColor(205, 22, 212)
                            self.pen = QPen(self.color,5)
                            self.brush = QBrush(self.color)
                        self.graphicsView.scene.addLine(self.node[self.edge[i].x].x+5,self.node[self.edge[i].x].y+5,self.node[self.edge[i].y].x+5,self.node[self.edge[i].y].y+5,self.pen)
        if self.function == 4:
            for i in range(len(self.node)):
                self.ni1 = abs(self.x1-self.node[i].x)
                self.ni2 = abs(self.y1-self.node[i].y)
                if self.ni1<10:
                    if self.ni2<10:
                        if self.s1 == -1:
                            self.s1 = i
                            self.graphicsView.scene.addEllipse(self.node[i].x,self.node[i].y,10,10,self.psel,self.bsel)
                        else:
                            self.s2 = i
            if self.s1 != -1:
                if self.s2 != -1:
                    for i in range(len(self.edge)):
                        if self.edge[i].x == self.s1 or self.edge[i].y == self.s1:
                            if self.edge[i].x == self.s2 or self.edge[i].y == self.s2:
                                self.edge[i].fl = 0

                    self.graphicsView.scene.clear()
                    for i in range(len(self.node)):
                        if self.node[i].fl == 1:
                            if self.node[i].color == 1:
                                self.pen = QPen(QtCore.Qt.black,5)
                                self.brush = QBrush(QtCore.Qt.black)
                            if self.node[i].color == 2:
                                self.pen = QPen(QtCore.Qt.yellow,5)
                                self.brush = QBrush(QtCore.Qt.yellow)
                            if self.node[i].color == 3:
                                self.pen = QPen(QtCore.Qt.green,5)
                                self.brush = QBrush(QtCore.Qt.green)
                            if self.node[i].color == 4:
                                self.pen = QPen(QtCore.Qt.blue,5)
                                self.brush = QBrush(QtCore.Qt.blue)
                            if self.node[i].color == 5:
                                self.pen = QPen(QtCore.Qt.red,5)
                                self.brush = QBrush(QtCore.Qt.red)
                            if self.node[i].color == 6:
                                self.color = QColor(205, 22, 212)
                                self.pen = QPen(self.color,5)
                                self.brush = QBrush(self.color)
                            if self.node[i].color == 7:
                                self.color = QColor(255, 161, 73)
                                self.pen = QPen(self.color,5)
                                self.brush = QBrush(self.color)
                            self.graphicsView.scene.addEllipse(self.node[i].x,self.node[i].y,10,10,self.pen,self.brush)
                    for i in range(len(self.edge)):
                        if self.edge[i].fl == 1:
                            if self.edge[i].color == 1:
                                self.pen = QPen(QtCore.Qt.black,5)
                                self.brush = QBrush(QtCore.Qt.black)
                            if self.edge[i].color == 2:
                                self.pen = QPen(QtCore.Qt.yellow,5)
                                self.brush = QBrush(QtCore.Qt.yellow)
                            if self.edge[i].color == 3:
                                self.pen = QPen(QtCore.Qt.green,5)
                                self.brush = QBrush(QtCore.Qt.green)
                            if self.edge[i].color == 4:
                                self.pen = QPen(QtCore.Qt.blue,5)
                                self.brush = QBrush(QtCore.Qt.blue)
                            if self.edge[i].color == 5:
                                self.pen = QPen(QtCore.Qt.red,5)
                                self.brush = QBrush(QtCore.Qt.red)
                            if self.edge[i].color == 6:
                                self.color = QColor(205, 22, 212)
                                self.pen = QPen(self.color,5)
                                self.brush = QBrush(self.color)
                            self.graphicsView.scene.addLine(self.node[self.edge[i].x].x+5,self.node[self.edge[i].x].y+5,self.node[self.edge[i].y].x+5,self.node[self.edge[i].y].y+5,self.pen)
                    self.s1 = -1
                    self.s2 = -1
        if self.function == 6:
            for i in range(len(self.node)):
                self.a1 = abs(self.x1-self.node[i].x)
                self.a2 = abs(self.y1-self.node[i].y)
                if self.a1<10:
                    if self.a2<10:
                        self.a3 = i
                    
                    
    def blos(self):
        if self.function == 5:
            G = nx.Graph()
            for ii in range(len(self.node)):
                if self.node[ii].color == 5 or 6 or 7:
                    self.node[ii].color = self.node[ii].pcolor
                if self.node[ii].fl == 1:
                    G.add_node((self.node[ii].x,self.node[ii].y))
            for ii in range(len(self.edge)):
                if self.edge[ii].color == 5 or 6:
                    self.edge[ii].color = self.edge[ii].pcolor
                if self.edge[ii].fl == 1:
                    G.add_edge((self.node[self.edge[ii].x].x,self.node[self.edge[ii].x].y),(self.node[self.edge[ii].y].x,self.node[self.edge[ii].y].y))
            M = nx.Graph()
            MM = self.find_maximum_matching(G,M)
            for ii in MM.node():
                for i in range(len(self.node)):
                    if ii==(self.node[i].x,self.node[i].y):
                        self.node[i].pcolor = self.node[i].color
                        self.node[i].color = 5
            for ii in MM.edges():
                for i in range(len(self.edge)):
                    if ii==((self.node[self.edge[i].x].x,self.node[self.edge[i].x].y),(self.node[self.edge[i].y].x,self.node[self.edge[i].y].y)) or ii==((self.node[self.edge[i].y].x,self.node[self.edge[i].y].y),(self.node[self.edge[i].x].x,self.node[self.edge[i].x].y)):
                        self.edge[i].pcolor = self.edge[i].color
                        self.edge[i].color = 5
            self.graphicsView.scene.clear()
            for i in range(len(self.node)):
                if self.node[i].fl == 1:
                    if self.node[i].color == 1:
                        self.pen = QPen(QtCore.Qt.black,5)
                        self.brush = QBrush(QtCore.Qt.black)
                    if self.node[i].color == 2:
                        self.pen = QPen(QtCore.Qt.yellow,5)
                        self.brush = QBrush(QtCore.Qt.yellow)
                    if self.node[i].color == 3:
                        self.pen = QPen(QtCore.Qt.green,5)
                        self.brush = QBrush(QtCore.Qt.green)
                    if self.node[i].color == 4:
                        self.pen = QPen(QtCore.Qt.blue,5)
                        self.brush = QBrush(QtCore.Qt.blue)
                    if self.node[i].color == 5:
                        self.pen = QPen(QtCore.Qt.red,5)
                        self.brush = QBrush(QtCore.Qt.red)
                    if self.node[i].color == 6:
                        self.color = QColor(205, 22, 212)
                        self.pen = QPen(self.color,5)
                        self.brush = QBrush(self.color)
                    if self.node[i].color == 7:
                        self.color = QColor(255, 161, 73)
                        self.pen = QPen(self.color,5)
                        self.brush = QBrush(self.color)
                    self.graphicsView.scene.addEllipse(self.node[i].x,self.node[i].y,10,10,self.pen,self.brush)
            for i in range(len(self.edge)):
                if self.edge[i].fl == 1:
                    if self.edge[i].color == 1:
                        self.pen = QPen(QtCore.Qt.black,5)
                        self.brush = QBrush(QtCore.Qt.black)
                    if self.edge[i].color == 2:
                        self.pen = QPen(QtCore.Qt.yellow,5)
                        self.brush = QBrush(QtCore.Qt.yellow)
                    if self.edge[i].color == 3:
                        self.pen = QPen(QtCore.Qt.green,5)
                        self.brush = QBrush(QtCore.Qt.green)
                    if self.edge[i].color == 4:
                        self.pen = QPen(QtCore.Qt.blue,5)
                        self.brush = QBrush(QtCore.Qt.blue)
                    if self.edge[i].color == 5:
                        self.pen = QPen(QtCore.Qt.red,5)
                        self.brush = QBrush(QtCore.Qt.red)
                    if self.edge[i].color == 6:
                        self.color = QColor(205, 22, 212)
                        self.pen = QPen(self.color,5)
                        self.brush = QBrush(self.color)
                    self.graphicsView.scene.addLine(self.node[self.edge[i].x].x+5,self.node[self.edge[i].x].y+5,self.node[self.edge[i].y].x+5,self.node[self.edge[i].y].y+5,self.pen)

    def move(self,event):
        self.b = event.localPos()
        self.x2 = int(self.b.x())
        self.y2 = int(self.b.y())
        self.min1 = 0
        self.mini1=0
        self.min2 = 0
        self.mini2=0
        self.mini3=0
        self.mini4=0
        self.f1=0
        self.f2=0
        if self.function == 2:
            for i in range(len(self.node)):
                self.mini1 = abs(self.x1-self.node[i].x)
                self.mini2 = abs(self.y1-self.node[i].y)
                if self.mini1<10:
                    if self.mini2<10:
                        self.min1 = i
                        self.f1=1
                self.mini3 = abs(self.x2-self.node[i].x)
                self.mini4 = abs(self.y2-self.node[i].y)
                if self.mini3<10:
                    if self.mini4<10:
                        self.min2 = i
                        self.f2=1
                if self.f1==1:
                    if self.f2==1:
                            self.graphicsView.scene.addLine(self.node[self.min1].x+5,self.node[self.min1].y+5,self.node[self.min2].x+5,self.node[self.min2].y+5,self.epen)
                            self.edge.append(st(self.min1,self.min2,1,1,self.ecolour))
        if self.function == 6:
            self.node[self.a3].x = self.x2
            self.node[self.a3].y = self.y2
            self.graphicsView.scene.clear()
            for i in range(len(self.node)):
                if self.node[i].fl == 1:
                    if self.node[i].color == 1:
                        self.pen = QPen(QtCore.Qt.black,5)
                        self.brush = QBrush(QtCore.Qt.black)
                    if self.node[i].color == 2:
                        self.pen = QPen(QtCore.Qt.yellow,5)
                        self.brush = QBrush(QtCore.Qt.yellow)
                    if self.node[i].color == 3:
                        self.pen = QPen(QtCore.Qt.green,5)
                        self.brush = QBrush(QtCore.Qt.green)
                    if self.node[i].color == 4:
                        self.pen = QPen(QtCore.Qt.blue,5)
                        self.brush = QBrush(QtCore.Qt.blue)
                    if self.node[i].color == 5:
                        self.pen = QPen(QtCore.Qt.red,5)
                        self.brush = QBrush(QtCore.Qt.red)
                    if self.node[i].color == 6:
                        self.color = QColor(205, 22, 212)
                        self.pen = QPen(self.color,5)
                        self.brush = QBrush(self.color)
                    if self.node[i].color == 7:
                        self.color = QColor(255, 161, 73)
                        self.pen = QPen(self.color,5)
                        self.brush = QBrush(self.color)
                    self.graphicsView.scene.addEllipse(self.node[i].x,self.node[i].y,10,10,self.pen,self.brush)
            for i in range(len(self.edge)):
                if self.edge[i].fl == 1:
                    if self.edge[i].color == 1:
                        self.pen = QPen(QtCore.Qt.black,5)
                        self.brush = QBrush(QtCore.Qt.black)
                    if self.edge[i].color == 2:
                        self.pen = QPen(QtCore.Qt.yellow,5)
                        self.brush = QBrush(QtCore.Qt.yellow)
                    if self.edge[i].color == 3:
                        self.pen = QPen(QtCore.Qt.green,5)
                        self.brush = QBrush(QtCore.Qt.green)
                    if self.edge[i].color == 4:
                        self.pen = QPen(QtCore.Qt.blue,5)
                        self.brush = QBrush(QtCore.Qt.blue)
                    if self.edge[i].color == 5:
                        self.pen = QPen(QtCore.Qt.red,5)
                        self.brush = QBrush(QtCore.Qt.red)
                    if self.edge[i].color == 6:
                        self.color = QColor(205, 22, 212)
                        self.pen = QPen(self.color,5)
                        self.brush = QBrush(self.color)
                    self.graphicsView.scene.addLine(self.node[self.edge[i].x].x+5,self.node[self.edge[i].x].y+5,self.node[self.edge[i].y].x+5,self.node[self.edge[i].y].y+5,self.pen)
    
    def save(self):
        name = QFileDialog.getSaveFileName(self.centralwidget, 'Save File')
        file = open(name[0],'w')
        nl = '\n'
        sep = ','
        file.write(str(len(self.node)))
        file.write(nl)
        for i in range(len(self.node)):
            file.write(str(self.node[i].x))
            file.write(nl)
            file.write(str(self.node[i].y))
            file.write(nl)
            file.write(str(self.node[i].fl))
            file.write(nl)
            file.write(str(self.node[i].pcolor))
            file.write(nl)
            file.write(str(self.node[i].color))
            file.write(nl)
        file.write(str(len(self.edge)))
        file.write(nl)
        for i in range(len(self.edge)):
            file.write(str(self.edge[i].x))
            file.write(nl)
            file.write(str(self.edge[i].y))
            file.write(nl)
            file.write(str(self.edge[i].fl))
            file.write(nl)
            file.write(str(self.edge[i].pcolor))
            file.write(nl)
            file.write(str(self.edge[i].color))
            file.write(nl)
        file.close()

    def open(self):
        op = QFileDialog.getOpenFileName(self.centralwidget, 'Open File')
        fil = open(op[0], 'r')
        self.graphicsView.scene.clear()
        self.node.clear()
        self.edge.clear()
        nn = int(fil.readline())
        for i in range(nn):
            x = int(fil.readline())
            y = int(fil.readline())
            fl = int(fil.readline())
            pcol = int(fil.readline())
            col = int(fil.readline())
            self.node.append(st(x,y,fl,pcol,col))
        ne = int(fil.readline())
        for i in range(ne):
            x = int(fil.readline())
            y = int(fil.readline())
            fl = int(fil.readline())
            pcol = int(fil.readline())
            col = int(fil.readline())
            self.edge.append(st(x,y,fl,pcol,col))
        for i in range(len(self.node)):
            if self.node[i].fl == 1:
                if self.node[i].color == 1:
                    self.pen = QPen(QtCore.Qt.black,5)
                    self.brush = QBrush(QtCore.Qt.black)
                if self.node[i].color == 2:
                    self.pen = QPen(QtCore.Qt.yellow,5)
                    self.brush = QBrush(QtCore.Qt.yellow)
                if self.node[i].color == 3:
                    self.pen = QPen(QtCore.Qt.green,5)
                    self.brush = QBrush(QtCore.Qt.green)
                if self.node[i].color == 4:
                    self.pen = QPen(QtCore.Qt.blue,5)
                    self.brush = QBrush(QtCore.Qt.blue)
                if self.node[i].color == 5:
                    self.pen = QPen(QtCore.Qt.red,5)
                    self.brush = QBrush(QtCore.Qt.red)
                if self.node[i].color == 6:
                    self.color = QColor(205, 22, 212)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color) 
                if self.node[i].color == 7:
                    self.color = QColor(255, 161, 73)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color)                      
                self.graphicsView.scene.addEllipse(self.node[i].x,self.node[i].y,10,10,self.pen,self.brush)
        for i in range(len(self.edge)):
            if self.edge[i].fl == 1:
                if self.edge[i].color == 1:
                    self.pen = QPen(QtCore.Qt.black,5)
                    self.brush = QBrush(QtCore.Qt.black)
                if self.edge[i].color == 2:
                    self.pen = QPen(QtCore.Qt.yellow,5)
                    self.brush = QBrush(QtCore.Qt.yellow)
                if self.edge[i].color == 3:
                    self.pen = QPen(QtCore.Qt.green,5)
                    self.brush = QBrush(QtCore.Qt.green)
                if self.edge[i].color == 4:
                    self.pen = QPen(QtCore.Qt.blue,5)
                    self.brush = QBrush(QtCore.Qt.blue)
                if self.edge[i].color == 5:
                    self.pen = QPen(QtCore.Qt.red,5)
                    self.brush = QBrush(QtCore.Qt.red)
                if self.edge[i].color == 6:
                    self.color = QColor(205, 22, 212)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color)
                self.graphicsView.scene.addLine(self.node[self.edge[i].x].x+5,self.node[self.edge[i].x].y+5,self.node[self.edge[i].y].x+5,self.node[self.edge[i].y].y+5,self.pen)

    #min vertex color problem start

    def isSafe(self, v, colour, c): 
        for i in range(self.l): 
            if self.mat[v][i] == 1 and colour[i] == c: 
                return False
        return True

    def graphColourUtil(self, m, colour, v): 
        if v == self.l: 
            return True

        for c in range(1, m+1): 
            if self.isSafe(v, colour, c) == True: 
                colour[v] = c 
                if self.graphColourUtil(m, colour, v+1) == True: 
                    return True
                colour[v] = 0

    def graphColouring(self, m): 
        colour = [0] * self.l
        if self.graphColourUtil(m, colour, 0) == None: 
            return False

        for i in range(self.l):
            self.node[i].color = colour[i]
        return True


    def np1(self):
        self.l = 0
        A = nx.Graph()
        for ii in range(len(self.node)):
            if self.node[ii].color == 5 or 6 or 7:
                self.node[ii].color = self.node[ii].pcolor
            if self.node[ii].fl == 1:
                A.add_node((self.node[ii].x,self.node[ii].y))
                self.l = self.l+1

        self.mat = [[0 for i in range(self.l)] for j in range(self.l)]
        for ii in range(len(self.edge)):
            if self.edge[ii].color == 5 or 6:
                self.edge[ii].color = self.edge[ii].pcolor
            if self.edge[ii].fl == 1:
                A.add_edge((self.node[self.edge[ii].x].x,self.node[self.edge[ii].x].y),(self.node[self.edge[ii].y].x,self.node[self.edge[ii].y].y))
                self.mat[self.edge[ii].x][self.edge[ii].y] = 1
                self.mat[self.edge[ii].y][self.edge[ii].x] = 1
        self.graphColouring(self.l)
        self.graphicsView.scene.clear()
        for i in range(len(self.node)):
            if self.node[i].fl == 1:
                if self.node[i].color == 1:
                    self.pen = QPen(QtCore.Qt.black,5)
                    self.brush = QBrush(QtCore.Qt.black)
                if self.node[i].color == 2:
                    self.pen = QPen(QtCore.Qt.yellow,5)
                    self.brush = QBrush(QtCore.Qt.yellow)
                if self.node[i].color == 3:
                    self.pen = QPen(QtCore.Qt.green,5)
                    self.brush = QBrush(QtCore.Qt.green)
                if self.node[i].color == 4:
                    self.pen = QPen(QtCore.Qt.blue,5)
                    self.brush = QBrush(QtCore.Qt.blue)
                if self.node[i].color == 5:
                    self.pen = QPen(QtCore.Qt.red,5)
                    self.brush = QBrush(QtCore.Qt.red)
                if self.node[i].color == 6:
                    self.color = QColor(205, 22, 212)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color) 
                if self.node[i].color == 7:
                    self.color = QColor(255, 161, 73)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color)                   
                self.graphicsView.scene.addEllipse(self.node[i].x,self.node[i].y,10,10,self.pen,self.brush)
        for i in range(len(self.edge)):
            if self.edge[i].fl == 1:
                if self.edge[i].color == 1:
                    self.pen = QPen(QtCore.Qt.black,5)
                    self.brush = QBrush(QtCore.Qt.black)
                if self.edge[i].color == 2:
                    self.pen = QPen(QtCore.Qt.yellow,5)
                    self.brush = QBrush(QtCore.Qt.yellow)
                if self.edge[i].color == 3:
                    self.pen = QPen(QtCore.Qt.green,5)
                    self.brush = QBrush(QtCore.Qt.green)
                if self.edge[i].color == 4:
                    self.pen = QPen(QtCore.Qt.blue,5)
                    self.brush = QBrush(QtCore.Qt.blue)
                if self.edge[i].color == 5:
                    self.pen = QPen(QtCore.Qt.red,5)
                    self.brush = QBrush(QtCore.Qt.red)
                if self.edge[i].color == 6:
                    self.color = QColor(205, 22, 212)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color)
                self.graphicsView.scene.addLine(self.node[self.edge[i].x].x+5,self.node[self.edge[i].x].y+5,self.node[self.edge[i].y].x+5,self.node[self.edge[i].y].y+5,self.pen)


    #min vertex color end

    def approx(self,G):
        degree_list = [val for (node,val) in G.degree()]
        VC = list() #vertex cover set
        max_node = degree_list.index(max(degree_list))
        while degree_list[max_node] > 0:
            degree_list[max_node] = 0
            VC.append(max_node)
            for node in G.neighbors(max_node):
                degree_list[node] =  degree_list[node] - 1
            max_node = degree_list.index(max(degree_list))
        return VC

    def np2(self):
        A = nx.Graph()
        for ii in range(len(self.node)):
            if self.node[ii].color == 5 or 6 or 7:
                self.node[ii].color = self.node[ii].pcolor
            if self.node[ii].fl == 1:
                A.add_node(ii)
        for ii in range(len(self.edge)):
            if self.edge[ii].color == 5 or 6:
                self.edge[ii].color = self.edge[ii].pcolor
            if self.edge[ii].fl == 1:
                A.add_edge(self.edge[ii].x,self.edge[ii].y)
        VC = self.approx(A)
        for i in range(len(VC)):
            self.node[VC[i]].pcolor = self.node[VC[i]].color
            self.node[VC[i]].color = 6
        self.graphicsView.scene.clear()
        for i in range(len(self.node)):
            if self.node[i].fl == 1:
                if self.node[i].color == 1:
                    self.pen = QPen(QtCore.Qt.black,5)
                    self.brush = QBrush(QtCore.Qt.black)
                if self.node[i].color == 2:
                    self.pen = QPen(QtCore.Qt.yellow,5)
                    self.brush = QBrush(QtCore.Qt.yellow)
                if self.node[i].color == 3:
                    self.pen = QPen(QtCore.Qt.green,5)
                    self.brush = QBrush(QtCore.Qt.green)
                if self.node[i].color == 4:
                    self.pen = QPen(QtCore.Qt.blue,5)
                    self.brush = QBrush(QtCore.Qt.blue)
                if self.node[i].color == 5:
                    self.pen = QPen(QtCore.Qt.red,5)
                    self.brush = QBrush(QtCore.Qt.red)
                if self.node[i].color == 6:
                    self.color = QColor(205, 22, 212)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color)
                if self.node[i].color == 7:
                    self.color = QColor(255, 161, 73)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color)
                self.graphicsView.scene.addEllipse(self.node[i].x,self.node[i].y,10,10,self.pen,self.brush)
        for i in range(len(self.edge)):
            if self.edge[i].fl == 1:
                if self.edge[i].color == 1:
                    self.pen = QPen(QtCore.Qt.black,5)
                    self.brush = QBrush(QtCore.Qt.black)
                if self.edge[i].color == 2:
                    self.pen = QPen(QtCore.Qt.yellow,5)
                    self.brush = QBrush(QtCore.Qt.yellow)
                if self.edge[i].color == 3:
                    self.pen = QPen(QtCore.Qt.green,5)
                    self.brush = QBrush(QtCore.Qt.green)
                if self.edge[i].color == 4:
                    self.pen = QPen(QtCore.Qt.blue,5)
                    self.brush = QBrush(QtCore.Qt.blue)
                if self.edge[i].color == 5:
                    self.pen = QPen(QtCore.Qt.red,5)
                    self.brush = QBrush(QtCore.Qt.red)
                if self.edge[i].color == 6:
                    self.color = QColor(205, 22, 212)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color)
                self.graphicsView.scene.addLine(self.node[self.edge[i].x].x+5,self.node[self.edge[i].x].y+5,self.node[self.edge[i].y].x+5,self.node[self.edge[i].y].y+5,self.pen)

    def np3(self):
        q = []
        A = nx.Graph()
        for ii in range(len(self.node)):
            if self.node[ii].color == 5 or 6 or 7:
                self.node[ii].color = self.node[ii].pcolor
            if self.node[ii].fl == 1:
                A.add_node(ii)
                q.append(1)
        for ii in range(len(self.edge)):
            if self.edge[ii].color == 5 or 6:
                self.edge[ii].color = self.edge[ii].pcolor
            if self.edge[ii].fl == 1:
                A.add_edge(self.edge[ii].x,self.edge[ii].y)
        VC = self.approx(A)
        for i in range(len(VC)):
            q[VC[i]] = 0
        for i in range(len(q)):
            if q[i] == 1:
                self.node[i].pcolor = self.node[i].color
                self.node[i].color = 7
        self.graphicsView.scene.clear()
        for i in range(len(self.node)):
            if self.node[i].fl == 1:
                if self.node[i].color == 1:
                    self.pen = QPen(QtCore.Qt.black,5)
                    self.brush = QBrush(QtCore.Qt.black)
                if self.node[i].color == 2:
                    self.pen = QPen(QtCore.Qt.yellow,5)
                    self.brush = QBrush(QtCore.Qt.yellow)
                if self.node[i].color == 3:
                    self.pen = QPen(QtCore.Qt.green,5)
                    self.brush = QBrush(QtCore.Qt.green)
                if self.node[i].color == 4:
                    self.pen = QPen(QtCore.Qt.blue,5)
                    self.brush = QBrush(QtCore.Qt.blue)
                if self.node[i].color == 5:
                    self.pen = QPen(QtCore.Qt.red,5)
                    self.brush = QBrush(QtCore.Qt.red)
                if self.node[i].color == 6:
                    self.color = QColor(205, 22, 212)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color)
                if self.node[i].color == 7:
                    self.color = QColor(255, 161, 73)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color)
                self.graphicsView.scene.addEllipse(self.node[i].x,self.node[i].y,10,10,self.pen,self.brush)
        for i in range(len(self.edge)):
            if self.edge[i].fl == 1:
                if self.edge[i].color == 1:
                    self.pen = QPen(QtCore.Qt.black,5)
                    self.brush = QBrush(QtCore.Qt.black)
                if self.edge[i].color == 2:
                    self.pen = QPen(QtCore.Qt.yellow,5)
                    self.brush = QBrush(QtCore.Qt.yellow)
                if self.edge[i].color == 3:
                    self.pen = QPen(QtCore.Qt.green,5)
                    self.brush = QBrush(QtCore.Qt.green)
                if self.edge[i].color == 4:
                    self.pen = QPen(QtCore.Qt.blue,5)
                    self.brush = QBrush(QtCore.Qt.blue)
                if self.edge[i].color == 5:
                    self.pen = QPen(QtCore.Qt.red,5)
                    self.brush = QBrush(QtCore.Qt.red)
                if self.edge[i].color == 6:
                    self.color = QColor(205, 22, 212)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color)
                self.graphicsView.scene.addLine(self.node[self.edge[i].x].x+5,self.node[self.edge[i].x].y+5,self.node[self.edge[i].y].x+5,self.node[self.edge[i].y].y+5,self.pen)

    def Safe(self, v, pos, path):  
        if self.graph[path[pos-1]][v] == 0: 
            return False 
        for vertex in path: 
            if vertex == v: 
                return False
        return True

    def hamCycleUtil(self, path, pos): 
        if pos == self.V:  
            if self.graph[path[pos-1]][path[0]] == 1: 
                return True
            else: 
                return False 
        for v in range(1,self.V):
            if self.Safe(v, pos, path) == True: 
                path[pos] = v 
                if self.hamCycleUtil(path, pos+1) == True: 
                    return True
                path[pos] = -1
        return False
  
    def hamCycle(self): 
        path = [-1] * self.V
        path[0] = 0
        if self.hamCycleUtil(path,1) == False:
            QMessageBox.about(self.centralwidget, "Error", "No hamiltonian path found")
            return False
        self.printSolution(path) 
        return True
  
    def printSolution(self, path): 
        for i in range(len(path)-1):
            for j in range(len(self.edge)):
                if self.edge[j].x == path[i] or self.edge[j].y == path[i]:
                    if self.edge[j].y == path[i+1] or self.edge[j].x == path[i+1]:
                        self.edge[j].color = 6


    def np4(self):
        self.V = 0
        A = nx.Graph()
        for ii in range(len(self.node)):
            if self.node[ii].color == 5 or 6 or 7:
                self.node[ii].color = self.node[ii].pcolor
            if self.node[ii].fl == 1:
                A.add_node((self.node[ii].x,self.node[ii].y))
                self.V = self.V+1

        self.graph = [[0 for i in range(self.V)] for j in range(self.V)]
        for ii in range(len(self.edge)):
            if self.edge[ii].color == 5 or 6:
                self.edge[ii].color = self.edge[ii].pcolor
            if self.edge[ii].fl == 1:
                A.add_edge((self.node[self.edge[ii].x].x,self.node[self.edge[ii].x].y),(self.node[self.edge[ii].y].x,self.node[self.edge[ii].y].y))
                self.graph[self.edge[ii].x][self.edge[ii].y] = 1
                self.graph[self.edge[ii].y][self.edge[ii].x] = 1
        self.hamCycle()
        self.graphicsView.scene.clear()
        for i in range(len(self.node)):
            if self.node[i].fl == 1:
                if self.node[i].color == 1:
                    self.pen = QPen(QtCore.Qt.black,5)
                    self.brush = QBrush(QtCore.Qt.black)
                if self.node[i].color == 2:
                    self.pen = QPen(QtCore.Qt.yellow,5)
                    self.brush = QBrush(QtCore.Qt.yellow)
                if self.node[i].color == 3:
                    self.pen = QPen(QtCore.Qt.green,5)
                    self.brush = QBrush(QtCore.Qt.green)
                if self.node[i].color == 4:
                    self.pen = QPen(QtCore.Qt.blue,5)
                    self.brush = QBrush(QtCore.Qt.blue)
                if self.node[i].color == 5:
                    self.pen = QPen(QtCore.Qt.red,5)
                    self.brush = QBrush(QtCore.Qt.red)
                if self.node[i].color == 6:
                    self.color = QColor(205, 22, 212)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color) 
                if self.node[i].color == 7:
                    self.color = QColor(255, 161, 73)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color)                   
                self.graphicsView.scene.addEllipse(self.node[i].x,self.node[i].y,10,10,self.pen,self.brush)
        for i in range(len(self.edge)):
            if self.edge[i].fl == 1:
                if self.edge[i].color == 1:
                    self.pen = QPen(QtCore.Qt.black,5)
                    self.brush = QBrush(QtCore.Qt.black)
                if self.edge[i].color == 2:
                    self.pen = QPen(QtCore.Qt.yellow,5)
                    self.brush = QBrush(QtCore.Qt.yellow)
                if self.edge[i].color == 3:
                    self.pen = QPen(QtCore.Qt.green,5)
                    self.brush = QBrush(QtCore.Qt.green)
                if self.edge[i].color == 4:
                    self.pen = QPen(QtCore.Qt.blue,5)
                    self.brush = QBrush(QtCore.Qt.blue)
                if self.edge[i].color == 5:
                    self.pen = QPen(QtCore.Qt.red,5)
                    self.brush = QBrush(QtCore.Qt.red)
                if self.edge[i].color == 6:
                    self.color = QColor(205, 22, 212)
                    self.pen = QPen(self.color,5)
                    self.brush = QBrush(self.color)
                self.graphicsView.scene.addLine(self.node[self.edge[i].x].x+5,self.node[self.edge[i].x].y+5,self.node[self.edge[i].y].x+5,self.node[self.edge[i].y].y+5,self.pen)



    def processtrigger(self, q):        
        if q.text() == 'Add node':
            self.function = 1
        if q.text() == 'Add edge':
            self.function = 2
        if q.text() == 'Delete node':
            self.function = 3
        if q.text() == 'Delete edge':
            self.function = 4
        if q.text() == 'Max matching':
            self.function = 5
            self.blos()
        if q.text() == 'Minimum Vertex color':
            self.np1()
        if q.text() == 'Vertex Cover':
            self.np2()
        if q.text() == 'Independent Set':
            self.np3()
        if q.text() == 'Hamiltonian Path':
            self.np4()
        if q.text() == 'Move node':
            self.function = 6
        if q.text() == 'Save File':
            self.save()
        if q.text() == 'Open File':
            self.open()
        if q.text() == 'Clear Scene':
            self.graphicsView.scene.clear()
            self.node.clear()
            self.edge.clear()
        if q.toolTip() == 'eBlack':
            self.ecolour = 1
            self.epen = QPen(QtCore.Qt.black,5)
            self.ebrush = QBrush(QtCore.Qt.black)
        if q.toolTip() == 'eYellow':
            self.ecolour = 2
            self.epen = QPen(QtCore.Qt.yellow,5)
            self.ebrush = QBrush(QtCore.Qt.yellow)
        if q.toolTip() == 'eGreen':
            self.ecolour = 3
            self.epen = QPen(QtCore.Qt.green,5)
            self.ebrush = QBrush(QtCore.Qt.green)
        if q.toolTip() == 'eBlue':
            self.ecolour = 4
            self.epen = QPen(QtCore.Qt.blue,5)
            self.ebrush = QBrush(QtCore.Qt.blue)
        if q.toolTip() == 'nBlack':
            self.ncolour = 1
            self.npen = QPen(QtCore.Qt.black,5)
            self.nbrush = QBrush(QtCore.Qt.black)
        if q.toolTip() == 'nYellow':
            self.ncolour = 2
            self.npen = QPen(QtCore.Qt.yellow,5)
            self.nbrush = QBrush(QtCore.Qt.yellow)
        if q.toolTip() == 'nGreen':
            self.ncolour = 3
            self.npen = QPen(QtCore.Qt.green,5)
            self.nbrush = QBrush(QtCore.Qt.green)
        if q.toolTip() == 'nBlue':
            self.ncolour = 4
            self.npen = QPen(QtCore.Qt.blue,5)
            self.nbrush = QBrush(QtCore.Qt.blue)
        self.graphicsView.mousePressEvent = self.pixelselect
        self.graphicsView.mouseReleaseEvent = self.move


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

