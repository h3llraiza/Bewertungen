from flask import Flask, request, render_template, redirect, url_for
from utils import verify_user, get_reviews_for_landlord, save_review

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bewerten', methods=['GET', 'POST'])
def bewerten():
    if request.method == 'POST':
        email = request.form['email']
        nachweis = request.files.get('nachweis')
        landlord = request.form['landlord']
        rating = request.form['rating']
        comment = request.form['comment']

        if verify_user(email, nachweis):
            save_review(email, landlord, rating, comment)
            return redirect(url_for('home'))
        else:
            return "Verifizierung fehlgeschlagen", 400

    return render_template('bewerten.html')

@app.route('/bewertungen', methods=['GET'])
def bewertungen():
    landlord = request.args.get('landlord')
    results = get_reviews_for_landlord(landlord)
    return render_template('bewertungen.html', landlord=landlord, reviews=results)

if __name__ == '__main__':
    app.run(debug=True)
