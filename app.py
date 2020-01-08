from flask import Flask, render_template, request
from develop.summain import runprog, blog_to_sum
from develop.data import data

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])

def hello_world():
    if request.method == 'POST':
        return render_template("blogtosum.html")
    else:
        values =runprog()
        dat = data()
        return render_template("analysis.html", data = dat, values = values)


@app.route('/summary',methods = ['POST', 'GET'])
def summary():
    if request.method == 'POST':
        tech = request.form['tech']
        blog = request.form['topic']
        x = blog_to_sum(tech,blog)
        # res = []
        # for i in range(len(x)):
        #     res.append(x[i])
        #
        # print(res)
        return render_template("summary.html", summary= x)


if __name__ == '__main__':
    app.run()
