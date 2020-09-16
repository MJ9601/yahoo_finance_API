for label in ax.xaxis.get_ticklabels():
    label.set_rotation(30)
date_format = mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)