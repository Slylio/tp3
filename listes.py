# -*- coding: utf-8 -*-
from tkinter import N

class Liste:
    """ The class Liste allows to represent a list from chained elements of type Cell. Each element of the 
    list contains a value and a pointer towards the next element. """
    
    def __init__(self):
        """Creates an instance of class Liste
        input   -- self : instance of class Liste
                    set the first element to None, and the size of the list to 0
        """
        self.mfirst = None
        self.size = 0

    def is_empty_list(self):
        """ Returns True if and only if Liste self is empty
        input   -- self : instance of class Liste
        output  -- v : bool
        """
        v = (self.mfirst == None)
        return v
    
    def __str__(self):
        """ Returns a string representing Liste self
        input   -- self : instance of class Liste
        output  -- string
        """
        result=""
        if self.mfirst!=None:
            c=self.mfirst
            i=1
            while c!=None:
                result+=str(c.data)
                if (i<self.size) :
                    result+=", "
                    i+=1
                c=c.next
        return "["+result+"]"
    def length(self):
        """ Returns the lenght of the list
        input   -- self : instance of class Liste
        output  -- n : int
        """
        return self.size
    def head(self):
        """ Returns the first element of the list (of type Cell)
        input   -- self : instance of class Liste
                pre-cond: self n'est pas vide
        output  -- p : element of type Cell
        """
        if self.mfirst == None:
            print("empty list")
        else:
            p = self.mfirst
            return p
        
    def first_value(self):
        """ Returns the value of the first element of the list of type object
        input   -- self : instance of class Liste
                pre-cond: self is not empty
        output  -- v : value of type object
        """
        if self.mfirst == None:
            print("liste vide")
        else:
            v = self.mfirst.data
            return v
        
    def insert_first(self, v):
        """ Inserts the value v at the head of the list
        input   -- self : instance of class Liste
                -- v : value of type object to insert at the first position
        output  -- self in which the element of value v has been inserted at the head of the list
                    the size of the list is updated
        """
        m = Cell()
        m.data=v
        if self.mfirst == None:
            m.next = None
        else:
            m.next=self.mfirst
        self.mfirst = m
        self.size += 1
        
    def insert_at(self,v,i):
        """ Returns the list in which the element of value v has been inserted at index i
        input   -- self : instance of class Liste
                -- v : value of type object to insert
                -- i : int index at which the element of value v is inserted
                    exception when the index i is too small or too big
        output  -- self in which the element of value v has been inserted at index i of the list
                    the size of the list is updated
        """
        if i==0:
            self.insert_first(v)
        else :
            cToInsert=Cell()
            cToInsert.data=v
            
            c1=self.get_at(i-1)
            c2=c1.next 
            
            c1.next=cToInsert
            cToInsert.next=c2
            self.size+=1
        return self

    def insert_last(self,v):  
        """ Inserts the value v at the end of the list
        input   -- self : instance of class Liste
                -- v : value of type object to insert at the last position
        output  -- self in which the element of value v has been inserted at the end of the list
                    the size of the list is updated 
        """
        n = self.length()
        if n == 0:
            self.insert_first(v)
        else:
            self.insert_at(v,n)
        
    def delete_value(self,v):
        """ Returns the list in which the element of value v i has been deleted
        input   -- self : instance of class Liste
                -- v : value of type object
        output  -- self in which the element of value v has been deleted
                    the size of the list is updated 
        """
        if self.size ==1 and self.mfirst.data==v:
            self.mfirst=None
        else :
            if self.mfirst.data==v:
                self.mfirst=self.mfirst.next
            else :
                i=1
                p=self.mfirst
                c=Cell()
                hit=False
                while not hit and i<self.size:
                    m=p
                    p=p.next
                    if p.data == v:
                        m.next=p.next
                        hit=True
                    i+=1
        self.size-=1
        return self
            

       
        
                            
    def get_at(self,v):
        """ Returns the element of the Liste self at index i
        input   -- self
                -- v : int (index of the searched element) 
        output  -- element of type Cell 
        """       
        c=self.mfirst
        n=self.size
        i=0
        while i<n and i<v and c.next!=None:
            c=c.next
            i+=1
        return c
            
    def get_value(self,v):
        """ Returns the value of the element of the liste at index i
        input   -- self
                -- v : int (index of the searched element) 
        output  -- obj : object 
        """
        c=self.mfirst
        n=self.size
        i=0
        while i<n and i<v and c.next!=None:
            c=c.next
            i+=1
        return c.data
       
    
    def map(self,f):
        """ Applies function f to each value of Liste self
        input   -- self : instance of class Liste
                -- f : function
        output  -- lmap: new Liste in which each value has been modified by function f
                    self is not modified
        """  
        for i in range(self.size):
            self.get_at(i).data=f(self.get_at(i).data)
        return self
    
    def count(self, v):
        """ Counts the number of occurrences of v in Liste self
        input   -- self : instance of class Liste
                -- v : object
        output  -- int : number of times v occurs in Liste self
        """ 
        result=0
        for i in range(self.size):
            if self.get_value(i)==v:
                result+=1
        return result
        
    def filter(self, f):
        """ Returns the list of the elements x of Liste self that verify f(x) = True
        input   -- self : instance of class Liste
                -- f : function
                pre-cond: verify that f returns True or False
        output  -- lfilter: new Liste of elements whose values verify f(x) = True
        """
        result=Liste()
        for i in range (self.size):
            if f(self.get_value(i))==True:
                result.insert_first(self.get_value(i))
        return result 
    
    def reduce(self, f,x):
        """ Returns the value obtained by applying the function f(x,y) to each value y of Liste self
        input   -- self : instance of class Liste
                -- f : function
                -- x : initial value of type object
        output  -- final value of type object
        """
        y = self.mfirst
        result = f(x,y.data)
        for i in range(self.size-1):
            y=y.next
            result=f(result, y.data)
        return result
        
class Cell():
    """ The class Cell represents an element of the list. It contains 2 attributes: a data of type object and a link to the next element
    """
 
    def __init__(self):
        """ Creates an instance of class Cell
        input   -- self : instance of class Cell
        """
        self.data = object
        self.next = None
        
    def __str__(self):
        """ Returns a string representing the self Cell
        input   -- self : instance of class Cell
        output  -- string, representation of the self cell
        """
        result = str(self.data) + ', next:'
        if self.next == None:
            result += 'None'
        else:
            result += str(self.next.data)
        return '{ ' + result + ' }' 
        
def incr(n):
    """ Returns an increments of n by 1
    input   -- n : number, the value to increment
    output  -- number, n+1
    """
    return n+1

def carre(n):
    """ Returns the squared value of n
    input   -- n : number
    output  -- number, n^2
    """
    return n * n

def test_negative(n):
    """ Tests if n is negative
    input   -- n : number(int or float)
    output  -- bool : True if n is negative, False otherwise"""
    return n < 0

def f(x,y):
    """ Adds y to x and returns the result
    input   -- x : Any
               y : Any
    output  -- Any, x + y
    """
    return x + y
        
if __name__ == "__main__":
    print("Hello Liste !!!")