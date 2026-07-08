class NodeBST:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.jumlah_node = 0

    def insert(self, key, data):
        self.root = self._insert(self.root, key, data)

    def _insert(self, node, key, data):
        if node is None:
            self.jumlah_node += 1
            return NodeBST(key, data)

        if key < node.key:
            node.left = self._insert(node.left, key, data)
        elif key > node.key:
            node.right = self._insert(node.right, key, data)
        else:
            node.data = data

        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.data
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root, hasil_hapus = self._delete(self.root, key)
        return hasil_hapus

    def _delete(self, node, key):
        if node is None:
            return node, None

        if key < node.key:
            node.left, hasil = self._delete(node.left, key)
            return node, hasil
        elif key > node.key:
            node.right, hasil = self._delete(node.right, key)
            return node, hasil
        else:
            hasil = node.data
            self.jumlah_node -= 1

            if node.left is None:
                return node.right, hasil
            if node.right is None:
                return node.left, hasil
            pengganti = node.right
            while pengganti.left is not None:
                pengganti = pengganti.left

            node.key = pengganti.key
            node.data = pengganti.data
            self.jumlah_node += 1 
            node.right, _ = self._delete(node.right, pengganti.key)
            return node, hasil

    def inorder(self):
        hasil = []
        self._inorder(self.root, hasil)
        return hasil

    def _inorder(self, node, hasil):
        if node is None:
            return
        self._inorder(node.left, hasil)
        hasil.append(node.data)
        self._inorder(node.right, hasil)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        kiri = self._height(node.left)
        kanan = self._height(node.right)
        return 1 + max(kiri, kanan)

    def count_nodes(self):
        return self.jumlah_node

    def is_empty(self):
        return self.root is None

    def display(self):
        data_order = self.inorder()
        if not data_order:
            print("  (belum ada order aktif)")
            return
        for d in data_order:
            print(f"  - {d}")