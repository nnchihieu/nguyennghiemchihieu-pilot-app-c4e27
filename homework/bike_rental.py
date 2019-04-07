from flask import *
from bike_database import Bikes
app = Flask(__name__)

@app.route('/new_bike', methods = ["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template('bike.html')
    elif request.method == "POST":
        form = request.form
        bike_Model = form['input_Model']
        bike_Dailyfee = form['input_Dailyfee']
        bike_Image = form['input_Image']
        bike_Year = form['input_Year']

        print(form)

        new_bike = {
          'Model': bike_Model,
          'Daily fee (VND)': bike_Dailyfee,
          'Image': bike_Image,
          'Year': bike_Year,
        }
        Bikes.insert_one(new_bike)
        return redirect('/new_bike')


if __name__ == '__main__':
  app.run(debug=True)
 