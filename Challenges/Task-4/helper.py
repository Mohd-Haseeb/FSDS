import pandas as pd


def excel_to_csv():
    df = pd.read_excel('../../FSDS_DATA_SET/Attribute DataSet.xlsx')
    print(df.tail())

    df.to_csv('../../FSDS_DATA_SET/atribute.csv',index=False)

# excel_to_csv()


def read_attribute_data():
    df_attr = pd.read_csv(r'../../FSDS_DATA_SET/Dress Sales.xlsx')

    # df_attr.drop('Unnamed: 0', axis=1, inplace=True)

    # df_attr.to_csv('attribute.csv',sep=',')

    print(df_attr.head())

# read_attribute_data()

# df =  pd.read_csv("/Users/mohdhaseeb/Desktop/FSDS-Bootcamp/FSDS_DATA_SET/atribute.csv")

# print(df.head())

