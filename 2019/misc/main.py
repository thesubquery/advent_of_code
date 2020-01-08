# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 19:42:51 2019

@author: lam
"""

import os
import aoc2019

path = r'C:\Users\lam\git_repos\advent_of_code\2019'
os.chdir(path)


class Intcode():
    def __init__(self, data):
        
        self.data        = [each for each in data]

        self.ptr         = 0
        self.opcode_args = {1: 3,
                            2: 3,
                            3: 1,
                            4: 1,
                            5: 2,
                            6: 2,
                            7: 3,
                            8: 3,
                            99: 0}

    def __repr__(self):
        result = [self.opcode] + self.param_mode
        return "|".join([str(each) for each in result])
    
    def get_arg(self, mode, arg, data):
        if mode == 0:
            return int(data[arg])
        elif mode == 1:
            return arg

    def get_num_args(self):
        return self.opcode_args[self.opcode]

    def update_inst(self):
        opcode          = self.data[self.ptr]
        self.opcode     = int(opcode[-2:])
        self.param_mode = [0, 0, 0]
        if len(opcode) > 2:
            index = 0
            for each in opcode[-3:-6:-1]:
                self.param_mode[index] = int(each)
                index += 1        
            
    def run(self, ID):
        self.ID = ID
        self.update_inst()
        while self.opcode != 99:
            
            num   = self.get_num_args()
            args  = [int(each) for each in self.data[self.ptr+1:self.ptr+1+num]]
            
            print(self.ptr, self.opcode, args, self.data[self.ptr:self.ptr+num+1])
            
            if self.opcode == 1:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                self.data[args[2]] = str(val1 + val2)
            elif self.opcode == 2:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                self.data[args[2]] = str(val1 * val2)
            elif self.opcode == 3:
                self.data[args[0]] = str(self.ID)
            elif self.opcode == 4:
                self.ID = int(self.data[args[0]])
            elif self.opcode == 5:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                if val1 > 0:
                    self.ptr = val2
                    self.update_inst()
                    continue
            elif self.opcode == 6:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                if val1 == 0:
                    self.ptr = val2
                    self.update_inst()
                    continue
            elif self.opcode == 7:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                if val1 < val2:
                    self.data[args[2]] = '1'
                else:
                    self.data[args[2]] = '0'
            elif self.opcode == 8:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                if val1 == val2:
                    self.data[args[2]] = '1'
                else:
                    self.data[args[2]] = '0'
            self.ptr += num + 1
            self.update_inst()
            
with open(os.path.join(path, 'input\day_5.txt')) as f:
    lines = f.readlines()
data = lines[0].strip().split(',')

intcode = Intcode(data)
intcode.run(5)



with open(os.path.join(path, 'input\input_22.txt')) as f:
    lines = f.readlines()


def is_int(string):
    try:
        int(string)
        return True
    except:
        return False


data = [each.strip() for each in lines]
for i in range(len(data)):
    inst  = data[i]
    index = inst.rfind(" ")
    if is_int(inst[index+1:]):
        data[i] = [inst[:index].strip(), inst[index+1:]]
    else:
        data[i] = [inst, ""]

class Node():
    def __init__(self, num):
        self.num  = num
        self.prev = None
        self.next = None 
    def __repr__(self):
        return "Node({})".format(self.num)

class LinkedList():
    def __init__(self, num):
        
        self.dict = {i: Node(i) for i in range(num)}
        self.head = self.dict[0]
        for i in range(num-1):
            self.dict[i].next = self.dict[i+1]

    def cut(self, N):

        if N >= 0:
            h1 = self.dict[0]
            t1 = self.dict[N-1]
            h2 = self.dict[N]
            t2 = self.dict[len(self.dict)-1]
        else:
            h1 = self.dict[0]
            t1 = self.dict[len(self.dict)+(N-1)]
            h2 = self.dict[len(self.dict)+(N)]
            t2 = self.dict[len(self.dict)-1]            
        
        self.head  = h2        
        t2.next    = h1
        t1.next    = None
        
        node = self.head
        for i in range(len(self.dict)):
            self.dict[i] = node
            node         = node.next

    def deal_with_increment(self, N):
        
        node  = self.head
        index = 0
        for i in range(len(self.dict)):
            self.dict[index] = node
            node             = node.next
            index           += N
            index           %= len(self.dict)

        for i in range(len(self.dict)-1):
            self.dict[i].next = self.dict[i+1]
        self.dict[len(self.dict)-1].next = None
      
        self.head = self.dict[0]

    def deal_into_new_stack(self):
        
        node      = self.dict[0]
        prev_node = None
        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            self.head = node
            node      = next_node                        
        node = self.head
        for i in range(len(self.dict)):
            self.dict[i] = node
            node         = node.next




rounds    = 101741582076661
deck_size = 119315717514047

ll        = LinkedList(deck_size)


for j in range(rounds):
    

history         = []
valid_deck_size = []
for i in range(10007, 10007 * 100):
    try:
        print(i)
        ll = LinkedList(i)
        for d in data:
            inst = d[0]
            if d[1]:
                N = int(d[1])
            else:
                N = 0
            if inst == 'deal with increment':
                ll.deal_with_increment(N)
            elif inst == 'deal into new stack':
                ll.deal_into_new_stack()
            elif inst == 'cut':
                ll.cut(N)
            else:
                print(inst)
                break
        
        num = [ll.dict[key].num for key in ll.dict.keys()]
        history.append(num.index(2019))
        print(i, history[-1])
        valid_deck_size.append(i)
    except:


    
    
    
    
    for i in range(deck_size):
        if ll.dict[i].num == 8775:
            history.append(i)
            print(j, i)
            
    if num not in history:
        history.append(num)
        print(j, num)
    else:
        print(j, num)
        break

    if j == rounds % 10007:
        break

    with open("history.txt", "a+") as f:
        f.write("{}, {}\n".format(j, num))

for i in range(10007):
    if ll.dict[i].num == 2019:
        print(i)

data[:10]        

ll = LinkedList(10)
ll.deal_into_new_stack()
[ll.dict[i].num for i in range(10)]


ll = LinkedList(10)
ll.deal_with_increment(3)
[ll.dict[i].num for i in range(10)]


ll = LinkedList(10)
ll.cut(-3)
[ll.dict[i].num for i in range(10)]
    

100 % 100

data[10:]




def deal_with_increment(deck, N):
    
    total = len(deck)
    
    tbl   = [0 for i in range(total)]
    index = 0
    
    for card in deck:
        tbl[index] = card
        index     += N
        index     %= total
    
    return [card for card in tbl]

ans = "0 7 4 1 8 5 2 9 6 3"

deck = [i for i in range(10)]
N = 3
[int(each) for each in ans.split(" ")] == deal_with_increment(deck, N)















