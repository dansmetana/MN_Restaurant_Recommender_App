#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: danielsmetana7@ MABA CLASS
"""
import pandas as pd
import streamlit as st

st.title("Twin Cities Restaurant Recommender")
st.markdown("Author: Daniel Smetana")

st.markdown("This application solves the constant question of where to eat by recommending restaurants to a user based upon their input. \
            Contained within the application are 215 of the Twin Cities' best and most-popular restaurants, making this app sustainable for long-term use without worry of repeats! \
            Furthermore, the list of restaurants is personally curated, filtering out undesirable spots that online search engines recommend, making this app truly unique.\
            All review stars shown are sourced from Google Reviews.")

st.markdown("Clicking submit below will produce your results and reset the form, allowing you to repeatedly use the application - searching until you find the restaurant that is calling your name.")


#Read the business dataset
mn_restaurant_data = pd.read_csv('TwinCities_Restaurant_Data.csv', encoding = "ISO-8859-1")

pd.DataFrame(mn_restaurant_data)



#isolate cities
mpls_restaurants = mn_restaurant_data[mn_restaurant_data["Minneapolis"] == "Y"]
stp_restaurants = mn_restaurant_data[mn_restaurant_data["St. Paul"] == "Y"]




#Functions to sort the data
requested_data = pd.DataFrame()


def restaurant_city_filter(requested_data, city):
    if city == "Minneapolis":
        requested_data = mpls_restaurants.copy()
        return requested_data
    elif city == "St. Paul":
        requested_data = stp_restaurants.copy()
        return requested_data
    elif city == "No Preference":
        requested_data = mn_restaurant_data.copy()
        return requested_data
    else:
        return "Error - Sorry, no restaurants match your search criteria"


def restaurant_type_filter(requested_data, restaurant_type):
    if restaurant_type == "Fast-Casual":
        requested_data = requested_data[requested_data["Restaurant Type"] == "Fast-Casual"].copy()
        return requested_data
    elif restaurant_type == "Casual Sit-Down":
        requested_data = requested_data[requested_data["Restaurant Type"] == "Casual Sit-Down"].copy()
        return requested_data
    elif restaurant_type == "Fancy Sit-Down":
        requested_data = requested_data[requested_data["Restaurant Type"] == "Fancy Sit-Down"].copy()
        return requested_data
    elif restaurant_type == "No Preference":
        requested_data = requested_data
        return requested_data
    else:
        return "Error - Sorry, no restaurants match your search criteria"


def restaurant_chain_local_filter(requested_data, chain_local):
    if chain_local == "Chain":
        requested_data = requested_data[requested_data["Chain or Local"] == "Chain"].copy()
        return requested_data
    elif chain_local == "Local":
        requested_data = requested_data[requested_data["Chain or Local"] == "Local"].copy()
        return requested_data
    elif chain_local == "No Preference":
        requested_data = requested_data
        return requested_data
    else:
        return "Error - Sorry, no restaurants match your search criteria"


def restaurant_cusine_type(requested_data, cuisine_type):
    if cuisine_type == "American":
        requested_data = requested_data[requested_data["Cuisine Type"] == "American"].copy()
        return requested_data
    elif cuisine_type == "Asian":
        requested_data = requested_data[requested_data["Cuisine Type"] == "Asian"].copy()
        return requested_data
    elif cuisine_type == "Italian":
        requested_data = requested_data[requested_data["Cuisine Type"] == "Italian"].copy()
        return requested_data
    elif cuisine_type == "Latin":
        requested_data = requested_data[requested_data["Cuisine Type"] == "Latin"].copy()
        return requested_data
    elif cuisine_type == "French":
        requested_data = requested_data[requested_data["Cuisine Type"] == "French"].copy()
        return requested_data
    elif cuisine_type == "Health":
        requested_data = requested_data[requested_data["Cuisine Type"] == "Health"].copy()
        return requested_data
    elif cuisine_type == "Mediterranean":
        requested_data = requested_data[requested_data["Cuisine Type"] == "Mediterranean"].copy()
        return requested_data
    elif cuisine_type == "No Preference":
        requested_data = requested_data
        return requested_data
    else:
        return "Error - Sorry, no restaurants match your search criteria"


def restaurant_meal_filter(requested_data, meal_type):
    if meal_type == "Brunch/Breakfast":
        requested_data = requested_data[requested_data["Brunch/Breakfast"] == "Y"].copy()
        return requested_data
    elif meal_type == "Lunch":
        requested_data = requested_data[requested_data["Lunch"] == "Y"].copy()
        return requested_data
    elif meal_type == "Dinner":
        requested_data = requested_data[requested_data["Dinner"] == "Y"].copy()
        return requested_data
    elif meal_type == "No Preference":
        requested_data = requested_data
        return requested_data
    else:
        return "Error - Sorry, no restaurants match your search criteria"



#Master function

def master():
    requested_data = pd.DataFrame()
    try:
        with st.form(key = "Input your search criteria", clear_on_submit = True):
            bypass_for_random = st.radio("Do you want to search based on specific criteria, or just receive a random restaurant? ", ("Search based on criteria", "Random"))
            city = st.selectbox("Please select the city: ", ("Minneapolis", "St. Paul", "No Preference"))
            restaurant_type = st.selectbox("Please select the type of restaurant experience: ", ("Fast-Casual", "Casual Sit-Down", "Fancy Sit-Down", "No Preference"))
            chain_local = st.selectbox("Please select local or chain restaurant: ", ("Local", "Chain",  "No Preference"))
            cuisine_type = st.selectbox("Please select the cuisine type: ", ("American", "Asian", "French", "Health", "Italian", "Latin", "Mediterranean", "No Preference"))
            meal_type = st.selectbox("Please select the meal time: ", ("Brunch/Breakfast", "Lunch", "Dinner", "No Preference"))
            random_or_top_N = st.radio("Do you want to see a random restaurant that meets your criteria, or the top N restaurants (sorted by Google Reviews)?", ("Random", "Top N"))
            top_N = st.slider("How many of the top restaurants do you want to see? ", min_value = 1, max_value = 10)
            top_N = int(top_N)
            submit_button = st.form_submit_button("Submit")


        if submit_button:
            if bypass_for_random == "Random":
                requested_data = mn_restaurant_data[["Restaurant Name", "Restaurant URL", "Review Stars"]].sample(n = 1)
                master_output = requested_data
                st.write("Below are your results - enjoy!")
                st.table(master_output)
            else:
                if random_or_top_N == "Random":
                   requested_data = restaurant_city_filter(requested_data, city=city)
                   requested_data = restaurant_type_filter(requested_data, restaurant_type = restaurant_type)
                   requested_data = restaurant_chain_local_filter(requested_data, chain_local = chain_local)
                   requested_data = restaurant_cusine_type(requested_data, cuisine_type = cuisine_type)
                   requested_data = restaurant_meal_filter(requested_data, meal_type = meal_type)
                   master_output = requested_data[["Restaurant Name", "Restaurant URL", "Review Stars"]].sample(n = 1)
                   st.write("Below are your results - enjoy!")
                   st.table(master_output)
                else:
                   requested_data = restaurant_city_filter(requested_data, city=city)
                   requested_data = restaurant_type_filter(requested_data, restaurant_type = restaurant_type)
                   requested_data = restaurant_chain_local_filter(requested_data, chain_local = chain_local)
                   requested_data = restaurant_cusine_type(requested_data, cuisine_type = cuisine_type)
                   requested_data = restaurant_meal_filter(requested_data, meal_type = meal_type)
                   requested_data = requested_data.sort_values(by = ["Review Stars"], ascending=False)
                   master_output = requested_data[["Restaurant Name", "Restaurant URL", "Review Stars"]].head(top_N)
                   st.write("Below are your results - enjoy!")
                   st.table(master_output)
    except ValueError:
        st.write("Oops! No restaurants match your search criteria - please try different criteria")

master()
