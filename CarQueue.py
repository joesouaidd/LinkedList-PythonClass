class car:
    
    def __init__(self, name, color, plate):
        self.name = name
        self.color = color
        self.plate = plate


class Node:
    def __init__(self, next, car):

        self.next = next
        self.car = car


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        # O(1)
        if self.size == 0:
            return True
        else:
            return False

    # add head: takes info, adds a node containing info to the beginning of the list
    def addHead(self, car):
        #O(1)
        n = Node(None, car)
        if self.isEmpty():  # the LL is empty
            self.head = n
            self.tail = n
            self.size += 1
        else:  # LL contains elements, I need to add at head
            n.next = self.head
            self.head = n
            self.size += 1

    # add Tail: takes info, add a node containing info to the end of the LL
    # O(1)
    def addTail(self, car):
        n = Node(None, car)
        if self.isEmpty():  # the LL is empty
            self.head = n
            self.tail = n
            self.size += 1

        else:  # the LL contains nodes
            self.tail.next = n
            self.tail = n
            self.size += 1

    # remove head: removes the first node in the LL and returns its value
    def removeHead(self):
        #O(1)
        if self.isEmpty():
            return None

        if self.size == 1:  # the LL contains a single node
            temp = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return temp

        else:  #the LL contians more than one element
            temp = self.head
            self.head = self.head.next
            self.size -= 1
            return temp

    # remove tail: removes the last node in the LL and returns its value
    #O(n), n being the size of the LL
    def removeTail(self):
        if self.isEmpty():
            return None
        elif self.size == 1:
            value = self.head.car.name
            self.head = None
            self.tail = None
            self.size = 0
            return value
        else:
            value = self.tail.car.name
            temp = self.head  # 1 jump
            for i in range(self.size - 2):  #O(n)
                temp = temp.next
                print("temp", temp.info)
            temp.next = None
            self.tail = temp
            self.size -= 1
            return value

    # prints the elements in the list
    def printElements(self):
        #O(n), n being the number of elements in the list
        temp = self.head
        while temp != None:
            print(temp.car.name, end=" ")
            temp = temp.next
        print()


class Queue:
    def __init__(self):
        self.elements = LinkedList()

    #O(1)
    def isEmptyQueue(self):
        return self.elements.isEmpty()

    #O(1)
    def enqueue(self, item):
        self.elements.addTail(item)

    #O(1)
    def dequeue(self):
        return self.elements.removeHead()

    def front(self):
        return self.head

    def size(self):
        return self.head.size


print("Hello and welcome to the car queue: \n")
q = Queue()
while True:
    sel = int(
        input("\n Please enter \n1 to insert a car \
  \n2 to remove a car \n==> "))

    if (sel == 1):
        carName = str(input("please enter the car Name: "))
        carColor = str(input("please enter the car Color: "))
        carPlate = int(input("please enter the car Plate: "))

        q.enqueue(car(carName, carColor, carPlate))

        q.elements.printElements()

    if (sel == 2):
        carRemoved = q.dequeue()
        print("The car removed is : ", carRemoved.car.name + "\nColor ",
              carRemoved.car.color + "\nPlate ", carRemoved.car.plate)
        q.elements.printElements()
