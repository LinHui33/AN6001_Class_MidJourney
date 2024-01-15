#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,request,render_template
import os
import requests
import json
import time


# In[ ]:


app = Flask(__name__)
os.environ["REPLICATE_API_TOKEN"] = "r8_SDFDlj2RkuATyk93dpn47zVT8PYGNYd3WE1wp"


# In[ ]:


@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        qn = request.form.get('qn')
        body = json.dumps({"version": "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf", "input": { "prompt": qn } })
        headers = {'Authorization': 'Token r8_SDFDlj2RkuATyk93dpn47zVT8PYGNYd3WE1wp','Content-Type': 'application/json'}
        output = requests.post('https://api.replicate.com/v1/predictions',data=body,headers=headers)
        time.sleep(10)
        get_url = output.json()['urls']['get']
        print(get_url)
        get_result = requests.post(get_url,headers=headers).json()['output']
        print(get_result)
        return render_template("index.html", result = get_result[0])
    else:
        return render_template("index.html", result = "Waiting for Question.............")


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




