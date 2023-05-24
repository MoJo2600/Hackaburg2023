import pandas as pd

data = pd.read_csv('adresses-201811.csv', delimiter=';')

extr = data['postal_code'].str.extract(r'^(\d{5})', expand=False)
data['postal_code'] = pd.to_numeric(extr)
#data.loc[1:, 'postal_code'].head(10)
#data['postal_code'] = data.postal_code.astype("int32", errors='ignore')
data.query('postal_code > 93000 & postal_code < 93300', inplace=True)
# data.query('', inplace=True)

data.sample(n = 10000, replace = False)

data.to_csv('adresses_regensburg.csv')

print(data)



# merge companies with streets to retrieve lat/lon
data = pd.read_csv('raw/ratisbona-companies-addresses.csv')

new_data = pd.merge(pd.read_csv('out/addresses-ratisbona.csv'), data, on=['street', 'postal_code', 'street_number', 'city'], how='inner')
new_data.reset_index(drop=True, inplace=True)

new_data["id"] = new_data.index+1

new_data.to_csv('data/companies-ratisbona.csv', index=False)