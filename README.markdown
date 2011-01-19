# pyGravatar

This is a Python interface to Gravatar[1]. It is very basic, but hopefully
will be helpful to some people.

[1]: http://en.gravatar.com/

## Installation

Install via pip

	pip install pyGravatar

## Usage

PyGravatar allows you to generate the URL for a gravatar, as well as retrieve
the profile information stored online.

	from gravatar import Gravatar
	g = Gravatar('gridaphobe@gmail.com')
	g.thumb
	
	'http://www.gravatar.com/avatar/16b87da510d278999c892cdbdd55c1b6?s=80&r=g'

## Author

Eric Seidel