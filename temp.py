def function( *args_list ):
    ans = []
    for l in args_list:
        print(l)
        ans.append( l.upper() )
    return ans
# Passing args arguments
object = function('Python', 'Functions', 'tutorial')
print( object )