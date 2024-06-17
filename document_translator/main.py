from typer import Typer

from .word import app as word_app

app = Typer(no_args_is_help=True)
app.add_typer(word_app, name="word")
