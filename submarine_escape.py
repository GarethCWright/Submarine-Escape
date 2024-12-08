from sys import exit

from submarine_dialogue import *


class Scene:
    pass


class Engine:
    def __init__(self, scene_map: "Map"):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.find_scene("finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.find_scene(next_scene_name)


class Finished(Scene):
    def enter(self):
        print("DA DA DAAAAA! You finsihed!")


class Death(Scene):
    def enter(self):
        print("Great job!")
        input()
        return "first_room"


class FirstRoom(Scene):
    def enter(self) -> str:
        print(DIALOGUE["firstroom_enter"])

        action = input(">")

        if action in ["shoot", "shoot them"]:
            print(DIALOGUE["firstroom_shoot"])
            return "death"
        elif action in ["tax", "tax the rich", "wealth tax"]:
            print(DIALOGUE["firstroom_taxes"])
            return "death"
        elif action in ["get drinks", "drinks"]:
            print(DIALOGUE["firstroom_drinks"])
            return "control_room"


class ControlRoom(Scene):
    def enter(self) -> str:
        print(DIALOGUE["controlroom_enter"])

        action = input(">")

        if action in ["tell", "tell billionaires", "tell them"]:
            print(DIALOGUE["tell_billionaires"])
        else:
            print(DIALOGUE["donttell_billionaires"])
        return "escapepod_alone"


class EscapepodEnterAlone(Scene):
    def enter(self) -> str:
        print(DIALOGUE["escapepod_enter_alone"])

        action = input(">")

        if action in ["ask billionaires", "billionaires", "get help"]:
            print(DIALOGUE["ask_billionaires"])
            return "death"
        elif action in ["look around"]:
            print(DIALOGUE["engineroom_enter"])
            return 'engine_room'

class EngineRoom(Scene):
    def enter(self):
        print(DIALOGUE["engineroom_enter"])
        input()
        return 'escapepod_paco'
        
class EscapepodEnterPaco(Scene):
    def enter(self):
        print(DIALOGUE["escapepod_enter_paco"])
        input()

        action = input(">")

        if action in ["activate tripwire", "tripwire"]:
            print(DIALOGUE["escapepod_tripwire"])
            return 'death'
        elif action in ["pigs", "release pigs"]:
            print(DIALOGUE["escapepod_pigs"])
            return 'keypad'
        else:
            print("You hesitate. The wealthy mob gets you and you die.")
            return 'death'
        
class Keypad(Scene):
    def enter(self):
        action = input(">")

        if action == "80085":
            print(DIALOGUE["keypad_guess"])
            #return 'finished'
        else:
            print(DIALOGUE["keypad_fail"])
            return 'death'


class Map:
    scenes = {
        "death": Death(),
        "first_room": FirstRoom(),
        "control_room": ControlRoom(),
        "escapepod_alone": EscapepodEnterAlone(),
        "engine_room": EngineRoom(),
        "escapepod_paco": EscapepodEnterPaco(),
        "keypad": Keypad(),
        "finished": Finished(),
    }

    def __init__(self, start_scene: str):
        self.start_scene = start_scene

    def find_scene(self, scene_name: str) -> Scene:
        return Map.scenes[scene_name]

    def opening_scene(self) -> Scene:
        return self.find_scene(self.start_scene)


a_map = Map("first_room")
a_game = Engine(a_map)
a_game.play()
