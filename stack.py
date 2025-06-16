# =================================================================
# CMPUT 175 - Introduction to the Foundations of Computation II
# Lab 4 - Web Browser
#
# ~ Created by CMPUT 175 Team ~
# =================================================================

class Stack:
    """
    A class representing a stack Abstract Data Type (ADT).
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.items = []
    
    def push(self, item):
        """
        Adds an item to the top of the stack.
        Inputs: The item to be added to the stack.
        Returns: None

        """
        
        self.items.append(item)
    
    def pop(self): 
        """
        Removes and returns the top item from the stack.
        Inputs: None
        Returns: The item removed from the top of the stack.

        Raises:
            Exception: If the stack is empty.
        
        """
        if self.isEmpty():
            raise Exception("Stack is empty. Cannot pop an item.")

        return self.items.pop(-1)
        
    
    def peek(self):  
        """
        Returns the top item of the stack without removing it.
        Inputs: None
        Returns: The top item of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if self.isEmpty():
           raise Exception("Stack is empty. Cannot peek")
        return self.items[-1]
           
    
    def isEmpty(self):
        """
        Checks if the stack is empty.
        Inputs: None
        Returns: bool - True if the stack is empty, False otherwise.
        """
        return self.items == []
    
    def size(self):
        """
        Returns the number of items in the stack.
        Inputs: None
        Returns: int - The number of items in the stack.
        """
        return len(self.items)
    
    def show(self):
        """
        Prints the items in the stack.
        Inputs: None
        Returns: None
        """
        print(self.items)
    
    def __str__(self):
        """
        Returns a string representation of the stack.
        Inputs: None
        Returns: str - A string representation of the stack.
        """
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
        """
        Removes all items from the stack. Does nothing if the stack is empty.
        Inputs: None
        Returns: None
        """
        self.items.clear()
        pass  



def main():
    s = Stack()
    print(s.isEmpty())
    
    s.push('A')
    s.push('B')
    s.push('C')
    print("Stack after pushing A, B, C:")
    print(f'Your Stack looks like this: ',end='')
    s.show()
    if s.items == ['A','B','C']:
        print('Test 1 Passed\n')
    else:
        print('Test 1 Failed\n')

    print("Size of stack")
    print(f'Your stack size is {s.size()}')
    if s.size() == 3:
        print('Test 2 Passed\n')
    else:
        print('Test 2 Failed\n')

    
    print("Peek")
    print(f'Last element added to your stack is {s.peek()}')
    if s.peek() == "C":
        print('Test 3 Passed\n')
    else:
        print(f'Test 3 Failed\n')
    
    popped = s.pop()
    print('Pop Method')
    print("Popped item:", popped)
    if popped == 'C':
        print('Test 4 Passed\n')
    else:
        print('Test 4 Failed\n')

    print(s.isEmpty())
  
    print("String:", str(s))
    
    s.clear()

    s.show()
    print(s.isEmpty())

if __name__ == "__main__":
    main()