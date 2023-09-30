# Wander Wisely app (trip manager)
## Purpose of creating Wander Wisely
Wander Wisely app was created to help with the organization of a journey. Fields of currency, geography and weather are three sectors on which I focused the most. This is simple, modern desktop app.

## Used technologies
1. Python (mainly: tkinter, sqlite3, matplotlib, requests, datetime, pillow)
2. SQL, API, CSV

<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-app/assets/125304122/5f842d0e-ddd7-4b2c-8442-cf4121349786' width = 50% height = 50%>
</p>

## API Key Configuration

To use certain features of this application, an API keys are required. 

Go to the <a href='https://apilayer.com/marketplace/fixer-api?_gl=1*15f9c1p*_ga*MTE5OTkwMzQ3MC4xNjk1Mzg1NTQy*_ga_HGV43FGGVM*MTY5NTM4NTU0My4xLjEuMTY5NTM4NTU2NS4zOC4wLjA.#pricing'> Fixer API </a> and  <a href='https://www.geoapify.com/pricing'> Geoapify </a> - log in to your existing account or register a new account if you don't have one (there are free plans avialable).

Below are the modules where you should provide the API keys:

#### Fixer 

1. frame1 Module:
<p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-app/assets/125304122/76fdc3a2-0be5-4a2b-a37f-3c1327487e4e" width = 50% height = 50%>
</p>

2. frame2 Module:
   <p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-app/assets/125304122/99587d22-f34b-42d9-a6db-f025884166f6" width = 50% height = 50%>
</p>


3. funcPlots Module:
   <p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-app/assets/125304122/06e75be8-a458-4d5f-b94f-fe71dfb75934" width = 50% height = 50%>
</p>

#### Geoapify

4. geoFunc Module:
   <p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-app/assets/125304122/32620b6b-1c32-4abd-a176-b02c6aee5165" width = 50% height = 50%>
</p>


### Main menu (frame 1)

The main frame of the Wander Wisely application serves as the central hub for users to plan their travel adventures. It provides essential features for inputting travel destination information, selecting the primary currency, and accessing various travel-related analyses. 
<p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-app/assets/125304122/d31927f5-978e-4f1f-a58b-ab195c23ad21" width = 50% height = 50%>
</p>


#### Components
1. Destination and Primary Currency Input

Upon launching the Wander Wisely app, users are greeted with a section to input their desired travel destination (country) and their everyday primary currency. The application is protected against case errors.
<p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-app/assets/125304122/6ed10939-fde4-4d8f-8ecf-db65660d0748" width = 50% height = 50%>
</p>


2. Travel Analysis Options

After entering the destination and primary currency, users are presented with a range of options to analyze and plan their trip effectively. These options include:

- Currency Analysis: Users can select this option to get insights into the currency exchange rates and conversion tools for their primary currency in the chosen destination. It provides real-time currency exchange rate information based on user input (displayed on the of the section).
<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-app/assets/125304122/3d861833-bcfa-403d-894a-1fc9e104db43' width = 30% height = 30%>
</p>


- Geographical Information: This option allows users to explore the geographical location of their chosen destination. Users can access information about popular landmarks and attractions in their selected destination.

- Weather Forecast: This feature provides users with up-to-date weather information for their chosen travel destination, helping them prepare for varying weather conditions during their trip. Also it provides a weather from year before departure date.

3. Navigation Buttons

To access each of the travel analysis options mentioned above, users can simply click on the corresponding button. These buttons provide an intuitive and user-friendly way to explore different aspects of their trip.

The application uses a mechanism to determine whether to display fake buttons or real buttons. Fake buttons are initially shown and are replaced with real buttons after valid user input is received. State of buttons couldn't been used because customtkinker buttons don't handle this function (usage of state causes bugs).
    
4. Exit Button

Located at the bottom of the main frame, there is an exit button that allows users to gracefully exit the Wander Wisely app when they have finished planning or using its features.

#### Error Handling

The application includes error handling to notify users of incorrect inputs or data retrieval issues.
Error messages are displayed as labels and automatically disappear after a set time.
<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-app/assets/125304122/3911cbb1-859d-441d-b27c-0c611eebfe6e' width = 50% height = 50%>
</p>


### Currency section (frame 2)
This section of the travel assistant application allows users to analyze changes in a selected currency. Users can choose a date range for currency analysis. After confirming the dates, users can select which type of chart they want to display.

<p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-app/assets/125304122/d014bbc9-fbdb-4adf-b27e-32fa4faca522" width = 50% height = 50%>
</p>


Usage Instructions:

1. Enter Date Range:
    Start by entering the desired start and end dates for the currency analysis in the "Enter the start date" and "Enter the end date" fields.
    Dates should be entered in the "YYYY-MM-DD" format.

2. Confirm Time Span:
    Click the "CONFIRM TIME SPAN" button to confirm the selected date range.

3. Choose Chart:
    After confirming the date range, you can choose from the following charts to display:
       - Comparison to the Current Rate: Shows a comparison of the selected currency's rate to the current rate.
       - Rate Compared to EUR, USD, PLN, CNY: Displays the selected currency's rate compared to EUR, USD, PLN, and CNY.
       - Currency Rate for the Last 30 Days: Shows the currency rate for the last 30 days.

#### Plot 1
<p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-app/assets/125304122/3044a7e8-9244-404c-b715-362e20dcf746" width = 50% height = 50%>
</p>


#### Plot 2
<p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-app/assets/125304122/ab090c2f-f9ec-41d9-a549-dd6880482908" width = 50% height = 50%>
</p>


#### Plot 3
<p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-app/assets/125304122/c50752ab-60dd-4085-bbc5-0f98e5dfece5" width = 50% height = 50%>
</p>


#### Error Handling
If the user enters a date in the wrong format, a message will prompt them to correct it.

<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-app/assets/125304122/dae760c2-7627-4cf2-ab70-69f61b1b2bc2' width = 50% height = 50%>
</p>


### Geographical section (frame 3)
In the geographical part of the Wander Wisely, users can explore geographical facts related to their destination country. Users will have the opportunity to discover information about their departure country, calculate the distance between their departure and destination countries, and explore nearby attractions.

Upon opening the Geographic Exploration section, in the bottom left corner of the application window, you will find the following information:
- Capital of the Destination Country: The capital city of the selected destination country.
- Five Largest Cities: The names of the five largest cities in the destination country, along with their respective populations.
    
This geographic information provides users with a quick overview of key details about their destination country, including its capital and major cities.

<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-app/assets/125304122/9ae8f054-c095-4b11-880d-08c9a37e0cd5' width = 50% height = 50%>
</p>


Usage Instructions:
1. Enter Departure Country:
    Start by entering your departure country in the "What is your departure country?" field.
    Ensure that you enter the full name of the country.

2. Select Distance Unit:
    Choose the unit in which the distance between your departure and destination countries will be displayed. You can choose between kilometers and miles.

3. Confirm Choices:
    Click the "CONFIRM COUNTRY" button to confirm your departure country and distance unit selection.

4. Explore Geographic Facts:
    Once confirmed, the application will display information about the distance between your departure country and the selected destination country.
    You'll also get a list of nearby attractions in the destination country's capital, with the option to open them in a web browser and save choices in the database.

<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-app/assets/125304122/e6af2c04-d63c-4c4c-8eb6-c748203821bb' width = 50% height = 50%>
</p>


<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-app/assets/125304122/11242589-d369-44fb-bde7-82129f03d610' width = 50% height = 50%>
</p>


#### Error Handling
If you enter an invalid country name when specifying your departure country, the application will display an error message.

<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-app/assets/125304122/0aa5dd98-cc78-4da2-b503-a8430b31e48e' width = 50% height = 50%>
</p>


### Weather section (frame 4)
In this section of the travel assistant application, users can check the weather forecast for their destination country. The Weather Forecast section provides users with the capability to view both historical weather data from a year ago and a weather forecast for the upcoming week.

<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-app/assets/125304122/3e56010e-99e4-4866-90cb-aeac446d9d8e' width = 50% height = 50%>
</p>


Usage Instructions:

1. Select Date of Departure:
    Use the calendar widget to select the date of your departure.
    Click on the date you want to choose, and it will be displayed as the selected departure date.

2. Submit Date:
    After selecting the date of departure, click the "SUBMIT DATE" button to proceed.

3. View Weather Data:
    Once the date of departure is confirmed, the application will display options to view weather-related information.
    Users can choose between two options:
    - Year Ago:
      This option allows you to view historical weather data from exactly one year ago on the selected date. It provides insights into what the weather was like on the same day in the past.
    - Next Week:
      This option provides a weather forecast for the upcoming week in your destination country.

<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-app/assets/125304122/fd42e35e-2d17-4ed0-8ad3-cb39d8ab3e31' width = 50% height = 50%>
</p>


#### Plot 1
<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-app/assets/125304122/55585a82-7869-4b77-bebe-e49c0afc240f' width = 50% height = 50%>
</p>


#### Plot 2
<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-app/assets/125304122/2dbbd426-bff7-4189-9e3d-22c1ffd18beb' width = 50% height = 50%>
</p>








