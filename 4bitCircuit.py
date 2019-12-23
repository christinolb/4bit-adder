# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 12:14:21 2019

@author: chris
"""
#class of logic gates
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
    
    def org(self):
        if self.a == 0b1 or self.b == 0b1:
            self.out=0b1
        else:
            self.out=0b0
    
    def xorg(self):
        if self.a != self.b:
            self.out=0b1
        else:
            self.out=0b0


def halfAdder(a, b):
    #creating andgate instance
    andg=LogicGates(a,b)
    andg.andg()
    carry=andg.out
    #creating xorgate instance
    xorg=andg
    xorg.xorg()
    asum=xorg.out
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
    return cIn3,sum3,sum2,sum1,sum0
    
def readcsv(filename):
    prompt=""
    with open(filename,"r") as f:
        for i in f.readlines():
            prompt=i.strip()
        
    return prompt
#convert from text to int and into variable for adder inputs
def split(A,B):
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

def toDecimal(fCout,sum3,sum2,sum1,sum0):
    zero=sum0*(2**0)
    one=sum1*(2**1)
    two=sum2*(2**2)
    three=sum3*(2**3)
    four=fCout*(2**4)
    decimalT=four+three+two+one+zero
    print("Binary: "+str(fCout)+str(sum3)+str(sum2)+str(sum1)+str(sum0))
    print("Decimal:",decimalT)
    
    
def main():
    aGo=True
    print("FOUR BIT ADDER")
    print("+"*14)
    #loop for user to use as they please
    while aGo:
        #exception handling for nonexisting files
        try:
            prompt=readcsv("read.csv")
            A=input(prompt)
            for i in A:
                if i != "0" and i != "1":
                    raise ValueError ("invalid input must be base 2")
            B=input(prompt)
            for i in B:
                if i != "0" and i != "1":
                    raise ValueError ("invalid input, must be base 2")
        except ValueError as ex:
            print(ex)
        else:
            a0,a1,a2,a3,b0,b1,b2,b3=split(A,B)
            fCout,sum3,sum2,sum1,sum0=fourBitAdder(a0,a1,a2,a3,b0,b1,b2,b3,0b0)
            toDecimal(fCout,sum3,sum2,sum1,sum0)
            inp=input("continue[y/n]?")
            if inp =="n":
                aGo = False
            
            
    
if __name__ == "__main__":
    main()