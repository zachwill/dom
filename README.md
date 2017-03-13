dom
===

An easy-to-use command line utility for checking domain name
availability using [Domainr's JSON API](https://market.mashape.com/domainr/domainr V2 API).


![Example of dom in action](http://i.imgur.com/oijaG.png)

Setup requires two things:

1. Installing dom
2. Obtaining an API key


Installation
------------

The simplest method is to install the package through `pip` by running:

    pip install dom

Alternatively, you can install from source:

1. Clone the repo:

    `$ git clone git@github.com:zachwill/dom.git`  
    `$ cd dom`

2. Run the following command to install:
	`python setup.py install`


Get an API key for Domainr
--------------------------

Due to abuse of their API, Domainr now requires an API key for each user. This key can be obtained through one
of the following ways:

1. Get a Mashape Domainr API key from the [Mashape Market](https://market.mashape.com/domainr/domainr)
    **Note:** While it is free up to 10,000 calls/mo., you are required to submit a valid credit card to cover 
    any requests over the free limit.
    * You can use something like [Privacy.com](https://privacy.com/) to create a credit temporary card. I've been told that some banks offer a similar feature as well.
2. Contact Domainr at `partners@domainr.com` to get a personal use client ID, as detailed 
   [here](https://github.com/UltrosBot/Ultros-contrib/issues/29#issuecomment-135285713)

Once you have obtained one of the two types of keys, insert either the Mashape API key or the Client ID into your local environment:
```
$ export DOMAINR_MASHAPE_KEY={your-mashape-key}
```
or
```
$ export DOMAINR_CLIENT_ID={your-client-id}
```

You can do this manually everytime before running dom, or you can search for how to do this on login. Digital Ocean
has an excellent guide here: [How To Read and Set Environmental and Shell Variables on a Linux VPS](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps).

Note that in the event that both keys are present, dom will default to using the Mashape Key.


Optional Flags
--------------

The optional `--ascii` flag can be used to look up domain availability without
the use of the Unicode characters.

```
dom --ascii zachwill

X  zachwill.com
A  zachwill.net
A  zachwill.org
A  zachwill.co
X  za.ch
X  z.ac
```

The `--available` flag only shows domain names that are currently available:

```
dom --available zachwill

✓  zachwill.net
✓  zachwill.org
✓  zachwill.co
✓  zachwill.io
✓  zachwill.me
```

The `--no-suggest` flag only check the exact domain names that are in query:

```
dom --no-suggest zachwill.com

✗  zachwill.com
```

And, the `--tld` flag only shows top-level domains:

```
dom --tld zachwill

✗  zachwill.com
✓  zachwill.net
✓  zachwill.org
```


Deploying
---------

You won't need to worry about this, but since the Python `upload`
command is so obtuse, I'm going to keep it here:

    python setup.py sdist bdist_egg upload
