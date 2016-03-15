from __future__ import division
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])

# print s

dates = pd.date_range('20130101', periods=6)

# print dates

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABC4'))

if isinstance(None, pd.DataFrame):
    print 12
# for x in df:
#     print x
#     print '~~~'
# print df

df2 = pd.DataFrame({ 'A' : 1.,
 'B' : pd.Timestamp('20130102'),
 'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
 'D' : np.array([3] * 4,dtype='int32'),
 'E' : pd.Categorical(["test","train","test","train"]),
 'test' : 'foo' })

# print df2
 
# print df.tail(0)
# 
# print df2.index
# print df2.columns
# print df2.describe()
# print df.T
# print df.sort_index(by='B', ascending =False)
# 
# print df.B

# print df[0:3]
# 
# print df.loc[dates[3]]
# 
# print df.loc[dates[3]:dates[5], ['A', 'C']]

# print df.iloc[-1]
# print df.iloc[[1,2,4], [0,2]]
# print df.iloc[1:3,:]


# print df2[df2.test == 'foo']

# print df[df > 0]
# 
# df2 = df.copy()
# 
# df2['E'] = ['1','2','3','4','1','2']
# 
# print df2
# print df2[df2['E'].isin(['3','5'])]

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))

df['F'] = s1

# print df
# 
# df.at[dates[1],'A'] = 0
# 
# df.iat[0,1] = 1002
# df.loc[:,'C'] = np.array([5]* len(df))
# print df

df2 = df.copy()
df2[df2 > 0] = -df2

# print df2
# df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
# df1.loc[dates[0]:dates[1],'E'] = 1
# 
# print df1
# print df1.dropna(how='any')
# print df1.fillna(value=5)
# print pd.isnull(df1)


# print df.mean()
# print df.mean(1)
# df.iloc[-1] = [3] * len(df.iloc[-1])
# print df
# print df.mean(1)
# s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(3)
# 
# print s
# print df.sub(s, axis='index')

# print df.apply(np.cumsum)
# print df.apply(lambda x: x.max() - x.min())
# 
# s = pd.Series(np.random.randint(0, 7, size=10))
# print s.value_counts()

df = pd.DataFrame(np.random.randn(10, 4))

# print df
# print len(df[2])
# pieces = [df[:3], df[3:7], df[7:]]
# print pieces[1]
# 
# print pd.concat(pieces)
# 
# 
# left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
# right = pd.DataFrame({'key': ['foo', 'xoo'], 'rval': [4, 5]})
# print pd.merge(left, right, on='key')

# df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
# s = df.iloc[3]
# print df.append(s, ignore_index=True)

# df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
#                            'foo', 'bar', 'foo', 'foo'],
#                     'B' : ['one', 'one', 'two', 'three',
#                            'two', 'two', 'one', 'three'],
#                     'C' : np.random.randn(8),
#                     'D' : np.random.randn(8)})
# 
# print df
# print df.groupby('A').sum()
# print df.groupby(['A','B']).sum()

# tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
#                  'foo', 'foo', 'qux', 'qux'],
#                 ['one', 'two', 'one', 'two',
#                 'one', 'two', 'one', 'two']]))
#     
# index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
# print index
# df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
# print df
# stacked = df2.stack()
# print stacked

# df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
#                      'B' : ['A', 'B', 'C'] * 4,
#                      'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
#                      'D' : np.random.randn(12),
#                      'E' : np.random.randn(12)})
# 
# print pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
# 
# 
# rng = pd.date_range('1/1/2012', periods=100, freq='S')
# ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
# print ts.resample('5Min', how='sum')
# print ts


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
plt.figure();ts.plot()