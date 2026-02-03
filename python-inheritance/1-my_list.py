#!/usr/bin/python3
'''my_list'''


class MyList(list):
    '''Mylist Class that inherite from list'''


    def print_sorted(self):
        '''print the list sorted'''
        print(sorted(self))
