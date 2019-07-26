def chop(lst):
    l = len(lst)
    if l == 0: return
    elif l == 1: del lst[0]
    else:
        del lst[0]
        del lst[l-2] #l-2 because we have already deleted an element, so the length has decreased by 1

def middle(lst):
    new_lst = lst[:]
    l = len(new_lst)
    if l == 0: return
    elif l == 1: del new_lst[0]
    else:
        del new_lst[0]
        del new_lst[l-2] #l-2 because we have already deleted an element, so the length has decreased by 1
    return new_lst
