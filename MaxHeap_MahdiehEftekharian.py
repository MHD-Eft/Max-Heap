#Implementation of Priority Queue by using Max Heap
#Author: Mahdieh Eftekharian
#Sutdent Num : 992164001
class MaxHeap:
    def __init__(self):
        self.Heap = []
        self.size = 0

	# Function to return the position of parent for the node currently at index
    def parent(self, index):
        return index // 2

	# Function to return existance of the left child for the node currently
    def leftChild(self, index):
        if ((2 * index) + 1 < len(self.Heap)) :
            return True
        else:
            return False

	# Function to return existance of the right child for the node currently
    def rightChild(self, index):
        if ((2 * index) + 2 < len(self.Heap)) :
            return True
        else:
            return False
    #This function copy passed heap to object by value   
    def copy(self,maxHeap : 'MaxHeap'):
        self.Heap=maxHeap.Heap.copy()
        self.size=len(self.Heap)    

	# returns true if the node is a leaf node
    def isLeaf(self, index):
		
        if index >= (self.size//2) and index < len(self.Heap):
            return True
        return False

	# swap two nodes of the heap
    def swap(self, findex, sindex):
        self.Heap[findex], self.Heap[sindex] = (self.Heap[sindex],self.Heap[findex])

	# fix the heap feature of tree
    def maxHeapify(self, index):

		# If the node is a non-leaf node and smaller than any of its child
        if not self.isLeaf(index):
            if (self.rightChild(index) and self.leftChild(index)):
                if (self.Heap[index] < self.Heap[(2 * index) + 1] or
					self.Heap[index] < self.Heap[(2 * index) + 2]):

					# Swap with the left child and heapify the left child
                    if (self.Heap[(2 * index) + 1] >
						self.Heap[(2 * index) + 2]):
                        self.swap(index, (2 * index) + 1)
                        self.maxHeapify((2 * index) + 1)

					# Swap with the right child and heapify the right child
                    else:
                        self.swap(index, (2 * index) + 2)
                        self.maxHeapify((2 * index) + 2)

            elif (self.leftChild(index) and self.Heap[index] < self.Heap[(2 * index) + 1] ):
                self.swap(index, (2 * index) + 1)

	#Inserting a node into the heap
    def insert(self, element):
		
        if (self.size > len(self.Heap)):
            return
        self.Heap.append(element) 
        current = self.size
        self.size += 1
        while (self.Heap[current] > self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)


       
	#Printing the element of the heap
    def Print(self):
		
        for i in range(0, (self.size // 2)):
            print("PARENT : " + str(self.Heap[i]) , end=" ")
            if ((2 * i) + 1 < len(self.Heap)) :
                print("LEFT CHILD : " + str(self.Heap[2 * i +1]) , end=" ")
            if ((2 * i) + 2 < len(self.Heap)) :
                print(	"RIGHT CHILD : " + str(self.Heap[2 * i + 2]))
        if (self.size ==1):
            print("PARENT : " + str(self.Heap[0]))
        print()
			

    
    
	# return and remove the maximum element from the heap
    def extract_max(self):
        if 1<len(self.Heap):
            max = self.Heap[0]
            self.size -= 1
            self.Heap[0] = self.Heap.pop()
            self.maxHeapify(0)
            return max
        elif 1==len(self.Heap):
            self.size -= 1
            return self.Heap.pop()
        return None
    
    #returns the maximum value of heap
    def find_max(self):
        if len(self.Heap):
            return self.Heap[0]

	#get two max heap and merge them into third max heap and return the third max heap
    #priority = 0 : normal merge with no priority
    #priority = 1 : gives the elements of first heap higher priority than second heap for merging into third heap
    #priority = 2 : gives the elements of second heap higher priority than first heap for merging into third heap

    def merge( self,max_heap1 : 'MaxHeap' ,max_heap2 : 'MaxHeap',priority = 0):
        len1=max_heap1.size
        len2=max_heap2.size
        mergedMaxHeap = MaxHeap()
        if priority == 0: 
            if len1 < len2:
                for i in range(len1):
                    mergedMaxHeap.insert(max_heap1.extract_max())
                    mergedMaxHeap.insert(max_heap2.extract_max())
                len2=max_heap2.size
                for i in range(len2):
                    mergedMaxHeap.insert(max_heap2.extract_max())
            elif len2 < len1:
                for i in range(len2):
                    mergedMaxHeap.insert(max_heap1.extract_max())
                    mergedMaxHeap.insert(max_heap2.extract_max())
                len1=max_heap1.size
                for i in range(len1):
                    mergedMaxHeap.insert(max_heap1.extract_max())
            else:
                for i in range(len2):
                    mergedMaxHeap.insert(max_heap1.extract_max())
                    mergedMaxHeap.insert(max_heap2.extract_max())

        elif priority == 1:
            if type(max_heap2.find_max())==str :
                max_heap1.add_to_all( 2*ord(max_heap2.find_max()))
            else:
                max_heap1.add_to_all( 2*max_heap2.find_max())
            mergedMaxHeap = max_heap1
            for i in range(len2):
                mergedMaxHeap.insert(max_heap2.extract_max())

        elif priority == 2:
            if type(max_heap1.find_max())==str :
                max_heap2.add_to_all(2*ord(max_heap1.find_max()))
            else:
                max_heap2.add_to_all( 2*max_heap1.find_max())
            mergedMaxHeap = max_heap2
            for i in range(len1):
                mergedMaxHeap.insert(max_heap1.extract_max())
		
        return mergedMaxHeap
    
    #Increases the priority of all elements of passed heap by adding k to elements
    def add_to_all(self , k):
        if self.size > 0 :
            if type(k)==str and type(self.Heap[0])==str:
                for i in range(self.size):
                    self.Heap[i]=chr(ord(self.Heap[i])+ord(k))

            elif type(k)==int and type(self.Heap[0])==str:
                for i in range(self.size):
                    self.Heap[i]=chr(ord(self.Heap[i])+k)
            elif type(k)==str:
                for i in range(self.size):
                    self.Heap[i]=self.Heap[i]+ord(k)
            else:
                for i in range(self.size):
                    self.Heap[i]=self.Heap[i]+k
        return 


# main
max_heap1 = MaxHeap()
max_heap2 = MaxHeap()
max_heap1copy = MaxHeap()
max_heap2copy = MaxHeap()
merged_max_heap = MaxHeap()
max_heap1.insert(5)
max_heap1.insert(3)
max_heap1.insert(17)
print("current max : " ,max_heap1.find_max())
max_heap1.insert(10)
max_heap1.insert(84)
max_heap1.insert(6)
max_heap1.insert(6)
max_heap1.insert(1)
max_heap1.insert(53)
print("maxHeap 1 : ")
max_heap1.Print()
print(max_heap1.size)
max_heap2.insert(1)
max_heap2.insert(3)
max_heap2.insert(300)
max_heap2.find_max()
print("current max : " ,max_heap2.find_max())
max_heap2.insert(4)
max_heap2.insert(11)
max_heap2.insert(0)
max_heap2.insert(13)
max_heap2.insert(5)
print('MAX HEAP 2 :')
max_heap2.Print()
print(max_heap2.size)
max_heap1copy.copy(max_heap1)
max_heap2copy.copy(max_heap2)
merged_max_heap=merged_max_heap.merge(max_heap1copy,max_heap2copy,0)
print('Merged HEAP :')
merged_max_heap.Print()
print(merged_max_heap.size)

                                 
                     





                             
		    



