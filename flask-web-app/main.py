from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)


'''
{%...%} loops
{}      print
{#...#} comments
'''

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score <= 50:
        res = 'PASS'
    else:
        res = 'FAIL'
    exp = {'score': score, 'res': res}
    return render_template('results.html', result=exp)


@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed and the marks is '+str(score)


@app.route('/results/<int:marks>')
def results(marks):
    result = ''
    if marks < 45:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))


@app.route('/submit', methods=['GET','POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        total_score += float(request.form['science']) + float(request.form['maths']) + \
                       float(request.form['c']) + float(request.form['datascience'])
        total_score /= 4
        if total_score >= 50:
            res = 'success'
        else:
            res = 'fail'
        return redirect(url_for(res, score=total_score))



if __name__ == '__main__':
    app.run(debug=True)
