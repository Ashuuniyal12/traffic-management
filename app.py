from flask import Flask, render_template, jsonify,redirect, url_for, request
import json 

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def Login():
  
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        print('user' +username+' password '+password)
        return redirect(url_for('helmet_video'))
    
    return render_template('Auth.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirm-password']

        # print('user {email} password {password} confirm passs {confirmPassword}')

        # users[email] = password
        # with open('details.json', 'w') as jf:
        #     json.dump(users, jf)

        return redirect(url_for('login'))
    
    return render_template('Signup.html')

@app.route('/helmet_compliance', methods=['POST', 'GET'])
def helmet_video():
    if request.method == 'POST':
        uploaded_file = request.files['video_file']

        if uploaded_file:
            # Get the selected file name
            file_name = uploaded_file.filename
            print("Uploaded File Name:", file_name)

            # Get the selected location from the form
            selected_location = request.form.get('location')
            print("Selected Location:", selected_location)

    locations = ['a', 'b', 'c', 'd', 'e']
    return render_template('Helmet.html', location=locations)



@app.route('/signal', methods=['POST', 'GET'])
def signal_video():
    if request.method == 'POST':
        uploaded_file = request.files['video_file']

        if uploaded_file:
            # Get the selected file name
            file_name = uploaded_file.filename
            print("Uploaded File Name:", file_name)

            # Get the selected location from the form
            selected_location = request.form.get('locations')
            print("Selected Location:", selected_location)

    locations = {'a','b','c','d','e'}
    return render_template('Signal.html', location = locations)

@app.route('/cellphone', methods=['POST', 'GET'])
def cellphone_video():
    if request.method == 'POST':
        uploaded_file = request.files['video_file']

        if uploaded_file:
            # Get the selected file name
            file_name = uploaded_file.filename
            print("Uploaded File Name:", file_name)

            # Get the selected location from the form
            selected_location = request.form.get('locations')
            print("Selected Location:", selected_location)

    locations = {'a','b','c','d','e'}
    return render_template('Cellphone.html', location = locations)

@app.route('/alert', methods=['POST', 'GET'])
def alert():    
    return render_template('Alert.html')



@app.route('/analytics', methods=['POST', 'GET'])
def analytics():    
    return render_template('Analytics.html')


@app.route('/email' , methods=['POST','GET'])
def email():
   print("Email alter recieved")



if __name__ == '__main__':
    app.run(debug=True)