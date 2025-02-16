class MinHeap:
    # 힙 자료구조 => 완전 이진 트리 -> 리스트를 사용할 것
    def __init__(self):
        self.heap= []

    # heap에 새로운 요소를 추가
    def heappush(self, item):
        self.heap.append(item) # 마지막 노드에 값 추가
        # heap 속성을 유지할 수 있도록 메서드를 호출
        self._sift_up(len(self.heap)-1) # 가장 마지막 인덱스
    # 힙 속성 유지를 위해 사용되는 보조 메서드
    def _sift_up(self, idx):
        parent_idx = (idx-1)//2 # 부모 노드와 나를 비교하기 위해서
        # 1. 루트노드에 도달할 때까지 계속 조사
        # 2. 내 값이 부모 노드 값보다 작다면 (최소힙) 부모와 swap
        while idx>0 and self.heap[idx] < self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            # swap 이후, 조사 index 업데이트
            idx = parent_idx
            parent_idx = (idx-1)//2
    # 최소 요소를 제거하고 반환
    def heappop(self):
        if len(self.heap)==0:
            raise IndexError('heap is empty')
        if len(self.heap)==1:
            return self.heap.pop() # 길이가 1이면 루트노드 반환하고 종료한다.
        root = self.heap[0]
        # 마지막 요소를 루트 위치로 이동
        self.heap[0] = self.heap.pop() # 마지막 요소를 루트 위치로 이동
        self._sift_down(0)    # 최소 힙 상태 유지 sift_down 연산을 진행해야 한다.
        return root
    # 삭제 후 최소 힙 상태를 유지하기 위한 보조 메서드
    def _sift_down(self,idx):
        N = len(self.heap)
        smallest = idx # 가장 작은 요소의 인덱스를 초기화
        left = 2*idx +1# 왼쪽 자식의 index
        right =2*idx +2  # 오른쪽 자식의 index
        '''
        왼쪽, 오른쪽 누구를 먼저 조사해야 하느냐?
        -> 완전 이진트리를  구성하고 있다면 
        -> 항상 왼쪽 자식이 있는데, 오른쪽 자식이 없는 경우는 있어도
        -> 오른쪽 자식이 있는데, 왼쪽 자식이 없는 경우는 없다. 
        '''
        if left< N and self.heap[left] < self.heap[smallest]:
            smallest = left # 왼쪽 자식이 현재 위치보다 작으면 swap
        if right < N  and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx: # 가장 작은 값이 조사 시작 idx와 다르다면
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._sift_down(smallest) # 자식 노드에 대해서 재귀적으로 sift-down
    # 리스트를 주면 heap으로 바꿔주면 좋겠다.
    def heapify(self, array):
        self.heap = array[:] # 주어진 리스트를 복사해서 내 heap 위치에 할당
        N = len(self.heap)
        # 힙의 구조에 맞게 처리
        for idx in range(N//2-1, -1, -1):
            self._sift_down(idx)

# 힙은 정렬된 상태를 보장하지 않는다.

mh = MinHeap()
mh.heappush(3)
mh.heappush(1)
mh.heappush(2)
print(mh.heap)
mh.heappush(0)
print(mh.heap)
print(mh.heappop())
print(mh.heap)

mh2 = MinHeap()
arr = [9,6,14,7,2,1]
mh2.heapify(arr)
print(mh2.heap)