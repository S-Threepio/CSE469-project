#!/usr/bin/python3
import struct
#self define node class
class Node(object):
	def __init__(self):
		self.data = None # contains the data
		self.next = None # contains the reference to the next node
		#the data should be pack in 32s d 16s I 12s I
		#self.blockData=struct.pack('32s d 16s I 12s I')

#a skeleton of bchoc we should implement it in more detail
class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	def append(self, data):
		self.size += 1
		new_node = Node() # create a new node
		new_node.data = data
		if(self.head==None):
			self.head = new_node
		else:
			temp_node=self.head
			while temp_node.next:
				temp_node=temp_node.next
			temp_node.next=new_node
	def reverse(self):
		pre_node=self.head
		#if the list size is 2
		if(self.size==2):
			cur_node=pre_node.next
			cur_node.next=pre_node
			pre_node.next=None
			self.head=cur_node
		else:
			cur_node=pre_node.next
			next_node=cur_node.next
			next_node=self.head
			while cur_node.next:
				next_node=cur_node.next
			
	def remove(self,data):
		pre_node=self.head
		#if remove item is the head
		if(pre_node.data==data):
			self.head=self.head.next
			pre_node.next=None
		#remove item is not in the head
		else:
			cur_node=pre_node.next
			while(cur_node.data!=data):
				pre_node=pre_node.next
				cur_node=pre_node.next
			#if the remove item is at the end of the list
			if(cur_node.next==None):
				pre_node.next=None
			else:
				pre_node.next=cur_node.next
				cur_node.next=None
			
			
	def verify(self):
		temp_node=self.head
	def log(self):
		temp_node=self.head
	def list_print(self):
		node = self.head # cant point to ll!
		while node:
			print(node.data)
			node = node.next
	def init(self):
		temp_node=self.head
		
#parse the input 
input=input()
inputArray=input.split(" ")
if(inputArray[0]=="bchoc"):
    #add commands
    if(inputArray[1]=="add"):
        print("perform add command")
        if(inputArray[2]=="-c"):
            case_id=inputArray[3]
            if(inputArray[4]=="-i"):
                item_id=inputArray[5]
                print(case_id,item_id)
                #call linkedlist add method here
            else:
                sys.exit("wrong argument")
        else:
            sys.exit("wrong argument")
    #checkout command
    elif(inputArray[1]=="checkout"):
        print("perform checkout command")
    elif(inputArray[1]=="checkin"):
        print("perform checkin command")
    elif(inputArray[1]=="log"):
        print("perform log command")
    elif(inputArray[1]=="remove"):
        print("perform remove command")
    elif(inputArray[1]=="init"):
        print("perform init command")
    elif(inputArray[1]=="verify"):
        print("perform verify command")
    else:
        sys.exit("unexpected commands")
else:
    sys.exit("unexpected input format")
print(inputArray)

#pack the data should be stored in bchoc
#test for linkedlist methods
print("test for linkedList method")
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.reverse()
ll.list_print()

