#findFN(Tree, current_level, sequence, level) -> str:
#    if current_level == level:
#        return prize
#    else:
#        if sequence[current_level-1] == 'l':
#            findFN(tree.left(current_level + 1, sequence)
#        else:
#           findFN(tree.right(current_level + 1, sequence)
                   
#written with the correct variable names
from prize_tree_sandcastles import *
from typing import Union

def find_prize(prize_tree: Union[BinaryTree, None], sequence:list[str], end_level:int, current_level: int) -> str:
    if current_level == end_level:
        return prize_tree.prize
    else:
        if sequence[current_level-1] == "l":
            return find_prize(prize_tree.left, sequence, end_level, current_level +1)
        else:
            return find_prize(prize_tree.right, sequence, end_level, current_level +1)
            
print(find_prize(prize_tree, ['l','l','l','l'], 4, 1))        