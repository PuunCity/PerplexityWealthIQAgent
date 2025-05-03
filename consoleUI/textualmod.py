from textual.app import App, ComposeResult
from textual.widgets import Label

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Label("Hi there")

MyApp().run()