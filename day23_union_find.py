class UnionFind():
    """Class implements union-find data structure"""
    def __init__(self, array):
        self.elements = {el: el for el in array}
        self.leaders = {el: [el] for el in array}

    def union(self, el1, el2):
        """combines groups that includes el1 and el2"""
        leader1 = self.elements[el1]
        leader2 = self.elements[el2]
        if leader1 != leader2:
            if len(self.leaders[leader1]) >= len(self.leaders[leader2]):
                new_leader = leader1
                leader_to_update = leader2
            else:
                new_leader = leader2
                leader_to_update = leader1
            for element in self.leaders[leader_to_update]:
                self.elements[element] = new_leader
            self.leaders[new_leader] += self.leaders[leader_to_update]
            del self.leaders[leader_to_update]

    def find(self, element):
        """returns leader of the group that includes el"""
        return self.elements[element]

    def count_groups(self):
        """returns the number of distincs groups"""
        return len(self.leaders)

def test_union_find():
    number_of_elements = 8
    array = range(number_of_elements)
    my_union_find = UnionFind(array)
    for i in array:
        assert my_union_find.find(i) == i
    assert my_union_find.count_groups() == number_of_elements
    my_union_find.union(0, 5)
    assert my_union_find.find(0) == my_union_find.find(5)
    my_union_find.union(5, 1)
    assert my_union_find.find(0) == my_union_find.find(1)
    assert my_union_find.count_groups() == number_of_elements - 2
    my_union_find.union(5, 2)
    assert my_union_find.find(2) == 0

if __name__ == "__main__":
    test_union_find()
