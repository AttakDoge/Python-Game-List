import json
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll, Horizontal # how do these work
from textual.widgets import Footer, RadioButton, RadioSet, Label

class test(App):
    BINDINGS = [('Q', 'quit', 'Quit')]
    def compose(self) -> ComposeResult:
        with VerticalScroll(): # what???
            with Horizontal(): # what???
                with open('testdata.json', 'r') as openfile: # loading testdata.json and disp shows only the top level (in this case, game1 and game2)
                    abcb = json.load(openfile) # turns json file into dictionary (see test2.py)
                with RadioSet():
                    for x in abcb:
                        yield RadioButton(x)
        yield Label(id="prs")
        yield Footer()
    
    def action_quit(self):
        self.exit()
    
    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        acbc = ("aaa","bbb","ccc")
        self.query_one('#prs', Label).update(acbc[event.radio_set.pressed_index])

test().run()