##### "It needs to be 20% cooler" - Rainbow Dash.

import sys
from termcolor import colored, cprint

textexample = 'Windows Vista wasn\'t very good.'

text = colored(textexample, 'red', attrs=['reverse', 'blink'])
print(text)
cprint(textexample, 'green', 'on_cyan')

print_red_on_cyan = lambda x: cprint(textexample, 'red', 'on_cyan')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint('Attention!', 'red', attrs=['bold'], file=sys.stderr)

### Do the thing.
print(colored('~~~RAINBOW~~~', 'red'))
print(colored('~~~RAINBOW~~~', 'yellow'))
print(colored('~~~RAINBOW~~~', 'green'))
print(colored('~~~RAINBOW~~~', 'cyan'))
print(colored('~~~RAINBOW~~~', 'blue'))
print(colored('~~~RAINBOW~~~', 'magenta'))
