# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_timings"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="We are open everyday from 7pm to 10pm!")

         return []

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_reservation"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            seat = tracker.get_slot("seat")
            section = tracker.get_slot("section")
            a="1"
            b="2"
            section_name = ""
            flag="Hello"


            if section == a:
                section_name = "Non AC"
            elif section == b:
                section_name = "AC"
            else:
                flag="Bye"
                dispatcher.utter_message(text="Not Valid Option! How many seats would you like to reserve? ")

            if flag=="Hello":
                message = "You have reserved {} seats in our {} section".format(seat,section_name)
                print(message)
                dispatcher.utter_message(text=message)

            return []
