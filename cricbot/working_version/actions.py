# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)


class ApiAction(Action):
    def name(self):
        return "action_match_news"

    def run(self, dispatcher, tracker, domain):
        api_link = "https://cricscore-api.appspot.com/csa"
        res = requests.get(api_link)
        if res.status_code == 200:
            data = res.json()
            if data:
                for match in data:
                    team = match["t1"] + ' VS ' + match["t2"]
                    dispatcher.utter_message(team)
            else:
                dispatcher.utter_message("There is no Live match today")
        else:
            dispatcher.utter_message("Oops!! There is a problem in API")

        return []


class ApiAction2(Action):
    def name(self):
        return "result_particular_match"

    def run(self, dispatcher, tracker, domain):
        api_link = "https://cricscore-api.appspot.com/csa"
        res = requests.get(api_link)
        team_name_tracker = tracker.get_slot('team_name')
        if res.status_code == 200:
            data = res.json()
            if data:
                flag = 0
                for match in data:
                    team_one = match["t1"]
                    team_two = match["t2"]
                    if team_one.lower() == team_name_tracker or team_two.lower() == team_name_tracker:
                        team_matched_id = str(match['id'])
                        required_match = requests.get(api_link + "?id=" + team_matched_id)
                        required_match_data = required_match.json()
                        flag = 1
                        for match_data in required_match_data:
                            dispatcher.utter_message(match_data['de'])
                if flag == 0:
                    dispatcher.utter_message("Actually we dont have any match for your team " + team_name_tracker)
            else:
                dispatcher.utter_message("Sorry! There is no Live match")
        else:
            dispatcher.utter_message("Oops!! There is a problem in API")

        return []
