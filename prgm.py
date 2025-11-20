import json
from textual.app import App, ComposeResult
from textual.widgets import Footer, RadioButton, RadioSet, Header, Label

class main(App):
    BINDINGS = [('Q', 'quit', 'Quit')]
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True, time_format="%#I:%M.%S", icon='☼')
        
        yield Footer(show_command_palette=False)
    def on_mount(self) -> None:
        self.title = "asdf"
    
    def action_quit(self):
        self.exit()
    

if __name__ == "__main__":
    app = main()
    app.run()