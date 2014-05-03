from instagram.client import InstagramAPI
import secret

access_token = secret.ACCESS_TOKEN
api = InstagramAPI(access_token=access_token)

# ## Get authenticated user's media
# recent_media, next = api.user_recent_media()
# photos = []
# for media in recent_media:
#     photos.append('<img src="%s"/>' % media.images['thumbnail'].url)
# print photos

# ## Get media from a specific user
# recent, next = api.user_recent_media(user_id='christophersu', count=10)
# for media in recent:
#     print media.images['standard_resolution'].url
# ## Working like media by id
# api.like_media(recent[0].id)

# ## Get ALL media from a specific user
# USER_ID = api.user_search('christophersu', count=1)[0].id
# recent, next = api.user_recent_media(user_id=USER_ID, count=-1)
# print len(recent)
# print next