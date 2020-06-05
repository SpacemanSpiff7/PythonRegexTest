# PythonRegexTest
Quickly  test your regular expressions in the command line

Install:

`git clone https://github.com/SpacemanSpiff7/PythonRegexTest`

usage: Regex Tester:

	$ python pre.py -o match -r <REGEX> -s <SOME STRING> [-f <OR SOME FILE>]

optional arguments:
  -h, --help       show this help message and exit
  -r REGEX_STRING  Regular expression. Wrap with single quotes or escape all
                   escape characters
  -s INPUT_STRING  String to search on
  -f FILEPATH      Search a file instead of input string
  -o OP            Regex operation from python 're' module to use (default is
                   'split'). Options are: match, split, sub, findall, or
                   fullmatch
