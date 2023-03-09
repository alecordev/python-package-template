__version__ = '0.0.1'

print("library")


from typer import Typer

app = Typer()


@app.command()
def hello():
    print("Hello.")


@app.command()
def bye(name: str):
    print(f"Bye {name}")


def main():
    print("main")


if __name__ == '__main__':
    main()
