#!/usr/bin/python3
from datetime import datetime
import os
import os.path
import struct
import hashlib
import datetime
import time
from decimal import Decimal
import sys

# Path to check the blockchain file
os.environ["BCHOC_FILE_PATH "] = "./"

#we need to implement these functions 
def append(case_id,item_list):
	#get prehash value
	bchoc_file_read=open("bchoc_file.bin","rb")
	data=bchoc_file_read.read()
	index=0
	length=0
	while index<=(len(data)-1):
		print(datetime.datetime.fromtimestamp(struct.unpack('d',data[index+32:index+40])[0]))
		length=struct.unpack('I',data[index+72:index+76])[0]
		index=index+length+76
		print("len: ",length)
		print("index: ",index)
	bchoc_file_read.close()
	pre_sha256=hashlib.sha256(data[index-length-76:]).hexdigest()
	print(pre_sha256)
	
	bchoc_file=open("bchoc_file.bin","ab")
	print("Case: ",case_id)
	for i in item_list:
		print(i)
		pre_hash=bytes(pre_sha256,'utf-8')
		dt=datetime.datetime.now()
		time_stamp=dt.timestamp()
		item_id=int(i)
		state=bytes("INITIAL",'utf-8')
		data_length=0
		bchoc_file.write(struct.pack('32sd16sI12sI',pre_hash,time_stamp,bytes(case_id,'utf-8'),0,state,data_length))
	bchoc_file.close()
 
def checkout(item_id):
	print(item_id)

def checkin(item_id):
	print(item_id)
	
def log(num_entries,case_id,item_id,reverse):
	#if num_entries is -1 then all log should be printed
	bchoc_file=open("bchoc_file.bin","rb")
	data=bchoc_file.read()
	print(len(data))
	index=0
	while index<=(len(data)-1):
		print(datetime.datetime.fromtimestamp(struct.unpack('d',data[index+32:index+40])[0]))
		print(struct.unpack('32s',data[index:index+32])[0])
		length=struct.unpack('I',data[index+72:index+76])[0]
		index=index+length+76
		print("len: ",length)
		print("index: ",index)
	print(num_entries)
	print(case_id)
	print(item_id)
	print(reverse)
	a=struct.unpack('d',data[32:40])
	timestamp=datetime.datetime.fromtimestamp(a[0])
	print(timestamp)
	print(struct.unpack('I',data[72:76])[0])
	bchoc_file.close()

def remove(item_id,reason,owner):
	print(item_id)
	print(reason)
	print(owner)
	
	
def init():
	if(os.path.exists('bchoc_file.bin')==False):
		print("Blockchain file not found. Create INITIAL block")
		dt=datetime.datetime.now()
		time_stamp=dt.timestamp()
		print(time_stamp)
		pre_hash=bytes("None",'utf-8')
		case_id=bytes("None",'utf-8')
		item_id=bytes("None",'utf-8')
		state=bytes("INITIAL",'utf-8')
		data_length=format(14,'b')
		data=bytes("Initial block",'utf-8')
		bchoc_file=open("bchoc_file.bin","ab")
		bchoc_file.write(struct.pack('32sd16sI12sI',pre_hash,time_stamp,case_id,0,state,14))
		bchoc_file.write(data)
		bchoc_file.write(b'\0')
		bchoc_file.close()
	else:
		print("Blockchain file found with INITIAL block")
	
def verify():
	print("verify")
	

# parse the input

inputArray = sys.argv
if inputArray[0] == "./bchoc":
    # add commands
    if inputArray[1] == "add":
        print("perform add command")
        if inputArray[2] == "-c":
            case_id = inputArray[3]
            #bchoc_file.write(bytes(case_id,'utf-8'))
            item_list = []
            for i in range(4, len(inputArray), 2):
                #print("another item")
                if inputArray[i] == "-i":
                    item_list.append(inputArray[i + 1])
                    #bchoc_file.write(inputArray[i + 1])
                else:
                    sys.exit(1)
            #print(item_list)
            append(case_id,item_list) 
        else:
            sys.exit(1)     
    # checkout command
    elif inputArray[1] == "checkout":
        print("perform checkout command")
        if len(inputArray) == 4 and inputArray[2] == "-i":
            item_id = inputArray[3]
            # call checkout command here
            checkout(item_id)
        else:
            sys.exit(1)
    elif inputArray[1] == "checkin":
        print("perform checkin command")
        if len(inputArray) == 4 and inputArray[2] == "-i":
            item_id = inputArray[3]
            # call checkin command here
            checkin(item_id)
        else:
            sys.exit(1)
    elif inputArray[1] == "log":
        num_entries=-1
        case_id=""
        item_id=""
        reverse=False
        for i in range(len(inputArray)):
            if(inputArray[i]=="-n"):
                num_entries=inputArray[i+1]
            if(inputArray[i]=="-c"):
                case_id=inputArray[i+1]
            if(inputArray[i]=="-i"):
                item_id=inputArray[i+1]
            if(inputArray[i]=="-r"):
                reverse=True
        log(num_entries,case_id,item_id,reverse)
    elif inputArray[1] == "remove":
        print("perform remove command")
        # call remove command here
        item_id=inputArray[3]
        reason=inputArray[5]
        owner=""
        if(len(inputArray)>6):
        	owner=inputArray[7]
        remove(item_id,reason,owner)
    elif inputArray[1] == "init":
        # call the Linked list constructor to check the LL or create intial block
        init()
    elif inputArray[1] == "verify":
        print("perform verify command")
        # call verify command here
        verify()
    else:
        sys.exit(1)
else:
    sys.exit(1)
print(inputArray)

# pack the data should be stored in bchoc

