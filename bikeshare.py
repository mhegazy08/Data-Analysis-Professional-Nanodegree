import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = list(CITY_DATA.keys())
months = ['january', 'feburary', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter one city from Chicago, New York City, or Washington: ").lower()
    while city not in cities:
        print("This is not one the 3 proposed cities, please choose another one.")
        city = input("Please enter one city from Chicago, New York City, or Washington: ").lower()
    

# TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please select the month, from the first half of the year, you want to filer by. \nType "all" if you don\'t want to filter by month.').lower()
    while month not in months:
        print("Please choose another option.")
        month = input('Please select the month, from the first half of the year, you want to filer by. \nType "all" if you don\'t want to filter by month.').lower()
              
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please choose a day of the week. \nType "all" if you don\'t want to filter by day.').lower()
    while day not in days:
        print("Please choose a suitable day")
        day = input('Please choose a day of the week. \nType "all" if you don\'t want to filter by day.').lower()

    print('-'*40)
    return city, month, day
###############################################################################

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
    filename = CITY_DATA[city]
    df = pd.read_csv(filename) #read the csv file.
    df['Start Time'] = pd.to_datetime(df['Start Time']) #convert the "Start Time" column to datetime.
    #create a new column for months and days of the week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # check if the user wants to filter or not
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # check if the user wants to filter by day or not
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df
#########################################################################################################################

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
#create a new column for the start hours
    df['hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month is: ", popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day of the week is: ", popular_day)


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour is: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
######################################################################################################
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    #count the number of times when the most commonly used start station was selected
    count_start = df['Start Station'].value_counts().max()
    print('The most commonly used start station was "{}" and it was selected {} times.'.format(popular_start_station, count_start))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    #count the number of times when the most commonly used end station was selected
    count_end = df['End Station'].value_counts().max()
    print('The most commonly used end station was "{}" and it was selected {} times.'.format(popular_end_station, count_end))

    # TO DO: display most frequent combination of start station and end station trip
    #Create first a new column for the combination of start/end stations
    df['Trip'] = "from " + df['Start Station'] + " to " + df['End Station']
    #Get the most frequebt combination
    popular_trip = df['Trip'].mode()[0]
    #count the number of times this combination was chosen
    count_end = df['Trip'].value_counts().max()
    print('The most frequent combination was "{}" and it was selected {} times.'.format(popular_trip, count_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The average travel time is: ", mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_users = df['User Type'].value_counts()
    #create a for loop to get all the possible user types and print a sentence for each user type
    for i in range(len(count_users)):
        print("The number of {}s is: {}".format(count_users.index[i], count_users[i])) #getting the user type using .index and then the corresponding count
                                               
    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
#create a for loop to get all the two genders and print a sentence for each gender
        for i in range(len(count_gender)):
            print("The number of {}s is: {}".format(count_gender.index[i], count_gender[i])) #getting the gender using .index and then the corresponding count
    except:
        print("The data for this city doesn't contain gender classification column.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        early_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        most_com_year = df['Birth Year'].mode()[0]
        print("The earliest year of birth is: ", early_year)
        print("The most recent year of birth is: ", recent_year)
        print("The most common year of birth is: ", most_com_year)
    except:
        print("There is no birth year column for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
##########################################################################################
def display_raw_data(city):
    """ Dispalys 5 random rows from the filter chosen of the specific city
        as long as the user is choosing yes. Continues showing 5 random rows 
        till the user chooses no. Got help in this function from egfwd community hub"""
    df = pd.read_csv(CITY_DATA[city])
    while True:
        response = input("Do you want to see a sample of raw data? (yes/no)").lower()
        if response not in ["yes", "no"]:
            print('Please type "yes" or "no" only.')
        elif response == "yes":
            print(df.sample(5))
        elif response == "no":
            print("\nExiting...")
            break
###########################################################################################    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
