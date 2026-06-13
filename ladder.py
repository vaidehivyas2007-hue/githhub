'''
   control structure:
    if, if else, ladder,nested, match case,ternory(short hand)

syntax:
---------------------
if cond1:
      if else
else:
      if else

'''

# wap to print max number for given three numbers.



a  =  int (input ( ' Enter a: ') )
b  = int (input ( ' Enter b: ') )
c   = int (input ( 'Enter c: ' ) )

if  a  >  b :
     if  a  >  c:
           print ( ' A is max ' )
     else:
           print( ' c  is  max ' )
else:
    if  b > c:
           print(' b is max')
       else:
         print( ' c is max')
         
