import sys
from datetime import datetime

def main(*args, **kwargs):
    if len(args) == 0 or args[0].lower() not in ['false', 'true']:
        print('usage: python stachometr.py <true | false>')
        return
    
    with open('rzuty.csv', 'a') as f:
        f.write(str(datetime.now()) + ',' + str(args[0].lower() == 'true') + '\n')

if __name__ == '__main__':
    main(*sys.argv)
