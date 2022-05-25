from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from sqlalchemy import null
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name: ')
    last_name = StringField('Last Name: ')
    d_o_b = DateField('Date of Birth: ')
    fav_num = IntegerField('Favourite Number: ')
    fav_food = SelectField('Favourite Food: ', choices=[
        ('pizza', 'Pizza'), ('spaghetti', 'Spaghetti'),
        ('chilli', 'Chilli'), ('ramen', 'Ramen'),
        ('steak', 'Steak')
        ])
    submit = SubmitField('Add Name')
    
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    username = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        d_o_b = form.d_o_b.data
        fav_num = form.fav_num.data
        fav_food = form.fav_food.data

        if len(first_name) == 0 or len(last_name) == 0 or d_o_b == null or fav_num == 0 or len(fav_food) == 0:
            message = "Please supply all information"
            
        else:
            message = f'Thank you, {first_name} {last_name}'
            username = f'Username: {fav_food}{first_name}{fav_num}'
            
    return render_template('home.html', form=form, message=message, username=username)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')
     
    