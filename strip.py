import re

def strip_copy(string, char=None):
    '''
    Function to mimic the strip() method.
    If no arguments are passed, function will strip 
    whitespace characters from beginning and ending of string. 
    Otherwise characters specifiedin second argument
    will be removed.
    '''
    if char == None:
        # Regex breakdown:
            # -Raw string
            # -Start match with any non-space char
            # -Followed by any char (space or not) 0 or more times
            # -Must end with a non-space char
        filter = re.compile(r'\S.*\S')
        print(re.search(filter, string).group())
        print(re.search(filter, string))

strip_copy('   ca  lif   or nia     ,  ')
