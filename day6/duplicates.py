#create a list with duplicates
#using the set function generate a dictionary
#then convert the dictionary back into a list with no duplicate
#prints the new list

def length_of_last_word(s):
        words = s.split()
        if len(words) == 0:
            return 0
        return len(words[-1])

print(length_of_last_word("Python Exercises"))
print(length_of_last_word("Python"))
print(length_of_last_word(""))
print(length_of_last_word("  "))
