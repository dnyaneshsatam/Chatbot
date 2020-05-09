from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import re
from rasa_sdk.events import Restarted , FollowupAction , ActionExecuted
import smtplib




class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        #time.sleep(15)
        config={ "user_key":"f91f284038da4cb9ea21469489a31d6f"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price_cat = tracker.get_slot('price_cat')
        price_txt = tracker.get_slot('price_txt')
        print("Location:",loc)
        print("Cuisine:",cuisine)
        print("Price_Cat:",price_cat)
        print("Price_Txt:",price_txt)
        min_price = 0
        max_price = 0
        
        if price_cat != None:
            price_cat=price_cat.lower()
            price_cat=price_cat.strip()
        
        if price_txt != None:
            price_txt=price_txt.lower()
            price_txt=price_txt.strip()
        
        response=""
        global mail_response 
        mail_response = ""
        ########## Code to find the city weather Foodie is operating or not  ################
        """
        if loc == None:
            response = "Sorry ,We do not operate in that area yet."
            dispatcher.utter_message(response)
            return [SlotSet('location',None)]
        else:
            file = open("city.txt",'r')
            file_data = file.read()
            file.close()
            city_search_result = re.search(loc,file_data.lower())
        
            if city_search_result == None:
                response = "Sorry ,We do not operate in that area yet.Can youplease specify some other location"
                dispatcher.utter_message(response)
                #FollowupAction("utter_ask_location")
                return [SlotSet('location',None)]
        """
        #################### End of City Search #########################        
        if loc != None:
            loc=loc.lower()
        
        if cuisine != None:
            cuisine=cuisine.lower()
        ###################### price_txt ##############################
        if price_txt != None and price_txt != "":
            
            search_result = re.findall('[0-9]{2,}',price_txt)
        
            if len(search_result) == 2:
                print('Case1')
                min_price = int(search_result[0])
                max_price = int(search_result[1])
            
            elif len(search_result) == 1:
                print('Case2')
                search_match = re.search('<.{0,2}[0-9]{2,}',price_txt)
            
                if search_match != None:
                    min_price = 0
                    max_price = int(re.findall('[0-9]{2,}',price_txt)[0])
                    
                else:
                    search_match = re.search('>.{0,2}[0-9]{2,}',price_txt)
                
                    if search_match != None:
                        min_price = int(re.findall('[0-9]{2,}',price_txt)[0])
                        max_price = 0
                        
                if min_price == 0 and max_price == 0:
                    
                    upper_limit = ['less','lesser','max','maximum','around','lower']
                    lower_limit = ['more','above','greater','minimum','upper']
                    price=int(re.search('[0-9]{2,3}',price_txt)[0])
                    
                
                    price_txt_split = price_txt.split()
                
                    for word in price_txt_split:
                        if word.lower() in upper_limit:
                            min_price=0
                            max_price=price
                            break
                    
                        if word.lower() in lower_limit:
                            max_price=0
                            min_price=price
                            break
            else:
                print('Case3')
                min_price=0
                max_price=0
            
            ## As here we have three category
            ## [1]. <300 [2] >= 300 & <= 700 [3] >= 700
            ## category
            print("--------------------")
            print("Min Price :",min_price)
            print("Max Price :",max_price)
            print("--------------------")
            
            if min_price >= 300:
                if min_price > 700 or max_price > 700:
                    price_cat = "more_700"
                elif min_price < 700 and max_price > 700:
                    price_cat = "more_700"
                elif min_price >= 700 and max_price == 0:
                    price_cat = "more_700"
                elif min_price < 700 and max_price <= 700:
                    price_cat = "btw_300_700"    
                else:
                    price_cat = "btw_300_700"
            elif min_price < 300 and max_price > 300 and max_price <= 700:
                price_cat = "btw_300_700"
            elif min_price < 300 and max_price > 300 and max_price > 700:
                price_cat = "more_700"
            else:
                price_cat = "lesser_300"
                       
                        
            if price_cat == "lesser_300":
                min_price = 0
                max_price = 300                
            elif price_cat == "btw_300_700":
                min_price = 300
                max_price = 700
            else:
                min_price = 700
                max_price = 0
            
            
        ###################### price_cat ##############################
        
        if price_cat != None and price_cat != "":
            if price_cat == "lesser_300":
                min_price = 0
                max_price = 300
            elif price_cat == "btw_300_700":
                min_price = 300
                max_price = 700
            else:
                min_price = 700
                max_price = 0
            
        
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        city_id=d1["location_suggestions"][0]["city_id"]
        cuisines_dict=zomato.get_cuisines(city_id)
        cuisine_id = ""
        cuisine_name = ""
        
        for cus_id,cus_name in cuisines_dict.items():
            if cus_name.lower() == cuisine:
                cuisine_id = str(cus_id)
                cuisine_name = cus_name
                break
        
        
        print("City ID:",str(city_id))
        print("Cuisine_id:",cuisine_id)
        print("Cuisine_name:",cus_name)
        print("Min Price :",min_price)
        print("Max Price :",max_price)
      

        results=zomato.restaurant_search("",lat,lon,cuisine_id,100)
        
        #print(results)
        d = json.loads(results)
        
        if d['results_found'] == 0:
            response= "No Results Found"
            mail_response = "No Results Found"
        else:
            #filter_result = [ ( x['restaurant']['name'] + "," + x['restaurant']['location']['address'] + " has been rated " + x['restaurant']['user_rating']['aggregate_rating'] + "Rs." + str(x['restaurant']['average_cost_for_two'])) for x in d['restaurants'] if x['restaurant']['average_cost_for_two'] >= min_price and x['restaurant']['average_cost_for_two'] <= max_price]
            
            #filter_result = []
            restaurant_count = 0
            
            if min_price > 0 and max_price > 0:
                
                for x in d['restaurants']:
                    if x['restaurant']['average_cost_for_two'] >= min_price and x['restaurant']['average_cost_for_two'] <= max_price:
                        restaurant_count  = restaurant_count  + 1
                        mail_response = mail_response + x['restaurant']['name'] + "," + x['restaurant']['location']['address'] + " has been rated " + x['restaurant']['user_rating']['aggregate_rating'] + " star Rs. " + str(x['restaurant']['average_cost_for_two']) + "\n"
                        if restaurant_count <= 5:
                            response = response + x['restaurant']['name'] + "," + x['restaurant']['location']['address'] + " has been rated " + x['restaurant']['user_rating']['aggregate_rating'] + " star Rs. " + str(x['restaurant']['average_cost_for_two']) + "\n"
                        
                        if restaurant_count >= 10:
                            break
                        
            elif min_price == 0 and max_price > 0:
                
                for x in d['restaurants']:
                    if x['restaurant']['average_cost_for_two'] <= max_price:
                        restaurant_count  = restaurant_count  + 1
                        mail_response = mail_response + x['restaurant']['name'] + "," + x['restaurant']['location']['address'] + " has been rated " + x['restaurant']['user_rating']['aggregate_rating'] + " star Rs. " + str(x['restaurant']['average_cost_for_two'])  + "\n"
                        if restaurant_count <= 5:
                            response = response + x['restaurant']['name'] + "," + x['restaurant']['location']['address'] + " has been rated " + x['restaurant']['user_rating']['aggregate_rating'] + " star Rs. " + str(x['restaurant']['average_cost_for_two'])  + "\n"
                        
                        if restaurant_count >= 10:
                            break
                
            elif min_price > 0 and max_price == 0:
                
                for x in d['restaurants']:
                    if x['restaurant']['average_cost_for_two'] >= min_price:
                        restaurant_count  = restaurant_count  + 1
                        mail_response = mail_response + x['restaurant']['name'] + "," + x['restaurant']['location']['address'] + " has been rated " + x['restaurant']['user_rating']['aggregate_rating'] + " star Rs. " + str(x['restaurant']['average_cost_for_two'])  + "\n"
                        if restaurant_count <= 5:
                            response = response + x['restaurant']['name'] + "," + x['restaurant']['location']['address'] + " has been rated " + x['restaurant']['user_rating']['aggregate_rating'] + " star Rs. " + str(x['restaurant']['average_cost_for_two'])  + "\n"
                        
                        if restaurant_count >= 10:
                            break
            
            else:
                                               
                for x in d['restaurants']:
                    restaurant_count  = restaurant_count  + 1
                    mail_response = mail_response + x['restaurant']['name'] + "," + x['restaurant']['location']['address'] + " has been rated " + x['restaurant']['user_rating']['aggregate_rating'] + " star Rs. " + str(x['restaurant']['average_cost_for_two']) + "\n"
                    if restaurant_count <= 5:
                        response = response + x['restaurant']['name'] + "," + x['restaurant']['location']['address'] + " has been rated " + x['restaurant']['user_rating']['aggregate_rating'] + " star Rs. " + str(x['restaurant']['average_cost_for_two']) + "\n"
                    
                    if restaurant_count >= 10:
                        break
        #self.msg = response
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]


class ActionSendMail(Action):
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher, tracker, domain):
        
        print('******In Mail Sent**********')
        mailid = tracker.get_slot('mailid')
        
        if mail_response != "No Results Found":
            
            try:
                
                s = smtplib.SMTP("smtp.gmail.com",587)
                s.ehlo()
                s.starttls()
                s.login("foodiechatchat@gmail.com","test@1234")
                
                FROM = 'foodiechatchat@gmail.com'
                TO = mailid
                SUBJECT = 'Foodie Recommends. Happy Foodying'
                MSG = mail_response

                message = """From: %s\nTo: %s\nSubject: %s \n\n%s""" % (FROM,TO,SUBJECT,MSG)

                s.sendmail(FROM,TO,message)
                s.quit()
                
                response = 'Please check your inbox. You should have received these details. Happy Foodying!'
            
            except:
                
                response = 'Sorry! Due to some technical issues we were unable to send you a mail'
        
        dispatcher.utter_message(response)
        return []


class ActionRestarted(Action):
    def name(self):         
        return 'action_restarted'   
    def run(self, dispatcher, tracker, domain):
        return[Restarted()]


class ActionValidateMail(Action):
    def name(self):
        return 'action_validate_mail'
        

    def run(self, dispatcher, tracker, domain):
                    
        print('In Mail Validation')
        mailid = tracker.get_slot('mailid')
        loc = tracker.get_slot('location')
        
        print("Mail id & Location is ->",mailid ,loc)
        flag = 0 
                
        if mailid == None:
            flag = 1           
        else:
                        
            #find_pattern =  '^[a-zA-Z]{1}\w{1,}\.{0,1}\w{1,}@{1}\w{2,}\.{1}[a-zA-Z]{2,}\.{0,1}[a-zA-Z]{0,2}'
            find_pattern = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            search_result = re.search(find_pattern,mailid)
        
            if search_result == None:
                flag = 1
        
        if flag == 1:
            response = "Sorry ,Please enter the valid email id"
            dispatcher.utter_message(response)
            return [SlotSet('mailid',None)]
            
        else:
            return [SlotSet('mailid',mailid)] 



class ActionValidateCity(Action):
    def name(self):
        return 'action_validate_city'
        

    def run(self, dispatcher, tracker, domain):
                    
        print('In Validation')
        loc = tracker.get_slot('location')
        print("Location->",loc)
        flag = 0 
        city_search_result= ""
                
        if loc == None:
            flag = 1           
        else:
            loc = loc.lower()
            file = open("city.txt",'r')
            file_data = file.read()
            file.close()
            city_search_result = re.search(loc,file_data.lower())
            
            
            if city_search_result == None:
                flag = 1
        
        print("==============Results & Flag============")
        print(city_search_result)
        print(flag)
        print("==============Results============")
        if flag == 1:
            response = "Sorry ,We do not operate in that area yet.Can youplease specify some other location"
            dispatcher.utter_message(response)
            return [SlotSet('location',None)]
            
        else:
            return [SlotSet('location',loc)] 


class ActionValidateCuisine(Action):
    def name(self):
        return 'action_validate_cuisine'
        

    def run(self, dispatcher, tracker, domain):
                    
        print('In Validation of cuisine')
        cuisine = tracker.get_slot('cuisine')
        
        print("Cuisine->",cuisine)
        flag = 0 
                
        if cuisine == None:
            flag = 1           
        else:
            
            cuisine_list = ['chinese','mexican','italian','american','south indian','north indian']

            cuisine = cuisine.lower()
            cuisine = cuisine.strip()
            
            flag = 1
            for i in cuisine_list:
                if i == cuisine:
                    flag = 0
                    print("Found cuisine :",cuisine)
                    break
        
        print("==============Results & Flag============")
        if flag == 1:
            print('Not Found cuisine')            
            response = "Sorry ,Please select Cuisine from below list."
            dispatcher.utter_message(response)
            return [SlotSet('cuisine',None)]
           
        else:
            print('Found cuisine')
            return [SlotSet('cuisine',cuisine)] 
        

class ActionValidatePrice(Action):
    def name(self):
        return 'action_validate_price'
        

    def run(self, dispatcher, tracker, domain):
                    
        print('In Validation of price')
        price_cat = tracker.get_slot('price_cat')
        price_txt = tracker.get_slot('price_txt')
        
        print("price_cat->",price_cat)
        print("price_txt->",price_txt)
        
        
        
        
        flag = 0 
        
        if price_cat == None and price_txt != None:
            price_txt =  price_txt.strip()
            find_digit = re.findall('[0-9]{2,}',price_txt)
            if len(find_digit) == 0:
                print("No digits exists in price")
                flag = 1
        
        if price_cat != None and price_txt == None:
            price_cat =  price_cat.strip()
            find_digit = re.findall('[0-9]{2,}',price_cat)
            if len(find_digit) == 0:
                print("No digits exists in price")
                flag = 1
                         
            price_cat_lst = ["Lesser_300","BTW_300_700","More_700"]
            if price_cat not in price_cat_lst:
                flag = 1 
        
        if price_cat == None and price_txt == None:
            print("No price selected both are blanks")
            flag = 1
            
        if price_cat != None and price_txt != None:
            print("Both Price contains value")
            flag = 1
        
                
        print("==============Results & Flag============")
        if flag == 1:
            print('Invalid Price based on above error')            
            response = "Sorry ,Please enter valid price"
            dispatcher.utter_message(response)
            return [SlotSet('price_cat',None),SlotSet('price_txt',None)]
           
        else:
            print('Entered Valid Price')
            if price_cat != None:
                return [SlotSet('price_cat',price_cat),SlotSet('price_txt',"")] 
            else:
                return [SlotSet('price_cat',""),SlotSet('price_txt',price_txt)]
        