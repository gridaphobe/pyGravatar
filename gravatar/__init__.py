"""Python module for interacting with Gravatar
"""

from urllib import urlencode
from urllib2 import urlopen
from hashlib import md5
import json

BASE_URL        = 'http://www.gravatar.com/avatar/'
SECURE_BASE_URL = 'https://secure.gravatar.com/avatar/'
PROFILE_URL     = 'http://www.gravatar.com/'
RATINGS         = ['g', 'pg', 'r', 'x']
MAX_SIZE        = 512
MIN_SIZE        = 1
DEFAULTS        = ['404', 'mm', 'identicon', 'monsterid', 'wavatar', 'retro']

class Gravatar(object):
    """Represents a Gravatar user
    """
    
    def __init__(self, email, secure = False, rating = 'g', size = 80,
                 default = None):
        self.email  = email
        self.secure = secure
        self.rating = rating
        self.size   = size
        self.default= default
        self.url    = self.link_to_img()
        self.profile= None
        
    def link_to_img(self):
        """Generates a link to the user's Gravatar"""
        # make sure options are valid
        if self.rating.lower() not in RATINGS:
            raise InvalidRatingError(self.rating)
        if self.size > MAX_SIZE or self.size < MIN_SIZE:
            raise InvalidSizeError(self.size)
        
        url = ''
        if self.secure:
            url = SECURE_BASE_URL
        else:
            url = BASE_URL
        
        url += md5(self.email.strip().lower()).hexdigest()
        options = {'s' : self.size, 'r' : self.rating}
        if self.default is not None:
            options['d'] = self.default
        url += '?' + urlencode(options)
        return url
    
    def get_profile(self):
        """Retrieves the profile data of the user and formats it as a
        Python dictionary.
        """
        url = PROFILE_URL
        url += md5(self.email.strip().lower()).hexdigest()
        url += '.json'
        profile = json.load(urlopen(url))
        # set the profile as an instance variable
        self.profile = profile['entry'][0]
    
    @property
    def user_urls(self):
        """Return a list of user's urls.
        """
        if self.profile is None:
            self.get_profile()
        return self.profile['urls']

class InvalidRatingError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value + " is not a valid gravatar rating"

class InvalidSizeError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value + " is not a valid image size"
