import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def input_error_check(user_input, option_list, option):
    """
    Checks whether user input was correct. If not, input options are shown again and user can make another input until input is correct.

    Arg:
        (str) user_input - input of user to the prior question
        (str) option_list - list of valid options for user input
        (str) option - topic of question for which user is asked for input. E.g. city, filter, month, day

    Returns:
        (str) user_inpit - input of user
    """
    # If user input was not correct, possible options are shown and user is prompted to choose an option
    while user_input not in option_list:
        print('Ups, your input was not recognized. Your options for {} are:'.format(option))
        for i in range(len(option_list)):
            print(option_list[i])
        if option == 'filter':
            user_input = input('Please choose a {}.\n'.format(option)).lower()
        else:
            user_input = input('Please choose a {}.\n'.format(option)).title()
                           
    return user_input


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = ['Chicago', 'New York City', 'Washington']
    city = input('Would you like to see data for Chicago, New York City, or Washington?\n').title()

    # check if input is a listed city
    city = input_error_check(city, city_list, 'city')

    # get user input for filter options (month, day, both, none).
    filter_options = ('month', 'day', 'both', 'none')
    filter = input('Would you like to filter the data? Available options are "month", "day", "both", or "none" for no filter.\n').lower()

    # check if input is a listed filter option
    filter = input_error_check(filter, filter_options, 'filter')

    month_list = ('January', 'February', 'March', 'April', 'May', 'June')
    day_list = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    # if filter option month was chosen, user is asked to input a month for the filter, day is set to 'all' 
    if filter == 'month':
        # get user input for month (January, February, ... , June)
        month = input('Which month would you like to see - January, February, March, April, May, or June?\n').title()
        # check if input is a listed month
        month = input_error_check(month, month_list, 'month')

        day = 'all'

    # if filter option 'day' was chosen, user is asked to input a day for the filter, month is set to 'all' 
    elif filter == 'day':
        # get user input for day of week (Monday, Tuesday, ... Sunday)
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
        # check if input is a listed day of week
        day = input_error_check(day, day_list, 'day')

        month = 'all'
    # if filter option 'both' was chosen, user is asked to input a month and day for the filter 
    elif filter == 'both':
        # get user input for month (January, February, ... June)
        month = input('Which month would you like to see - January, February, March, April, May, or June?\n').title()
        # check if input is a listed month
        month = input_error_check(month, month_list, 'month')

        # get user input for day of week (Monday, Tuesday, ... Sunday)
        day = input('Which day would you like to see - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
        # check if input is a listed day of week
        day = input_error_check(day, day_list, 'day')
 
    # if filter option 'none' was chosen, month and day are set to 'all'
    elif filter == 'none':
        month = 'all'
        day = 'all'
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
    # read csv file for selected city
    df = pd.read_csv(CITY_DATA[city.lower()])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # if filter option month was not set to 'all', DataFrame is filtered for selected month
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # if filter option day was not set to 'all', DataFrame is filtered for selected day
    if day != 'all':
        # filter by day to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def mode_count(df, column, option):
    """
    Function that calculates the mode and total count of DataFrame columns
    depending on the 'option' input.

    Arg:
              df - DataFrame for calculation
        (str) column - which column shall be evaluated
        (str) option - what shall be calculated

    Returns:
        mode_val or max_count
    """
        
    if option =='mode':
        mode_val = df[column].mode()[0]
        return mode_val
    elif option =='count':
        max_count = df[column].value_counts().max()
        return max_count


def total_avg_trip(df, column_calc, column_sort, sort_by, option):
    """
    Function that calculates the sum and average of DataFrame columns
    depending on the 'option' input.

    Arg:
              df - DataFrame for calculation
        (str) column_calc - which column shall be evaluated
        (str) cloumn_sort - input to sort/group evaluated data
        (Str) sort_by - criteria for sorting/grouping of evaluated data
        (str) option - what shall be calculated

    Returns:
        total_trip or avg_trip
    """
    if option == 'total':
        total_trip = df[column_calc][df[column_sort] == sort_by].sum()
        return total_trip
    elif option == 'avg':
        avg_trip = df[column_calc][df[column_sort] == sort_by].mean()
        return avg_trip

    total_trip = df['Trip Duration'][df['Start Station']==mcsst].sum()
    avg_trip = df['Trip Duration'][df['Start Station']==mcsst].mean()


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel for {} filtered by month = {} and day = {}...\n'.format(city.title(), month, day))
    start_time = time.time()

    # display the most common month (mcm) and total number of trips
    month_list = ('January', 'February', 'March', 'April', 'May', 'June')
    mcm = mode_count(df, 'month', 'mode')
    mcm_count = mode_count(df, 'month', 'count')
    print('The most common month: {} with a total of {} rentals.'.format(month_list[mcm-1], mcm_count))
    
    # display the most common day of week (mcw) and total number of trips
    mcd = mode_count(df, 'day_of_week', 'mode')
    mcd_count = mode_count(df, 'day_of_week', 'count')
    print('The most common day: {} with a total of {} rentals.'.format(mcd, mcd_count))
    

    # display the most common start hour (mch) and total number of trips
    mch = mode_count(df, 'hour', 'mode')
    mch_count = mode_count(df, 'hour', 'count')
    print('The most common hour: {} with a total of {} rentals.'.format(mch, mch_count))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, city, month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip for {} filtered by month = {} and day = {}...\n'.format(city.title(), month, day))
    start_time = time.time()

    # display most commonly used start station (mcsst), total number of trips, total trip duration and average trip duration 
    mcsst = mode_count(df, 'Start Station', 'mode')
    mcsst_count = mode_count(df, 'Start Station', 'count')
    total_trip = total_avg_trip(df, 'Trip Duration', 'Start Station', mcsst, 'total')
    avg_trip = total_avg_trip(df, 'Trip Duration', 'Start Station', mcsst, 'avg')
    print('The most commonly used start station: {}\n...total trip count: {} \n...average trip duration: {}s \n...total trip duration: {}s \n'.format(mcsst, mcsst_count, int(avg_trip), int(total_trip)))

    # display most commonly used end station (mcest), total number of trips, total trip duration and average trip duration 
    mcest = mode_count(df, 'End Station', 'mode')
    mcest_count = mode_count(df, 'End Station', 'count')
    total_trip = total_avg_trip(df, 'Trip Duration', 'End Station', mcest, 'total')
    avg_trip = total_avg_trip(df, 'Trip Duration', 'End Station', mcest, 'avg')
    print('The most commonly used end station: {} \n...total trip count: {} \n...average trip duration: {}s \n...total trip duration: {}s \n'.format(mcest, mcest_count, int(avg_trip), int(total_trip)))
    

    # display most frequent route (mcf) from start to end station, total number of trips, total trip duration and average trip duration 
    df['Route'] = df['Start Station'] + ' to ' + df['End Station']
    mfr = mode_count(df, 'Route', 'mode')
    mfr_count = mode_count(df, 'Route', 'count')
    total_trip = total_avg_trip(df, 'Trip Duration', 'Route', mfr, 'total')
    avg_trip = total_avg_trip(df, 'Trip Duration', 'Route', mfr, 'avg')
    print('The most frequent route: {} \n...total count: {} \n...average trip duration: {}s \n...total trip duration: {}s \n'.format(mfr, mfr_count, int(avg_trip), total_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, city, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Statistics for {} filtered by month = {} and day = {}...\n'.format(city.title(), month, day))
    start_time = time.time()
    
    # display total travel time
    total_trip = df['Trip Duration'].sum()
    print('Total travel time: {}s'.format(int(total_trip)))

    # display mean travel time
    avg_trip = df['Trip Duration'].mean()
    print('Average travel time: {}s'.format(int(avg_trip)))

    # display total number of trips
    total_trip_count = df['Start Time'].value_counts().sum()
    print('Total number of trips: {}\n'.format(total_trip_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats for {} filtered by month = {} and day = {}...\n'.format(city.title(), month, day))
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts()
    print('Counts of User Types in database: \n{}\n'.format(user_count))

    # Output for user that for Washington no gender and year of birth data is available 
    if city == 'Washington':
        print('Sorry, no gender and year of birth data available for {}.'.format(city.title()))

    # Display counts of gender and earliest (min_yob), most recent (max_yob), and most common (mc_yob) year of birth
    # for Chicago and New York City
    else:
        gender_count = df['Gender'].value_counts()
        print('Counts of Gender in database: \n{} \n'.format(gender_count))
        min_yob = df['Birth Year'].min()
        max_yob = df['Birth Year'].max()
        mc_yob = mode_count(df, 'Birth Year', 'mode')
        print('Earliest year of birth: {}'.format(int(min_yob)))
        print('Most recent year of birth: {}'.format(int(max_yob)))
        print('Most common year of birth: {}'.format(int(mc_yob)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(data, city):
    """
    Ask user to display first 5 rows of raw data.
    If first 5 rows want to be shown, user can decide to see the next 5 rows.
    If Washington is selected as city, only the first 6 columns are shown as there
    is no gender and year of birth data available.

    """

    j = 0
    # Ask user if raw data shall be shown
    show = input('Would you like to see the first 5 rows of raw data? Y/N \n')
    # While user wants to see raw data
    while show.lower() == 'y':
        # Print each line separate
        for j in range(j,j+5):
            # For Washington, only 6 columns are printed
            if city == 'Washington':
                print('Row {}'.format(j+1))
                print('[{}]\n'.format(data.T.iloc[1:7,j]))
            # For Chicago and New York City 8 columns are printed
            else:
                print('Row {}'.format(j+1))
                print('[{}]\n'.format(data.T.iloc[1:9,j]))
            
        j += 1
        show = input('Would you like to see the next 5 rows of raw data? Y/N \n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
       
        time_stats(df, city, month, day)
        station_stats(df, city, month, day)
        trip_duration_stats(df, city, month, day)
        user_stats(df, city, month, day)
        show_data(df, city)

        restart = input('\nWould you like to restart? Y/N \n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
