import tweepy
import csv
import time

class authentication:

    def __init__(self):
        # Go to http://apps.twitter.com and create an app.
        # The consumer key and secret will be generated for you after
        self.consumer_key =""
        self.consumer_secret=""

        # After the step above, you will be redirected to your app's page.
        # Create an access token under the the "Your access token" section
        self.access_token=""
        self.access_token_secret=""

    def getconsumer_key(self):
        return self.consumer_key
    def getconsumer_secret(self):
        return self.consumer_secret
    def getaccess_token(self):
        return self.access_token
    def getaccess_token_secret(self):
        return self.access_token_secret


class world_armies_data:
    def adgpi(self,api):
        adgpi_results = api.user_timeline("adgpi",count=150,since_id=892271492137799680)
        if len(adgpi_results) > 0:
            with open('/home/chiragsodani/Aditya/adgpi.csv','a',newline='') as f:
                    writer=csv.writer(f)
                    for tweet in adgpi_results[::-1]:
                        writer.writerow([tweet.created_at,tweet.id,tweet.retweet_count,tweet.favorite_count])
    
    def ISPR_Official(self,api):
        ispr_results = api.user_timeline("ISPR_Official",count=150,since_id=877753761015320576)
        if len(ispr_results) > 0:
            with open('/home/chiragsodani/Aditya/ispr.csv','a',newline='') as f:
                writer=csv.writer(f)
                for tweet in ispr_results[::-1]:
                    writer.writerow([tweet.created_at,tweet.id,tweet.retweet_count,tweet.favorite_count])
    
    def USArmy(self,api):
        usarmy_results = api.user_timeline("USArmy",count=150,since_id=892175582456414208)
        if len(usarmy_results) > 0:
            with open('/home/chiragsodani/Aditya/us.csv','a',newline='') as f:
                writer=csv.writer(f)
                for tweet in usarmy_results[::-1]:
                    writer.writerow([tweet.created_at,tweet.id,tweet.retweet_count,tweet.favorite_count])
    
    def BritishArmy(self,api):
        britisharmy_results = api.user_timeline("BritishArmy",count=150,since_id=892067352841396224)
        if len(britisharmy_results) > 0:
            with open('/home/chiragsodani/Aditya/british.csv','a',newline='') as f:
                writer=csv.writer(f)
                for tweet in britisharmy_results[::-1]:
                    writer.writerow([tweet.created_at,tweet.id,tweet.retweet_count,tweet.favorite_count])
    
    def AustralianArmy(self,api):
        australianarmy_results = api.user_timeline("AustralianArmy",count=150,since_id=892160106476863488)
        if len(australianarmy_results) > 0:
            with open('/home/chiragsodani/Aditya/australian.csv','a',newline='') as f:
                writer=csv.writer(f)
                for tweet in australianarmy_results[::-1]:
                    writer.writerow([tweet.created_at,tweet.id,tweet.retweet_count,tweet.favorite_count])
    
    def mod_russia(self,api):
        russia_results = api.user_timeline("mod_russia",count=150,since_id=892089999113334784)
        if len(russia_results) > 0:
            with open('/home/chiragsodani/Aditya/russia.csv','a',newline='') as f:
                writer=csv.writer(f)
                for tweet in russia_results[::-1]:
                    writer.writerow([tweet.created_at,tweet.id,tweet.retweet_count,tweet.favorite_count])
    
    def armeedeterre(self,api):
        france_results = api.user_timeline("armeedeterre",count=150,since_id=890933679807234048)
        if len(france_results) > 0:
            with open('/home/chiragsodani/Aditya/france.csv','a',newline='') as f:
                writer=csv.writer(f)
                for tweet in france_results[::-1]:
                    writer.writerow([tweet.created_at,tweet.id,tweet.retweet_count,tweet.favorite_count])

if __name__ == '__main__':

    # Get access and key from another class
    auth = authentication()
    
    # Get data
    data = world_armies_data()
    
    # Authentication
    consumer_key = auth.getconsumer_key()
    consumer_secret = auth.getconsumer_secret()
    access_token = auth.getaccess_token()
    access_token_secret = auth.getaccess_token_secret()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    data.adgpi(api)
    data.ISPR_Official(api)
    data.USArmy(api)
    data.BritishArmy(api)
    data.AustralianArmy(api)
    data.mod_russia(api)
    data.armeedeterre(api)
    #count = count + 1
    #print(count)
    #time.sleep(900)
