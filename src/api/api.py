from itertools import count
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, Length


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
bootstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    username = StringField('Full Names', validators=[InputRequired(), Length(min=4, max=15)])
    password = StringField('Zip code', validators=[InputRequired(), Length(max=80)])

@app.route('/create_phrase', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        sentence = form.username.data
        passcode = int(form.password.data)
        words = sentence.split()

        states = [
            ["Alabama:35004,36925"],
            ["Alaska:99501,99950"],
            ["Arizona:85001,86556"],
            ["Arkansas:71601,72959"],
            ["California:90001,96162"],
            ["Colorado:80001,81658"],
            ["Connecticut:06001,06928"],
            ["Delaware:19701,19980"],
            ["Florida:32003,34997"],
            ["Georgia:30002,39901"],
            ["Hawaii:96701,96898"],
            ["Idaho:83201,83877"],
            ["Illinois:60001,62999"],
            ["Indiana:46001,47997"],
            ["Iowa:50001,52809"],
            ["Kansas:66002,67954"],
            ["Kentucky:40003,42788"],
            ["Louisiana:70001,71497"],
            ["Maine:03901,04992"],
            ["Maryland:20588,21930"],
            ["Massachusetts:01001,05544"],
            ["Michigan:48001,49971"],
            ["Minnesota:55001,56763"],
            ["Mississippi:38601,39776"],
            ["Missouri:63001,65899"],
            ["Montana:59001,59937"],
            ["Nebraska:68001,69367"],
            ["Nevada:88901,89883"],
            ["New Hampshire:03031,03897"],
            ["New Jersey:07001,08989"],
            ["New Mexico:87001,88439"],
            ["New York:00501,14925"],
            ["North Crolina:27006,28909"],
            ["North Dakota:58001,58856"],
            ["Ohio:43001,45999"],
            ["Oklahoma:73001,74966"],
            ["Oregon:97001,97920"],
            ["Pennsylvania:15001,19640"],
            ["Rhode Island:02801,02940"],
            ["South Carolina:29001,29945"],
            ["South Dakota:57001,57799"],
            ["Tennessee:37010,38589"],
            ["Texas:73301,88595"],
            ["Utah:84001,84791"],
            ["Vermont:05001,05907"],
            ["Virginia:20101,24658"],
            ["Washington:98001,99403"],
            ["West Virginia:24701,26886"],
            ["Wisconsin:53001,54990"],
            ["Wyoming:82001,83414"]
        ]

        for i, word in enumerate(words):
            
            '''
            if first letter is a vowel
            '''
            if word[0] in 'aeiouAEIOU':
                words[i] = words[i]+ "ay"
            else:
                '''
                else get vowel position and postfix all the consonants 
                present before that vowel to the end of the word along with "ay"
                '''
                has_vowel = False
                
                for j, letter in enumerate(word):
                    if letter in 'aeiou':
                        words[i] = word[j:] + word[:j] + "ay"
                        has_vowel = True
                        break

                #if the word doesn't have any vowel then simply postfix "ay"
                if(has_vowel == False):
                    words[i] = words[i]+ "ay"
        pig_latin = ''
        for i in range(len(words)):
            if (i == 0):
                pig_latin+=words[i].capitalize()
            else:
                pig_latin+=' '+words[i].lower()
        #if name.startswith('a') | name.startswith('e') | name.startswith('a')
        for i in states:
            county_z = i[0].split(':')
            zip_c = county_z[1].split(',')
            zip1 = int(zip_c[0])
            zip2 = int(zip_c[1])

            if zip1 <= passcode and passcode <= zip2:
                state = county_z[0]
                break
        county =''
        popu=''
        strpass=str(form.password.data)
        with open('Scripts/{}.txt'.format(state),'r') as file:
            lines = file.read().split('\n')

            for line in range(len(lines)):
                if (lines[line].strip()) == strpass:
                    county = lines[line+1]

        
        with open('Scripts/co_est2020.txt') as file:
            lines = file.readlines()
            
            for line in range(len(lines)):
                line_  =lines[line].split(',')

                if (line_[6] == county and line_[5]==state):
                    popu = line_[-1]
        
        return '<h2>'+pig_latin+"'s zip code is in "+county+' and has a population of '+popu+'</h2>'

    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

