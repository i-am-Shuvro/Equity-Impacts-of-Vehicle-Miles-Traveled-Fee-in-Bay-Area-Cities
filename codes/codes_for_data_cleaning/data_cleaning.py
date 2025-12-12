#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: notebook.ipynb
Conversion Date: 2025-12-12T06:05:43.875Z
"""

import pandas as pd
#importing data
df_location = pd.read_csv('survey_location.csv')
df_household = pd.read_csv('survey_household.csv')
df_trip = pd.read_csv('survey_trip.csv')
df_vehicle = pd.read_csv('survey_vehicle.csv')
df_person = pd.read_csv('survey_person.csv')

#Filtering by selected cities
keep_cities = ["SAN FRANCISCO", "DALY CITY", "OAKLAND", "Berkeley", "ALAMEDA"]
df_location = df_location[df_location["city"].isin(keep_cities)]
df_location = df_location[["sampno", "city"]]
df_location.to_csv("survey_location_filtered.csv", index=False)

#Re-import and select key variables
df_location_filtered = pd.read_csv("survey_location_filtered.csv")
df_household_sub = df_household[["sampno", "urbrur", "gasprice", "hhfaminc"]]
df_trip_sub = df_trip[["sampno","vmt_mile"]]
df_trip_sub = df_trip_sub[df_trip_sub["vmt_mile"] != -1]
df_vehicle_sub = df_vehicle[["sampno", "vehno","veh_year","fuel_type_nrel"]]
df_vehicle_sub = df_vehicle_sub[df_vehicle_sub["fuel_type_nrel"].notna()]
df_person_sub = df_person[["sampno", "perno"]]

#Merging
df_lochh = pd.merge(df_location_filtered, df_household_sub, on="sampno", how="inner")
df_lochhveh = pd.merge(df_lochh, df_vehicle_sub, on="sampno", how="inner")
df_all = pd.merge(df_lochhveh, df_trip_sub, on="sampno", how="inner")
df_all = pd.merge(df_all, df_person_sub, on="sampno", how="inner")

num_cols = df_all.select_dtypes(include=["number"]).columns
df_all = df_all[(df_all[num_cols] >= 0).all(axis=1)]

#Adding fuel economy standards
df_mpg_std = pd.read_csv("Average fuel economy standard.csv")
df_all_mpg = pd.merge(
    df_all,        
    df_mpg_std,    
    on="veh_year",
    how="left"     
)
df_all_mpg.loc[df_all_mpg["veh_year"] < 1977, "mpg_std"] = 18

df_all_mpg.to_csv("df_df_cleanest+mpg.csv", index=False)