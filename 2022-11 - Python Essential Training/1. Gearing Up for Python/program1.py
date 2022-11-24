import time, random

### You fuckers thought I was gonna follow the example and put "print('Hello, world!')"?
### Nah.

def zombocom():
    ### Wow, a function!
    for i in range(1, random.randint(10,100)):
        print(f'{time.asctime()} - Will has thought about Zombocom {i} times today.')
        time.sleep(0.2)
        if i == 69:
            print('lol')

zombocom()


### Did this for the meme potential.