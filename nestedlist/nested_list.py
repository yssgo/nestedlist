def nested_list(nn, cls_=None, *init_args, **init_kwargs):
    ''' # Signature:
    #
    # dim_list(nn:list[int], cls_=None, *init_args, **init_kwargs)->list
    #

    '''
    def dim_list(nn, cls_, lev=0, cls_args=(), cls_kwargs={}):
        '''# Signature
        #
        # dim_list(nn:list[int], cls_, lev=0, cls_args:tuple=(), cls_kwargs:dict={})->list
        #

        '''
        if lev == len(nn) - 1:
            lst = [None] * nn[lev]
            for kk in range(nn[lev]):
                if cls_ is None:
                    lst[kk] = None
                else:
                    lst[kk] = cls_(*cls_args, **cls_kwargs)
            return lst
        else:
            lst = [None] * nn[lev]
            for kk in range(nn[lev]):
                lst[kk] = dim_list(nn, cls_, lev + 1, cls_args, cls_kwargs)
            return lst

    return dim_list(nn, cls_=cls_, cls_args=init_args, cls_kwargs=init_kwargs)
  
