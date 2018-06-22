import time
import pandas as pd
import numpy as np
import itertools as it
import operator

def m_c(k):
    """ 
    Takes argument to check most common element
    Returns:
    (srt) most common element in series
    """
    sl=sorted((x,i) for i,x in enumerate(k))
    gro=it.groupby(sl,key = operator.itemgetter(0))
    def _af(gh):
        item,itera = gh
        co = 0
        m_i = len(k)
        for _,wh in itera:
            co += 1
            m_i=min(m_i,wh)
        return co,-m_i
    return max(gro,key=_af)[0]

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    cities= ['chicago','new york city','washington']
    
    while True:
        city =input("Please Enter City:  ").lower()
        if city  in cities:
            break
        else:
            print("Please enter right input!")
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all','january','february','march','april','june']
    
    while True:
        month=input("Please Enter month:  ").lower()
        if month in months:
            break
        else:
            
            print("Please enter right input!")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    
    while True:
        
        day=input("Please Enter Day: ").lower()
        if day in days:
            break
        else:
            print("Please enter right input!")

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    if month!= 'all':
        months=['january','february','march','april','may','june']
        month= months.index(month)+1
        df=df[df['month']==month]
    if day!= 'all':
        df=df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time']=pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month']=df['Start Time'].dt.month
    common_month=df['month'].mode()[0]
    g1=input("If you want to know the most common month please press yes else no:  ")
    if g1.lower() == 'yes':
        print("Most common month:",common_month,"th month")
    # TO DO: display the most common day of week
    df['day_of_week']=df['Start Time'].dt.weekday_name
    common_day=df['day_of_week'].mode()[0]
    g2=input("If you want to know the most common day please press yes else no:  ")
    if g2.lower() == 'yes':
        print("Most common day:",common_day)

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    g3=input("If you want to know the most common hour please press yes else no:  ")
    if g3.lower() == 'yes':
        print("Most common hour:",common_hour,".00")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    t1=input("If you want to know the most common start station please press yes else no:  ")
    if t1.lower() == 'yes':
        print("Most common Start Station is: \n",m_c(df['Start Station']))

    # TO DO: display most commonly used end station
    t2=input("If you want to know the most common end station please press yes else no:  ")
    if t2.lower() == 'yes':
        print("Most common End Station is: \n",m_c(df['End Station']))

    # TO DO: display most frequent combination of start station and end station trip
    t3=input("If you want to know the most frequent combination of start station and end station trip please press yes else no:  ")
    if t3.lower() == 'yes':
        print("Most frequent used stations are: \n",df.groupby(['Start Station', 'End Station']).size().nlargest(2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total=df['Trip Duration'].sum()
    l2=input("If you want to know the total travel time please press yes else no:  ")
    if l2.lower() == 'yes':
        print(" The total travel time of the trip is :",total," hours")

    # TO DO: display mean travel time
    mean=df['Trip Duration'].mean()
    l3=input("If you want to know the mean travel time please press yes else no:  ")
    if l3.lower() == 'yes':
        print("The mean travel time is: ",( mean)," hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    q1=input("If you want to know the count of user types please press yes else no:  ")
    if q1.lower() == 'yes':
        print(user_types)
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        
        gender = df['Gender'].value_counts()
        q2=input("If you want to know the count of gender please press yes else no:  ")
        if q2.lower() == 'yes':
            print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        q3=input("If you want to know the earliest birth year please press yes else no:  ")
        if q3.lower() == 'yes':
            print("earliest",df['Birth Year'].min())
        q4=input("If you want to know the recent birth year please press yes else no:  ")
        if q4.lower() == 'yes':
            
            print("most recent",max(df['Birth Year']-2018)+2018)
        q5=input("If you want to know the most common birth year please press yes else no:  ")
        if q5.lower() == 'yes':
            print("most common",m_c(df['Birth Year']))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def Raw_Data(city,month,day):
    """Display the raw data of the user and prints it"""
    print("The city you have entered is: ",city)
    print("The month you have entered is: ",month)
    print("The day you have entered is: ",day)

def main():
    while True:
        city, month, day = get_filters()
        Raw_Data(city,month,day)
        
            
        df = load_data(city, month, day)
        tr=input("Do you want to see the given dataframe press yes or no: ")
        if tr.lower() == 'yes':
            i=0
            count=0
            while i==0:
                print("Printing five rows")
                print(df.iloc[count:count+6])
                ty=input("If you want to see next five lines press yes or no: ")
                if ty.lower() == 'yes':
                    count=count+5
                else:
                    i=1
                
        
        
        r1=input("If you want to know the time statictics of the city please press yes else no:  ")
        if r1.lower() == 'yes':
            time_stats(df)
        r2=input("If you want to know the Station statictics of the city please press yes else no:  ")
        if r2.lower() == 'yes':
            station_stats(df) 
        r3=input("If you want to know the Trip duration statictics of the city please press yes else no:  ")
        if r3.lower() == 'yes':
            trip_duration_stats(df)
        r4=input("If you want to know the User statictics of the city please press yes else no:  ")
        if r4.lower() == 'yes':
            user_stats(df)
        
            
        #time_stats(df)
        #station_stats(df)
        #trip_duration_stats(df)
        #user_stats(df)

        restart = input('\nWould you like to know the statictics of another city? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
