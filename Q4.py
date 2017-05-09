def mystery(l):
   if l == []:
      return (l)
   else:
      return (l[-1:] + mystery(l[:-1]))
