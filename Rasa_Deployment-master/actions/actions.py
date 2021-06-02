# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         dispatcher.utter_message(text="Hey! How are you?")

#         return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        platform_asked = tracker.get_slot("platform")

        def link_sender(link_asked):
            if platform_asked == "Youtube" or platform_asked == "youtube" or platform_asked=="yt" or platform_asked=="you tube" or platform_asked=="YOUTUBE" or platform_asked=="YOU TUBE":

                return "The link to the Youtube channel is: <a href=\"https://www.youtube.com/channel/UCqFPDb2aCMzvdOpLpBF9kZw\">https://www.youtube.com/channel/UCqFPDb2aCMzvdOpLpBF9kZw </a>."
        
            elif platform_asked == "Facebook" or platform_asked == "facebook" or platform_asked=="fb" or platform_asked=="FACEBOOK" or platform_asked=="FB":
                return "This is the link to facebook: <a href=\"https://www.facebook.com/HariOmHomeoClinic/\">https://www.facebook.com/HariOmHomeoClinic/</a>"

            elif platform_asked == "Twitter" or platform_asked == "twitter" or platform_asked=="tweet" or platform_asked=="TWITTER" or platform_asked=="TWEET":
                return "This is the twitter link: < a target=\"_blank\" href=\"https://twitter.com/HariOmHomeo\">https://twitter.com/HariOmHomeo</a>"

            elif platform_asked == "Instagram" or platform_asked == "instagram" or platform_asked=="insta" or platform_asked=="INSTA" or platform_asked=="INSTAGRAM":
                return "Instagram page link: <a href=\"https://www.instagram.com/hariomhomeo/\">https://www.instagram.com/hariomhomeo/</a>"

            else:
                return "I'm actually confused :( We have links to facebook, twitter, instagram and yourube. "

        
        result_link = str(link_sender(platform_asked))

        dispatcher.utter_message(text=result_link)

        return []

class AppointmentDetails(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["name", "email"]


        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
        
        

       

        # All slots are filled.
        return [SlotSet("requested_slot", None)], first_name, last_name

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"



    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        # name_given = tracker.get_slot("name")
        # name_given = name_given.split(' ')
        # first_name = name_given[0]
        # last_name = name_given[-1]

        dispatcher.utter_message(template="utter_details_thanks",
                                 Name=tracker.get_slot("name"),
                                 Email=tracker.get_slot("email"),
                                )
