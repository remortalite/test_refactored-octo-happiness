class TreeStore:

    def __init__(self, items: list[dict]):
        self.items = items
        self.tree = self._parseTreeFromItems()

    def _parseTreeFromItems(self):
        tree = dict()
        for item in self.items:
            tree[item["id"]] = item
        return tree

    def getAll(self):
        return self.items

    def getItem(self, id: int):
        return self.tree.get(id, None)

    def getChildren(self, id: int):
        children = []
        for item in items:
            if item['parent'] == id:
                children.append(item)
        return children

    def getAllParents(self, id: int):
        item = self.getItem(id=id)
        parents = []
        while True:
            parent_id = item['parent']
            if parent_id == 'root':
                break
            item = self.getItem(id=parent_id)
            parents.append(item)
        return parents


if __name__ == '__main__':
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    ts = TreeStore(items)

    print(ts.getAll())
    print(ts.getItem(id=1))
    print(ts.getChildren(id=4))
    print(ts.getAllParents(id=7))

