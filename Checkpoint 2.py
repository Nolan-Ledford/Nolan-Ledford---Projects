from random import randint
import time
from bakery import assert_equal
from dataclasses import dataclass
from drafter import *
@dataclass
class Sandcastle:
    style: str
    height: int
    image: str
@dataclass
class State:
    name: str
    surfed: bool
    napped: bool
    built_castle: bool
    hero: bool
    start_time: float
    sandcastles: list[Sandcastle]
    
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
    if hero_condition > 0: 
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

start_server(State("", False, False, False, False, 0.0, [
            Sandcastle('gothic', 3, 'Gothic 3.png'),
            Sandcastle('gothic', 2, 'Gothic 2.png'),
            Sandcastle('gothic', 1, 'Gothic 1.png'),
            Sandcastle('modern', 3, 'Modern 3.png'),
            Sandcastle('modern', 2, 'Modern 2.png'),
            Sandcastle('modern', 1, 'Modern 1.png'),
            Sandcastle('fairytale', 3, 'Fairytale 3.png'),
            Sandcastle('fairytale', 2, 'Fairytale 2.png'),
            Sandcastle('fairytale', 1, 'Fairytale 1.png'),
            ]))
