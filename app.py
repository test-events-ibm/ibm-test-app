from flask import Flask, render_template,request, jsonify
import json

app = Flask(__name__)


@app.route('/',methods = ['POST'])
def hello():
    # if request.method=='POST':
    data = json.loads(str(request.data, encoding='utf-8'))
    print(data)
    jobj = json.dumps(data,indent=4)
    with open('data.json','w') as newf:
        newf.write(jobj)
    return render_template('update.html')

if __name__ == '__main__':
    app.run(debug=True)