"""
A simple example script to get all posts on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""
import facebook
import requests
import json

#from pymongo import MongoClient

#from Bundle import Bundle
count = 1
c = 0

#conn = MongoClient('mongodb://172.16.117.5:27017')
#db = conn.opinion_mining
#fb_coll = db.fb_channels

fw = open('fb_post_comment','w')

def writeInMongo_fb(posts):
    global count 
    count = count + 1
    newBundle = Bundle()
    channel_name = posts['from']['name']
    newBundle.data['bundle_id'] = posts['id']
    time = []
    time.append(posts['created_time'])
    time.append(posts['updated_time'])
    newBundle.data['meta']['date'] = time
    #newBundle.data['meta']['channel'] = 'Facebook'
    newBundle.data['meta']['channel'] = channel_name
    newBundle.data['meta']['type'] = posts['type']
    if posts.has_key('message'):
            newBundle.data['text']['content'] = posts['message']
    if posts.has_key('shares'):
            newBundle.data['meta']['shares'] = posts['shares']
    if posts.has_key('description'):
            if posts['type'] == 'video' :
                newBundle.data['video']['content'] = posts['description']
            elif posts['type'] == 'image' :
                newBundle.data['image']['content'] = posts['description']
    if posts.has_key('story'):
        newBundle.data['text']['meta']['tittle'] = posts['story']
    newBundle.data['meta']['author_name'] = posts['from']['name']
    newBundle.data['meta']['author_id'] = posts['from']['id']
    url_list = []
    url_list.append(posts['actions'][0]['link'])
    if posts.has_key('link'):
    	url_list.append(posts['link'])
    newBundle.data['meta']['urls'] = url_list
    if posts.has_key('source'):
            newBundle.data['video']['entities']['source'] = posts['source']
    if posts.has_key('picture'):
            newBundle.data['video']['entities']['keyframe'] = posts['picture']
    #if posts.has_key('message_tags'):
            #m = len(p['message_tags'])
            #mention_list = []
            #for p_m in p['message_tags']['0'] :
                    #mention_list.append(p_m['name'])
            #newBundle.data['text']['entities']['mention'] = posts['message_tags']['0'][0]['name']
    c_out = 0
    if posts.has_key('likes'):
        for d in posts['likes']['data'] :
            c_out = c_out + 1
    #print c_out , posts['id']
    newBundle.data['meta']['favoriteCount'] = c_out
    if posts.has_key('comments'):
    	l = len(posts['comments']['data'])
    	newBundle.data['meta']['count'] = l
    fb_coll.insert_one(newBundle.data)
    #print 'Successfull insertion in FB collection', posts['id']
    l = 0
    if posts.has_key('comments'):
    	l = len(posts['comments']['data'])
    	#newBundle.data['meta']['count'] = l
    	for p in posts['comments']['data'] :
            newBundle = Bundle()
            newBundle.data['bundle_id'] = p['id']
            #print 'has comment' , posts['id'] , p['id']
            newBundle.data['meta']['replyTo'] = posts['id']
            newBundle.data['text']['content'] = p['message']
            newBundle.data['meta']['favoriteCount'] = p['like_count']
            newBundle.data['meta']['date'] = posts['created_time']
            newBundle.data['meta']['author_name'] = p['from']['name']
            newBundle.data['meta']['author_id'] = p['from']['id']
            newBundle.data['meta']['type'] = 'comment'
            newBundle.data['meta']['channel'] = channel_name
            m = 0
            if p.has_key('message_tags'):
            	m = len(p['message_tags'])
            	mention_list = []
            	for p_m in p['message_tags'] :
            		if p_m.has_key('name') :
            			mention_list.append(p_m['name'])
            	newBundle.data['text']['entities']['mention'] = mention_list
            fb_coll.insert_one(newBundle.data)
            print >> fw, 'comment' , posts['id'], '->>>>>>>>>>>' , p['id'],'----------------', m
    
    print >> fw, 'complete post ', posts['id'], '->>>>>', count, l

def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    global count
    count = count+1
    #print post
    f = open('./facebook/'+str(count)+'.json','w')
    json.dump(post,f,indent = 4)
    f.close()


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
def post() :
    access_token ='531517557044774|vnSh1QJqRT7R32J8ZO_apKyn2M0'
    #access_token = 'EAACEdEose0cBAICrZCjVKWx7mZAo0zSpx5ItjsCuokTWe3afbTnXohBWiyGw6QMZBoEdFv8ZA08vvykbjjn7avQcEr0qR7tdQHKhcfCFX8kwpGvqGDwVAeEuGOXZAvZA0ViC21ZChIETM5TlS1YZAHGkmaTkc0tZBUs7br51YD9MGFaYlpMcGpsxPnxm2EIp2bR8ZD'
    # Look at Bill Gates's profile for this example by using his Facebook id.
    user = 'indianarmy.adgpi'
    post_list = []
    fd = open ('page_list', 'w')
    print 'Data collecting from fb'
    graph = facebook.GraphAPI(access_token)
    profile = graph.get_object(user)
    posts = graph.get_connections(profile['id'], 'posts')
    
    for post in posts['data'] :
    		print post
    		writeInMongo_fb(post)
    post_list.append(post)
    print 'First page is completed'
    l = len(posts)
    while True : 
        try: 
            
            print  'Next page exist'
            global c
            try :
            	posts = requests.get(posts['paging']['next']).json()
            except KeyError, e:
            	break
            
            l =  len(posts)
            #print len(posts['data']) 	
            [some_action(post=post) for post in posts['data']]
            for post in posts['data'] :
                #print posts
                some_action(post)
                #writeInMongo_fb(post)
            #for i in xrange(len(posts['data'])):
            	#writeInMongo_fb(posts['data'][i])
            #post_list.append(posts['data'][i])
            print 'old one'
            #print posts
        except KeyError, e:
        	print str(e)
        	pass
            #print str(e), c
            #if str(e) == 'paging' :
            	#c = c +1
            #if c>= 10 :
            	#break
            #else :
            	#pass
        #except Exception, e:
            #print str(e)
            #break
    #return post_list
     
        
    #return posts

# Wrap this block in a while loop so we can keep paginating requests until
# finished.
'''
while True:
    try:
        # Perform some action on each post in the collection we receive from
        # Facebook.
        [some_action(post=post) for post in posts['data']]
        global count
        count += len(posts['data'])
        print count
        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break
'''

post()
