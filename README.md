dom
===
[![Build Status](https://secure.travis-ci.org/myusuf3/dom.png?branch=master)](http://travis-ci.org/myusuf3/dom)

An easy-to-use command line utility for checking domain name
availability using [Domainr's JSON API](http://domai.nr/api/docs/json).

![](http://i.imgur.com/oijaG.png)


Installation
------------

If you want to use the package through `pip`, simply run:

    pip install dom

Or, if you'd prefer to clone the repo, run the following command:

    git clone git@github.com:zachwill/dom.git
    cd dom
    python setup.py install


Deploying
---------

You won't need to worry about this, but since the Python `upload`
command is so obtuse, I'm going to keep it here:

    python setup.py sdist bdist_egg upload
