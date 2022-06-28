from flask import Flask, render_template, request
import util

app = Flask(__name__)
@app.route("/", methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def main_page():
    loc = util.get_location_names()
    if request.method == "POST":       
        bhk = request.form.get('bhk')
        bath = request.form.get('bath') 
        total_sqft = request.form.get("sqft")
        location = request.form.get("location")
        print(total_sqft, bhk, bath, location)
        price_predicted = util.get_estimated_price(location, total_sqft, bhk, bath)
        return render_template("base.html",loc=loc, price_predicted=price_predicted)   
    
    return render_template("base.html",loc=loc)  

if __name__ == '__main__':
    app.run(debug = True)
    