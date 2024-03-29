# It should return the name of the elevator closest to the called floor ("left"/"right").

# In the case where both elevators are equally distant from the called floor, choose the elevator to the right.

# You can assume that the inputs will always be valid integers between 0-2.

# Examples:

# elevator(0, 1, 0) # => "left"
# elevator(0, 1, 1) # => "right"
# elevator(0, 1, 2) # => "right"
# elevator(0, 0, 0) # => "right"
# elevator(0, 2, 1) # => "right"

# in javascript


# function elevator(left, right, call){
#   let leftDis=Math.abs(call-left)
#   let rightDis=Math.abs(call-right)
#   if(rightDis <= leftDis){
#     return 'right'
#   }else{
#     return 'left'
#   }
# }




def elevator(left, right, call):
    '''Return the closest elevator depending on the floor (call). If both are the same, return right'''
    left_distance = abs(call-left)
    right_distance = abs(call-right)
    if right_distance <= left_distance:
        return 'right'
    return 'left'