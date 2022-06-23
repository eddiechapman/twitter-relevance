# Twitter Review Website

> Review article metadata for relevance regarding Twitter research project. 

Application built with Flask and Bootstrap5 and deployed with Heroku.

## Installation

Clone repository

```
$ git clone https://github.com/eddiechapman/twitter-relevance.git
```

Enter the project directory and create and activate a Python virtual environment

```
$ cd twitter-relevance
$ python3 -m venv venv
$ source venv/bin/activate
```

Install required Python packages

```
(venv) $ pip install -r requirements.txt
```

## Development

You can run the website on your laptop for testing purposes with `flask run`. 

You'll need to be in the project directory with the Python virtual environement active.

```
(venv) $ flask run
 * Serving Flask app 'main.py' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 821-654-522
```

Navigate to http://127.0.0.1:5000 in your web browser and you should see the website.


## Deployment

If you want others to use the website, you have to deploy it to production. 

I followed instructions in Miguel Grinberg's [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku) for deploying a Flask app with Heroku. 

You'll need to make a free [Heroku](https://www.heroku.com/) account and download the [Heroku CLI app](https://devcenter.heroku.com/articles/heroku-cli).

### Environment Variables

Deploying the app through Heroku requires you to set a few environment variables using the Heroku dashboard.

Go to **Settings** and click **Reveal Config Vars**.

There should already be a variable for `DATABASE_URL`, if you followed the steps in the Flask Mega Tutorial for provisioning a database.

Beneath that, add a key called `FLASK_ENV` with a value of `production`.

Go back to the terminal and run 

```python
$ python3

>>> import secrets
>>> secrets.token_hex(16)
'8f42a73054b1749f8f58848be5e6502c'
```

Copy the long string of numbers and letters from the final command. Back in the Heroku dashboard, add another config variable called `SECRET_KEY` and paste that long string as the value. 

