#############
# PROBLEM 4 #
#############

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    unique = {}
    for key in aDict.keys() :
        if aDict[key] not in unique.keys() :
            unique[aDict[key]] = []
        unique[aDict[key]] += [key]
    sorted = []
    for key in unique.keys() :
        if len(unique[key]) == 1 :
            sorted += unique[key]
    sorted.sort()
    return sorted

#############
# PROBLEM 6 #
#############

class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
    
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """ 
        super(USResident, self).__init__(name)
        self.name = name
        if status != "citizen" and status != "legal_resident" and status != "illegal_resident" :
            raise ValueError()
        self.status = status
        
    def getStatus(self):
        """
        Returns the status
        """
        return self.status
    
#############
# PROBLEM 7 #
#############

class Member(object):
    def __init__(self, founder):
        """ 
        founder: string
        Initializes a member. 
        Name is the string of name of this node,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.parent = mother   

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.parent 

    def is_parent(self, mother):
        """
        mother: Member
        Returns: Boolean, whether or not `mother` is the 
        parent of this Member
        """
        return self.parent == mother  

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children 


class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # convert name to Member node (should check for validity)
        mom_node = self.names_to_nodes[mother]   
        # add each child
        for c in list_of_children:           
            # create Member node for a child   
            c_member = Member(c)               
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member    
            # set child's parent
            c_member.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c_member)         
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 

        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 

        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed) 

        Keyword arguments: 
        a -- string that is the name of node a
        b -- string that is the name of node b

        cousin type:
          -1 if a and b are the same node.
          -1 if either one is a direct descendant of the other
          >=0 otherwise, it calculates the distance from 
          each node to the common ancestor.  Then cousin type is 
          set to the smaller of the two distances, as described 
          in the exercises above

        degrees removed:
          >= 0
          The absolute value of the difference between the 
          distance from each node to their common ancestor.
        """
        na = self.names_to_nodes[a]
        nb = self.names_to_nodes[b]
        # Helper function that determines all the ancestors of a node (including that node)
        def getAncestors (n, ls = []):
            if n == None :
                return ls
            ls += [n]
            return getAncestors(n.parent)
        # Helper function that determines the depth of the node in the tree
        def getDepth (n) :
            if n == None :
                return 0
            return 1 + getDepth(n.parent)
        depthA = getDepth(na)
        depthB = getDepth(nb)
        degreesRemoved = abs(depthA - depthB)
        
        # Handling any exceptions
        if a == b or na.is_child(nb) or nb.is_child(na) :
            return (-1, degreesRemoved)
        
        # Swapping the nodes since we want to determine the ith cousin from the higher node
        if depthA > depthB :
            na, nb = nb, na
            depthA, depthB = depthB, depthA
        
        nbAncestor = getAncestors(nb)
        cnt = -1
        while not na in nbAncestor :
            na = na.parent
            cnt += 1
        return (cnt, degreesRemoved)