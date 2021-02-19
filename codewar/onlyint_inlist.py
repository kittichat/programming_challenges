def filter_list(l):
  for i in l:
    print(i)
    if type(i) == str:
      l.remove(i)
  return l

array1 = [1,2,'test','testfs','testef']
filter_list(array1)
print(array1)
