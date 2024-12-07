def print_params(a=1, b='stroka', c=True):
     print(a, b, c)
values_list = [22, 'BlowMeUp', False]
values_dict = {'a':33, 'b': True, 'c': 'Shapka'}

values_list2 = ['Black', "Night"]



print_params(*values_list2, 42)
print_params(**values_dict)
print_params(*values_list)
