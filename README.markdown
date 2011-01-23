# pyGravatar

This is a Python interface to [Gravatar][1]. It is very basic, but hopefully
will be helpful to some people.

[1]: http://en.gravatar.com/

## Installation

Install via pip

	pip install pyGravatar

## Usage

PyGravatar allows you to generate the URL for a gravatar, as well as retrieve
the profile information stored online.

	>>> from gravatar import Gravatar
	>>> g = Gravatar('gridaphobe@gmail.com')
	>>> g.thumb
	'http://www.gravatar.com/avatar/16b87da510d278999c892cdbdd55c1b6?s=80&r=g'

	>>> g.profile
	{ long python dict of my info :) }

	>>> g.emails
	[{u'primary': u'true', u'value': u'gridaphobe@gmail.com'}]

You can also request a different size/rating thumbnail, use SSL, and change
the default thumb for emails that aren't registered.

	>>> g.size = 512 # the largest accepted
	>>> g.rating = 'x'
	>>> g.secure = True
	>>> g.thumb
	'https://secure.gravatar.com/avatar/16b87da510d278999c892cdbdd55c1b6?s=512&r=x'

Or you can pack it all nicely into one line

	>>> Gravatar('gridaphobe@gmail.com', secure=True, size=512, rating='x').thumb
	'https://secure.gravatar.com/avatar/16b87da510d278999c892cdbdd55c1b6?s=512&r=x'

## Author

Eric Seidel