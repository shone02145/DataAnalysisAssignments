from IPython.display import display, Markdown
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import pandas as pd

def display_title(s, pref='Figure', num=1, center=False):
    ctag = 'center' if center else 'p'
    s = f'<{ctag}><span style="font-size: 1.2em;"><b>{pref} {num}</b>: {s}</span></{ctag}>'
    s = f'{s}<br><br>' if pref=='Figure' else f'<br><br>{s}'
    display(Markdown(s))

def central(x):
    x_mean = np.mean(x)
    x_median = np.median(x)
    result = stats.mode(x, keepdims=True)
    x_mode = result.mode[0] if hasattr(result.mode, "__getitem__") else result.mode
    return x_mean, x_median, x_mode

def dispersion(x):
    std_dev = np.std(x)
    minimum = np.min(x)
    maximum = np.max(x)
    range_val = maximum - minimum
    q25 = np.percentile(x, 25)
    q75 = np.percentile(x, 75)
    iqr = q75 - q25
    return std_dev, minimum, maximum, range_val, q25, q75, iqr

def display_central_tendency_table(df, num=1, round_dict=None):
    display_title('Central tendency summary statistics.', pref='Table', num=num)
    df_central = df.apply(lambda x: central(x), axis=0)
    if round_dict is not None:
        df_central = df_central.round(round_dict)
    df_central.index = ['mean', 'median', 'mode']
    display(df_central)

def display_dispersion_table(df, num=1, round_dict=None):
    display_title('Dispersion summary statistics.', pref='Table', num=num)
    df_dispersion = df.apply(lambda x: dispersion(x), axis=0)
    if round_dict is not None:
        df_dispersion = df_dispersion.round(round_dict)
    df_dispersion.index = ['st.dev.', 'min', 'max', 'range', '25th', '75th', 'IQR']
    display(df_dispersion)

def plot_descriptive(df):
    co2 = df['co2_emissions']
    gdp = df['gdp_per_capita']
    pop = df['population']
    year = df['year']

    fig, axs = plt.subplots(1, 3, figsize=(10, 3), tight_layout=True)
    axs[0].scatter(gdp, co2, alpha=0.5, color='b')
    axs[1].scatter(pop, co2, alpha=0.5, color='r')
    axs[2].scatter(year, co2, alpha=0.5, color='g')

    xlabels = ['gdp per capita', 'population', 'year']
    for ax, s in zip(axs, xlabels):
        ax.set_xlabel(s)
    axs[0].set_ylabel('co2 emissions')

    for ax in axs[1:]:
        ax.set_yticklabels([])

    plt.show()
