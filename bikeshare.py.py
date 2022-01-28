import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    city = input("In order to view available bikeshare data, type the city name: \nChicago\nor New York City\nor Wahington\n").lower()
    
    while city not in CITY_DATA.keys():
        print('\nThat\'s invalid input\n')
        city = input("In order to view available bikeshare data, type the city name: \nChicago\nor New York City\nor Wahington\n").lower()
        
    month=input("\nTo filter city for specific month, please type the month or all for not filtering by month: \n-January\n-February\n-March\n-April\n-May\n-June\n-All\n").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print('\nPlease select correctly\n')
        month=input("\nTo filter city for specific month, please thype the month or all for not filtering by month: \n-January\n-February\n-March\n-April\n-May\n-June\n-All\n").lower()
        
    day=input("\nAnd to filter data with specific day, kindly type an abb. of day such as (Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday) or all to bring out data with no filter\n").lower()
    while day not in ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']:
        print('Please enter a valid day')
        day=input("\nAnd to filter data with specific day, kindly type an abb. of day such as (Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday) or all to bring out data with no filter\n").lower()
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    
    if month != 'all':
        months=['january', 'february', 'march', 'april', 'may', 'june']
        month=months.index(month)+1
        df=df[df['month'] == month]
    if day != 'all':
        df=df[df['day_of_week'].str.startswith(day.title())]
                                               
    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print("The most common month is: ", df['month'].mode()[0])
    print("The most common start day is: ", df['day_of_week'].mode()[0])
    print("The most common start hour is: " ,df['Start Time'].dt.hour.mode()[0])                                           
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print("Most commonly used start station is: ", df['Start Station'].mode()[0])
    print("Most commonly used end station is: ", df['End Station'].mode()[0])
    df['combined'] = df ['Start Station'] + "_" + df['End Station']
    print("Most frequent combined stations: ", df['combined'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print("Here total travel time: ", df['Trip Duration'].sum())
    print(" and here mean travel time: ", df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print("Let\'s see types of users and their count: \n", df['User Type'].value_counts().to_frame())
                                               
    try:
        gender_count = df['Gender'].value_counts().to_frame()
        print("When we see the count of each gender: \n", gender_count)
    except:
        print('Finding count of gender ....\nAwfully sorry we have no data about gender')
    print('Finding your data\n\n')
                                               
    try:
        year_of_birth = int(df['Birth Year'].min())
        print("Our earlist member was born in: ", yaer_of_birth)
    except:
        print("Finding year our earlist member was born .....\nSorry this info. is missed")
    print('Finding your data\n\n')
                                               
    try:
        recently_born = int(df['Birth Year'].max())
        print("Our latest joined member was born in: ", recently_born)
    except:
        print("Checking year of birth of our recent members......\nAlso their info is missed.")
                                               
    try:
        common_birth_year = int(df['Birth Year'].mode()[0])
        print("The common year of birth wa have: ", common_birth_year)
    except:
        print("Let\'s checking the common year of birth ......\nSorry again not available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    print("Raw data is available upon request")
    display_raws = input("Do you want to check raw data? Please enter yes or no\n").lower()
    while display_raws not in ["yes" , "no"]:
        print("We can dispaly accurately if  you answer us more clear")
        display_raws = input("Do you want to check raw data? Please enter yes or no\n").lower()
    if display_raws.lower() == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], chunksize = 5):
                print(chunk)
                display_raws = input("Would you like to see extra 5 raws? enter yes or no\n").lower()
                while display_raws not in ['yes', 'no']:
                    print("Do you really need extra data?")
                    display_raws = input("Would you like to see extra 5 raws? enter yes or no\n").lower()
                if display_raws.lower() == 'yes':
                    continue                               
                if display_raws.lower() == 'no':
                    print("Thank you!")                           
                    break                           
        except KeyboardInterrupt:
            print("Thank You!")                                       
                                               
def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)          
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart not in ["yes", "no"]:
                print("We could not identify your answer\n")                  
                restart = input('\nWould you like to restart? Enter yes or no.\n').lower()  
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
