from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters

from DBCm import UseDatabase

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': '*Savitri#_9',
                          'database': 'vsearchlogDB', 'auth_plugin':'mysql_native_password'}


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    """ Returns the filled template of the entry page """
    return render_template('entry.html', the_title='Welcome to search4letters on the web!', the_letters='aeiou')


def log_request(request: 'flash_request', response:str) -> None:
    ''' Logs the changes done by the user into the db '''

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (request.form['phrase'],
                              request.form['letters'],
                              request.remote_addr,
                              request.user_agent.browser,
                              response, ))


@app.route('/viewlog')
def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results
                  from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', 
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)



if __name__ == '__main__':
    app.run(debug=True)

