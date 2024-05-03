from datetime import datetime
import pandas as pd
from createReq import create_req
from cmpush import sendReq

df = pd.read_excel('output.xlsx', sheet_name='Sheet3')

# generic_query = "Leg(flightNumber;equals;889;20Jun2024;;;;;UTC;LEG):Leg(departureAirport;is;GAU)"
c = 0
total = 0
success = 0

with open('warning/warnings.txt', 'w') as file:
    file.write("")

for index, row in df.iterrows():
    print(f"Processing row {c} of {len(df)}")
    c += 1
    total += 1
    flight_date = row['flight_date']
    flight_number = row['flightnumber'][2:]
    departure_airport = row['DEPARTURE']
    generic_query = f'Leg(flightNumber;equals;{flight_number};{flight_date};;;;;UTC;LEG):Leg(departureAirport;is;{departure_airport})'

    if departure_airport.strip() == '' or flight_date.strip() == '' or flight_number.strip() == '' or row['arr_or_depart'].strip() == '' or not row['pltid']:
        print(f"    SOAP request failed: required fields are missing. Writing to file warning/warnings.txt")
        with open('warning/warnings.txt', 'a') as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Error in row {c} with id {row['id']}\n")
        continue

    acars_out = None 
    if row['AcarsOUT'] is not pd.NaT:
        acars_out = row["AcarsOUT"] 
        acars_out = pd.to_datetime(acars_out).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    acars_off = None
    if row['AcarsOFF'] is not pd.NaT:
        acars_off = row["AcarsOFF"]
        acars_off = pd.to_datetime(acars_off).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    acars_on = None
    if row['AcarsON'] is not pd.NaT:
        acars_on = row["AcarsON"]
        acars_on = pd.to_datetime(acars_on).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    acars_in = None
    if row['AcarsIN'] is not pd.NaT:
        acars_in = row["AcarsIN"]
        acars_in = pd.to_datetime(acars_in).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    staffnumber = int(row['pltid'])

    takeoff = None
    landing = None 

    if row['arr_or_depart'] == 'D':
        takeoff = 'true'
    
    if row['arr_or_depart'] == 'A':
        landing = 'true'

    # print(generic_query, acars_out, acars_off, acars_on, acars_in, staffnumber, takeoff, landing)
    body = create_req(generic_query, acars_out, acars_off, acars_on, acars_in, staffnumber, takeoff, landing)

    if sendReq(body, str(staffnumber) + flight_date + flight_number + departure_airport + row['arr_or_depart']):
        success += 1

print(f"{success} out of {total} requests were successful")
 