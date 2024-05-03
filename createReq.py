import pandas as pd 

def create_req(generic_query, acars_out = None, acars_off = None, acars_on = None, acars_in = None, staffnumber = None, takeoff = None, landing = None):
    a =  f'''
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
        <soap:Header>
            <ns6:SabreHeader xmlns:ns6="http://services.sabre.com/STL_Header/v02_02"
                xmlns:ns9="http://schemas.xmlsoap.org/ws/2002/12/secext">
                <ns6:Service operation="SetFlightLogAttributes" ttl="100" version="15.0.0">FlightLogService</ns6:Service>
                <ns6:Identification>
                    <ns6:CustomerID>AI</ns6:CustomerID>
                    <ns6:CustomerAppID>SWS1:SBR-AIInt2Crew:99308768gg</ns6:CustomerAppID>
                    <ns6:ConversationID>08022104</ns6:ConversationID>
                    <ns6:MessageID>08022104</ns6:MessageID>
                    <ns6:TimeStamp>2023-07-25T00:00:00.000Z</ns6:TimeStamp>
                </ns6:Identification>
            </ns6:SabreHeader>
            <ns9:Security xmlns:ns6="http://services.sabre.com/STL_Header/v02_02"
                xmlns:ns9="http://schemas.xmlsoap.org/ws/2002/12/secext"/>
            <wsse:Security>
                <wsse:UsernameToken>
                    <wsse:Username>V1:cmxaisystem:CAE Products:AI1</wsse:Username>
                    <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">Y6VG8u3T</wsse:Password>
                </wsse:UsernameToken>
            </wsse:Security>
        </soap:Header>
        <soap:Body>
            <cmxflg:SetFlightLogAttributesRQ version="15.0.0" xsi:schemaLocation="http://stl.sabre.com/AirCrews/CrewManager10/FlightLogService/v15 FlightLogService-15.0.0.xsd "
                xmlns:cmx="http://stl.sabre.com/AirCrews/CrewManager10/CommonDataTypes/v15"
                xmlns:cmxflg="http://stl.sabre.com/AirCrews/CrewManager10/FlightLogService/v15"
                xmlns:p="http://services.sabre.com/sp/cmm/types/v01_00"
                xmlns:p1="http://services.sabre.com/STL_Payload/v02_02"
                xmlns:p2="http://services.sabre.com/STL_MessageCommon/v02_02"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                <cmxflg:SetFlightLogItems>
                    <cmxflg:SetFlightLogItem internalId="1">
                    <cmx:GenericQuery endDateTimeRange="2099-04-30T23:59:00" startDateTimeRange="2000-04-01T00:00:00">
                        <cmx:GenericSearch>{generic_query}</cmx:GenericSearch>
                    </cmx:GenericQuery>
                    <cmx:FlightLogAttributes>
                        <cmx:CompressedCustomAttribs>''' 

    b = ''
    if acars_out:
        b += f'<cmx:CustomAttribute isRulesModified="false" name="flightLog.TIMES.AcarsOUT">{acars_out}</cmx:CustomAttribute>\n'

    if acars_off:
        b += f'<cmx:CustomAttribute isRulesModified="false" name="flightLog.TIMES.AcarsOFF">{acars_off}</cmx:CustomAttribute>\n'

    if acars_on:
        b += f'<cmx:CustomAttribute isRulesModified="false" name="flightLog.TIMES.AcarsON">{acars_on}</cmx:CustomAttribute>\n'

    if acars_in:
        b += f'<cmx:CustomAttribute isRulesModified="false" name="flightLog.TIMES.AcarsIN">{acars_in}</cmx:CustomAttribute>\n'
    
    c = f'''</cmx:CompressedCustomAttribs>
                        <cmx:CrewFlightLogAttrsList>
                            <cmx:CrewFlightLogAttributes staffNumber="{staffnumber}">
                                <cmx:RosteredCustomAttributes>'''

    d = ''

    if takeoff:
        d += f'<cmx:CustomAttribute isRulesModified="false" name="flightLog.CREW.Takeoff">{takeoff}</cmx:CustomAttribute>\n'

    if landing:
        d += f'<cmx:CustomAttribute isRulesModified="false" name="flightLog.CREW.Landing">{landing}</cmx:CustomAttribute>\n'

    e = '''</cmx:RosteredCustomAttributes>
                            </cmx:CrewFlightLogAttributes>
                        </cmx:CrewFlightLogAttrsList>
                    </cmx:FlightLogAttributes>
                    </cmxflg:SetFlightLogItem>
                </cmxflg:SetFlightLogItems>
            </cmxflg:SetFlightLogAttributesRQ>
        </soap:Body>
        </soap:Envelope>
    '''


    return a + b + c + d + e 

# Example
# print(create_req('nwsmkls', '2024-04-26T07:48:00.000Z', '2024-04-26T08:02:00.000Z', None, '2024-04-26T08:50:00.000Z', '80055988', 'true', None))
