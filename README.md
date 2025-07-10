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

## Project Components
- Flights
    - has Baggage Fee
    - has crew
    - Has a status(Landing, Departing, Boarding, Waiting for checkin(?), Open, Full)
    - Can have stops
    - has seats
        - has passengers
    - has passengers
    - has arrival and departing times
    - has check in time 
- Flight Crew
    - Is allocated to a flight
    - Have Current City
    - Can receive special requests
- Passengers
    - can Book, cancel and modify Flights
    - Has and can receive loyalty points
    - Has and can  be allocated a seat in a flight
    - Can do online check-ins
    - Can make special requests
- Cities
    - has Airports
    - has Distance between other cities
- Airports
    - Has Flights 
    - Belongs to a City
- Airlines
    - Has passengers
    - Has available Crew
    - Has customers support 
        - Has pending customer support 
    - Can Aproove special requests
- Customer Support 
    - Has pending Requests


## Possible Ideas
- Simulate Real-time flights using virtual clocks to simulate the airlines working

## Roadmap
1. Booking 
    - Create Planes
        - Booked Flights
    - Create Flight class
        - items
            - Flight Status
                - Available
                - Departed
                - Arrival
                - Landing 
            - Capacity
                - Capacity Status
                    - Full 
                    - Empty
                    - Boarding
            - Model(?)
            - From
            - To
            - Gate
            - Airport
            - Departure(Time)
            - Arrival(Time)
            - Available Seats(dict)
        - Methods
            - Depart
            - Arrive
            - is_full
            - has_seat
            - available_seats
            - Get Model
            - Get Destination
            - Set Destination
    - Create Passenger class
        - Items
            - Booked Flights
        - Methods
            - request_book_flight
            - cancel_flight
            - get_booked_flights
    - Create Airline Worker
        - Flights Manager 
        - Boarding Manager(?)
    - Create Airline
        -
        - items
            - Flights
        - Methods
            - Show Flights to and from:
    - Create Airport Class
        - City
        - Gates
2. Flight search
3. Seat selection
4. Online Check-in
5. Flight Status
6. Multi-city Booking
7. Baggage Information
8. Loyalty Program
9. Customer Support
10. Special  Requests
     

