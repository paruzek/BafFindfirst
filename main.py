import re
import os

def build_match_function(pattern):
    def matches_rule(itext):
        find_pattern = re.compile(pattern, re.DOTALL|re.MULTILINE)
        return find_pattern.finditer(itext)
    return (matches_rule)

def rules(filename):
    with open(filename, encoding="utf-8") as pattern_file:
        for line in pattern_file:
            yield build_match_function(line)

def main(directory="navsrc", rules_file="findfirst_rule.txt"):
    i = 0
    for filename in os.listdir(directory):
        print(filename)  
        ifile = open(os.path.join(directory,filename), "r", encoding="cp850")
        itext = ifile.read()
        ifile.close
        for matches_rule in rules(rules_file):
            for match in  matches_rule(itext):
                print(match.group(1))
                i += 1
    print(i)

main()
        

