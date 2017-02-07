'''
Created on Feb 4, 2017
@author: loanvo

Description:
'''

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

df = pd.read_csv('all.csv', header=0, names=["rating", 'review_count', 'isbn',
                                                          'booktype', 'author_url', 'year',
                                                          'genre_urls', 'dir', 'rating_count', 'name'])
print(df.head())


print('--------------------------type() only tell the type of a variable. It does not tell data type of each column. For example, type(df) gives:\n', type(df))
print('--------------------------type(df.rating):\n', type(df.rating))

print('--------------------------df.dtypes give type of each columns in the dataframe:\n', df.dtypes)

print('------------- some entries have null year -------------------')
print(df[df.year.isnull()])
df = df[~df.year.isnull()]  # equivalent to: df = df[df.year.notnull()]
# print(df[df.year.isnull()])
print('After eliminate null entries, we can change the type of the column')
df['year'] = df.year.astype(int)
df['rating_count'] = df.rating_count.astype(int)
df['review_count'] = df.review_count.astype(int)
print('--------------------------After changing rating_count, review_count and year into integer:\n', df.dtypes)
print('--------------------------shape of the data frame:\n', df.shape)

print('--------------------------names of all columns:\n', df.columns)
print('--------------------------ratio of number of rating<3:\n', np.sum(df.rating < 3) / df.shape[0])
print('--------------------------ratio of number of rating calculated by np.mean func:\n', np.mean(df.rating < 3))
print('--------------------------Using query:\n', df.query("rating > 4.8"))
print('--------------------------Using boolean index selection: year<0: \n', df[df.year < 0])
print('--------------------------Using boolean index selection: year<0 and rating>4:\n', df[(df.year < 0) & (df.rating > 4)])

print('--------------------------df.rating.hist():\n', df.rating.hist())
sns.set_context("notebook")
meanrat = df.rating.mean()
print(meanrat, np.mean(df.rating), df.rating.median())  # get the means and medians in different ways
plt.figure()
with sns.axes_style("whitegrid"):
    df.rating.hist(bins=30, alpha=.9)
    plt.axvline(meanrat, 0, .75, color='r', label='mean')  # ymin and ymax: between 0 and 1, 0 being the bottom of the plot, 1 the top of the plot
    plt.xlabel('average rating of book')
    plt.ylabel("Counts")
    plt.title("Ratings histogram")
    plt.legend()
plt.figure()
plt.subplot(211)
df.review_count.hist(bins=np.arange(0, 40000, 400))
plt.subplot(212)
df.review_count.hist(bins=100)
plt.xscale("log")
plt.figure()
plt.scatter(df.year, df.rating, lw=0, alpha=.08)
plt.xlim([1900, 2010])
plt.xlabel("Year")
plt.ylabel("Rating")

print('--------------------------Vector/numpy array vs. list:\n',)
alist = list(range(1, 6))
avector = np.arange(1, 6)
print('a list:', alist)
print('an numpy array or vector:', avector)
print('a list + a list:', alist + alist)
print('a np.array + np.array:', avector + avector)
print('a list * 2:', alist * 3)
print('a np.arary * 2:', avector * 3)
print('a list + [1] (has to list(1) or [1], otherwise it will throw an error as a list cannot be concatenated with an integer :', alist + [1])
print('a np.array + 1:', avector + 1)
# plt.show()


