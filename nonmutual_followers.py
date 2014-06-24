# Find out which of the people you follow don't follow you back

class NonmutualFollowers:
    def find(self, user_id):
        user_follows = []
        user_followed_by = []

        uf, next = self.api.user_follows(user_id)
        for u in uf:
            # print "adding " + u.username
            user_follows.append(u.username)
        while next:
            uf, next = self.api.user_follows(user_id)
            for u in uf:
                # print "adding " + u.username
                user_follows.append(u.username)

        # could be more efficient by just checking if they're in the other array here
        ufb, next = self.api.user_followed_by(user_id)
        for u in uf:
            # print "adding " + u.username
            user_followed_by.append(u.username)
        while next:
            ufb, next = self.api.user_followed_by(user_id)
            for u in ufb:
                # print "adding " + u.username
                user_followed_by.append(u.username)

        return [user for user in user_follows if user not in user_followed_by]

    def __init__(self, api):
        self.api = api