#!/usr/bin/python3

import re
import subprocess
import sys

# list of custom filter regexs
FILTER_REGEXS = [
  r"^ system commands enabled\.$",
  r"^entering extended mode$",
  r"^ restricted \\write18 enabled.$",
  r"^LaTeX2e <[0-9\-]+>$",
  r"^luaotfload | main : initialization completed in ",
  r"^Babel <.*> and hyphenation patterns for .* language\(s\) loaded\.$",
  r"^Document Class: ",
  r"^Package scrlfile, .* \(loading files\)$",
  r"^ *Copyright \(C\) Markus Kohm$",
  r"^Package hyperref Message: Driver \(autodetected\): ",
  r"^Package hyperref Message: Driver: hpdftex.",
  r"^For additional information on amsmath, use the `\?' option\.$",
  r"^Document Style algorithmicx .* - a greatly improved "
      r"`algorithmic' style$",
  r"^Document Style - pseudocode environments for use with the "
      r"`algorithmicx' style$",
  r"^Loading lettrine\.cfg$",
  r"^\*geometry\* driver: ",
  r"^\*geometry\* detected driver: ",
  r"^AED: lastpage setting LastPage$",
  r"^ *[0-9]+ words of node memory still in use:$",
  r"^ *[0-9]+ [a-z_]+(, [0-9]+ [a-z_]+)* nodes$",
  r"^ *avail lists: ",
  r"^SyncTeX written on ",
  r"^Transcript written on ",
  r"^Loading configuration file `contour\.cfg'\.$",
  r"^contour: Using driver file `.*'\.",
  r"^contour: Using [0-9]+ copies for ",
]



# run LaTeX command with supplied arguments
process = subprocess.Popen(sys.argv[1:], stdout=subprocess.PIPE)

# while LaTeX is still running
while process.poll() is None:
  # get next line (blocks), strip final newline
  line = process.stdout.readline().decode()
  if len(line) == 0: continue
  line = line[:-1]
  
  if len(line) == 0:
    # skip if line is empty
    continue
  elif line[0] in "(":
    # skip if line starts with "(" and doesn't have the form
    # "(blabla)  ", these are usually warning lines and blabla is
    # the package that emits the warning
    if re.match(r"\([A-Za-z0-9]+\)  ", line) is None: continue
  elif line[0] in ")[]{}<>":
    # skip if line starts with a bracket of any other type
    continue
  
  # skip if line matches one of the custom filter regexs as specified above
  if any(re.search(regex, line) is not None for regex in FILTER_REGEXS):
    continue
  
  # print line if not skipped, flush
  print(line, flush=True)

# return with LaTeX exit code
sys.exit(process.returncode)
