from prize_tree_sandcastles import *
from drafter import *
from dataclasses import dataclass
from random import randint
import time


@dataclass
class State:
    name: str
    surfed: bool
    napped: bool
    built_castle: bool
    hero: bool
    start_time: float
    sandcastles: list[Sandcastle]
    prize_tree: Union[BinaryTree, None]
    
   
@route
def index(state: State) -> Page:
    return Page(state, [
        "Welcome to the beach! Input your name to continue.",
        TextBox(name="name", kind="text", default_value="Beach Goer"),
        Button(text="Next", url="/start")
        ])


@route
def start(state: State, name: str) -> Page:
    state.name = name
    return main_page(state)


@route
def main_page(state: State) -> Page:
    if state.surfed and state.napped and state.built_castle:
        return Page(state, [
            ("Hi " + state.name + " There are lot's of things to do at the beach. Complete all the activites to win a prize."),
            Button(text="Go surf", url="/surf"),
            Button(text="Go nap", url="/nap"),
            Button(text="Build a Sandcastle", url="/build"),
            Button(text="Win a prize", url="/prize_page")
            ])
    
    else:
        return Page(state, [
            ("Hi " + state.name + "! There are lot's of things to do at the beach. Complete all the activites to win a prize."),
            Button(text="Go surf", url="/surf"),
            Button(text="Go nap", url="/nap"),
            Button(text="Build a Sandcastle", url="/build")
            ])
    

@route
def surf(state:State) -> Page:
    state.surfed = True
    return Page(state, [
        "Welcome to surfing. Click the button to hop on a board",
        Button(text="Hop on", url="/ride_wave")
        ])


@route
def ride_wave(state:State) -> Page:
    hero_condition = randint(0,100)
    if hero_condition > 85: 
        return Page(state, [
            Image(url="Distressed Swimmer.png", width=None, height=None),
            "Uh OH. It looks like someone is in trouble.",
            "Do you want to help them?",
            SelectBox("rescue", ["Yes", "No"]),
            Button(text="Continue", url="/hero_page")
            ])
    else:
        return Page(state, [
            Image(url="Ride Wave.png", width=None, height=None),
            "Wow that was a big wave. Nice job",
            Button(text="Go Back", url="/main_page")
            ])
    
    
@route
def hero_page(state:State, rescue:str) -> Page:
    if rescue == "Yes":
        state.hero = True
        return Page(state, [
            Image(url="hero.png", width=None, height=None),
            "Thank goodness you saved that person. That was close!",
            Button(text="Go Back", url="/main_page")
            ])
    else:
        return Page(state, [
            "The lifeguard saved him. Thanks anyway.",
            Image(url="Thumbs UP.png", width=None, height=None),
            Button(text="Go Back", url="/main_page"),
            ])
                    
                    
@route
def nap(state:State) -> Page:
    state.start_time = time.time()
    return Page(state, [
        "ZZZZZZZZZZZZ",
        Image(url = "Sleepy.png", width=None, height=None),
        Button(text="WAKE UP", url="/wake_up")
        ])


@route
def wake_up(state:State) -> Page:
    elapsed_time = time.time() - state.start_time
    if elapsed_time > 3:
        state.surfed = False
        state.napped = False
        state.built_castle = False
        state.hero = False
        return Page(state, [
            "You slept too long and got sunburned",
            "All of your tokens are gone.",
            "You'll have to start over now.",
            Button(text="Start again", url="/main_page")
            ])
    else:
        state.napped = True
        return Page(state, [
            "That was a good nap",
            Button(text="Go Back", url="/main_page")
            ])
    
    
@route
def build(state:State) -> Page:
    return Page(state, [
        "Select from the following options to build your sandcastle",
        "Select a style",
        SelectBox("style", ["gothic", "modern", "fairytale"]),
        "Enter a height from 1 to 3",
        TextBox(name="height", kind="text", default_value="1"),
        Button(text="Build", url="/castle_output")
    ])
    
    
@route
def castle_output(state:State, style:str, height:str) -> Page:
    if float(height) > 3:
        return Page(state, [
            "That's too big. Enter a smaller height.",
            Button(text="Go Back", url="/build")
            ])
    else: 
        height = round(float(height))
        image = state.sandcastles[0].image
    
        for castle in state.sandcastles:
            if style == castle.style and castle.height == height:
                image = castle.image
                break
        state.built_castle = True
        return Page(state, [
            "Here is your sandcastle",
            Image(url=image, width=None, height=None),
            Button(text= "Go back", url="/main_page")
        ])


@route
def prize_page(state:State) -> Page:
    if state.hero:
        return Page( state, [
            "You are the hero of the day.",
            "For your efforts you win the golden prize.",
            Image(url="Golden Trophy.png", width=None, height=None)
            ])
    else:
        return Page(state, [
            "Tree image",
            "Welcome to the prize tree.",
            "To win a prize, you get to pick a branch of the tree.",
            "Start by picking how high up the tree you will climb, up to 6 levels.",
            SelectBox("end_level", ['1','2','3','4','5','6']),
            "Now, pick how you will climb the branches of the tree. You can either go left or right as you climb up.",
            "Enter an L for left or R for right. Enter 1 L or R for each level you speciifed.",
            "For example, if you want to go 4 levels, you could enter LLRL.",
            TextBox(name="sequence", kind="text", default_value=None),
            Button(text="Next", url="/pick_prize")
            ])


def find_prize(current_tree: Union[BinaryTree, None], sequence:str, end_level:int, current_level: int) -> str:
    if current_level == end_level:
        return current_tree.prize
    else:
        if sequence[current_level - 1] == "l":
            return find_prize(current_tree.left, sequence, end_level, current_level + 1)
        else:
            return find_prize(current_tree.right, sequence, end_level, current_level + 1)


@route
def pick_prize(state:State, end_level:int, sequence:str) -> Page:
    prize = find_prize(state.prize_tree, sequence, end_level, 1)
    return Page(state, [
        "Here is your prize",
        prize
        ])


start_server(State("", False, False, False, False, 0.0, sandcastles,
            prize_tree_assembly(temp_prize_list_FN(preset_prize_list), 6, 1)))