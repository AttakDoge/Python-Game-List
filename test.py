import json
import pandas as pd
import os
import pyperclip as pc
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll, Horizontal # how do these work
from textual.widgets import Footer, RadioButton, RadioSet, Label, Button, Markdown

def stars(number):
    empty = 5 - number
    star = '★' * number + '☆' * empty
    return star

launch_loc = ''
exe = ''
top_title = """\
## Game Selector
"""
website = ''

class test(App):
    BINDINGS = [('Q', 'quit', 'Quit')]
    def compose(self) -> ComposeResult:
        yield Markdown(top_title)
        with VerticalScroll(): # allows for scrolling
            with open('ex_format.json', 'r') as openfile: # loading ex_format.json, will change this in the future to be more user friendly or smth
                data = json.load(openfile) # turns json file into array (see test2.py)
                global game_data # make it global so that we cane use it later for game selection
                game_data = pd.DataFrame(data) # turns array into dataframe (see test3.py)
            with RadioSet():
                for x in game_data['name']: # add game names to radio list
                    yield RadioButton(x)
        with VerticalScroll(): # Game data display
            yield Label("Game Name: ", id="name")
            yield Label("Developer: ", id="dev")
            yield Label("Tags: ", id="tags")
            yield Label("Date added: ", id='date_added')
            yield Label("Rating: ", id='rating')
            yield Label("Game Website: ", id="website")
            with Horizontal(): # place buttons next to each other
                yield Button("Launch Game", id='launch', variant='primary') # button to launch game
                yield Button("Copy Website Link", id="copy", variant="primary") # button to copy website to clipboard
        yield Footer()
    
    def action_quit(self):
        self.exit()
    
    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        '''
        old testing
        #acbc = ("aaa","bbb","ccc")
        #self.query_one('#prs', Label).update(acbc[event.radio_set.pressed_index])
        '''

        global game_data, launch_loc, exe, website
        game = game_data.iloc[event.radio_set.pressed_index]

        self.query_one('#name', Label).update("Game Name: " + game['name'])
        self.query_one('#dev', Label).update("Developer: " + game['developer'])
        self.query_one('#tags', Label).update("Tags: " + ", ".join(game['tags']))
        self.query_one('#date_added', Label).update("Date added: " + game['date_added'])
        self.query_one('#rating', Label).update("Rating: " + stars(game['rating']))
        launch_loc = game['path_to_game']
        exe = game['game_exe']
        self.query_one("#website", Label).update("Game Website: " + game['page_link'])
        website = game['page_link']
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'launch':
            global launch_loc, exe, website
            if not(launch_loc == ''):
                self.notify(message='Placeholder, will launch app in future: ' + launch_loc + exe)
                # code not ready yet to test, no actual testing data yet
                '''
                cwd = os.getcwd()
                try:
                    os.chdir(launch_loc)
                    os.startfile(exe)
                except Exception as e:
                    self.notify(f'App could not start due to error: {e}')
                finally:
                    os.chdir(cwd)
                '''
            else:
                self.notify(message='No game selected, select one then try again.', severity="error")
        elif event.button.id == "copy":
            if not(website == ''):
                pc.copy(website) # copy website to clipboard using pyperclip
                self.notify(message="Copied!")
            else:
                self.notify(message="No game selected, select one then try again.", severity="error")

test().run()