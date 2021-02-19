#  Last revised 7/22/19
#  "Webapp" class, to provide a server based on the "Flask" web framework
#
#	MIT License
#   Copyright (c) 2019 Julian A. West


from flask import Flask, request, jsonify



class WebApp:
    """ This class uses the micro web framework "Flask"
    """

    def __init__(self, eventObj):

        self.eventObj = eventObj    # Object to manage the data about the Events


        # Instantiate the "Flask" object
        self.app = Flask(__name__)



        """
        Define the Flask routing (mapping URL's to Python functions)
        """

        ################################################################
        #  API endpoint to provide search capabilities
        #  It accepts GET parameters specifying the search type (only "eventName" implemented so far) and the search data
        #  Example: localhost:5000/search/eventName/Ladies%20Night%20Out%20at%20Suite%20Lounge%20Hosted%20by%20Big%20Tigger
        ################################################################

        # "@" signifies a decorator - a way to wrap a function and modify its behavior
        @self.app.route("/search/<searchType>/<searchString>")
        def search(searchType, searchString):
            """

            :param searchType:      string with the name of the search-type operation (only "eventName" implemented so far)
            :param searchString:    string being searched for (exact matches)
            :return:                JSON data (with correct Content-Type header) with the located Event record, or with an error message,
                                        or empty is no record located
            """

            #return "SEARCHING<br><b>Type of search</b>: " + searchType + " <b>Searching for:</b> `" + searchString + "`"

            if searchType == "eventName":
                print("Searching by Event Name for `" + searchString + "`")
                searchResult = self.eventObj.searchByEventName(searchString)
                print("SEARCH RESULT in JSON form: ", searchResult)
                if searchResult is None:
                    response = {}
                else:
                    response = searchResult
            else:
                response = {"error": "This search type not yet implemented"}
                # Alternatively, one might elect to return a 405 HTTP error for wrong request

            return jsonify(response) # This function also takes care of the Content-Type header



        ################################################################
        #  API endpoint to provide update capabilities
        #  It accepts JSON data specifying: 1) the ID of the Event to update ; 2) the key field to update;  3) the new value for that key
        #  Example:
        #     curl localhost:5000/update -H "Content-Type: application/json" -d '{\"id\": 60405139398 , \"key\": \"currency\" , \"value\": \"Monopoly Money\"}'
        ################################################################

        @self.app.route("/update", methods=['GET', 'POST'])
        def update():
            """
            If using curl to generate a request, it should include -H "Content-Type: application/json"  (however, this method tolerates wrong Content-Type)

            Example:
            curl localhost:5000/update -H "Content-Type: application/json" -d '{\"id\": 53667810867 , \"key\": \"some key\" , \"value\": \"new Value\"}'

            :return: string with status of the requested update operation
            """
            print("Inside update()")

            if request.method != 'POST':
                return "The request was *NOT* a POST.  No action taken...."

            print("The request was a POST")


            # Attempt to parse data as JSON
            jsonData = request.get_json(force=True, silent=True)    # The force" flag allows lenience for requests that failed to include "Content-Type: application/json"
                                                                    # The "silent" flag prevents the immediate return of an error-message page in case of JSON parsing failure
            print("JSON data: ", jsonData)

            if jsonData is None:
                return "POST request received, but JSON parsing failed.\nThe received POST data was:\n          " + str(request.data) + "\n"
            else:
                print("JSON data successfully received:\n         " + str(request.data) + "\n")
                print("JSON data as a Python dictionary:", jsonData)

                id = jsonData["id"]
                key = jsonData["key"]
                value = jsonData["value"]
                print("Attempting to locate record with id = %d and modifying the key `%s` with the new value `%s`" % (id, key, value))

                errStatus = self.eventObj.modifyEvent(id, key, value)
                print("STATUS of update operation: ", errStatus)
                if errStatus != "":
                    return "Update FAILED. Reason: " + errStatus + "\n"
                    # Alternatively, one might elect to return a 404 HTTP error in case error not found

                return "Record updated successfully\n"




        self.app.run(debug=True)        # CORE of UI : transfer control to the "Flask object"
                                        # This  will start a local WSGI server.  Threaded mode is enabled by default


    # End of class instantiator
