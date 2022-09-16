import pytest
"""
Currently the pytests are very very limited, and very very generic
(but they exists ;-)

All others reals/tests should be run manually with a real browser, in a real env ;-(
"""

import htbulma as b
from htag import Tag

def test_version():
    assert b.__version__
    print("HTBulma %s" % b.__version__)

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
                print("(WITHOUT PARAM):",i,repr(instance))
            except TypeError as e:
                p.append(i)

    pp=[]   # list for no zero or one parameter
    for i in p:
        try:
            instance=i("row")
            print("(WITH 1 PARAM):",i,repr(instance))
        except TypeError as e:
            pp.append(i)

    for i in pp:
        instance=i(".",".")
        print("(WITH 2 PARAMS):",i,repr(instance))

    # if it works -> all objects can be instanciated with 0, 1 or 2 params
    
#test_constructor()
