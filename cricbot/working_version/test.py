# import logging
# import requests
# from rasa_core_sdk import Action
#
#
# api_link = "https://cricscore-api.appspot.com/csa"
# res = requests.get(api_link)
# team_name_tracker = "ireland"
# if res.status_code == 200:
#     data = res.json()
#     if data:
#         flag = 0
#         temp_name = ''
#         for match_i in data:
#             team_one = match_i["t1"]
#             team_two = match_i["t2"]
#             match_id = match_i["id"]
#             print(match_id)
#             if team_one.lower() == team_name_tracker or team_two.lower() == team_name_tracker:
#                 print ("entered")
#                         # team_matched_id = match['id']
#                         # required_match = requests.get(api_link + "?id=" + team_matched_id)
#                         # required_match_data = required_match.json()
#                         # flag = 1
#                         # for match_data in required_match_data:
#                         #     dispatcher.utter_message(match_data['de'])
#                     # temp_name = temp_name+match['t1'].lower()
#         if flag == 0:
#             print ("Actually we dont have any match for your team " + team_name_tracker)
#     else:
#          print ("Sorry! There is no such match for your team")
# else:
#      print("Oops!! There is a problem in API")