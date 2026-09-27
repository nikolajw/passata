import secrets
from importlib import resources

import typer

app = typer.Typer()

@app.command()
def main(choices: int = 10, min_word_length: int = 15, is_complex: bool = False):
    """
    Generates a multi-word passphrase
    """
    data = load_words()
    passwords = [generate_pwd(data, min_word_length) for _ in range(choices)]
    for password in passwords:
        print(password)


def generate_pwd(data, min_length: int) -> str:
    pwd: str = ""
    while len(pwd) < min_length:
        word = secrets.choice(data).capitalize()
        pwd += word

    return pwd


def load_words() -> list[str]:
    words = set()
    package_dir = resources.files("passata")

    for entry in package_dir.iterdir():
        if entry.name.endswith(".txt"):
            with entry.open("r") as f:
                words.update(line.strip() for line in f)

    return list(words)
