#  Last revised 7/21/19
#  Class "EventData", providing an object to manage the data about the Events

#	MIT License
#   Copyright (c) 2019 Julian A. West

import json


class EventData:
    """
    Object to manage the data about the Events.

    Note:   except for import from a JSON text file, this class deals with Python dictionaries/lists of dictionaries,
            rather than JSON strings;
            final generation of JSON content is handled by Flask in the class "WebApp"
    """

    def __init__(self):
        self.eventList = {}     # List of Python dictionaries of Event data



    def populateEventDataFromFileDump(self, filename):
        """
        The data is expected in a JSON text file created
        by copy-and-pasting data from https://www.eventbriteapi.com/v3/events/search/?token=4GQQFB6MUA5Y2RNBIQ55

        Extract the value for "events", and return it as a Python dictionary

        param filename: A string with a filename of a file in the same directory
        :return: A Python dictionary of the value for "events" in the JSON file
        """
        #filename = "dataFromEventBright.json"

        with open(filename, "r") as read_file:
            data = json.load(read_file)     # This returns a Python dictionary

        self.eventList = data["events"]     # Extract the "events" top-level

        return self.eventList



    def searchByEventName(self, name):
        """
        Look up an Event by its full name.  Return it as a Python dictionary, or None if not found

        :param name:    string with the full name of an event
        :return:        Python dictionary with data for the Event if found, or None if not found
        """

        for event in self.eventList:    # Search thru all events
            if event["name"]["text"] == name:
                print("SEARCH RESULT as a Python dict: ", event)
                return event

        return None



    def searchByEventID(self, id):
        """
        Look up an Event by its full name.  Return it as a Python dictionary, or None if not found

        :param id:      int with the ID of an event
        :return:        Python dictionary with data for the Event if found, or None if not found
        """

        print("Searching with event with id = " + str(id))
        for event in self.eventList:    # Search thru all events
            if event["id"] == str(id):
                print("SEARCH RESULT as a Python dict: ", event)
                return event

        return None



    def modifyEvent(self, id, key, newValue):
        """
        Look up an Event by its full name, and replace the value of the specified key.

        :param id:          int with the ID of an event
        :param key:         string with the attribute key to update
        :param newValue:    string with the new value for the attribute to update
        :return:            a string with an error message in case of error; an empty string if successful
        """

        # First, attempt to locate the Event
        event = self.searchByEventID(id)
        if event is None:
            return "Event ID " + str(id) + " not found"

        if not key in event:
            return "Event located, but it lacks a key named `" + key + "`"

        # Carry out the actual update operation
        event[key] = newValue

        return ""   # No error message (operation successful)
