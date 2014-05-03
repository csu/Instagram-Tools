# Like all media by a user
# by Christopher Su
# May 3, 2014

from instagram.client import InstagramAPI
import secret

USERNAME = 'christophersu'

access_token = secret.ACCESS_TOKEN
api = InstagramAPI(access_token=access_token)
USER_ID = api.user_search(USERNAME, count=1)[0].id
recent, next = api.user_recent_media(user_id=USER_ID, count=-1)
for cur in recent:
    api.like_media(cur.id)
    print "Liked %s" % cur.link