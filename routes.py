from flask import Flask, render_template, request, make_response, redirect, url_for, jsonify, flash, send_from_directory, abort
from werkzeug.utils import secure_filename
import mysql.connector as mysql
import hashlib, binascii, peewee
from library.DatabaseConnection import DatabaseConnection
from model.User import User
from controller.UserController import UserController
from base64 import b64encode
import os, peewee, imghdr
# import logging
# logger = logging.getLogger('peewee')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)


app = Flask("Social Games", template_folder="templates", static_folder="", static_url_path="/")
UPLOAD_FOLDER = 'D:/SocialGames/images/profilePicture'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_PATH'] = 'D:/SocialGames/images/profilePicture'
app.secret_key = "super secret key"
app.config['ALLOWED_EXTENSIONS'] = ['jpg', 'png', 'gif', 'jpeg']
userController = UserController()

# naming convention sobkhane projojjo. eikhane ami likhsi loginForm, but eita form na, pura page. so naam thik korte hobe
# input validation sob backend e thakbe, frontend eo.
# jeigula page geenrate kore, sheigula page. baad baki sob-form, shoho ja ase sob components e thake.
# re usbale page gula ektai layout thakbe. conditional statement diye korte hobe. 
# jodi relative import hoy, taile proti ta file tar current directory er baire jabe na. so relative import kora jabe na.
# by default current directory = jei script execute kortesi sheitar directory
# so, relative import er jaygay baire setup.py file rakhte hobe.

# tasks:
# 1. cookie set
# 2. logout
# 3. validation front end, back end
# 4. jegulas page type, shegula pages namok folder e. baad baki sob components folder e.

# plan:
#   1. database set korbo. gameTable. 1st player ke, 2nd player ke. game id, date, time
#   2. moveTable-ke kon move dise
#   3. db hocche communication er way, ke kon move dicche 


# ekta user jokhon authenticate korbe, tokhon welcome screen thakbe. play gamne button e click korle dekhbe kon player er sathe khelbe
# player 2/3 select korbo. jeitai korbo na ken, ekta game table banabe db te. je login korbe she player 1, bakira id hishebe player
# jei id(player) select korbo, game start hobe. je game start 

@app.route('/')
def home():
    # landing page
    return redirect(url_for('apiLoginPage'))


@app.route('/login')
def logIn():
    currentSession = request.cookies.get('currentSession')
    if currentSession is None or userController.validateCurrentSession(currentSession) is False:
        return render_template('user/page-login.html',
                                action = "authenticate", 
                                pageHeader = "Sign In",
                                errorMessage = "",
                                buttonValue = "Sign In",
                                buttonLength = "",
                                buttonId = "loginSubmitButton")
    if userController.validateCurrentSession(currentSession):
        response = redirect(url_for('homePage'))
        return response


@app.route('/user-registration')
def userRegistration():
    return render_template('user/user-registration.html', 
                            action = "validate-registration", 
                            pageHeader = "Register", 
                            userFound = "",
                            buttonValue = "Register",
                            buttonId = "registerUser")


@app.route('/validate-registration', methods = ['POST','GET'])
def registrationSuccessful():
    if request.method == 'POST':
        currentSession = request.cookies.get('currentSession')
        if currentSession is None:
            # return redirect(url_for('logIn'))
            email = request.form['email']
            password = request.form['password']
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            foundUser = userController.findUserByEmail(email)
            if foundUser == "User found":
                return render_template('user/user-registration.html',
                                        action = "validate-registration", 
                                        pageHeader = "Register", 
                                        userFound = "User Found",
                                        buttonValue = "Register")
            elif foundUser == "User Not found":
                userController.createUserFromRegistrationForm(email, password, firstName, lastName)
                return render_template('user/homePage.html',
                                        action="home-page",
                                        pageHeader="Click to Play game",
                                        buttonValue="Play Game")


def setCurrentSession(currentSession, email):
    currentUser = User.get(User.email == email)
    if currentSession == "":
        currentUser.currentSession = ""
        currentUser.save()
    else:
        currentUser.currentSession = currentSession
        currentUser.save()


@app.route('/authenticate', methods = ['POST','GET'])
def authenticate():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if userController.authenticateUser(email, password):
            response = make_response(redirect(url_for('homePage')))
            currentSession = b64encode(os.urandom(20)).decode('utf-8')
            print("The generated session id is: ", currentSession)
            response.set_cookie('email',email)
            response.set_cookie('currentSession',currentSession)
            setCurrentSession(currentSession, email)
            return response
        return render_template('user/page-login.html',
                                action = "authenticate",
                                pageHeader = "Sign in",
                                errorMessage = "Failed to login!",
                                buttonValue = "Submit"
        )


@app.route('/home-page')
def homePage():
    currentSession = request.cookies.get('currentSession')
    userRole = userController.getUserRole(currentSession)
    print(currentSession)
    if currentSession is None:
            return redirect(url_for('apiLoginPage'))
    return render_template('commons/home-page.html',
                            role = userRole)


@app.route('/friends', methods = ['GET'])
def friends():
    currentSession = request.cookies.get('currentSession')
    if currentSession is None:
            return redirect(url_for('logIn'))
    if request.method == 'GET':
        name = request.form.get('friendName')
        currentSession = request.cookies.get('currentSession')
        return render_template('friends/page.html',
                                role = userController.getUserRole(currentSession))


@app.route('/admin')
def adminPanel():
    currentSession = request.cookies.get('currentSession')
    if currentSession is None:
            return redirect(url_for('logIn'))
    amIAdmin = userController.isMyRoleAdmin(currentSession)
    if amIAdmin:
        return render_template('admin/admin.html',
                                role = userController.getUserRole(currentSession))
    return redirect(url_for('homePage'))
                            

@app.route('/get-current-user')
def getCurrentUser():
    currentSession = request.cookies.get('currentSession')
    if currentSession is None:
            return redirect(url_for('logIn'))
    currentUser = userController.getUser(currentSession)
    return currentUser.email


@app.route('/get-friends')
def getFriends():
    email = request.args.get('email')
    currentSession = request.cookies.get('currentSession')
    if currentSession is None:
            return redirect(url_for('logIn'))
    return f"{userController.findUsersWithEmail(email, currentSession)}"


@app.route('/get-pending-requests')
def getPendingRequests():
    currentSession = request.cookies.get('currentSession')
    if currentSession is None:
            return redirect(url_for('logIn'))
    pendingRequests = userController.getPendingRequests(currentSession)
    return f"{pendingRequests}"


@app.route('/get-my-friends')
def getMyFriends():
    currentSession = request.cookies.get('currentSession')
    if currentSession is None:
            return redirect(url_for('logIn'))
    user_id = userController.getUserWithSessionId(currentSession)
    getMyFriends = userController.getMyFriends(user_id)
    return f"{getMyFriends}"


@app.route('/add-friend')
def addFriends():
    currentSession = request.cookies.get('currentSession')
    if currentSession is None:
            return redirect(url_for('logIn'))
    user_id = userController.getUserWithSessionId(currentSession)
    friend_id = request.args.get('friend_id')
    print(user_id, friend_id)
    return f"{userController.addFriend(user_id, friend_id)}"


@app.route('/accept-friend')
def acceptFrienRequest():
    friend_id = request.args.get('friend_id')
    currentSession = request.cookies.get('currentSession')
    if currentSession is None:
        return redirect(url_for('logIn'))
    user_id = userController.getUserWithSessionId(currentSession)
    return f"{userController.acceptFrienRequest(user_id, friend_id)}"


@app.route('/remove-friend')
def removefriends():
    userToBeRemoved = request.args.get('userToBeRemoved')
    currentSession = request.cookies.get('currentSession')
    if currentSession is None:
        return redirect(url_for('logIn'))
    user_id = userController.getUserWithSessionId(currentSession)
    return f"{userController.removefriend(user_id,userToBeRemoved)}"
    

# block-friend
# 1. current user nibo currentSession cookie theke
# 2. args theke friend id nibo
# 3. userController er blockFriend function call korbo with parameter current user id, friend id
# 4. return true
@app.route('/block-friend')
def blockFriend():
    currentSession = request.cookies.get('currentSession')
    if currentSession is None:
        return redirect(url_for('logIn'))
    user_id = userController.getUserWithSessionId(currentSession)
    friend_id = request.args.get('friend_id')
    userController.blockFriend(user_id, friend_id)
    return ""


@app.route('/unblock-friend')
def unblockFriend():
    currentSession = request.cookies.get('currentSession')
    if currentSession is None:
        return redirect(url_for('logIn'))
    user_id = userController.getUserWithSessionId(currentSession)
    friend_id = request.args.get('friend_id')
    userController.unblockFriend(user_id, friend_id)
    return ""


@app.route('/profile')
def profile():
    currentSession = request.cookies.get('currentSession')
    userId = userController.getUserWithSessionId(currentSession)
    try:
        with open(f'images/profilePicture/{userId}.png') as f:
            return render_template('profile/profile.html',
                                    id = userId,
                                    role = userController.getUserRole(currentSession),
                                    buttonValue = 'Change Picture',
                                    onclickAction = 'uploadPicture()',
                                    buttonLength = "w-50",
                                    buttonId = "uploadPictureButton")
    except FileNotFoundError:
        return render_template('profile/profile.html',
                        id = 0,
                        role = userController.getUserRole(currentSession),
                        buttonValue = 'Upload Picture',
                        onclickAction = "uploadPicture()",
                        buttonLength = "w-50",
                        buttonId = "uploadPictureButton")


@app.route('/create-new-game', methods = ['GET','POST'])
def createGame():
    if request.method == 'GET':
        response = []
        print(request.args.get('gameTitle'))
        response.append(request.args.get('gameTitle'))
        response.append(request.args.get('gameCode'))
        response.append(request.args.get('numberOfPlayers'))
        response.append(request.args.get('gameIcon'))
        return f"{response}"


@app.route('/modify-profile')
def modifyProfile():
    password = request.args.get('password')
    firstName = request.args.get('firstName')
    lastName = request.args.get('lastName')
    userController.modifyProfile(request.cookies.get('currentSession'), password, firstName, lastName)
    return ""


@app.route('/upload-picture', methods = ['POST','GET'])
def uploadPicture():
    if request.method == 'POST':
        print("came inside upload pic function")
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'


# /api/login
# 1. input: none
# 2. return: authenticated session and empty error string as dict if authenticated, empty string and customized error message as dict if failed to authenticate
# 3. method:
#   1. jodi request method POST hoy:
#       1. form theke email nibo
#       2. form theke password nibo
#       3. jodi userController er authenticateUser method er return value true hoy:
#           1. currentSession banabo
#           2. db theke user read korbo email diye
#           3. user er currentSession e save korbo currentSession
#           4. return korbo
#               {
#                   'data': currentSession,
#                   'error': null}
#   2. return korbo
#       {
#           'data': "",
#           'error': {
#                       'errorCode' : 'INVALID_CREDENTIALS' -> individual error code for individual error
#                       'errorMessage' : 'The credentials you provided are wrong. Please try again'
#                   }


@app.route('/api/login', methods = ['POST'])
def apiLogin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if userController.authenticateUser(email, password):
            currentSession = str(os.urandom(20))
            user = User.get(User.email == email)
            user.currentSession = currentSession
            return (
                    f"{{"
                        f"'data': {currentSession},"
                        f"'error': ''"
                    f"}}"
                    )
    # return  """{
    #        'data': "",
    #        'error': {
    #                    'errorCode' : 'INVALID_CREDENTIALS',
    #                    'errorMessage' : 'The credentials you provided are wrong. Please try again'
    #                 }
    # }"""
    return "wrong"


@app.route('/login-page')
# apiLoginPage
# input: nothing
# return: nothing
# method:
#   1. 
def apiLoginPage():
    return render_template('user/page-login.html',
                            action = "api/authenticate",
                            pageHeader = "Sign In",
                            errorMessage = "",
                            buttonValue = "Sign In",
                            buttonLength = "",
                            buttonId = "apiLoginSubmitButton")


@app.route('/api/authenticate', methods = ["POST","GET"])
def apiAuthenticate():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        # print(email, password)
        if userController.authenticateUser(email, password):
            currentSession = b64encode(os.urandom(20)).decode('utf-8')
            setCurrentSession(currentSession, email)
            return (
                        f"{{"
                            f'"data": "{currentSession}",'
                            f'"error": ""'
                        f"}}"
                    )
        return (
                    f"{{"
                        f'"data": "",'
                        f'"error":' 
                                f'{{'
                                    f'"errorCode": "INVALID_CREDRENTIALS",'
                                    f'"errorMessage": "Please insert right credentials!"'
                                f'}}'
                    f"}}"
                )


@app.route('/api/validate-cookie', methods = ['POST'])
def validateCookie():
    if request.method == 'POST':
        currentSession = request.form.get('currentSession')
        if userController.validateCurrentSession(currentSession) is False:
            return (
                f"{{"
                    f'"data": false,'
                    f'"error": ""'
                f"}}"
            )
        return (
            f"{{"
                    f'"data": true,'
                    f'"error": ""'
            f"}}"
        )


@app.route('/api/set-cookie-in-database', methods = ['POST'])
def setCookieInDatabase():
    if request.method == 'POST':
        currentSession = request.form.get('currentSession')
        print("cookie is: ",currentSession)
        return "Set cookie in db"


@app.route('/api/forward', methods = ['POST'])
def forward():
    if request.method == 'POST':
        if request.form.get('directTo') == 'login':
            return redirect(url_for('logIn'))
        return redirect(url_for('homePage'))


@app.route('/get-email')
def getEmail():
    try:
        user = User.get(User.currentSession == request.cookies.get('currentSession'))
        print(user)
        return user.email
    except peewee.DoesNotExist:
        return ""


@app.route('/logout')
def logOut():
    currentSession = request.cookies.get('currentSession')
    if userController.logOut(currentSession):
        response = make_response(redirect(url_for('apiLoginPage')))
        response.set_cookie('email', expires=0)
        response.set_cookie('currentSession', expires=0)
        response.set_cookie('expires', expires=0)
        return response


@app.route('/get-request-header')
def getRequestHeader():
    authorizationToken = request.headers.get('Authorization')
    return authorizationToken


@app.route('/upload-game-icon')
def uploadGameIcon():
    return render_template('games/upload-game-icon.html')


def allowed_image(filename):
    if not "." in filename:
        return False
    fileExtension = filename.rsplit(".",1)[1]
    if fileExtension.lower() not in app.config['ALLOWED_EXTENSIONS']:
        return False
    return True
    

@app.route('/save-game-icon', methods = ['POST'])
def saveGameIcon():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('uploadGameIcon'))
        if file and allowed_image(file.filename):
            filename = secure_filename(file.filename)
            print("file name is: ",filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('showGameIcon',
                                    filename=filename))
        return redirect(url_for('uploadGameIcon'))


@app.route('/show-game-icon/<filename>')
def showGameIcon(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
                               

if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug=True)


# social games naam er ekta app, user registration, authenticate korbe, onno user er naam/id diye search korbe
# friend request pathabe, oi friend accept korle friend hishebe joma hobe
# eibar, template folder e sob file eksathe rakha jabe na, feature onujayi folder vaag korbo
# jemon, login/registration/account settings-user naam er folder e thakbe, user related sobkjisu ek folder e thakbe
# jei partgula common-header, footer-arekta footer naam hobe commons
# 1. user search korbe kivabe? friend list ekta page thabe-myaccount er niche ekta page thakbe myfriendlist, shuru te blank thakbe
# bootstrap theke layout nibo, kono user list dekhano jabe na. search korte hobe. name/id diye search kora jabe
# arekta part thakbe: invite by email. she system e nai, invite korbe email e
# so, jokhon search korbe, backend e function thakbe jeita db theke search korbe: searchByNameOrEmail, so duitai search korte parbe
# naam ta substring hoileo hobe. ajax/jquery diye ashte hobe, kono page reload hobe na.
# list of user pabo. sheita user ke show korbo ajax diye, page reload hobe na
# temporary div e search result show korbo. she jeita select korbe, sheita ke friend req pathabo
# pathaile-table lagbe, userId, friendId naam e field thakbe, status-requested/accepted/rejected naam e value thakbe

# jokhon amra ekta link visit kori, oita ekta get request, ta pic hok css js hok sob e get. sob e http protocol e, data read kortesi so get
# server e data pathacchi na, jodio url er part hishebe kichu query pathano jaay


# sobgula page er aage ami ekta kore prefix lagabo, e.g.-loginform er jaygay ami likhsi page-login karon oita loginForm na.
# so, sobkhetrei tai korbo, shudhu page-xxx likhbo. form er khetre form-xxx likhbo. jeigula form o na page o na oigula block-xxx/ section-xxx
# client server architecture e, client jane na DB bole kisu ase kina. client request POST korbe, server response pathabe, client oita GET kore

# server e request korte hoile 3 ta jinish laage: 
# 1. url, kothay request korbe
# 2. method: kisu bola na thakle default GET. GET hoile data post kora jaay na. POSt hoile body te pathay. request er 2 ta part: hearder and body/
# POST hoile Body te pathay
# 3. Data: name value pairs
# 
# ajker task:
# notes review kore bujhaite hobe done() kiavbe kaaj kortese step by step. ready and onclick er way te done() kivabe kaaj kore bujhaite hobe
#  ei ajax diye sample request. server e friend name pathabo, oi url simple ekta value return korbe: "got the name"