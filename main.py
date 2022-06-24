import pandas as pd
import json
import streamlit as st

def calculate_profit_loss(data):


    print("Original DataFrame")

    print(data)


    # Create column for profit and loss
    data['KAR'] = None
    data['ZARAR'] = None

    data = data.astype({"DISTRIBUTOR_ADI": str})
    data = data.astype({"ID": float})
    data = data.astype({"SATIS_FIYATI": float})
    data = data.astype({"ALIS_FIYATI": float})
    data = data.astype({"KAR": float})
    data = data.astype({"ZARAR": float})

    print(data.dtypes)

    # set index
    index_selling = data.columns.get_loc('SATIS_FIYATI')
    index_cost = data.columns.get_loc('ALIS_FIYATI')
    index_profit = data.columns.get_loc('KAR')
    index_loss = data.columns.get_loc('ZARAR')

    print(index_selling, index_cost, index_profit, index_loss)


    # Loop for accessing every index in DataFrame
    # and compute Profit and loss
    # and store into new column in DataFrame
    for row in range(0, len(data)):
        if data.iat[row, index_selling] > data.iat[row, index_cost]:
            data.iat[row, index_profit] = data.iat[row,
                                                   index_selling] - data.iat[row, index_cost]
        else:
            data.iat[row, index_loss] = data.iat[row,
                                                 index_cost]-data.iat[row, index_selling]


    return data


if __name__ == '__main__':
    with open('records.json') as data_file:
        json_data = json.load(data_file)
    data = pd.DataFrame.from_dict(json_data['records'])
    result = calculate_profit_loss(data)
    st.title("KAR ZARAR ANALIZI")
    st.header('HAM VERİ')
    st.table(data)
    st.header('HESAP SONUCU')
    st.table(result)
