# this comment appears first
# and spans 2 lines

# this comment does not show up in the output of getcomment().
'''
spamle file to serve as the basis for inspect example
'''


def module_level_function(arg1, arg2='default', *args, **kwargs):
    '''this function is declared in the module'''
    local_variable = arg1 * 2
    return local_variable


class A(object):
    '''the A class'''

    def __init__(self, name):
        self.name = name

    def get_name(self):
        "returns the name of the instance"
        return self.name


instance_of_a = A('sample_instance')


class B(A):
    '''
    this is the B class
    it is derived from A
    '''

    # this method is not part of A
    def do_something(self):
        '''does some work'''

    def get_name(self):
        "overrides version from A"
        return 'B(' + self.name + ')'
