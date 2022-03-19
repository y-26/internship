#!/usr/bin/env python
# coding: utf-8

# In[2]:


def pytha(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
    
print(pytha(2,4,'x'))
print(pytha(2,'x',5))
print(pytha('x',8,5))
print(pytha(3,4,9))


# In[ ]:





# In[ ]:




