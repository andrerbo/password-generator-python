import click
from generator import setup, generate_password, check


@click.option('-l', '--lenght', required=True, type=int, default=12)
@click.option('-p', '--punctuation', is_flag=True, default=False)
@click.command()
def main(lenght: int, punctuation: bool) -> None:
    chars = setup(punctuation)
    password = generate_password(lenght, chars)
    while not check(password, chars):
        password = generate_password(lenght, chars)
    print(password)


if __name__ == '__main__':
    main()