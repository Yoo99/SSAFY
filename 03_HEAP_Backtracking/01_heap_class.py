#  최소 힙 구현
class MinHeap:
    # 힙 자료구조 -> 완전 이진트리로 진행 -> 따라서 리스트를 쓸 예정
    def __init__(self):
        self.heap = []
    # heap에 새로운 요소를 추가
    def heappush(self,item):
        self.heap.append(item) # 마지막 노드에 값 추가
        # 힙 속성을 유지 할 수 있도록 메서드를 호출
        self._sift_up(len(self.heap) -1)
    # heap 속성 유지를 위해 사용되는 보조메서드
    def _sift_up(self,idx):
        parent_idx = (idx -1)//2 # 부모 노드와 나를 비교하기 위해서
        # 1. 루트 노드에 도달할 때까지 계속 조사
        # 2. 내 값이 부모 노드 값보다 작다면 (최소힙) 부모와 swap
        while idx > 0 and self.heap[idx] <self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx# swap 이후, 조사 index 업데이트
            parent_idx = (idx-1)//2
# 힙은 정렬되어 있음을 의미하지는 않는다.
# 최소 요소를 제거하고 반환
    def heappop(self):
        if len(self.heap) ==0:
            raise IndexError('힙이 비었습니다.')
        if len(self.heap) == 1:
            return self.heap.pop() # 길이가 1이면 루트노드 반환하고 종료
        root = self.heap[0]
        # 마지막 요소를 루트 위치로 이동한다.
        self.heap[0] = self.heap.pop()
        self._sift_down(0)# 최소힙의 사태 유지가 되지 않는다. shift down 연산
        return root
    # 삭제 후 최소 힙 상태를 유지하기 위한 보조 메서드
    def _sift_down(self,idx):
        N = len(self.heap)  # 전체 길이 처음에 초기화
        smallest = idx # 가장 작은 요소의 인덱스를 초기화
        left = 2 *idx+1 # 왼쪽 자식의 idx
        right = 2*idx +2  # 오른쪽 자식의 idx
        '''
        완전 이진트리라면
        왼쪽, 오른쪽 누구를 먼저 조사해야 하느냐? 
        -> 완전 이진 트리를 구성하고 있다면 
        -> 항상 왼쪽 자식이 있는데, 오른쪽 자식이 없는 경우는 있어도 
        -> 오른쪽 자식이 있는데, 왼쪽 자식이 없는 경우는 없다. 
        '''
        if left< N and self.heap[left]<self.heap[smallest]:
            smallest = left # 왼쪽 자식이 현재 위치보다 작으면 swap
        if right < N and self.heap[left] < self.heap[smallest]:
            smallest = right # 오른쪽  자식이 현재 위치보다 작으면 swap
        if smallest != idx : # 가장 작은 값이 조사 시작 idx와 다르다면
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._sift_down(smallest) # 자식 노드에 대해서 재귀적으로 sift-down
# 리스트를 주면 heap으로 바꿔주면 좋겠다.
    def heapify(self, array):
        self.heap = array[:]  # 주어진 리스트를 복사해서 내 heap 위치에 할당해준다
        N = len(self.heap)
        # 힙의 구조에 맞게 처리
        # 부모 노드에 있는 애부터 처리를 해나가야 한다.
        # 내가 가지고 있는 리프 노드가 되기 전까지 모든 과정에 대해서 작업을 진행해야 한다.
        # for문으로 계속해서 sift_down 호출하는 방식으로 진행할 예정
        for idx in range(N//2-1, -1, -1):
            self._sift_down(idx)

mh = MinHeap() # instance 생성
mh.heappush(3)
mh.heappush(1)
mh.heappush(2)
print(mh.heap)
mh.heappush(0)
print(mh.heap)

print(mh.heappop())
print(mh.heap)

mh2 = MinHeap()
arr  = [9,6,14,7,2,1]
mh2.heapify(arr)
print(mh2.heap)