# Wander Wisely app (trip manager)
## Purpose of creating Wander Wisely
Wander Wisely app was created to help with the organization of a journey. Fields of currency, geography and weather are three sectors on which I focused the most. This is simple, modern desktop app.

## Used technologies
1. Python (mainly: tkinter, sqlite3, matplotlib, requests, datetime, pillow)
2. SQL, API, CSV

### Main menu (frame 1)

The main frame of the Wander Wisely application serves as the central hub for users to plan their travel adventures. It provides essential features for inputting travel destination information, selecting the primary currency, and accessing various travel-related analyses. 
<p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-repo/assets/125304122/21de5d3a-7f62-4131-927f-c47c5745cc28" width = 50% height = 50%>
</p>

#### Components
1. Destination and Primary Currency Input

Upon launching the Wander Wisely app, users are greeted with a section to input their desired travel destination (country) and their everyday primary currency. The application is protected against case errors.
<p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-repo/assets/125304122/c67cb216-251f-4c18-8b9b-d1f35cc097e0" width = 50% height = 50%>
</p>
2. Travel Analysis Options

After entering the destination and primary currency, users are presented with a range of options to analyze and plan their trip effectively. These options include:

- Currency Analysis: Users can select this option to get insights into the currency exchange rates and conversion tools for their primary currency in the chosen destination. It provides real-time currency exchange rate information based on user input (displayed on the of the section).
<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-repo/assets/125304122/d8663838-fb11-4610-9cb5-6aa3d41d2c70' width = 30% height = 30%>
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
    <img src = 'https://github.com/poolinaaa/trip-manager-repo/assets/125304122/5dad989c-3049-49d2-8ab4-03e13f85e81e' width = 50% height = 50%>
</p>



### Currency section (frame 2)
<p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-repo/assets/125304122/7f687c33-7f9e-4e44-8348-fa233b03b2fc" width = 50% height = 50%>
</p>

#### Plot 1
<p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-repo/assets/125304122/4972e5d5-3cde-48fa-8c62-6ddd8417eb3a" width = 50% height = 50%>
</p>

#### Plot 2
<p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-repo/assets/125304122/a54cc0b7-c7bc-4322-bb5c-802e188d6773" width = 50% height = 50%>
</p>

#### Plot 3
<p align = 'center'>
    <img src = "https://github.com/poolinaaa/trip-manager-repo/assets/125304122/4f0cc856-a5f9-4996-8244-4c5d23192237" width = 50% height = 50%>
</p>

#### Error Handling
Error label will appear if user enters incorrect dates.
<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-repo/assets/125304122/0b1f31b7-ecbf-49fb-bbe8-77d5c6691d2a' width = 50% height = 50%>
</p>

### Geographical section (frame 3)
<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-repo/assets/125304122/97cd6f90-71c9-4e50-b8d2-f2f8e0b425ea' width = 50% height = 50%>
</p>
<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-repo/assets/125304122/2c28dd22-ac72-438d-9b3b-0bd5638dc28e' width = 50% height = 50%>
</p>

<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-repo/assets/125304122/5810a32d-7688-4611-9ba8-95c2cfa0e285' width = 50% height = 50%>
</p>

<p align = 'center'>
    <img src = 'https://github.com/poolinaaa/trip-manager-repo/assets/125304122/091972df-0ff5-4c33-b06f-31d80acad5ae' width = 50% height = 50%>
</p>



### Weather section (frame 4)
![obraz](https://github.com/poolinaaa/trip-manager-repo/assets/125304122/dcfab838-28dc-49e6-bdd4-b7bd5ff882f6)

![obraz](https://github.com/poolinaaa/trip-manager-repo/assets/125304122/62a593b2-9876-432c-b597-bcae16cab234)

![obraz](https://github.com/poolinaaa/trip-manager-repo/assets/125304122/a0989b09-e69b-4811-bec2-9e62f386ff8d)

![obraz](https://github.com/poolinaaa/trip-manager-repo/assets/125304122/3e0e0886-9585-4786-8082-22f9ff5e27d5)





