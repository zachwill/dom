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
