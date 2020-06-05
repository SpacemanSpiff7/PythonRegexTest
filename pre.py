import sys
import argparse
import re

if __name__ == "__main__":
    p = argparse.ArgumentParser(prog='Regex Tester', usage='Regex Tester:\n\n\t$ python pre.py -o match -r <REGEX> -s <SOME STRING> [-f <OR SOME FILE>] ')
    p.add_argument('-r', action='store', dest='regex_string', help='Regular expression. Wrap with  single quotes or escape all escape characters')
    p.add_argument('-s', action='store', dest='input_string', help='String to search on')
    p.add_argument('-f', action='store', dest='filepath', help='Search a file instead of input string')
    p.add_argument('-o', action='store', dest='op', default='split', help='Regex operation from python \'re\' module to use (default is \'split\').\nOptions are: match, split, sub, findall, or fullmatch')

    if len(sys.argv) == 1:
        p.print_help()
        exit(1)
        
    args = p.parse_args()

    searchstring = ""
    if args.filepath != None:
        with open(args.filepath, 'r') as ifp:
            searchstring = '\n'.join(ifp.readlines())
    
    else:
        searchstring = args.input_string

    accepted_operations = {'match':re.match, 'split':re.split, 'sub':re.sub, 'findall':re.findall, 'fullmatch':re.fullmatch}

    try:
        result = accepted_operations[args.op](args.regex_string, searchstring)
        if len(searchstring) > 10:
            strpreview = searchstring[:10] + '...({} chars not shown)'.format(len(searchstring) - 10)
        else:
            strpreview = searchstring
        print('Results for re.{}( \'{}\' , \'{}\' )'.format(args.op, args.regex_string, strpreview))
        print(result)
    except KeyError:
        print('Regex op must match one of following: {}'.format(accepted_operations))
        exit(1)

    exit(0)
