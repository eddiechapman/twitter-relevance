# Twitter Relevance Review Website

Review article metadata for relevance regarding Twitter research project. 

## Installation

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku

Download Heroku CLI https://devcenter.heroku.com/articles/heroku-cli

```console
(venv) eddie@laptop:~/repos/twitter-relevance$ flask shell
```

```python
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
App: app [production]
Instance: /home/eddie/repos/twitter-relevance/instance
>>> from app import db
>>> db.create_all()
>>> exit()
```

```console
(venv) eddie@laptop:~/repos/twitter-relevance$ flask import-articles --csv_file ~/Downloads/diss.csv 
```

```
(venv) eddie@pearl:~/repos/twitter-relevance$ flask run
 * Serving Flask app 'app.py' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

```
eddie@pearl:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/a5dc6344-c892-4540-9159-2c690eb107b6?requestor=SFMyNTY.g2gDbQAAAAk5Ni4xMS40LjluBgDQ-maHgQFiAAFRgA.qnjFT80dSOjseRp5_3WELftLbjSRIGGpJUnC_ZJsfQo
Logging in... done
Logged in as eddie.chapman4@gmail.com
```