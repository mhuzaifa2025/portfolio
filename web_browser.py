

from stack import Stack

def getAction():
    '''
    takes action from user and checks if it is valid
    Inputs: none
    Returns: string
    '''
    action=input("Enter = to enter a URL, < to go back, > to go forward, q to quit: "
)
    if action in ["<",">","=","q"]:
        return action
    else:
        raise Exception("Invalid entry.")
      
    
            

def goToNewSite(current, bck, fwd):
    '''
    This function prompts the user to enter a new website address, and returns the index to the current site
    Inputs: string
    Returns: string
    '''   
    new_site=input("URL: ")
    bck.push(current)
    fwd.clear()
    return new_site
    
    
def goBack(current, bck, fwd):
    '''
    This function is called when the user enters “<" during getAction() it checks if there is a webpage stored before current web page.
    Inputs: string
    Returns: string
    '''  
    if bck.isEmpty():
        print("Cannot go back.")
        return current
     
    fwd.push(current)
    return bck.pop() 
    

def goForward(current, bck, fwd):
    '''
    This function is called when the user enters “>” during getAction().it checks if there is a webpage stored after current web page.
    Inputs: string
    Returns: string
    '''    
    if fwd.isEmpty():
        print("Cannot go forward.")
        return current
    bck.push(current)
    return fwd.pop()

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True   
    
    print('Browser closing... Goodbye!')    
        
if __name__ == "__main__":
    main()
