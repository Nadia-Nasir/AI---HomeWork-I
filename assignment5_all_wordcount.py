"""Wordcount exercise
Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""
def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')
#========================================================================
def get_file_data(fname):
    with open(fname) as f_obj:
        contents = f_obj.read()
    print('\nFILE CONTENTS ARE: ')
    print('===================')
    print(contents)
    contents = contents.split()
    sort_dict = {}
    count = 0
    for i in range(0,len(contents)):
      for words in contents:
        if(words.lower() == contents[i].lower()):
          count += 1
      sort_dict[contents[i].upper()] = count
      count = 0
    return sort_dict
#========================================================================
def  print_words(fname):
    sort_dict = get_file_data(fname)
    print('\nDictionary ')
    print('===========')
    print(sort_dict)
#==========================================================================
def  print_top(filename):
    sort_dict = {}
    sort_dict = get_file_data(filename)
    print('\nSORT BY MOST COMMON WORDS:')
    print('=============================')
    for key, value in sorted(sort_dict.items(), key=lambda item: (item[1]),reverse = True):
        print(key + ' = ' + str(value))







import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    #sys.exit(1)

  option = input()
  filename = 'Data.txt'
  if option == '--count':
    print_words(filename)

  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
