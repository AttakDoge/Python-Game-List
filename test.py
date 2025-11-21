import json
import pandas as pd
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll, Horizontal # how do these work
from textual.widgets import Footer, RadioButton, RadioSet, Label, Collapsible

class test(App):
    BINDINGS = [('Q', 'quit', 'Quit')]
    def compose(self) -> ComposeResult:
        with VerticalScroll(): # allows for scrolling
            with open('ex_format.json', 'r') as openfile: # loading ex_format.json, will change this in the future to be more user friendly or smth
                data = json.load(openfile) # turns json file into array (see test2.py)
                global game_data # make it global so that we cane use it later for game selection
                game_data = pd.DataFrame(data) # turns array into dataframe (see test3.py)
            with RadioSet():
                for x in game_data['name']: # add game names to radio list
                    yield RadioButton(x)
        with VerticalScroll():
            yield Label(id="name")
            yield Label(id="dev")
            yield Label(id="tags")
        yield Footer()
    
    def action_quit(self):
        self.exit()
    
    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        '''
        old testing
        #acbc = ("aaa","bbb","ccc")
        #self.query_one('#prs', Label).update(acbc[event.radio_set.pressed_index])
        '''

        global game_data
        game = game_data.iloc[event.radio_set.pressed_index]

        self.query_one('#name', Label).update("Game Name: " + game['name'])
        self.query_one('#dev', Label).update("Developer: " + game['developer'])
        self.query_one('#tags', Label).update("Tags: " + ", ".join(game['tags']))

test().run()