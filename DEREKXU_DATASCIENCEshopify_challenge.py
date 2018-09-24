#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:22:53 2018

@author: Derek
"""

# import necessary libraries
import pandas as pd

og_df = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv", index_col=0)


# calculate AOV of initial data set

order_amount = og_df['order_amount'].sum()
num_orders = og_df['order_amount'].count()

print("The total sales presented in the data set: " + str(order_amount))

print("The number of orders present in the data set: " + str(num_orders))

print("Thus, the average order value is: $" + str(round(order_amount/num_orders, 2)))


# show a dataframe containing unusually large numbers of sales and order value
print("Ten largest order values: ")

ten_large = og_df.sort_values('order_amount', axis=0, ascending=False, inplace=False, kind='mergesort', na_position='last')
                
print(ten_large.loc[:,['shop_id', 'order_amount', 'total_items']].head(20))

bad_data = og_df[og_df['order_amount'] > 2000]

print(bad_data.loc[:,['shop_id', 'order_amount', 'total_items']])

clean_data = og_df.drop(bad_data.index[:])

print(clean_data[clean_data['order_amount'] > 2000].head())


#reassign values to order_amount and num_orders using clean data
order_amount = clean_data['order_amount'].sum()
num_orders = clean_data['order_amount'].count()

print("Total sales in clean data: " + str(order_amount))
print("Number of orders in clean data: " + str(num_orders))
print("New AOV is: $" + str(round(order_amount/num_orders, 2)))