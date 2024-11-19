from dataclasses import dataclass
from random import randint
from typing import Union

@dataclass
class Sandcastle:
    style: str
    height: int
    image: str

sandcastles = [
            Sandcastle('gothic', 3, 'Gothic 3.png'),
            Sandcastle('gothic', 2, 'Gothic 2.png'),
            Sandcastle('gothic', 1, 'Gothic 1.png'),
            Sandcastle('modern', 3, 'Modern 3.png'),
            Sandcastle('modern', 2, 'Modern 2.png'),
            Sandcastle('modern', 1, 'Modern 1.png'),
            Sandcastle('fairytale', 3, 'Fairytale 3.png'),
            Sandcastle('fairytale', 2, 'Fairytale 2.png'),
            Sandcastle('fairytale', 1, 'Fairytale 1.png'),
            ]


@dataclass
class Tree:
    pass


@dataclass
class BinaryTree(Tree):
    value: int
    prize: str
    left: Union[Tree, None]
    right: Union[Tree, None]

    
preset_prize_list = [
    "Beach Ball", "Beach Ball", "Beach Ball", "Beach Ball", "Beach Ball",
    "Sea Shell", "Sea Shell", "Sea Shell", "Sea Shell", "Sea Shell",
    "Sand Dollar","Sand Dollar","Sand Dollar","Sand Dollar","Sand Dollar",
    
    "Brand new surfboard", "Jet Ski", "Nothing", "Ray Bans", "Stanley Cup",
    
    "Cooler", "Cooler", "Cooler", "Cooler", "Cooler",
    "Water", "Water", "Water", "Water", "Water",
    "Free Fries", "Free Fries", "Free Fries", "Free Fries", "Free Fries",
    
    "A new car", "A new skateboard", "Nothing", "Free fries for life", "Nothing",
    
    "A Funnel Cake", "A Funnel Cake", "A Funnel Cake", "A Funnel Cake", "A Funnel Cake",
    "A Football", "A Football", "A Football", "A Football", "A Football",
    "Volleyball", "Volleyball", "Volleyball", "Volleyball", "Volleyball",
    
    "Nothing", "A boat", "Beach Chair", "Beach Umbrella", "Nothing",
    
    "Suncreen", "Suncreen", "Suncreen", "Suncreen", "Suncreen",
    "Sun Hat", "Sun Hat", "Sun Hat",
    ]


def temp_prize_list_FN(preset_prize_list:list[str]) -> list[str]:
    temp_prize_list = preset_prize_list
    return temp_prize_list


def prize_tree_assembly(prize_list: list[str], depth: int, current_value: int) -> Union[BinaryTree, None]:
    if depth == 0:
        return None
    
    left_child = prize_tree_assembly(prize_list, depth - 1, current_value * 2)
    right_child = prize_tree_assembly(prize_list, depth - 1, current_value * 2 + 1)
    
    current_position = randint(0, len(preset_prize_list)-1)
    current_prize = prize_list[current_position]
    prize_list.pop(current_position)
    
    return BinaryTree(
        value = current_value,
        prize = current_prize,
        left = left_child,
        right = right_child)

