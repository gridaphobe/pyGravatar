"""
Python module for interacting with Gravatar.
"""
__author__  = 'Eric Seidel'
__version__ = '0.0.1'
__email__   = 'gridaphobe@gmail.com'

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
    """
    Represents a Gravatar user.
    """
    
    def __init__(self, email, secure = False, rating = 'g', size = 80,
                 default = None):
        self._email_hash = md5(email.strip().lower()).hexdigest()
        self.secure     = secure
        self.rating     = rating
        self.size       = size
        self.default    = default
        self.thumb      = self.link_to_img()
        self.profile    = None
    
    def link_to_img(self):
        """
        Generates a link to the user's Gravatar.
        """
        # make sure options are valid
        if self.rating.lower() not in RATINGS:
            raise InvalidRatingError(self.rating)
        if not (MIN_SIZE <= self.size <= MAX_SIZE):
            raise InvalidSizeError(self.size)
        
        url = ''
        if self.secure:
            url = SECURE_BASE_URL
        else:
            url = BASE_URL

        options = {'s' : self.size, 'r' : self.rating}
        if self.default is not None:
            options['d'] = self.default
        url += self.hash + '?' + urlencode(options)
        return url
    
    def get_profile(self):
        """
        Retrieves the profile data of the user and formats it as a
        Python dictionary.
        """
        url = PROFILE_URL + self.hash + '.json'
        profile = json.load(urlopen(url))
        # set the profile as an instance variable
        self.profile = profile['entry'][0]
    
    @property
    def hash(self):
        """
        Return email hash.
        """
        return self._email_hash

    @property
    def urls(self):
        """
        Return a list of user's urls.
        """
        if self.profile is None:
            self.get_profile()
        return self.profile['urls']
    
    @property
    def accounts(self):
        """
        Return a list of user's linked accounts.
        """
        if self.profile is None:
            self.get_profile()
        return self.profile['accounts']
    
    @property
    def verified_accounts(self):
        """
        Return a list of user's verified accounts.
        """
        return [a for a in self.accounts if a['verified'] == 'true']
    
    @property
    def ims(self):
        """
        Return a list of user's IM accounts.
        """
        if self.profile is None:
            self.get_profile()
        return self.profile['accounts']
    
    @property
    def photos(self):
        """
        Return a list of user's photos.
        """
        if self.profile is None:
            self.get_profile()
        return self.profile['photos']
    
    @property
    def emails(self):
        """
        Return a list of user's emails.
        """
        if self.profile is None:
            self.get_profile()
        return self.profile['emails']


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
