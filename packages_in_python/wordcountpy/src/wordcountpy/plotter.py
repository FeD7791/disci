import matplotlib.pyplot as plt
from wordcountpy.count_words import count_words as word_counts

def plot_words(word_counts, n=10):
    ''' Plot abarchartofwordcounts.'''
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel('Word')
    plt.ylabel('Count')
    return fig

