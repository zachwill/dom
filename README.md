dom
===

An easy-to-use command line utility for checking domain name
availability using [Domainr's JSON API v1](https://domainr.readme.io/v1.0/docs).

![](http://i.imgur.com/oijaG.png)

Installation
------------

Previously, you could install and use the package through `pip` by simply running:

    pip install dom

At the moment, it will throw a KeyError because the API is deprecated and doesn't handle the return value correctly. To use an updated version, perform the following steps:

1. Clone the repo:

    `$ git clone git@github.com:zachwill/dom.git`  
    `$ cd dom`

2. Do one of the following:
    
    a. Get a Mashape Domainr API key from [here](https://market.mashape.com/domainr/domainr)
    **Note:** While it is free up to 10,000 calls/mo., you are required to submit a valid credit card to cover 
    any requests over the free limit.

    b. Contact Domainr at `partners@domainr.com` to get a personal use client ID, as detailed [here](https://github.com/UltrosBot/Ultros-contrib/issues/29#issuecomment-135285713)

4. Insert either the Mashape API key or the Client ID into the `domainr/domainr.ini` file as documented in the file comments.

5. Run the following command to install:
	`python setup.py install`

6. To avoid accidentally publishing your API key, you can also perform the following command:
	`git update-index --assume-unchanged domainr/domainr.ini`
This will tell git to not expect any changes on your end and to ignore it when pushing changes.


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
