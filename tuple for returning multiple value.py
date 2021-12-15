'''we have learnt that function return single value.But,at a time we need to return
more than one value to funtion .In such situation it is preferable to group together 
multiple value and return them togethere'''

def max_min(vals):
    x=max(vals)
    y=min(vals)
    return(x,y)
vals=(45,56,68,98,111,235,25,24.99999)
(max_marks,min_marks)=max_min(vals)
print("highest marks:",max_marks)
print("minimum marks:",min_marks)