# Minimalistic-Eventbright-JSON-API

A bare-bones Python/Flask API that was *created as an exercise*, but a clean code that could be expanded into something usable to search and update data through API endpoints for any JSON data source.

# 2 API's for live events, using sample data from Eventbrite

## One API endpoint (returns JSON) to search and return events by event name

## One API endpoint (accepts JSON) that allows a user to update the locally stored event record

1)	I scraped off a page worth of events (50 items) from https://www.eventbriteapi.com/v3/events/search/?token=[Private_OAuth_Key], and copy-and-pasted it into the file “dataFromEventBright.json” (in the "src" folder.)  Of course, in a real system, one would probably use Python to fetch it with a curl operation

2)	I created a Flask/Python program to read in the above file, provide in-memory storage as a Python list of Dictionaries (in real life, likely to use a database), and provide the 2 desided API's

3)	Examples of **SEARCH API**, offering a search by event name.  

     For example, there is an event called *“Ladies Night Out at Suite Lounge Hosted by Big Tigger”*.

     It can be searched as:
     
     `localhost:5000/search/eventName/Ladies%20Night%20Out%20at%20Suite%20Lounge%20Hosted%20by%20Big%20Tigger` 
          
     and it returns the JSON data for that event (see screenshot [*search1.PNG*](https://github.com/JuliansPolymathExplorations/minimalistic-Eventbright-API/blob/master/screenshots/search1.PNG)); also, a few error checks ([*search2.PNG*](https://github.com/JuliansPolymathExplorations/minimalistic-Eventbright-API/blob/master/screenshots/search2.PNG) and [*search3.PNG*](https://github.com/JuliansPolymathExplorations/minimalistic-Eventbright-API/blob/master/screenshots/search3.PNG))
     
     In case of error, it returns JSON code with error information.

4)	Examples of **UPDATE API**.  It accepts a JSON string such as 

     {"id": 60405139398 , 
      "key": "currency" , 
      "value": "Monopoly Money"
     }


     and it locates the event with the given ID and replaces the value of the specified key with the new value.  (That ID is the one of the event from the previous search.)
     
     It returns plain text, including in case of error.  In a real system, it'd probably return JSON code with status results.

     It can be run from a terminal or Windows PowerShell (if curl is installed) as:
     
     `curl localhost:5000/update -H "Content-Type: application/json" -d '{\"id\": 60405139398 , \"key\": \"currency\" , \"value\": \"Monopoly Money\"}'`
     
     (screenshot [*update1.PNG*](https://github.com/JuliansPolymathExplorations/minimalistic-Eventbright-API/blob/master/screenshots/update1.PNG) shows a few error checks and then a successful update; [*update2.PNG*](https://github.com/JuliansPolymathExplorations/minimalistic-Eventbright-API/blob/master/screenshots/update2.PNG) shows the updated record from a search for it)
