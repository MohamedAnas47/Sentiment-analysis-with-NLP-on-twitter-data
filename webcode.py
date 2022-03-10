from flask import *
import pymysql
app=Flask(__name__)
con=pymysql.connect(host="localhost",user="root",passwd="",port=3306,db="sentiment_analysis")
cmd=con.cursor()
app.secret_key="ab"
# @app.route('/')
# def start():
#     return render_template("index.html")
@app.route('/')
def log():
    return render_template("loginpage.html")

@app.route('/login',methods=['get','post'])
def login():
    username=request.form['textfield']
    password=request.form['textfield2']
    cmd.execute("select * from login where username='"+username+"' and password='"+password+"'")
    s=cmd.fetchone()
    if s is None:
        return '''<script>alert("invalid password");window.location="/"</script>'''
    elif s[3]=="admin":
        return '''<script>alert("success");window.location="/homepage"</script>'''
    elif s[3]=="user":
        session['lid']=s[0]
        return '''<script>alert("success");window.location="/user_homepage"</script>'''
    else:
        return '''<script>alert("failed");window.location="/"</script>'''




@app.route('/homepage')
def homepage():
    return render_template("homepage.html")
@app.route('/view_user')
def view_user():
    cmd.execute("SELECT `view user`.*,`login`.* FROM `login` JOIN `view user` ON `view user`.`Login_id`=`login`.`Id` ")
    s=cmd.fetchall()
    return render_template("view user.html",val=s)
@app.route('/logout',methods=['post'])
def logout():
    return render_template("loginpage.html")
@app.route('/feedback')
def feedback():
    cmd.execute("SELECT `feedback`.*,`view user`.`Username` FROM `feedback` JOIN `view user` ON `feedback`.`user_id`=`view user`.`Login_id`")
    s=cmd.fetchall()
    return render_template("feedback.html",val=s)
@app.route('/Registration')
def Registration():
    return render_template("Registration.html")
@app.route('/Registration1',methods=['post'])
def Registration1():
    Username=request.form['textfield']
    Housename=request.form['textfield2']
    Place=request.form['textfield3']
    Post=request.form['textfield4']
    Pin=request.form['textfield5']
    Mob_Number=request.form['textfield6']
    Email_id=request.form['textfield7']
    Username=request.form['textfield8']
    Password=request.form['textfield9']
    cmd.execute("insert into login values(null,'"+Username+"','"+Password+"','user')")
    id=con.insert_id()
    cmd.execute("insert into `view user` values(null,'"+Username+"','"+Housename+"','"+Place+"','"+Post+"','"+Pin+"','"+Mob_Number+"','"+Email_id+"','"+str(id)+"')")
    con.commit()
    return '''<script>alert("registered");window.location="/"</script>'''


@app.route('/user_homepage')
def user_homepage():
    return render_template("user homepage.html")
@app.route('/user_feedback')
def user_feedback():
    return render_template("userfeedback.html")
@app.route('/send_feedback',methods=['post'])
def send_feedback():
    feedback=request.form['textfield']
    cmd.execute("insert into feedback values (null,'"+feedback+"',curdate(),'"+str(session['lid'])+"')")
    con.commit()
    return '''<script>alert("feedback send");window.location='/user_homepage'</script>'''
@app.route('/search')
def search():
    return render_template("search.html")
@app.route('/adduser')
def adduser():
    cmd.execute("SELECT product.*, twitter.*, twitter FROM product JOIN twitter ON product.ID = twitter.product_ID")
    s = cmd.fetchall()
    return render_template("adduser_search.html",val=s)
@app.route('/product_add',methods=['get','post'])
def product_add():
    return render_template("product new.html")
@app.route('/product_add1',methods=['get','post'])
def product_add1():
    Product_Name=request.form['textfield']
    Description=request.form['textfield2']
    Twitter_handle=request.form['textfield3']


    cmd.execute("insert into product values(null,'" +Product_Name+ "','" +Twitter_handle+ "','"+Description+"')")
    con.commit()
    return '''<script>alert("success");window.location="user_homepage"</script>'''
@app.route('/twitter_handle')
def twitter_handle():
    return render_template("twitter handle.html")
@app.route('/view_comparison')
def view_comparison():
    cmd.execute("SELECT * FROM product ")
    s = cmd.fetchall()
    return render_template("view comparison.html", val=s)


@app.route('/blockuser',methods=['get','post'])
def blockuser():
    id = request.args.get('id')
    cmd.execute("update login set type='blocked' where Id='" + str(id) + "'")
    con.commit()
    return '''<script>alert("Blocked");window.location="/view_user"</script>'''
@app.route('/unblockuser',methods=['get','post'])
def unblockuser():
    id = request.args.get('id')
    cmd.execute("update login set type='user' where Id='" + str(id) + "'")
    con.commit()
    return '''<script>alert("unblocked");window.location="/view_user"</script>'''

@app.route('/delete',methods=['get','post'])
def delete():
    id = request.args.get('id')
    cmd.execute("DELETE FROM `product` WHERE `Id`='" + str(id) + "'")
    con.commit()
    return '''<script>alert("deleted");window.location="/user_homepage"</script>'''















app.run(debug=True)