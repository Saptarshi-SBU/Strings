# python3
import numpy as np
import sys

def ConstructBWT(text):
  """
   Burrows-Wheeler Transform
  """
  bwt = ''
  bwt_mat = []
  bwt_ans = []

  text = text + '$'
  print('text {}'.format(text))
  # Implement this function yourself
  for i in range(0, len(text)):
    last = text[len(text) - 1]
    text = text[0 : len(text) - 1]
    text = ''.join([last, text])
    bwt_mat.append(text)
  bwt_mat.sort();

  for item in bwt_mat:
    print (item)
    bwt_ans.append(item[-1])

  print ('bwt: {}'.format(bwt_ans))
  for i in bwt_ans:
      bwt = bwt + i

  return bwt_mat, bwt

def PreprocessBWT(bwt):
  """

  Preprocess the Burrows-Wheeler Transform bwt of some text

  and compute as a result:

    * starts - for each character C in bwt, starts[C] is the first position 

        of this character in the sorted array of 

        all characters of the text.

    * occ_count_before - for each character C in bwt and each position P in bwt,

        occ_count_before[C][P] is the number of occurrences of character C in bwt

        from position 0 to position P inclusive.

  """
  # Implement this function yourself
  counts = {}
  occ_counts_before = {}
  charset = set(bwt)

  for i in charset:
    counts[i] = 0;
    occ_counts_before[i] = { 0 : 0 }

  for i in range(len(bwt)):
    counts[bwt[i]] += 1
    print i, bwt[i]
    for k in charset:
        occ_counts_before[k][i + 1] = counts[k]

  sorted_bwt = sorted(bwt) 
  starts = {x : sorted_bwt.index(x) for x in charset }
  print ('starts {}'.format(starts))
  for i in occ_counts_before:
    print ('occ {} : {}'.format(i, occ_counts_before[i]))
  return starts, occ_counts_before       

def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """

  Compute the number of occurrences of string pattern in the text

  given only Burrows-Wheeler Transform bwt of the text and additional

  information we get from the preprocessing stage - starts and occ_counts_before.

  """

  # Implement this function yourself
  top_index = 0
  bottom_index = len(bwt) - 1
  print ('pattern {}'.format(pattern))

  #reverse lookup using bwt-matrix
  while top_index <= bottom_index:
      if len(pattern):
        #scan pattern in reverse order  
        symbol = pattern[-1]
        #reduce pattern
        pattern = pattern[0 : len(pattern) - 1]
        #lookup pattern symbol
        if symbol in bwt:
            #index range for which partial query lookup is valid
            print ('==>symbol {} top {} bottom {}'.format(symbol, top_index, bottom_index))    
            print ('starts {} occ {}/{}'.format(starts[symbol], \
                occ_counts_before[symbol][top_index],
                occ_counts_before[symbol][bottom_index + 1]))
            top_index = starts[symbol] + \
                occ_counts_before[symbol][top_index]
            bottom_index = starts[symbol] + \
                occ_counts_before[symbol][bottom_index + 1] - 1
            print ('<==symbol {} top {} bottom {}'.format(symbol, top_index, bottom_index))    
        else:
            return 0
      else:
            return bottom_index - top_index + 1
  return 0

def InverseBWT(bwt, kmers):
  '''
    Inverse bwt to retrieve the text
  '''
  if len(kmers) == 0:
      a_column = sorted(bwt)
      n_column = bwt
      kmers = [i + j for i, j in zip(n_column, a_column)] 
      kmers = sorted(kmers)
      return InverseBWT(bwt, kmers)
  elif len(kmers[0]) == len(bwt):
      text = kmers[0].split('$')
      return text[1] + text[0]
  else:
      n_column = bwt
      kmers = [i + j for i, j in zip(n_column, kmers)] 
      kmers = sorted(kmers)
      return InverseBWT(bwt, kmers)

if __name__ == '__main__':

  bwt = "ACTAGACTAG" #sys.stdin.readline().strip()

  pattern_count = 1 #int(sys.stdin.readline().strip())

  patterns = ["ACTAG"] #sys.stdin.readline().strip().split()

  # Preprocess the BWT once to get starts and occ_count_before.

  # For each pattern, we will then use these precomputed values and

  # spend only O(|pattern|) to find all occurrences of the pattern

  # in the text instead of O(|pattern| + |text|).  

  bwt_mat, bwt = ConstructBWT(bwt)

  starts, occ_counts_before = PreprocessBWT(bwt)

  occurrence_counts = []

  for pattern in patterns:

    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))

  print(' '.join(map(str, occurrence_counts)))

  print(InverseBWT(bwt, []))
