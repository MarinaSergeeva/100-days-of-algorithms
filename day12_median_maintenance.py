import heapq

class MedianMaintainer:
    def __init__(self):
        self._minheap = [] # for smallest half of fthe array, uses negated numbers
        self._maxheap = [] # for largest half of the array
        self.median = None # if similar number of elements - use value form maxheap

    def insert_element(self, el):
        if len(self._minheap) == 0 and len(self._maxheap) == 0:
            self._maxheap.append(el)
            self.median = el
        else:
            if el >= self._maxheap[0]:
                heapq.heappush(self._maxheap, el)
                if len(self._maxheap) > len(self._minheap) + 1:
                    el_to_move = heapq.heappop(self._maxheap)
                    heapq.heappush(self._minheap, -el_to_move)
            else:
                heapq.heappush(self._minheap, -el)
                if len(self._minheap) > len(self._maxheap):
                    el_to_move = - heapq.heappop(self._minheap)
                    heapq.heappush(self._maxheap, el_to_move)
            self.median = self._maxheap[0]

    def get_median(self):
        return self.median

def test_maintain_median():
    myMedianMaintainer = MedianMaintainer()
    input_array = [1, 5, 7, 3, 4]
    expected_medians = []
    for el in input_array:
        myMedianMaintainer.insert_element(el)
        expected_medians.append(myMedianMaintainer.get_median())
    assert expected_medians == [1, 5, 5, 5, 4]
