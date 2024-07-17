from amadeus import Client, ResponseError
from rich.console import Console
from rich.table import Table
from babel.numbers import format_currency
from airports.passenger import OriginAirports, DestinationAirports, adults, children, TravelClass, departureDate, returnDate
from dotenv import load_dotenv
import os

# Inisialisasi Amadeus API Client
load_dotenv()
amadeus = Client(
    client_id=os.getenv("AMADEUS_CLIENT_ID"),
    client_secret= os.getenv("AMADEUS_CLIENT_SECRET")
)

console = Console()

def fetch_flight_data():
    try:
        # Mencari penerbangan
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=OriginAirports(),
            destinationLocationCode=DestinationAirports(),
            departureDate=departureDate(),
            returnDate=returnDate(),
            adults=adults(),
            children=children(),
            travelClass=TravelClass(),
            currencyCode='IDR'
        )

        # Mengumpulkan data penerbangan
        flight_data = []
        for offer in response.data:
            airline = offer['itineraries'][0]['segments'][0]['carrierCode']
            departure = offer['itineraries'][0]['segments'][0]['departure']['iataCode']
            arrival = offer['itineraries'][0]['segments'][0]['arrival']['iataCode']
            price = float(offer['price']['total'])
            currency = offer['price']['currency']
            formatted_price = format_currency(price, currency, locale='id_ID')
            flight_data.append([airline, departure, arrival, formatted_price])

        return flight_data

    except ResponseError as error:
        console.print(f"[bold red]Error fetching flight data: {error}")
        return []

def display_flight_data(flight_data):
    table = Table(title="\nFlight Offers")

    table.add_column("Airline", justify="left", style="cyan", no_wrap=True)
    table.add_column("Departure", justify="center", style="magenta")
    table.add_column("Arrival", justify="center", style="magenta")
    table.add_column("Price", justify="right", style="green")

    for flight in flight_data:
        table.add_row(*flight)

    console.print(table)

# Fetch and display the flight data
flight_data = fetch_flight_data()
if flight_data:
  display_flight_data(flight_data)
else:
  console.print("[bold red]No flight data found.")
  
