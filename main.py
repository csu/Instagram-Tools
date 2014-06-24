from instagram.client import InstagramAPI
import secret

from nonmutual_followers import NonmutualFollowers

def main():

    access_token = secret.ACCESS_TOKEN
    api = InstagramAPI(access_token=access_token)

    username = "christophersu"
    me = api.user_search(username, count=1)[0].id

    # run whatever you want
    print NonmutualFollowers(api).find(me)

if __name__ == "__main__":
    main()