
## interactive_story_ask_location_cuisine_price_send_mail_yes
* greet
    - utter_greet
* enter_location
    - utter_ask_location
* enter_location{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_city
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price_cat": "BTW_300_700"}
    - slot{"price_cat": "BTW_300_700"}
	- slot{"price_txt": ""}
    - action_validate_price
    - slot{"price_cat": "BTW_300_700"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "satam_dnyanesh@yahoo.com"}
    - slot{"mailid": "satam_dnyanesh@yahoo.com"}
    - action_validate_mail
    - slot{"mailid": "satam_dnyanesh@yahoo.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_ask_location_cuisine_price_send_mail_no
* greet
    - utter_greet
* enter_location
    - utter_ask_location
* enter_location{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_city
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price_cat": "More_700"}
    - slot{"price_cat": "More_700"}
	- slot{"price_txt": ""}
    - action_validate_price
    - slot{"price_cat": "More_700"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted

## interactive_story_ask_location_given_cuisine_price_send_mail_yes
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_txt": "<600"}
    - slot{"cuisine": "chinese"}
    - slot{"price_txt": "<600"}
	- slot{"price_cat": ""}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "<600"}
    - utter_ask_location
* enter_location{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_city
    - slot{"location": "pune"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "satam.dnyanesh@gmail.com"}
    - slot{"mailid": "satam.dnyanesh@gmail.com"}
    - action_validate_mail
    - slot{"mailid": "satam.dnyanesh@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_ask_location_given_cuisine_price_send_mail_no
* greet
    - utter_greet
* restaurant_search{"cuisine": "Maxican", "price_txt": "Rs. 500 to 1000"}
    - slot{"cuisine": "Maxican"}
    - slot{"price_txt": "Rs. 500 to 1000"}
	- slot{"price_cat": ""}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "Rs. 500 to 1000"}
    - utter_ask_location
* enter_location{"location": "surat"}
    - slot{"location": "surat"}
    - action_validate_city
    - slot{"location": "surat"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted

## interactive_story_ask_cuisine_given_location_price_send_mail_yes
* greet
    - utter_greet
* restaurant_search{"location": "hydrabad", "price_txt": "below 800"}
    - slot{"location": "indore"}
    - slot{"price_txt": "below 800"}
	- slot{"price_cat": ""}
    - action_validate_city
    - slot{"location": "indore"}
    - action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "below 800"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - action_search_restaurants
    - slot{"location": "indore"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "satam_dnyanesh@yahoo.com"}
    - slot{"mailid": "satam_dnyanesh@yahoo.com"}
    - action_validate_mail
    - slot{"mailid": "satam_dnyanesh@yahoo.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_ask_cuisine_given_location_price_send_mail_no
* greet
    - utter_greet
* restaurant_search{"location": "hydrabad", "price_txt": "below 800"}
    - slot{"location": "indore"}
    - slot{"price_txt": "below 800"}
	- slot{"price_cat": ""}
    - action_validate_city
    - slot{"location": "indore"}
    - action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "below 800"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - action_search_restaurants
    - slot{"location": "indore"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted

## interactive_story_ask_price_given_location_cuisine_send_mail_yes
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_city
    - slot{"location": "chandigarh"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price_cat": "Lesser_300"}
    - slot{"price_cat": "Lesser_300"}
	- slot{"price_txt": ""}
    - action_validate_price
    - slot{"price_cat": "Lesser_300"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "satam_dnyanesh@yahoo.com"}
    - slot{"mailid": "satam_dnyanesh@yahoo.com"}
    - action_validate_mail
    - slot{"mailid": "satam_dnyanesh@yahoo.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_ask_price_given_location_cuisine_send_mail_no
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_city
    - slot{"location": "chandigarh"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price_cat": "Lesser_300"}
    - slot{"price_cat": "Lesser_300"}
	- slot{"price_txt": ""}
    - action_validate_price
    - slot{"price_cat": "Lesser_300"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted


## interactive_story_given_location_cuisine_price_send_mail_yes
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "mumbai", "price_txt": "<1000"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "mumbai"}
    - slot{"price_txt": "<1000"}
	- slot{"price_cat": ""}
    - action_validate_city
    - slot{"location": "mumbai"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "<1000"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "satam.dnyanesh@gmail.com"}
    - slot{"mailid": "satam.dnyanesh@gmail.com"}
    - action_validate_mail
    - slot{"mailid": "satam.dnyanesh@gmail.com"}
    - utter_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_given_location_cuisine_price_send_mail_no
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "mumbai", "price_txt": "<1000"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "mumbai"}
    - slot{"price_txt": "<1000"}
	- slot{"price_cat": ""}
    - action_validate_city
    - slot{"location": "mumbai"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "<1000"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted

## interactive_story_given_price_ask_location_cuisine_send_mail_yes
* greet
    - utter_greet
* select_price{"price_txt": "between 400 to 800"}
    - slot{"price_txt": "between 400 to 800"}
	- slot{"price_cat": ""}
    - action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "between 400 to 800"}
    - utter_ask_location
* enter_location{"location": "nagpur"}
    - slot{"location": "nagpur"}
    - action_validate_city
    - slot{"location": "nagpur"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"location": "nagpur"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "abcd123@xyz.com"}
    - slot{"mailid": "abcd123@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "abcd123@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_given_price_ask_location_cuisine_send_mail_no
* greet
    - utter_greet
* select_price{"price_txt": "between 400 to 800"}
    - slot{"price_txt": "between 400 to 800"}
	- slot{"price_cat": ""}
    - action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "between 400 to 800"}
    - utter_ask_location
* enter_location{"location": "nagpur"}
    - slot{"location": "nagpur"}
    - action_validate_city
    - slot{"location": "nagpur"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"location": "nagpur"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted


## interactive_story_given_location_ask_price_cuisine_send_mail_yes
* greet
    - utter_greet
* enter_location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_city
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price_cat": "BTW_300_700"}
    - slot{"price_cat": "BTW_300_700"}
    - slot{"price_txt": ""}
	- action_validate_price
    - slot{"price_cat": "BTW_300_700"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "sai123@frrdg.vom"}
    - slot{"mailid": "sai123@frrdg.vom"}
    - action_validate_mail
    - slot{"mailid": "sai123@frrdg.vom"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_given_location_ask_price_cuisine_send_mail_no
* greet
    - utter_greet
* enter_location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_city
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price_cat": "BTW_300_700"}
    - slot{"price_cat": "BTW_300_700"}
    - slot{"price_txt": ""}
	- action_validate_price
    - slot{"price_cat": "BTW_300_700"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted

## interactive_story_given_cuisine_ask_price_location_send_mail_yes
* greet
    - utter_greet
* select_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* enter_location{"location": "jammu"}
    - slot{"location": "jammu"}
    - action_validate_city
    - slot{"location": "jammu"}
    - utter_ask_price
* restaurant_search{"price_cat": "BTW_300_700"}
    - slot{"price_cat": "BTW_300_700"}
    - slot{"price_txt": ""}
	- action_validate_price
    - slot{"price_cat": "BTW_300_700"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "jammu"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "dany123@xyz.com"}
    - slot{"mailid": "dany123@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "dany123@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_given_cuisine_ask_price_location_send_mail_no
* greet
    - utter_greet
* select_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* enter_location{"location": "jammu"}
    - slot{"location": "jammu"}
    - action_validate_city
    - slot{"location": "jammu"}
    - utter_ask_price
* restaurant_search{"price_cat": "BTW_300_700"}
    - slot{"price_cat": "BTW_300_700"}
    - slot{"price_txt": ""}
	- action_validate_price
    - slot{"price_cat": "BTW_300_700"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "jammu"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted


## interactive_story_given_price_ask_cuisine_location_send_mail_yes
* greet
    - utter_greet
* restaurant_search{"location": "mumbai", "price_txt": "below 500"}
    - slot{"location": "mumbai"}
    - slot{"price_txt": "below 500"}
	- slot{"price_cat": ""}
    - action_validate_city
    - slot{"location": "mumbai"}
    - action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "below 500"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "abcd@xyz.com"}
    - slot{"mailid": "abcd@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "abcd@xyz.com"}
    - utter_goodbye
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_given_price_ask_cuisine_location_send_mail_no
* greet
    - utter_greet
* restaurant_search{"location": "mumbai", "price_txt": "below 500"}
    - slot{"location": "mumbai"}
    - slot{"price_txt": "below 500"}
	- slot{"price_cat": ""}
    - action_validate_city
    - slot{"location": "mumbai"}
    - action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "below 500"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted

############################################# LOCATION VALIDATION #################################################

## story_with_restaurant_search_with_greet_enter_invalid_location
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* enter_location{"location": "mumbra"}
    - slot{"location": "mumbra"}
	- action_validate_city
	- slot{"location": null}
    - utter_ask_location

## story_with_restaurant_search_without_greet_enter_invalid_location
* restaurant_search
	- utter_ask_location
* enter_location{"location": "bandra"}
    - slot{"location": "bandra"}
	- action_validate_city
	- slot{"location": null}
    - utter_ask_location
	
## story_with_enter_location_with_greet_enter_incorrect_location
* greet
    - utter_greet
* enter_location
	- utter_ask_location
* enter_location{"location": "mumbra"}
    - slot{"location": "mumbra"}
	- action_validate_city
	- slot{"location": null}
    - utter_ask_location

## story_with_enter_location_without_greet_enter_incorrect_location
* enter_location
	- utter_ask_location
* enter_location{"location": "bandra"}
    - slot{"location": "bandra"}
	- action_validate_city
	- slot{"location": null}
    - utter_ask_location

## interactive_story_location_validation__send_mail
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* enter_location{"location": "puna"}
    - slot{"location": "puna"}
    - action_validate_city
    - slot{"location": null}
    - utter_ask_location
* enter_location{"location": "Mumbra"}
    - slot{"location": "Mumbra"}
    - action_validate_city
    - slot{"location": null}
    - utter_ask_location
* enter_location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_city
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price_cat": "More_700"}
    - slot{"price_cat": "More_700"}
    - action_validate_price
    - slot{"price_cat": "More_700"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "abc@xyz.com"}
    - slot{"mailid": "abc@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "abc@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_location_validation_send_mail_no
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* enter_location{"location": "puna"}
    - slot{"location": "puna"}
    - action_validate_city
    - slot{"location": null}
    - utter_ask_location
* enter_location{"location": "Mumbra"}
    - slot{"location": "Mumbra"}
    - action_validate_city
    - slot{"location": null}
    - utter_ask_location
* enter_location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_city
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price_cat": "More_700"}
    - slot{"price_cat": "More_700"}
    - action_validate_price
    - slot{"price_cat": "More_700"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted

## story_which_folows_after_valid_location_entry
* enter_location
	- utter_ask_location
* enter_location{"location": "bangalore"}
    - slot{"location": "bangalore"}
	- action_validate_city
	- slot{"location": "bangalore"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price_cat": "BTW_300_700"}
    - slot{"price_cat": "BTW_300_700"}
    - slot{"price_txt": ""}
	- action_validate_price
    - slot{"price_cat": "BTW_300_700"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "dany123@xyz.com"}
    - slot{"mailid": "dany123@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "dany123@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted


## interactive_story_ask_price_given_location_cuisine_enter_invalid_location
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chendigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chendigarh"}
	- action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - action_validate_city
    - slot{"location": null}
	- utter_ask_location
* enter_location{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_validate_city
    - slot{"location": "Nagpur"}	   
    - utter_ask_price
* restaurant_search{"price_cat": "Lesser_300"}
    - slot{"price_cat": "Lesser_300"}
	- slot{"price_txt": ""}
    - action_validate_price
    - slot{"price_cat": "Lesser_300"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted

## interactive_story_ask_location_given_invalid_location_first_then_correct_send_mail_yes
* greet
    - utter_greet
* restaurant_search{"cuisine": "Maxican", "price_txt": "Rs. 500 to 1000"}
    - slot{"cuisine": "Maxican"}
    - slot{"price_txt": "Rs. 500 to 1000"}
	- slot{"price_cat": ""}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "Rs. 500 to 1000"}
    - utter_ask_location
* enter_location{"location": "sorat"}
    - slot{"location": "sorat"}
    - action_validate_city
    - slot{"location": null}
	- utter_ask_location
* enter_location{"location": "surat"}
    - slot{"location": "surat"}
    - action_validate_city
    - slot{"location": "surat"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "dany123@xyz.com"}
    - slot{"mailid": "dany123@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "dany123@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_ask_location_given_invalid_location_first_then_correct_send_mail_no
* greet
    - utter_greet
* restaurant_search{"cuisine": "Maxican", "price_txt": "Rs. 500 to 1000"}
    - slot{"cuisine": "Maxican"}
    - slot{"price_txt": "Rs. 500 to 1000"}
	- slot{"price_cat": ""}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "Rs. 500 to 1000"}
    - utter_ask_location
* enter_location{"location": "sorat"}
    - slot{"location": "sorat"}
    - action_validate_city
    - slot{"location": null}
	- utter_ask_location
* enter_location{"location": "surat"}
    - slot{"location": "surat"}
    - action_validate_city
    - slot{"location": "surat"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "dany123@xyz.com"}
    - slot{"mailid": "dany123@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "dany123@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

########################### CUISINE VALIDATION ##########################

## story_with_restaurant_search_without_greet_enter_invalid_cuisine
* restaurant_search
	- utter_ask_cuisine
* select_cuisine{"cuisine": "Sandwitch"}
    - slot{"cuisine": "Sandwitch"}
	- action_validate_cuisine
	- slot{"cuisine": null}
    - utter_ask_cuisine

## story_with_enter_location_without_greet_enter_incorrect_cuisine
* select_cuisine
	- utter_ask_cuisine
* select_cuisine{"cuisine": "Sandwitch"}
    - slot{"cuisine": "Sandwitch"}
	- action_validate_cuisine
	- slot{"cuisine": null}
    - utter_ask_cuisine

## interactive_story_cuisine_validation__send_mail_yes
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* enter_location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_city
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "Soouth Indian"}
    - slot{"cuisine": "Soouth Indian"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price_cat": "More_700"}
    - slot{"price_cat": "More_700"}
    - action_validate_price
    - slot{"price_cat": "More_700"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "abc@xyz.com"}
    - slot{"mailid": "abc@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "abc@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_cuisine_validation__send_mail_no
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* enter_location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_city
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "Soouth Indian"}
    - slot{"cuisine": "Soouth Indian"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price_cat": "More_700"}
    - slot{"price_cat": "More_700"}
    - action_validate_price
    - slot{"price_cat": "More_700"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted

## interactive_story_ask_location_given_cuisine_price_enter_invalid_cuisine_first
* greet
    - utter_greet
* restaurant_search{"cuisine": "chainese", "price_txt": "<600"}
    - slot{"price_txt": "<600"}
	- slot{"price_cat": ""}
	- action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "<600"}
	- slot{"cuisine": "chainese"}
    - action_validate_cuisine
	- slot{"cuisine": null}
	- utter_ask_cuisine
* select_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* enter_location{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_city
    - slot{"location": "pune"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "dany123@xyz.com"}
    - slot{"mailid": "dany123@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "dany123@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_ask_location_given_cuisine_price_enter_invalid_cuisine_first_no_send
* greet
    - utter_greet
* restaurant_search{"cuisine": "chainese", "price_txt": "<600"}
    - slot{"price_txt": "<600"}
	- slot{"price_cat": ""}
	- action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "<600"}
	- slot{"cuisine": "chainese"}
    - action_validate_cuisine
	- slot{"cuisine": null}
	- utter_ask_cuisine
* select_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* enter_location{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_city
    - slot{"location": "pune"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted


########################### PRICE VALIDATION ##########################

## story_with_restaurant_search_without_greet_enter_invalid_price_cat
* restaurant_search
	- utter_ask_price
* select_price{"price_cat": "BTW_300_800"}
    - slot{"price_cat": "BTW_300_800"}
	- slot{"price_txt": ""}
	- action_validate_price
	- slot{"price_cat": null}
	- slot{"price_txt": null}
	- utter_ask_price

## story_with_restaurant_search_without_greet_enter_invalid_price_cat
* restaurant_search
	- utter_ask_price
* restaurant_search{"price_cat": "BTW_300_800"}
    - slot{"price_cat": "BTW_300_800"}
	- slot{"price_txt": ""}
	- action_validate_price
	- slot{"price_cat": null}
	- slot{"price_txt": null}
	- utter_ask_price

## story_with_enter_location_without_greet_enter_invalid_price_cat
* select_price
	- utter_ask_price
* select_price{"price_cat": "BTW_300_800"}
    - slot{"price_cat": "BTW_300_800"}
	- slot{"price_txt": ""}
	- action_validate_price
	- slot{"price_cat": null}
	- slot{"price_txt": null}
	- utter_ask_price
	
## story_with_restaurant_search_without_greet_enter_invalid_price_txt
* restaurant_search
	- utter_ask_price
* select_price{"price_txt": "greater"}
    - slot{"price_cat": ""}
	- slot{"price_txt": "greater"}
	- action_validate_price
	- slot{"price_cat": null}
	- slot{"price_txt": null}
	- utter_ask_price

## story_with_enter_location_without_greet_enter_invalid_price_cat
* select_price
	- utter_ask_price
* select_price{"price_txt": "lower"}
    - slot{"price_cat": ""}
	- slot{"price_txt": "lower"}
	- action_validate_price
	- slot{"price_cat": null}
	- slot{"price_txt": null}
	- utter_ask_price
	
## interactive_story_price_cat_validation_send_mail_yes
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* enter_location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_city
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price_cat": "More than 700"}
    - slot{"price_cat": "More than 700"}
	- slot{"price_txt": ""}
    - action_validate_price
    - slot{"price_cat": null}
    - slot{"price_txt": null}
	- utter_ask_price
* restaurant_search{"price_cat": "More_700"}
    - slot{"price_cat": "More_700"}
	- slot{"price_txt": ""}
    - action_validate_price
    - slot{"price_cat": "More_700"}
	- slot{"price_txt": ""}
	- action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "abc@xyz.com"}
    - slot{"mailid": "abc@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "abc@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_price_cat_validation_send_mail_no
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* enter_location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_city
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price_cat": "More than 700"}
    - slot{"price_cat": "More than 700"}
	- slot{"price_txt": ""}
    - action_validate_price
    - slot{"price_cat": null}
    - slot{"price_txt": null}
	- utter_ask_price
* restaurant_search{"price_cat": "More_700"}
    - slot{"price_cat": "More_700"}
	- slot{"price_txt": ""}
    - action_validate_price
    - slot{"price_cat": "More_700"}
	- slot{"price_txt": ""}
	- action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted

## interactive_story_price_txt_validation_send_mail_yes
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* enter_location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_city
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* select_price{"price_txt": "More than"}
    - slot{"price_cat": ""}
	- slot{"price_txt": "More than"}
    - action_validate_price
    - slot{"price_cat": null}
    - slot{"price_txt": null}
	- utter_ask_price
* select_price{"price_txt": "> 700"}
    - slot{"price_cat": ""}
	- slot{"price_txt": "> 700"}
    - action_validate_price
    - slot{"price_cat": ""}
	- slot{"price_txt": "> 700"}
	- action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "abc@xyz.com"}
    - slot{"mailid": "abc@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "abc@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_price_txt_validation_send_mail_no
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* enter_location{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_city
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* select_price{"price_txt": "More than"}
    - slot{"price_cat": ""}
	- slot{"price_txt": "More than"}
    - action_validate_price
    - slot{"price_cat": null}
    - slot{"price_txt": null}
	- utter_ask_price
* select_price{"price_txt": "> 700"}
    - slot{"price_cat": ""}
	- slot{"price_txt": "> 700"}
    - action_validate_price
    - slot{"price_cat": ""}
	- slot{"price_txt": "> 700"}
	- action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted

## interactive_story_ask_location_given_cuisine_price_txt
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_txt": "lower"}
    - slot{"cuisine": "chinese"}
	- action_validate_cuisine
    - slot{"cuisine": "chinese"}
	- slot{"price_txt": "lower"}
	- slot{"price_cat": ""}
	- action_validate_price	
    - slot{"price_txt": null}
	- slot{"price_cat": null}
 	- utter_ask_price
* select_price{"price_txt": "<600"}
	- slot{"price_cat": ""}
    - slot{"price_txt": "<600"}
	- action_validate_price	
    - slot{"price_txt": "<600"}
	- slot{"price_cat": ""}	
	- utter_ask_location
* enter_location{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_city
    - slot{"location": "pune"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "dany123@xyz.com"}
    - slot{"mailid": "dany123@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "dany123@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted

## interactive_story_ask_location_given_cuisine_price_cat
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price_cat": "lower 500"}
    - slot{"cuisine": "chinese"}
	- action_validate_cuisine
    - slot{"cuisine": "chinese"}
	- slot{"price_txt": ""}
	- slot{"price_cat": "lower 500"}
	- action_validate_price	
    - slot{"price_txt": null}
	- slot{"price_cat": null}
 	- utter_ask_price
* select_price{"price_cat": "Lesser_300"}
	- slot{"price_cat": "Lesser_300"}
    - slot{"price_txt": ""}
	- action_validate_price	
    - slot{"price_txt": ""}
	- slot{"price_cat": "Lesser_300"}	
	- utter_ask_location
* enter_location{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_city
    - slot{"location": "pune"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_send_mail
* deny
    - utter_goodbye
    - action_restarted

########################### EMAILID VALIDATION ##########################

## send_mail_with_invalid_id
* send_mail{"mailid": "abc@xyz.com.ere.rtrt"}
    - slot{"mailid": "abc@xyz.com.ere.rtrt"}
    - action_validate_mail
    - slot{"mailid": null}
	- utter_ask_mail

## send_mail_with_valid_id
* send_mail
    - utter_ask_mail
* send_mail{"mailid": "abc@xyz.com"}
    - slot{"mailid": "abc@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "abc@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted
 
## send_mail_with_first_invalid_then_valid_id
* send_mail
    - utter_ask_mail
* send_mail{"mailid": "12abc@xyz.com"}
    - slot{"mailid": "12abc@xyz.com"}
    - action_validate_mail
    - slot{"mailid": null}
	- utter_ask_mail
* send_mail{"mailid": "abc_lmn@xyz.com"}
    - slot{"mailid": "abc_lmn@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "abc_lmn@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted
	
	
### Send_mail_invalid_with_full_story	
* greet
    - utter_greet
* enter_location
    - utter_ask_location
* enter_location{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_city
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* select_cuisine{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price_cat": "BTW_300_700"}
    - slot{"price_cat": "BTW_300_700"}
	- slot{"price_txt": ""}
    - action_validate_price
    - slot{"price_cat": "BTW_300_700"}
    - slot{"price_txt": ""}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "satam@dnyanesh@yahoo.com"}
    - slot{"mailid": "satam@dnyanesh@yahoo.com"}
    - action_validate_mail
    - slot{"mailid": null}
	- utter_ask_mail
* send_mail{"mailid": "satam_dnyanesh@yahoo.com"}
    - slot{"mailid": "satam@dnyanesh@yahoo.com"}
    - action_validate_mail
    - slot{"mailid": "satam@dnyanesh@yahoo.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted
	
## interactive_story_ask_location_given_invalid_location_first_then_correct_send_mail_yes
* greet
    - utter_greet
* restaurant_search{"cuisine": "Maxican", "price_txt": "Rs. 500 to 1000"}
    - slot{"cuisine": "Maxican"}
    - slot{"price_txt": "Rs. 500 to 1000"}
	- slot{"price_cat": ""}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_validate_price
    - slot{"price_cat": ""}
    - slot{"price_txt": "Rs. 500 to 1000"}
    - utter_ask_location
* enter_location{"location": "sorat"}
    - slot{"location": "sorat"}
    - action_validate_city
    - slot{"location": null}
	- utter_ask_location
* enter_location{"location": "surat"}
    - slot{"location": "surat"}
    - action_validate_city
    - slot{"location": "surat"}
    - action_search_restaurants
    - slot{"location": "surat"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* send_mail{"mailid": "dany_&*123@xyz.com"}
    - slot{"mailid": "dany_&*123@xyz.com"}
    - action_validate_mail
    - slot{"mailid": null}
	- utter_ask_mail
* send_mail{"mailid": "dany#*123@xyz.com@.dd"}
    - slot{"mailid": "dany#*123@xyz.com@.dd"}
    - action_validate_mail
    - slot{"mailid": null}
	- utter_ask_mail
* send_mail{"mailid": "dany@xyz.com"}
    - slot{"mailid": "dany@xyz.com"}
    - action_validate_mail
    - slot{"mailid": "dany@xyz.com"}
    - action_send_mail
    - utter_goodbye
    - action_restarted


## story_affirm_ask_for_emailid
* affirm
    - utter_ask_mail

## story_deny_ask_say_goodbye
* deny
    - utter_goodbye
	- action_restarted

## say goodbye
* goodbye
	- utter_goodbye
