# Wander Wisely app (trip manager)
## Purpose of creating Wander Wisely
Wander Wisely app was created to help with the organization of a journey. Fields of currency, geography and weather are three sectors on which I focused the most. This is simple, modern desktop app.

## Used technologies
1. Python (mainly: tkinter, sqlite3, matplotlib, requests, datetime, pillow)
2. SQL, API, CSV

### Main menu (frame 1)

The main frame of the Wander Wisely application serves as the central hub for users to plan their travel adventures. It provides essential features for inputting travel destination information, selecting the primary currency, and accessing various travel-related analyses. 

#### Components
1. Destination and Primary Currency Input

Upon launching the Wander Wisely app, users are greeted with a section to input their desired travel destination (country) and their everyday primary currency. This step is crucial as it helps the application tailor information and recommendations to the user's specific travel needs.

2. Travel Analysis Options

After entering the destination and primary currency, users are presented with a range of options to analyze and plan their trip effectively. These options include:

- Currency Analysis: Users can select this option to get insights into the currency exchange rates and conversion tools for their primary currency in the chosen destination. It provides real-time currency exchange rate information based on user input (displayed on the of the section).

- Geographical Information: This option allows users to explore the geographical location of their chosen destination. Users can access information about popular landmarks and attractions in their selected destination, helping them plan their itinerary.

- Weather Forecast: This feature provides users with up-to-date weather information for their chosen travel destination, helping them prepare for varying weather conditions during their trip.

3. Navigation Buttons

To access each of the travel analysis options mentioned above, users can simply click on the corresponding button. These buttons provide an intuitive and user-friendly way to explore different aspects of their trip.

The application uses a mechanism to determine whether to display fake buttons or real buttons. Fake buttons are initially shown and are replaced with real buttons after valid user input is received. State of buttons couldn't been used because customtkinker buttons don't handle this function (usage of state causes bugs).
    
4. Exit Button

Located at the bottom of the main frame, there is an exit button that allows users to gracefully exit the Wander Wisely app when they have finished planning or using its features.

#### Error Handling

The application includes error handling to notify users of incorrect inputs or data retrieval issues.
Error messages are displayed as labels and automatically disappear after a set time.



### Currency section

### Geographical section

### Weather section


