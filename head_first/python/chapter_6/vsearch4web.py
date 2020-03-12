
from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters

app = Flask(__name__)

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
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
    return render_template('entry.html',
                           the_title='Welcome to search4letters on \
                           the web!',
                           the_letters='aeiou')

def log_request(request: 'flash_request', response:str) -> None:
  with open('vsearch.log', 'a') as log:
    print(request.form, request.remote_addr, request.user_agent, response, file=log, sep='|')

@app.route('/viewlog')
def view_the_log() -> 'html':
  contents = []
  with open('vsearch.log') as log:
    for line in log:
      contents.append([])
      for item in line.split('|'):
        contents[-1].append(escape(item))
  titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
  return render_template('viewlog.html', 
                          the_title='View Log',
                          the_row_titles=titles,
                          the_data=contents,)

if __name__ == '__main__':
    app.run(debug=True)

