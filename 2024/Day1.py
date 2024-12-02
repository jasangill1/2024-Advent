Data = """
90335   63839
39658   98833
58540   26663
34246   52806
83116   82954
"""

rows = Data.strip().split('\n')

x2, y2 = zip(*(map(int, row.split())for row in rows))
print('Total Distance:',sum([abs(y - x) for x, y in zip(sorted(x2),sorted(y2))]))



