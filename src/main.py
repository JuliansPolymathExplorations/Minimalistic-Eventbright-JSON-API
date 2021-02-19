#  Last revised 7/22/19
#  MAIN PROGRAM
#
#  Run from the browser as http://localhost:5000/
#
#	MIT License
#   Copyright (c) 2019 Julian A. West


from web_app import WebApp

import event_data



class MainProgram:

    def __init__(self):

        # Instantiate the object to manage the data about the Events, and then populate it
        eventObj = event_data.EventData()

        filename = "dataFromEventBright.json" # JSON data copy-and-pasted from running:
                                              # https://www.eventbriteapi.com/v3/events/search/?token=4GQQFB6MUA5Y2RNBIQ55
                                              # At the top level, it contains a "pagination" objects and an "events" array

        self.eventDict = eventObj.populateEventDataFromFileDump(filename)   # Returns a Python list of event data

        #print(self.eventList)

        # For debugging, poke around the data of the first Event
        firstEvent = self.eventDict[0]
        #print(firstEvent)
        print("name.text: " , firstEvent["name"]["text"])
        print("id: " , firstEvent["id"])

        # For debugging, try out a search by event name
        searchNameString = "Ladies Night Out at Suite Lounge Hosted by Big Tigger"
        searchResult = eventObj.searchByEventName(searchNameString)
        print("SEARCH RESULT in JSON form: ", searchResult)


        WebApp(eventObj)    # Instantiate the WebApp class, which provides a UI interface and sets up Flask routing



'''
MAIN PROGRAM EXECUTION
'''
MainProgram()
