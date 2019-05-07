"""
Реализация бинарного дерева

"""
class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
    
    def hasLeftChild(self):
        #Возвращает BSTNode левого потомка
        return self.LeftChild

    def hasRightChild(self):
        #Возвращает BSTNode левого потомка
        return self.RightChild

    def isRoot(self):
        #Возвращает True если BSTNode является корнем 
        return not self.Parent

    def isLeaf(self):
        #Возвращает True если элемент не имеет потомков
        return not(self.LeftChild or self.RightChild)

class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если не найден узел
        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        if self.Root==None:
            return None
        elif self.Root:
            return self._FindNodeByKey(key,self.Root)
        else:
            return None
            
    def _FindNodeByKey(self,key,currentNode):
        # приватный метод поиска
        if not currentNode:
            return None
        elif currentNode.NodeKey==key:
            nodeRes=BSTFind()
            nodeRes.Node=currentNode
            nodeRes.NodeHasKey=True
            nodeRes.ToLeft=None
            return nodeRes
        elif key<currentNode.NodeKey:
            if currentNode.hasLeftChild():
                return self._FindNodeByKey(key,currentNode.LeftChild)
            else:
                nodeRes=BSTFind()
                nodeRes.Node=currentNode
                nodeRes.NodeHasKey=False
                nodeRes.ToLeft=True
                return nodeRes
        else:
            if currentNode.hasRightChild():
                return self._FindNodeByKey(key,currentNode.RightChild)
            else:
                nodeRes=BSTFind()
                nodeRes.Node=currentNode
                nodeRes.NodeHasKey=False
                nodeRes.ToLeft=False
                return nodeRes


    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        if key==None:
            return None
        allNodes=self.GetAllNodes()
        for node in allNodes:
            if node.NodeKey==key:
                return False 
        if self.Root:
            self._AddKeyValue(key,val,self.Root)
            return True
        else:
            Node=BSTNode(key,val,None)
            self.Root=Node
            return True
        
    def _AddKeyValue(self,key,val,currentNode):
        # приветный метод добавления Node
        if key<currentNode.NodeKey:
            if currentNode.hasLeftChild()!=None:
                self._AddKeyValue(key,val,currentNode.LeftChild)
            else:
                currentNode.LeftChild=BSTNode(key,val,currentNode)
        elif key>currentNode.NodeKey:
            if currentNode.hasRightChild()!=None:
                self._AddKeyValue(key,val,currentNode.RightChild)
            else:
                currentNode.RightChild=BSTNode(key,val,currentNode)
        elif key==currentNode.NodeKey:
            pass
        else:
            pass

  
    def FinMinMax(self, FromNode, FindMax=True):
        # ищем максимальное/минимальное (узел) в поддерева
        if FromNode==None or not isinstance(FromNode,BSTNode):
            return None
        key=FromNode.NodeKey
        bst=self.FindNodeByKey(key)
        if bst.NodeHasKey==True:
            if FindMax==True:
                if FromNode.RightChild==None:
                    return FromNode
                while FromNode.RightChild!=None:
                    FromNode=FromNode.RightChild
                    if FromNode.RightChild==None:
                        return FromNode
            elif FindMax==False:
                if FromNode.LeftChild==None:
                    return FromNode
                while FromNode.LeftChild!=None:
                    FromNode=FromNode.LeftChild
                    if FromNode.LeftChild==None:
                        return FromNode
            else: 
                pass
        else: 
            pass

    def GetAllNodes(self,allNodes=None):
        #Получаем все элементы дерева
        if allNodes is None:
            allNodes=[]
        if self.Root is None:
            return allNodes
        else:
            Root=self.Root
            if not (self.Root in allNodes):
                allNodes.append(self.Root)
            if Root.LeftChild!=None and Root.RightChild!=None:
                self.Root=Root.LeftChild
                allNodes.extend(self.GetAllNodes())
                self.Root=Root.RightChild
                allNodes.extend(self.GetAllNodes())
            elif Root.LeftChild!=None and Root.RightChild==None:
                self.Root=Root.LeftChild
                allNodes.extend(self.GetAllNodes())
            elif Root.LeftChild==None and Root.RightChild!=None:
                self.Root=Root.RightChild
                allNodes.extend(self.GetAllNodes())
            self.Root=allNodes[0]
            return allNodes    

    def CompareTwo(self, node_1, node_2):
        #Сравниваем ключи двух элементов
        if node_1.NodeKey>node_2.NodeKey:
            return True
        else:
            return False
    
    def DeleteNodeByKey(self,key):
        nodeexist=self.FindNodeByKey(key)
        if nodeexist.NodeHasKey!=True:
            return False
        elif nodeexist.NodeHasKey==True:
            node_for_delete=nodeexist.Node
            parent_node_for_delete=node_for_delete.Parent
            #Блок с двумя детьми
            if node_for_delete.LeftChild!=None and node_for_delete.RightChild!=None:
                children=node_for_delete.RightChild
                if children.LeftChild==None:
                    #Меняем потомка у родителя удаляемого элемента
                    if node_for_delete.NodeKey>parent_node_for_delete.NodeKey:
                        parent_node_for_delete.RightChild=children  
                    elif node_for_delete.NodeKey<parent_node_for_delete.NodeKey:
                        parent_node_for_delete.LeftChild=children
                    children.LeftChild=node_for_delete.LeftChild
                elif children.LeftChild!=None:
                    #Ищем подходящий лист    
                    while children.LeftChild!=None:
                        children=children.LeftChild
                    if children.RightChild!=None:
                        children=children.RightChild
                    children_parent=children.Parent
                    #Удаляем из детей у старого родителя
                    if children_parent.NodeKey>children.NodeKey:
                        children_parent.LeftChild=None
                    elif children_parent.NodeKey<children.NodeKey:
                        children_parent.RightChild=None
                    #Обновляем родителя в элементе замене удаляемому
                    children.Parent=parent_node_for_delete
                    #Привязываем к новому родителю    
                    if node_for_delete.NodeKey>parent_node_for_delete.NodeKey:
                        parent_node_for_delete.RightChild=children  
                    elif node_for_delete.NodeKey<parent_node_for_delete.NodeKey:
                        parent_node_for_delete.LeftChild=children
                    #Добавляем потомков
                    children.LeftChild=node_for_delete.LeftChild
                    children.RightChild=node_for_delete.RightChild            
            # Блок если правый ребенок
            elif node_for_delete.LeftChild==None and node_for_delete.RightChild!=None:
                children=node_for_delete.RightChild
                children.Parent=parent_node_for_delete
                if node_for_delete.NodeKey>parent_node_for_delete.NodeKey:
                    parent_node_for_delete.RightChild=children
                elif node_for_delete.NodeKey<parent_node_for_delete.NodeKey:
                    parent_node_for_delete.LeftChild=children
                else:
                    pass
            # Блок если если левый ребенок
            elif node_for_delete.LeftChild!=None and node_for_delete.RightChild==None:
                children=node_for_delete.LeftChild
                children.Parent=parent_node_for_delete
                if node_for_delete.NodeKey>parent_node_for_delete.NodeKey:
                    parent_node_for_delete.RightChild=children
                elif node_for_delete.NodeKey<parent_node_for_delete.NodeKey:
                    parent_node_for_delete.LeftChild=children
                else:
                    pass
            # Блок если нет детей
            elif node_for_delete.LeftChild==None and node_for_delete.RightChild==None:
                if node_for_delete.NodeKey>parent_node_for_delete.NodeKey:
                    parent_node_for_delete.RightChild=None
                elif node_for_delete.NodeKey<parent_node_for_delete.NodeKey:
                    parent_node_for_delete.LeftChild=None
                else:
                    pass
            return True
        else:
            return False
    
    def printAll(self):
        all=self.GetAllNodes()
        for node in all:
            print(node.NodeKey,node,"*Родитель",node.Parent,"*левый потомок",node.LeftChild,"*правый потомок",node.RightChild,"*")

    def Count(self):
        # количество узлов в дереве
        q_ty=0
        allElements=self.GetAllNodes()
        for element in allElements:
            if element.NodeKey!=None:
                q_ty+=1
        return q_ty

    def WideAllNodes(self):
        #Реализация обхода в ширину
        if self.Root!=None:
            parents=[]
            children=[]
            output=[]
            output.append(self.Root)
            parents.append(self.Root)
            while parents!=[]:
                for everynode in parents:
                    if everynode.LeftChild!=None:
                        children.append(everynode.LeftChild)
                        output.append(everynode.LeftChild)
                    else:
                        pass
                    if everynode.RightChild!=None:
                        children.append(everynode.RightChild)
                        output.append(everynode.RightChild)
                    else:
                        pass
                parents.clear()
                for everynode in children:
                    if everynode!=None:
                        parents.append(everynode)
                    else:
                        pass
                children.clear()
            output=tuple(output)
            return output

    def DeepAllNodes(self,par=0,Roots=[],Q_tys=[]):
        #Обход дерева в глубину
        Roots.append(self.Root)
        Q_tys.append(self.Count())
       # print(Roots)
       # print(Q_tys)
        node=self.Root
        res=[]
        parent=node
        if par==0:
            if node.LeftChild!=None:
                self.Root=self.Root.LeftChild
                res=self.DeepAllNodes(par=0)
            res.append(node)
            if node.RightChild!=None:
                self.Root=parent.RightChild
                res=res+self.DeepAllNodes(par=0)
        elif par==1:
            if node.LeftChild!=None:
                self.Root=self.Root.LeftChild
                res=self.DeepAllNodes(par=1)
            if node.RightChild!=None:
                self.Root=parent.RightChild
                res=res+self.DeepAllNodes(par=1)
            res.append(node)
        elif par==2:
            res.append(node)
            if node.LeftChild!=None:
                self.Root=self.Root.LeftChild
                res=res+self.DeepAllNodes(par=2)
            if node.RightChild!=None:
                self.Root=parent.RightChild
                res=res+self.DeepAllNodes(par=2)
        if len(res)==Q_tys[0]: 
            self.Root=Roots[0]
            Roots.clear()
            Q_tys.clear()
            out=tuple(res)
            return out
        else:
            return res


            



            




"""


A=BSTNode(8,"значение 1",None)
BT=BST(A)
BT.AddKeyValue(4,"значение 2")
BT.AddKeyValue(12,"значение 3")
BT.AddKeyValue(2,"значение 4")
BT.AddKeyValue(6,"значение 5")
BT.AddKeyValue(10,"значение 6")
BT.AddKeyValue(14,"значение 6")
BT.AddKeyValue(1,"значение 6")
BT.AddKeyValue(3,"значение 6")
BT.AddKeyValue(5,"значение 6")
BT.AddKeyValue(7,"значение 6")
BT.AddKeyValue(9,"значение 6")
BT.AddKeyValue(11,"значение 6")
BT.AddKeyValue(13,"значение 6")
BT.AddKeyValue(15,"значение 6")
print("***********************")
#BT.printAll()
#print(BT.FindNodeByKey(47))
#BT.DeleteNodeByKey(12)
#print(BT.Count())
print("***********************")
#print(BT.GetAllNodes())
print("***********************")
BT.printAll()
#M=BT.FindNodeByKey(47)
#print(BT.FindNodeByKey(47))
print(BT.WideAllNodes())
print(BT.DeepAllNodes(0))
print(BT.DeepAllNodes(1))
print(BT.DeepAllNodes(2))
"""