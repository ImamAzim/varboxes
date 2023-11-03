Usage
=====


.. code-block:: python

    from varboxes import VarBox
    vb = VarBox('MyApp')
    # you can create any variable as attribute of the varbox:
    vb.a = 1
    # now, you could quit this session, restart the computer, and recreate a varbox (with the same app name):
    vb2 = VarBox('MyApp')
    print(vb2.a)
    >>>  1
    # and the attribute has been remembered!!
