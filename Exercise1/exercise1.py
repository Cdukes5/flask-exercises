from flask import Flask, render_template
import datetime
import calendar
import pytz
    
app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.datetime.now(pytz.timezone('US/Eastern'))

    ctime = current_time.strftime("%B %d %Y %H:%M:%S")

    return render_template('index.html', ctime = calendar.day_name[current_time.weekday()] + ', ' +ctime)

if __name__ == "__main__":
    app.run(debug=True)