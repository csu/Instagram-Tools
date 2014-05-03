from instagram.client import InstagramAPI
import secret

access_token = secret.ACCESS_TOKEN
api = InstagramAPI(access_token=access_token)

### Get authenticated user's media
# recent_media, next = api.user_recent_media()
# photos = []
# for media in recent_media:
#     photos.append('<img src="%s"/>' % media.images['thumbnail'].url)
# print photos

### Get media from a specific user
recent, next = api.user_recent_media(userid='christophersu', count=10)
for media in recent:
    print media.images['standard_resolution'].url