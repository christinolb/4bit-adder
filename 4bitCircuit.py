# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 12:14:21 2019

@author: chris
"""


class LogicGates():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.out=None
        
    def andg(self):
        if self.a == 0b1 and self.b == 0b1:
            self.out=0b1
        else:
            self.out=0b0
            
    def nandg(self):
        if self.a == 0b1 and self.b == 0b1:
            self.out=0b0
        else:
            self.out=0b1
    
    def org(self):
        if self.a == 0b1 or self.b == 0b1:
            self.out=0b1
        else:
            self.out=0b0
            
    def norg(self):
        if self.a == 0b1 or self.b == 0b1:
            self.out=0b0
        else:
            self.out = 0b1
        
    
    def notg(self,x):
        if x == 0b1:
            self.out=0b0
        else:
            self.out=0b1
    
    def xorg(self):
        if self.a != self.b:
            self.out=0b1
        else:
            self.out=0b0
            
    def xnorg(self):
        if self.a == self.b:
            self.out=0b1
        else:
            self.out=0b0



def halfAdder(a, b):
    #creating andgate
    andg=LogicGates(a,b)
    andg.andg()
    carry=andg.out
    #creating xorgate
    xorg=andg
    xorg.xorg()
    asum=xorg.out
#    print(carry,asum)
    return asum, carry
    
def fullAdder(a,b,c):
    #first adder
    asum,aCout=halfAdder(a,b)
    #second adder
    fsum,bCout=halfAdder(asum,c)
    #or gate
    orgate=LogicGates(aCout,bCout)
    orgate.org()
    cOut=orgate.out
    return cOut,fsum

def fourBitAdder(a0,a1,a2,a3,b0,b1,b2,b3,cIn):
    cIn1,sum0=fullAdder(a0,b0,cIn)
    cIn2,sum1=fullAdder(a1,b1,cIn1)
    cIn3,sum2=fullAdder(a2,b2,cIn2)
    cIn3,sum3=fullAdder(a3,b3,cIn3)
    print(cIn3,sum3,sum2,sum1,sum0)
    return cIn3,sum3,sum2,sum1,sum0
    
    
    
    

def readcsv(filename):
    pre=[]
    numbers=[]
    with open(filename,"r") as f:
        for i in f.readlines():
            pre.append(i)
        for i in pre:
            numbers.append(i.strip())
        A=numbers[0]
        B=numbers[1]
        f.close()
    return A,B

def toBinary(A,B):
    a0=a1=a2=a3=b0=b1=b2=b3=0
    a3=int(A[0])
    a2=int(A[1])
    a1=int(A[2])
    a0=int(A[3])
    b3=int(B[0])
    b2=int(B[1])
    b1=int(B[2])
    b0=int(B[3])
    return  a0,a1,a2,a3,b0,b1,b2,b3

        
def main():
    aGo=True
    print("FOUR BIT ADDER")
    print("+"*14)
    while aGo:
        try:
            filename=input("Enter .txt filename (press enter to exit)[read.txt]: ")
            A,B=readcsv(filename) 
        except FileNotFoundError:
            if filename == "":
                aGo = False
            elif filename != "":
                print()
                print(filename,"does not extist, please enter an existing .txt file.")
        else:
            print("\nIntput:",A,"and",B)
            a0,a1,a2,a3,b0,b1,b2,b3=toBinary(A,B)
            fCout,sum3,sum2,sum1,sum0=fourBitAdder(a0,a1,a2,a3,b0,b1,b2,b3,0b0)
        
    
if __name__ == "__main__":
    main()
    
    