import investpy
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Definitions and initializations
currency = []
save_path = '/home/ubuntu/Desktop/ALLPAIRS/'

# Today's date
today_date = datetime.today().strftime('%d/%m/%Y')

# Get list of currencies and the ruble pairing ones
currency_list = investpy.get_currency_crosses_list()
[currency.append(x) for x in currency_list if '/BGN' in x]

# Remove duplicate ones:
currency_pairs = list(dict.fromkeys(currency))

# Loop through the cleaned pairs
for currency_pair in currency_pairs:
    # call the API and get the information
    investing_api = investpy.get_currency_cross_historical_data(currency_cross=currency_pair, from_date='01/01/1900',
                                                                to_date=today_date, order='ascending', interval='Daily')

    invest_plot = pd.DataFrame(investing_api)
    new = invest_plot.reset_index()
    new.plot(x ='Date', y='Close', kind = 'line')
    saveto = save_path + currency_pair.replace("/","")  + '.png'
    plt.savefig(saveto)
    print(currency_pair + " Saved to " + saveto)
    
