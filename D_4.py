# DESCRIPTION:
# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.
# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.
# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.
# EXAMPLES
# fix_string('T0PP1NG5') => 'TOPPINGS'
# fix_string('5OUR') => 'SOUR'
# fix_string('1GLO0') => 'IGLOO'
# correct error
#from the number to the letter 

# def fix_string(word):
#     empty_str = str()
#     for letter in word:
#         if letter == '5':
#             empty_str += 'S'
#         elif letter == '0':
#             empty_str += 'O'
#         elif letter == '1':
#             empty_str += 'I'
#         else:
#             empty_str += letter
#     return empty_str

# print(fix_string('5OUR'))

def duplicate_encode(word):
    for letter in word:
        result = ''
        num_of_ltrs = word.count(letter)
        if num_of_ltrs <= 1:
            result += '('
        if num_of_ltrs >= 2:
            result += ')'
        return result
    print(result('den'))
    print(duplicate_encode(result('den')))
      
