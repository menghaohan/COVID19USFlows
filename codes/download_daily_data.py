import requests
import os
import pandas as pd
import numpy as np
import argparse


parser = argparse.ArgumentParser(description='Start month, start day, and output_folder are necessary')
parser.add_argument('--start_month', type=str, default=True, help='Start month')
parser.add_argument('--start_day', type=str, default=True, help='Start day')
parser.add_argument('--end_month', type=str, help='End month')
parser.add_argument('--end_day', type=str, help='End day')
parser.add_argument('--output_folder', type=str, default=True, help='Output folder: ./')
parser.add_argument('--ct', action = 'store_true', help='ct2ct')
parser.add_argument('--county', action = 'store_true', help='county2county')
parser.add_argument('--state', action = 'store_true', help='state2state')

args = parser.parse_args()

start_month = str(args.start_month).zfill(2)
start_day = str(args.start_day).zfill(2)
output_folder = args.output_folder

if args.end_month == None:
    end_month = str(args.start_month).zfill(2)
else:
    end_month = str(args.end_month).zfill(2)
    
if args.end_day == None:
    end_day = str(args.start_day).zfill(2)
else:
    end_day = str(args.end_day).zfill(2)

# Download files of one day
def download_file(scale, month, day, output_folder):
    if os.path.exists(f"{output_folder}/{scale}/") == False:
        os.mkdir(f"{output_folder}/{scale}/")
    if scale == "ct2ct":
        if os.path.exists(f"{output_folder}/{scale}/{month}_{day}/") == False:
            os.mkdir(f"{output_folder}/{scale}/{month}_{day}/")
    try:
        if scale == "ct2ct":
            for i in range(20):
                r = requests.get(url=f"https://raw.githubusercontent.com/GeoDS/COVID19USFlows/master/daily_flows/{scale}/{month}_{day}/daily_{scale}_{month}_{day}_{i}.csv")
                with open(f"{output_folder}/{scale}/{month}_{day}/daily_{scale}_{month}_{day}_{i}.csv", 'wb') as file:
                    file.write(r.content)
        else:
            r = requests.get(url=f"https://raw.githubusercontent.com/GeoDS/COVID19USFlows/master/daily_flows/{scale}/daily_{scale}_{month}_{day}.csv")
            with open(f"{output_folder}/{scale}/daily_{scale}_{month}_{day}.csv", 'wb') as file:
                file.write(r.content)
        return True
    except Exception as e:
        print(e)
        return False

# Create time series dataframe
time_df = pd.date_range(start=f'2020-{start_month}-{start_day}', end=f'2020-{end_month}-{end_day}')
time_df = pd.DataFrame(time_df, columns=["date"])
time_df["year"] = time_df["date"].apply(lambda x: str(x.year).zfill(2))
time_df["month"] = time_df["date"].apply(lambda x: str(x.month).zfill(2))
time_df["day"] = time_df["date"].apply(lambda x: str(x.day).zfill(2))

# Download files at each scale
if args.ct == True:
    time_df.apply(lambda x: download_file('ct2ct', x.month, x.day, output_folder), axis=1)
if args.county == True:
    time_df.apply(lambda x: download_file('county2county', x.month, x.day, output_folder), axis=1)
if args.state == True:
    time_df.apply(lambda x: download_file('state2state', x.month, x.day, output_folder), axis=1)