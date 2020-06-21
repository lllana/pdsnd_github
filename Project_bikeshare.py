import time
import pandas as pd
import numpy as np

# data used
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

GENDER_COLUMN = "Gender"
BIRTH_YEAR_COLUMN = "Birth Year"   

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = (str(input("Would you like to see the data for Chicago, New York City or Washington? "))).lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = (str(input("What month would you like to get the data for? All, January, February, March, April, May, June? "))).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = (str(input("Which day of the week? All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday? "))).lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most common month:', common_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of the week:', common_day_of_week)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', popular_start)

    # TO DO: display most commonly used end station
    popular_finish = df['End Station'].mode()[0]
    print('Most Frequent End Station:', popular_finish)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip route'] = 'From: ' + df['Start Station'] + ' To: ' + df['End Station']
    popular_route = df['Trip route'].mode()[0]
    print('Most Frequent combination of start station and end station trip:', popular_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_dur_sec = sum(df['Trip Duration'])

    trip_dur_min = trip_dur_sec / 60
    trip_dur_hour = trip_dur_sec / 3600

    print('Total travel time in sec: ', trip_dur_sec)
    print('Total travel time in min: ', trip_dur_min)
    print('Total travel time in hours: ',trip_dur_hour)

    # TO DO: display mean travel time
    mean_travel_time_sec = df['Trip Duration'].mean()
    mean_travel_time_min = mean_travel_time_sec / 60
    
    print('Mean travel time in sec: ', mean_travel_time_sec)
    print('Mean travel time in min: ', mean_travel_time_min)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types are: ", user_types)
    
    if GENDER_COLUMN and BIRTH_YEAR_COLUMN in df.columns:
        # TO DO: Display counts of genderno
        gender_counts = df[GENDER_COLUMN].value_counts()
        print("Gender counts are: ", gender_counts)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df[BIRTH_YEAR_COLUMN].min()
        print("The earliest year of birth: ", earliest_year)

        most_recent_year = df[BIRTH_YEAR_COLUMN].max()
        print("The most recent year of birth: ", most_recent_year)

        most_common_year = df[BIRTH_YEAR_COLUMN].mode()[0]
        print("The most common year of birth: ", most_common_year)
    else:
        print("Gender data is not available for Washington")
        print("Birth data is not available for Washington")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        i = 0
        raw = input("\nWould you like to see first 5 rows of raw data; type 'yes' or 'no'?\n").lower()
        pd.set_option('display.max_columns',200)
        while True:            
            if raw == 'no':
                break   
            print(df[i: i + 5])
            raw = input('\nWould you like to see next rows of raw data?\n').lower()
            i += 5   
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n').lower()
        if restart.lower() != 'yes':
            break
            p
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
