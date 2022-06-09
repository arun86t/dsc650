---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-3-71a09796abfe> in <module>
     32         .getOrCreate()
     33 
---> 34     partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
     35     n = 100000 * partitions
     36 

ValueError: invalid literal for int() with base 10: '-f'
