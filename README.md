# ycaro-airlines
Project made for Software Project class for the 2025.1 semester

## Project Functional Requirements
Airline Reservation System
• Flight Search: Users can search for flights based on various criteria;
• Booking Management: Users can book, cancel, and modify flight bookings;
• Online Check-in: Users can check in online for their flights;
• Seat Selection: Users can select and change their seats;
• Baggage Information: Information about baggage allowances and fees;
• Loyalty Program Management: Management and redemption of frequent flyer points;
• Flight Status Updates: Real-time updates on flight status;
• Special Requests: Handling of special requests like meals and accessibility needs;
• Multi-City Booking: Booking flights with multiple stopovers;
• Customer Support Interface: Assisting customers with their queries and issues

## Requirements in progress (date: 16/07/2025)
-  Flight Search: Users can search for flights based on various criteria; 
-  Booking Management: Users can book, cancel, and modify flight bookings;
-  What is done:
    - Base model
    - Customer, Planes, Flights, and Account Models
    - Started Working on Account and Flight Controllers
    - No user interface as of now

### How to test it without ui?
```bash
$ git clone https://github.com/ycaro-sales/ycaro-airlines.git
$ cd ycaro-airlines
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ cd src 
$ IPython --no-autoident
>>> from models.accounts import * 
>>> from models.airlines import *
>>> from controllers.AccountController import *
>>> from controllers.FlightsController import *
>>> # test controllers and models from here
```


## Project Structure
Models
- Flight Crew
- Flights
- Flight Crew
- Passengers
- Cities
- Airports
- Airlines
- Customer Support 
Controllers
- AccountController
- FlightController
- AirlinesController
Views


## Possible Ideas
- Simulate Real-time flights using virtual clocks to simulate the airlines working

