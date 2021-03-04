from flask import Flask,request,render_template
#from alphabot import AlphaBot
import logging
import time
app = Flask(__name__)

#bot = AlphaBot()
#bot.stop()

@app.route('/' , methods=['GET' , 'POST'])
def root():

    if request.method == 'POST':
    
        if request.form['btn'] == "1":
            
            while request.form['btn'] != "0":
                print("avanti")
                #bot.forward()
                time.sleep(2)


        elif request.form['btn'] == "-1":
            
            while request.form['btn'] != "0":
                print("indietro")
                #bot.backward()
                time.sleep(2)

        elif request.form['btn'] == "0":
            print("stop")

    return render_template('index.html')




if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)