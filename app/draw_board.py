def put_loc(index,data):
    '''return lenth*y+x'''
    '''1=food 2=snake 3=you'''
    """map=0"""
    lenth=data['board']['height']
    for i in data['board']['food']:
        index=index[0:lenth*i['y']+i['x']]+'1'+index[i['x']+lenth*i['y']+1:]
    for x in data['board']['snakes']:
        for i in x['body']:
            index=index[0:lenth*i['y']+i['x']]+'2'+index[i['x']+lenth*i['y']+1:]
    for i in data['you']['body']:
        index=index[0:lenth*i['y']+i['x']]+'3'+index[i['x']+lenth*i['y']+1:]
    return index
        
def draw_board(lenth,index):
    for i in range(lenth):
        print(index[i*lenth:(i+1)*lenth])
