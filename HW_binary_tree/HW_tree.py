class Node:
    """
    Класс, представляющий узел бинарного дерева.
    
    Атрибуты класса:
        value (int): значение узла
        left (Node): ссылка на левого потомка
        right (Node): ссылка на правого потомка
        height (int): высота поддерева с корнем в данном узле
    """
    def __init__(self, value) -> None:
        """
        Конструктор класса Node.
        
        Параметры:
            value (int): значение узла
        """
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self) -> str:
        """Метод для отображения информации об узле в строковом виде."""

        res = f'\nзначение и высота поддерева запрашиваемого узла: {self.value} / {self.height}'
        if self.left:
            res +=  f' значение и высота левого потомка: {self.left.value} / {self.left.height}'
        if self.right:
            res +=  f' значение и высота правого потомка: {self.right.value} / {self.right.height}'            
        return res

class Tree:
    """        
        Класс, представляющий собой сбалансированное по высоте бинарное дерево поиска.
    
    Атрибуты класса:
        root (Node): ссылка на корневой узел дерева
        count (int): указывает на количество узлов в дереве
    """
    def __init__(self, root) -> None:
        self.root = root
        self.count = 1
        """
        Конструктор класса Tree.
        
        Параметры:
            root (Node): ссылка на корневой узел дерева
        """
     
    def search(self, node, data, parent = None) -> tuple:
        """
        Метод, позволяющий найти узел по передаваемому в метод значению.
        
        Параметры:
            node (Node): ссылка на узел дерева, с которого будет начинаться поиск
            data (int): значение, по которому ищем узел
            parent (Node): ссылка на узел, являющийся родительским по отношению к узлу, от которого начинается поиск
        """        
        if node is None or data == node.value:
            return node, parent
        if data > node.value: 
            return self.search(node.right, data, node)
        if data < node.value:
            return self.search(node.left, data, node)

    def insert(self, value) -> None:
        """
        Метод, который запускает добавление узла в дерево путем применения метода add_node()
        Если узел с таким значением уже существует, то он не будет добавлен
        Также метод присваивает новый root после балансировки методом add_node()

        Параметры:
            value (int): значение узла, создаваемого при помощи этого метода 
        """     
        res = self.search(self.root, value)
        if res[0] is None:
            self.root = self.add_node(self.root, value)
            self.count += 1
        else:
            print(f'Узел с таким значением {value} уже существует, поэтому мы ничего не добавили')        

    def add_node(self, node, value) -> Node:
        """
        Метод, который позволяет определить, куда будем в дерево добавлять новый узел, проверить не нарушается ли баланс
        (т.е. не отличается ли высота поддеревьев одного узла более чем на 1) 
        и осуществить балансировку дерева в связи с добавлением нового узла, если отличается.

        Параметры:
            node (Node): ссылка на узел дерева, с которого будет начинаться проверка на возможность добавления узла
            value (int): значение узла, создаваемого  при помощи этого метода 
        """     
        if node is None: 
            return Node(value)
        if node.value < value:
            node.right = self.add_node(node.right, value)
        else: 
            node.left = self.add_node(node.left, value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right)) 
        
        return self.balansing(node, value)   

    def get_height(self, node) -> int:
        """
        Метод, позволяющий определить высоту (под)дерева.
        
        Параметры:
            node (Node): ссылка на узел дерева, являющийся корневым узлом (под)дерева, высоту которого будем определять
        """
        if node is None: 
            return 0
        else:
            return node.height

    def balansing(self, node, value) -> None:
        """
        Метод, который запускает вращение в нужную сторону, если оно необходимо

        Параметры:
            node (Node): ссылка на узел дерева, длина чтьих поддеревьев сравнивается для выявления необходимости запуска балансировки
            value (int): значение узла, который мы добавляли в дерево методом add_node 
        """    

        rotation_direction = self.get_rotation_direction(node)
        if rotation_direction > 1:
            if value < node.left.value:
                return self.rotate_right(node) 
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
        
        if rotation_direction < -1:
            if  value > node.right.value:
                return self.rotate_left(node) 
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node) 
        return node
        
    def get_rotation_direction(self, node) -> int:
        """
        Метод, который позволяет вычисляющий насколько отличается длина поддеревьев узла

        Параметры:
            node (Node): ссылка на узел дерева, высоту поддеревьев которого мы сравнивание
        """     
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def rotate_left(self, node) -> None:
        """
        Метод, при помощи которого осуществляется левое вращение. 

        Параметры:
            node (Node): ссылка на узел дерева, длина правого поддерева которого превышает длину левого более чем на 1
        """     

        new_root = node.right
        temp = new_root.left

        new_root.left = node
        node.right = temp

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1

        return new_root
       
    def rotate_right(self, node) -> None:
        """
        Метод, при помощи которого осуществляется правое вращение. 

        Параметры:
            node (Node): ссылка на узел дерева, длина левого поддерева которого превышает длину правого более чем на 1
        """    
        new_root = node.left
        temp = new_root.right

        new_root.right = node
        node.left = temp

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        new_root.height = max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1

        return new_root    
 
    def delete(self, value) -> None:
        """
        Метод, который запускает удаление узла дерева методом delete_node()
        Также метод присваивает новый root после балансировки после удаления узла

        Параметры:
            value (int): значение узла к удалению 
        """     
        self.root = self.delete_node(self.root, value)
        self.count -= 1

    def delete_node(self, node, value) -> None:
        """
        Метод, который находит и удаляет узел, значение которого равно value, 
        а также осуществляет балансировку дерева после удаления

        Параметры:
            node (Node): по сути это рутовый узел
            value (int): значение узла к удалению 
        """     
        if node is None:
            return node
        
        if value < node.value:
            node.left = self.delete_node(node.left, value)
        elif value > node.value:
            node.right = self.delete_node(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            
            temp = self.get_min_node(node.right)
            node.value = temp.value
            node.right = self.delete_node(node.right, temp.value)

        if node is None:
            return None
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        rotation_direction = self.get_rotation_direction(node)
        if rotation_direction > 1:
            if self.get_rotation_direction(node.left) >= 0:
                return self.rotate_right(node) 
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
        
        if rotation_direction < -1:
            if  self.get_rotation_direction(node.right) <= 0:
                return self.rotate_left(node) 
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node) 
        return node

    def get_min_node(self, node) -> Node:
        """
        Метод, необходим для реализации метода delete_node, 
        применяется, если у удаляемого узла есть и правый и левый потомок.
        Метод находит узел с минимальным значением у правого потомка удаляемого узла 
        Значение этого узла потом в методе delete_node перетрет значение удаляемого узла

        Параметры:
            node (Node): по сути это рутовый узел
            value (int): значение узла к удалению 
        """    
        current = node
        while current.left is not None:
            current = current.left
        return current
            

# initial_node = Node(9)
# tree_1 = Tree(initial_node)
# tree_1.insert(8)
# tree_1.insert(7)
# tree_1.insert(6)
# tree_1.insert(5)
# tree_1.insert(10)
# tree_1.insert(12)
# print(f'\nколичество элементов дерева: {tree_1.count}, root дерева:{tree_1.root}')
# tree_1.delete(10)
# print(f'\nколичество элементов дерева: {tree_1.count}, root дерева:{tree_1.root}')

