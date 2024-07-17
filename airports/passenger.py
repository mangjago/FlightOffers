from InquirerPy import prompt
from InquirerPy.validator import EmptyInputValidator
from InquirerPy.prompts.expand import ExpandChoice
from InquirerPy.separator import Separator
from airports.airports import get_airports_name
from datetime import datetime

def dateOfDate():
  return datetime.now().strftime("%Y-%m-%d")
  
def OriginLocation():
  questions = [
      {
        'type': 'input',
        'message': 'Kota/IATA keberangkatan?',
        'name': 'destination',
        'validate': lambda result: len(result) > 0,
        'invalid_message': 'Mohon masukkan lokasi keberangkatan'
      }
  ]
  
  result = prompt(questions)
  city = result["destination"]
  iata, name = get_airports_name(city)
  return iata, name
  
# User select airport
def OriginAirports():
  iata, name = OriginLocation()
    
  questions = [
    {
      'type': 'rawlist',
      'name': 'airports',
      'choices': name,
      'message': 'Bandara keberangkatan?',
      'default': 1
    }
  ]
  
  result = prompt(questions)
  get_iata = name.index(result["airports"])
  return iata[get_iata].upper()
  
def DestinationLocation():
  questions = [
      {
        'type': 'input',
        'message': 'Kota/IATA tujuan?',
        'name': 'destination',
        'validate': lambda result: len(result) > 0,
        'invalid_message': 'Mohon masukkan lokasi tujuan'
      }
  ]
  
  result = prompt(questions)
  city = result["destination"]
  iata, name = get_airports_name(city)
  return iata, name
  
def DestinationAirports():
  iata, name = DestinationLocation()
    
  questions = [
    {
      'type': 'rawlist',
      'name': 'airports',
      'choices': name,
      'message': 'Bandara Tujuan?',
      'default': 1
    }
  ]
  
  result = prompt(questions)
  get_iata = name.index(result["airports"])
  return iata[get_iata].upper()

def adults():
  questions = [
    {
      "type": "number",
      "name":"adults",
      "message": "Jumlah penumpang dewasa?",
      "min_allowed": 1,
      "validate": EmptyInputValidator()
    }
  ]
  result = prompt(questions)
  return result["adults"]
  
def children():
  questions = [
    {
      "type": "number",
      "name":"children",
      "message": "Jumlah penumpang anak-anak?",
      "min_allowed": 0,
      "validate": EmptyInputValidator()
    }
  ]
  result = prompt(questions)
  return result["children"]

def TravelClassChoices(_):
  return [
    ExpandChoice(key="e", name="Ekonomi", value="ECONOMY"),
    ExpandChoice(key="b", name="Bisnis", value="BUSINESS")
  ]

def TravelClass():
  questions = [
    {
      "type": "expand",
      "choices": TravelClassChoices,
      "message": "Pilih tipe kelas penerbangan?",
      "default": "e",
      "cycle": False
    }
  ]
  result = prompt(questions)
  return result[0]
  
def departureDate():
  questions = [
      {
        'type': 'input',
        'message': 'Tanggal keberangkatan (yy-mm-dd)?',
        'name': 'departureDate',
        'default': dateOfDate(),
        'validate': lambda result: len(result) > 0,
        'invalid_message': 'Mohon masukkan tanggal keberangkatan'
      }
  ]
  result = prompt(questions)
  return result["departureDate"]

def returnDate():
  questions = [
      {
        'type': 'input',
        'message': 'Tanggal Kembali (yy-mm-dd)?',
        'name': 'returnDate',
        'default': dateOfDate(),
        'validate': lambda result: len(result) > 0,
        'invalid_message': 'Mohon masukkan tanggal kembali'
      }
  ]
  
  result = prompt(questions)
  return result["returnDate"]