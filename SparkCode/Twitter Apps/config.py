
class Twitter:
    def __init__(self):
        self.CONSUMER_KEY = None
        self.CONSUMER_SECRET = None
        self.ACCESS_TOKEN = None
        self.ACCESS_SECRET = None

    def get_conf(self):
        self.CONSUMER_KEY, self.CONSUMER_SECRET, self.ACCESS_TOKEN, self.ACCESS_SECRET = (str(x.split(':')[1]).strip() for x in open(
            '/Users/vikas/vikas/Twitter.txt').readlines())
        return self.CONSUMER_KEY, self.CONSUMER_SECRET, self.ACCESS_TOKEN, self.ACCESS_SECRET
