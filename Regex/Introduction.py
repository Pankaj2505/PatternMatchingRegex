# Always use Raw string for pattern creation for regex

import re



#*******************************************************************************
# Match function

text = "my name is pankaj, and live on street 35 in 2nd cross"
text1 = "34 is my lucku no"


def um_match(text):
    """will check the match operator, Re.match check only the start of index
     we use this to validate the user input"""
    pattern = r'\d+'
    match = re.match(pattern, text)
    if match:
        print("found", match.group(0), "at Position", match.start())
    else:
        print('No match found')


def is_integer(text):
    """This method will return True only if the input contains all integer"""

    # pattern = r'\d+'
    # as you can see function will fail for pattern like 123A, we need to add some boundary to the pattern
    # one such is $, match automatically look for start of string

    pattern = r'^\d+$'
    match = re.match (pattern, text)

    if match:
        return True
    else:
        return False


#um_match(text1)
#print(is_integer('123A'))

def test_is_integer():
    """Test script to test the is_integer method"""
    passtest = ['123','1','233']
    failtest = ['abc','123A','1.24']

    for value in passtest:
        if is_integer(value):
            print("PassTest list is succesful")
        else:
            print("Some issue with function, failed test at", value)

    for value in failtest:
        if not is_integer(value):
            print("Failtest list is succesful")
        else:
            print("Some issue with function, failed test at", value)

#test_is_integer()



#****************************************************************************************************
# Search
 # only search the first match
text = "my name is pankaj, and live on street 35 in 2nd cross at 45678 zip"
text1 = "34 is my lucky no"


def um_search (text):
    """will check the search operator, Re.search  will search in entire text
     we use this to search entire paragraph, its not gonna find the second search """
    pattern = r'\d+'
    match = re.search(pattern, text)
    if match:
        print("found", match.group(0), "at Position", match.start())
    else:
        print('No match found')

um_search(text)


def is_integer(text):
    """This method will return True only if the input contains all integer"""

    # pattern = r'\d+'
    # as you can see function will fail for pattern like 123A, we need to add some boundary to the pattern
    # one such is $, match automatically look for start of string

    pattern = r'^\d+$'   # carat make sure pattern matching start from begining , and doller make sure to search till end
    match = re.search (pattern, text)

    if match:
        return True
    else:
        return False


def test_is_integer():
    """Test script to test the is_integer method"""
    passtest = ['123','1','233']
    failtest = ['abc','123A','1.24']

    for value in passtest:
        if is_integer(value):
            print("PassTest list is succesful")
        else:
            print("Some issue with function, failed test at", value)

    for value in failtest:
        if not is_integer(value):
            print("Failtest list is succesful")
        else:
            print("Some issue with function, failed test at", value)

test_is_integer()



#****************************************************************************************
#Find all
# match all the pattern
# if we have a long text message , find all will block the code ,to search all pattern

text = "my name is pankaj, and live on street 35 in 2nd cross at 45678 zip,121321"
text1 = "34 is my lucky no"


def um_search (text):
    """will check the search operator, Re.search  will search in entire text
     we use this to search entire paragraph, its not gonna find the second search """
    pattern = r'\d+'
    match = re.findall(pattern, text)
    if match:
        print("found", match.group(0), "at Position", match.start())
    else:
        print('No match found')

um_search(text)


def is_integer(text):
    """This method will return True only if the input contains all integer"""

    # pattern = r'\d+'
    # as you can see function will fail for pattern like 123A, we need to add some boundary to the pattern
    # one such is $, match automatically look for start of string

    pattern = r'^\d+$'   # carat make sure pattern matching start from begining , and doller make sure to search till end
    match = re.findall (pattern, text)

    if match:
        return True
    else:
        return False


def test_is_integer():
    """Test script to test the is_integer method"""
    passtest = ['123','1','233']
    failtest = ['abc','123A','1.24']

    for value in passtest:
        if is_integer(value):
            print("PassTest list is succesful")
        else:
            print("Some issue with function, failed test at", value)

    for value in failtest:
        if not is_integer(value):
            print("Failtest list is succesful")
        else:
            print("Some issue with function, failed test at", value)

test_is_integer()

