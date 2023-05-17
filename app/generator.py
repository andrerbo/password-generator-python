import random

# lowercase: from 97 to 122 -> range(97, 123)
# uppercase: from 69 to 90 -> range(69, 91)
# punctuation: -> [33, 35, 36, 37, 38, 42, 43, 45, 46, 58, 59, 63, 64, 95]

def generate_password(lenght: int, chars: dict) -> str:

    if len(chars) == 2:
        choices = random.choices(
            ['uppercase', 'lowercase'],
            [0.5, 0.5],
            k=lenght
        ) 
    else: 
        choices = random.choices(
            ['uppercase', 'lowercase'],
            [0.5, 0.5],
            k=1
        ) \
        + random.choices(
            [x for x in chars.keys()],
            [0.4, 0.4, 0.2],
            k=lenght-1
        )
        
    password = ''
    for i in choices:
        password += chr(random.choice(chars[i]))
    
    return password


def setup(has_punctuation: bool) -> dict:

    chars = {
        'lowercase': [x for x in range(97, 123)],
        'uppercase': [x for x in range(69, 91)],
        'punctuation': [33, 35, 36, 37, 38, 42, 43, 45, 46, 58, 59, 63, 64, 95]
    }

    if not has_punctuation:
        chars.pop('punctuation')

    return chars


def check(password: str, chars: dict) -> bool:
    if punctuation := chars.get('punctuation'):
        for i in password:
            if ord(i) in punctuation:
                return True    
        return False
    return True


def get_password(lenght: int, punctuation: bool) -> str:
    chars = setup(punctuation)
    password = generate_password(lenght, chars)
    while not check(password, chars):
        password = generate_password(lenght, chars)
    
    return password
