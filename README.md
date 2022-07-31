![License](https://badgen.net/github/license/otc-cirdan/gw2pc)
![Last Commit](https://badgen.net/github/last-commit/otc-cirdan/gw2pc)
[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=otc-cirdan/gw2pc)](https://dependabot.com)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/otc-cirdan/gw2pc.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/otc-cirdan/gw2pc/alerts/)

# Guild Wars 2 Price Check
Live price checks for Guild Wars 2 trading

# Synopsis
This is the code for [gw2pc.com](https://gw2pc.com), a website which uses the
Guild Wars 2 API to calculate prices for items that are commonly traded between
players. It is created and hosted by Cirdan for use on the
[Overflow](https://discord.gg/7tWwz499rX) Discord server, but is free to use
by anyone who needs it.

# Contributing
Contributions are welcome. The website is written using the Django web
framework, with Material used for styling. Use the `rebuild_venv.sh` script to
install the Python dependencies, and `npm install` to populate `node_modules`
with the required CSS and JS dependencies. You can now run `manage.py runserver`
to start a local webserver. You may need to modify `gw2pc/local_settings.py`, in
particular, the `ALLOWED_HOSTS` variable.

The live website is hosted using Zappa on Amazon AWS serverless. Essentially, a
Cloudfront instance handles caching and serving static files from an S3 bucket,
while dynamic webpages are provided by calling a Lambda function. This is all
configured by calling something like `zappa deploy prod`, provided that you have
AWS credentials, and the scripts used to update these are present in the
repository.

Note that it is currently required to call `sass` manually as shown in the
update scripts, Django's `sass_processor` does not work due to some unsupported
fork of the `sass` binary which does not support modern features. If you update
CSS in `static/css/style.scss`, you will need to call the command shown in that
update script in order to update the CSS file.

## Setup
### Dependencies
* Python 3.8+
* Pipenv
* Yarn/Npm

### Initialize python environment
```bash
pipenv --python 3.8
pipenv shell
```

If hitting problems with python install you might be missing the following:

Linux:

```bash
sudo apt install python3-dev
```

Windows:

https://visualstudio.microsoft.com/visual-cpp-build-tools/


### Running
```bash
make install
make build
make run
curl 127.0.0.1:8000
```

# TODO
* The current `views.py` discourages code reuse. It made sense while just
  outlining the project, but now that we have a few pages, they should be
  refactored and converted to use class-based views.
* The current table rendering code, in which the table layout is done in an
  .html include and the individual cells are rendered using a series of
  templatetages, is quite ugly. Tables should probably just be a Class with a
  method `.render()`.
* The `format_gold_*` set of functions is a bit silly, and deciding whether or
  not to use icons and whether or not to show the coppers should probably be
  handled through arguments.
* Should we actually use gold/silver/copper icons?
* The HTML pages also, to an extent, discourage code reuse. Is there anything
  that can be factored out?
