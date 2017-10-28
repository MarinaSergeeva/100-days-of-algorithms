class Heap:
    def __init__(self, array=None):
        self.tree = []
        if array is not None:
            self.tree = array
            self.heapify()
            # for el in array:
            #     self.push(el)

    def push(self, el):
        self.tree.append(el)
        position = len(self.tree) - 1
        parent_position = position >> 1
        while position != 0 and self.tree[parent_position] > self.tree[position]:
            self.tree[parent_position], self.tree[position] = self.tree[position], self.tree[parent_position]
            position = parent_position
            parent_position = position >> 1

    def pop(self):
        res = self.tree[0]
        last_el = self.tree.pop()
        if len(self.tree) > 0:
            self.tree[0] = last_el
            self.bubble_down(0)
        return res

    def bubble_down(self, position):
        # children of element i are in positions 2 * i + 1 and 2 * i + 2
        left_child = (position << 1) + 1
        while left_child < len(self.tree):
            right_child = (position << 1) + 2
            if self.tree[position] <= self.tree[left_child] and \
                    (right_child >= len(self.tree) or self.tree[position] <= self.tree[right_child]):
                break # the heap property is restored
            if right_child >= len(self.tree) or self.tree[right_child] >= self.tree[left_child]:
                child_to_replace = left_child
            else:
                child_to_replace = right_child
            self.tree[position], self.tree[child_to_replace] = self.tree[child_to_replace], self.tree[position]
            position = child_to_replace
            left_child = (position << 1) + 1

    def heapify(self):
        for i in range(len(self.tree) // 2, -1, -1):
            self.bubble_down(i)

def test_heap():
    my_list = [3, 8, 1, 5, 2]
    myHeap = Heap(my_list)
    assert myHeap.tree == [1, 2, 3, 5, 8]
    for el in sorted(my_list):
        assert myHeap.pop() == el
    myHeap.push(0)
    assert myHeap.pop() == 0

if __name__ == "__main__":
    test_heap()
