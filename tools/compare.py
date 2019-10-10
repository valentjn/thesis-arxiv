#!/usr/bin/python3

import argparse
import functools
import multiprocessing
import os
import shlex
import shutil
import subprocess



directory = "/tmp/compare"



def run(args, pipe=True, **kwargs):
  print("Running \"{}\"...".format(
      " ".join([shlex.quote(arg) for arg in args])))
  if pipe: kwargs["stdout"] = subprocess.PIPE
  process = subprocess.run(args, check=True, **kwargs)
  if pipe: return process.stdout.decode()



def convertToPng(pdfPaths, i):
  subDirectory = os.path.join(directory, "out{}".format(i+1))
  firstImagePath = os.path.join(directory, "pdf{}-0.png".format(i))

  if os.path.isfile(firstImagePath):
    print("{} already exists.".format(firstImagePath))
  else:
    print("Converting PDF file {} to PNGs...".format(i+1))
    pngPath = os.path.join(directory, "pdf{}.png".format(i))
    run(["convert", "-density", "100", pdfPaths[i], "-alpha", "flatten",
         pngPath])



def diffPage(imagePaths, diffPaths, j):
  if os.path.isfile(diffPaths[j]):
    print("{} already exists.".format(diffPaths[j]))
  else:
    print("Diffing page {}...".format(j + 1))
    run(["composite", imagePaths[j][0], imagePaths[j][1],
         "-compose", "difference", diffPaths[j]])

  output = run(
      ["identify", "-format", "%[fx:mean]#%[fx:maxima]", diffPaths[j]]).strip()
  return [float(x) for x in output.split("#")]



def generateResult(imagePaths, diffPaths, resultPaths, j):
  run(["convert", imagePaths[j][0], diffPaths[j], imagePaths[j][1],
       "+append", resultPaths[j]])



def main():
  parser = argparse.ArgumentParser(
      description="Compares two PDF files by comparing rasterized pages")
  parser.add_argument("--mean-threshold", metavar="VALUE", type=float,
      default=0, dest="meanThreshold",
      help="Mean difference threshold between 0 and 1")
  parser.add_argument("--max-threshold", metavar="VALUE", type=float,
      default=0, dest="maxThreshold",
      help="Maximum difference threshold between 0 and 1")
  parser.add_argument("pdfPath1", metavar="FILE1",
      help="first PDF file to compare")
  parser.add_argument("pdfPath2", metavar="FILE2",
      help="second PDF file to compare")
  args = parser.parse_args()

  os.makedirs(directory, exist_ok=True)
  pdfPaths = [args.pdfPath1, args.pdfPath2]

  with multiprocessing.Pool() as pool:
    pool.map(functools.partial(convertToPng, pdfPaths), range(2))

  pageCount = 0
  imagePaths = []

  while True:
    curImagePaths = [
        os.path.join(directory, "pdf{}-{}.png".format(i, pageCount))
        for i in range(2)]
    if any([not os.path.isfile(x) for x in curImagePaths]): break
    pageCount += 1
    imagePaths.append(curImagePaths)

  diffPaths = [os.path.join(directory, "diff-{}.png".format(j))
               for j in range(pageCount)]

  with multiprocessing.Pool() as pool:
    brightnesses = pool.map(
        functools.partial(diffPage, imagePaths, diffPaths), range(pageCount))

  brightnesses = {i : x for i, x in enumerate(brightnesses)}
  pagesChanged = [i for i in range(pageCount)
      if (brightnesses[i][0] > args.meanThreshold) and
         (brightnesses[i][1] > args.maxThreshold)]
  pagesChanged.sort(key=lambda i: -brightnesses[i][0])

  resultsDirectory = os.path.join(directory, "results")
  if os.path.isdir(resultsDirectory): shutil.rmtree(resultsDirectory)
  os.makedirs(resultsDirectory)
  resultPaths = [os.path.join(resultsDirectory, "result_{}.png".format(j+1))
                 for j in range(pageCount)]

  with multiprocessing.Pool() as pool:
    pool.map(
        functools.partial(generateResult, imagePaths, diffPaths, resultPaths),
        pagesChanged)

  if len(pagesChanged) > 0:
    print("Pages with changes (sorted by mean difference "
        "in descending order): {}".format(
          ", ".join([str(x+1) for x in pagesChanged])))
    subprocess.Popen(["gwenview", resultPaths[pagesChanged[0]]],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
  else:
    print("No changes detected.")



if __name__ == "__main__":
  main()
