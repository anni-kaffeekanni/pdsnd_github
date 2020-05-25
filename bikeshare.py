import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#weekdaysand month_name added to turn weekdayand month numbers into names
weekdays={0:'monday',1:'tuesday',2:'wednesday',3:'thursday',4:'friday',5:'saturday',6:'sunday'}
months_name={1:'january',2:'february',3:'march',4:'april',5:'may',6:'june'}

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
    city=input('enter name of the city you want to look at: ').lower()
    while (city in CITY_DATA) == False:
        print('! Error ! Please enter one fo the following cities:\n   chicago, new york city, washington\n')
        city=input('\nenter name of the city you want to look at: ').lower()
    print('--> You are looking at data from city: ' + city)
        #hier noch iteration hin,die nach 5 Versuchen abbricht


    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all','january','february','march','april','may','june']
    month=input('\nenter the month you want to look at (enter "all" to select all): ').lower()
    while (month in months) == False:
        print('! Error ! Please enter one fo the following month (enter "all" to select all):\n   january, february, march, april, may, june or "all" to select all')
        month=input('\nenter the month you want to look at (enter "all" to select all): ').lower()
        #hier noch iteration hin,die nach 5 Versuchen abbricht
    print('--> You are looking at data from month ' + month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_of_week=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day=input('\nenter the wekkday you want to look at (enter "all" to select all): ').lower()
    while day not in days_of_week:
        print('! Error ! Please enter one fo the following weekdays:\n    monday, tuesday, wednesday, thursday, friday, saturday, sunday or "all" to select all')
        day=input('\nenter the wekkday you want to look at (enter "all" to select all): ').lower()
        #hier noch iteration hin,die nach 5 Versuchen abbricht
    print('--> You are looking at data from weekday ' + day)

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
    print('\n... loading bikeshare data from '+city)
     # load data file into a dataframe
    df =  pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.dayofweek
    df['hour']=df['Start Time'].dt.hour


    print('\n... filtering data for month '+month+ ' and weekday '+day)

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = list(months_name.values())
        month = months.index(month) +1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        #convert user input for day to corresponding day of the week
        days=list(weekdays.values())
        day = days.index(day)

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if len(df['month'].unique()) == 1:
        print('!filtered by month! No most common month can be calculated')
    else:
        print('--Most common month: '+ months_name[df['month'].mode()[0]])

    # TO DO: display the most common day of week
    if len(df['day_of_week'].unique()) == 1:
        print('!filtered by month! No most common month can be calculated')
    else:
        print('--Most common weekday: '+ weekdays[df['day_of_week'].mode()[0]])

    # TO DO: display the most common start hour
    print('--Most common hour: '+ str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print('--Most common start station:')
    print('  -->'+start_station)

    # TO DO: display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print('--Most common start station:')
    print('  -->'+end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station_combination=(df['Start Station']+'-'+df['End Station']).mode()[0]
    print('--Most common travel route:')
    print('  --> from "'+start_end_station_combination.split('-')[0]+'" to "'+start_end_station_combination.split('-')[1]+'"')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration=np.sum(df['Trip Duration'])
    #print('total_trip_duration in s: '+str(total_trip_duration))
    total_trip_duration_s = total_trip_duration % 60
    total_trip_duration_min = (total_trip_duration // 60) % 60
    total_trip_duration_h = total_trip_duration // (60*60)
    print('--total travel time: {0} h {1} min {2} s'.format(total_trip_duration_h,total_trip_duration_min,total_trip_duration_s))

    # TO DO: display mean travel time
    mean_trip_duration=np.mean(df['Trip Duration'])
    mean_trip_duration_s = mean_trip_duration % 60
    mean_trip_duration_min = (mean_trip_duration // 60) % 60
    mean_trip_duration_h = mean_trip_duration // (60*60)
    print('--mean travel time: {0} h {1} min {2} s'.format(int(mean_trip_duration_h),int(mean_trip_duration_min),int(mean_trip_duration_s)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nuser type statistics:\n')
    user_stat=df['User Type'].value_counts()
    for user in user_stat.index:
        print('--{0}:  {1} ({2} %)'.format(user,user_stat[user],round((user_stat[user]/user_stat.sum())*100),1))
    print('--{0}:  {1}'.format('no user type info',df['User Type'].isnull().sum()))


    # TO DO: Display counts of gender
    print('\ngender type statistics:\n')
    if 'Gender' in df.columns:
        gender_stat=df['Gender'].value_counts()
        for gender in gender_stat.index:
            print('--{0}:  {1} ({2} %)'.format(gender,gender_stat[gender],round((gender_stat[gender]/gender_stat.sum())*100),1))
        print('--{0}:  {1}'.format('no gender info',df['Gender'].isnull().sum()))
    else:
        print('--no gender info for this dataset\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    print('user age statstics:\n')
    if 'Birth Year' in df.columns:
        #calculate user age at travel times
        df['user age']=df['Start Time'].dt.year-df['Birth Year']
        print('--oldest user of age '+str(int(max(df['user age']))))
        print('--youngest user of age '+str(int(min(df['user age']))))
        print('--most common user age '+str(int(df['user age'].mode()[0])))
    else:
        print('--no user age info for this dataset')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_rawdata(df)
    #ask user if rawdata is desired
    raw_data_request=input('\nWould you like to see raw data? Enter yes or no.\n')
    ii=0
    #display 5 lines of rawdata while user wants to see data
    while raw_data_request.lower()=='yes':
        [print(dict(df.iloc[ii+i,1:])) for i in  range(0,4)]
        ii+=5
        raw_data_request=input('\nWould you like to see more raw data? Enter yes or no.\n')

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
        break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #ckeck if data for the filtered periode available
        if df.empty:
            print('no data for this filter')
        else:
            time_stats(df) #calculates and displays most frequent time of travel
            station_stats(df) #calculates and displays most frequent stations
            trip_duration_stats(df)# calculates and disprays trip duration statistics
            user_stats(df)#calculates and displays user statistics

        #display raw data
        display_rawdata(df)

if __name__ == "__main__":
	main()
