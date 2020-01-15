import re
import os

def build_match_function(pattern, replace):    
    def matches_rule(itext):
        find_pattern = re.compile(pattern, re.MULTILINE|re.DOTALL)
        return find_pattern.findall(itext)
    def apply_rule(itext):
        otext = re.sub(pattern,replace.strip(),itext)
        return otext
    return (matches_rule, apply_rule)

def rules(filename):
    with open(filename, encoding="utf-8") as pattern_file:
        for line in pattern_file:
            pattern, replace = line.split("|",2)
            yield build_match_function(pattern,replace)

def main(directory="navsrc", rules_file="findfirst_rule.txt"):
    i,j  = 0,0
    for r, d, f in os.walk(directory):
        for filename in f:
            ifile = open(os.path.join(r,filename), "r", encoding="cp850")
            itext = ifile.read()
            ifile.close()
            for matches_rule, apply_rule in rules(rules_file):
                result = matches_rule(itext)
                if  result:
                    print("{} - {}".format(os.path.join(r,filename), len(result)))
                    i += 1
                    j += len(result)
                    #print(result)
                    #itext = apply_rule(itext)
            ofile = open(os.path.join(r,filename), "w+", encoding="cp850")
            ofile.write(itext)
            ofile.close
    print("Objects: {}, Matches: {}".format(i , j))

main()

#TODO ASCENDING(FALSE)
#TODO ... BEGIN .... REPEAT
#TODO Comment rule
