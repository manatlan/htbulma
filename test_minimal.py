import pytest

import htbulma as b
from htag import Tag

def test_version():
    assert b.__version__

def test_constructor():
    """ the most obvious thing to (badly) test htbulm's objects
    it tries to instanciate them, with 0, 1 or 2 parameters
    """
    assert b.ALL

    parent = Tag.div()
    
    p=[]    # list for non zero parameter
    for i in b.ALL:
        if "service" in str(i):
            instance=i(parent)
            print("SERVICE:",i,repr(instance))
        else:
            try:
                instance=i()
                print("NO PARAM:",i,repr(instance))
            except TypeError as e:
                p.append(i)

    pp=[]   # list for no zero or one parameter
    for i in p:
        try:
            instance=i("row")
            print("ONE PARAM:",i,repr(instance))
        except TypeError as e:
            pp.append(i)

    for i in pp:
        instance=i(".",".")
        print("TWO PARAM:",i,repr(instance))

    # if it works -> all objects can be instanciated with 0, 1 or 2 params
    
#test_constructor()
