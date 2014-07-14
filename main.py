#appcfg.py rollback C:\propertyfieldmanagement
#appcfg.py update C:\propertyfieldmanagement
DefaultHead='''<html><head><style type="text/css">

</style><title>Property Field Management</title></head>'''
DefaultScript='''
<script>
function calctotalmiles()
{
var start=document.getElementById("OdometerStart").value;
var end=document.getElementById("OdometerEnd").value;
document.getElementById("TotalMiles").value=String(Number(end)-Number(start));
}
function googleitproperty()
{
var webaddress="http://www.google.com/search?q=";
webaddress+=document.getElementById("PropertyAddress").value;
window.open(webaddress);
}
function propertyselected()
{
var propertyx= document.getElementById("Property").selectedIndex;
document.getElementById("PropertyAddress").value=selectaddress[propertyx];
}
function CalendarDateDue()
{
document.getElementById("DateDue").value=document.getElementById("duedate").value;
}

function TodayDateCompleted()
{
d=new Date();
mm=d.getMonth()+1;
if (mm<10){mm="0"+mm;}
dd=d.getDate();
if (dd<10){dd="0"+dd;}
D=d.getFullYear()+"-"+mm+"-"+dd;
document.getElementById("DateCompleted").value=D;
if(document.getElementById("DateScheduled").value==""){document.getElementById("DateScheduled").value=D;}
}
function CalendarDateScheduled()
{
document.getElementById("DateScheduled").value=document.getElementById("scheduleddate").value;
}
function TodayDateOrdered()
{
d=new Date();
mm=d.getMonth()+1;
if (mm<10){mm="0"+mm;}
dd=d.getDate();
if (dd<10){dd="0"+dd;}
D=d.getFullYear()+"-"+mm+"-"+dd;
document.getElementById("DateOrdered").value=D;

d.setDate(d.getDate()+2);
mm=d.getMonth()+1;
if (mm<10){mm="0"+mm;}
dd=d.getDate();
if (dd<10){dd="0"+dd;}
D=d.getFullYear()+"-"+mm+"-"+dd;
document.getElementById("DateDue").value=D;
}
function AllocateMileage()
{
document.getElementById("Allocate").value=document.getElementById("SelectMileageAllocation").value;
}
function ShowPageMenu()
{
HideFilterForm()
HideSortForm()
document.getElementById("MenuAdministrator").style.display="block";
document.getElementById("ShowPageMenuButton").style.display="none";
document.getElementById("HidePageMenuButton").style.display="block";
}
function HidePageMenu()
{
document.getElementById("MenuAdministrator").style.display="none";
document.getElementById("ShowPageMenuButton").style.display="block";
document.getElementById("HidePageMenuButton").style.display="none";
}
function ShowFilterForm()
{
HidePageMenu()
document.getElementById("filterform").style.display="block";
document.getElementById("ShowFilterFormButton").style.display="none";
document.getElementById("HideFilterFormButton").style.display="block";
}
function HideFilterForm()
{
document.getElementById("filterform").style.display="none";
document.getElementById("ShowFilterFormButton").style.display="block";
document.getElementById("HideFilterFormButton").style.display="none";
}
function ShowSortForm()
{
HidePageMenu()
document.getElementById("sortform").style.display="block";
document.getElementById("ShowSortFormButton").style.display="none";
document.getElementById("HideSortFormButton").style.display="block";
}
function HideSortForm()
{
document.getElementById("sortform").style.display="none";
document.getElementById("ShowSortFormButton").style.display="block";
document.getElementById("HideSortFormButton").style.display="none";
}

function AddBid()
{
      var bidx = document.getElementById("SelectBids").selectedIndex;
      var bidy = document.getElementById("SelectBids").options;
alert("bidx="+bidx+"   bidy="+bidy);

      quantity1=document.getElementById("quantity1").value;
      quantity2=document.getElementById("quantity2").value;
      var verbiage=""
      verbiage=bidy[bidx].text.replace(/#1/g,quantity1).replace(/#2/g,quantity2)
      
if (QuantityCodes[bidx]=="1"){verbiage=verbiage.replace(/$/g,UnitCosts[bidx]);}
else if (QuantityCodes[bidx]=="1x")
{verbiage=verbiage.replace(/$/g,quantity1*UnitCosts[bidx]);}
else if (QuantityCodes[bidx]=="1x2x"){verbiage=verbiage.replace(/$/g,quantity1*quantity2*UnitCosts[bidx]);}
else if (QuantityCodes[bidx]=="1+2x"){verbiage=verbiage.replace(/$/g,(Math.round((0.4+Number(quantity1)+Number(quantity2))*UnitCosts[bidx])));}
else {}
  
document.getElementById("BidDetails").value+=verbiage+"\n";
document.getElementById("quantity1").value='';
document.getElementById("quantity2").value='';
          
}

    var beforevalue=''
    var aftervalue=''
    var previouscolor=''

    function activeinputFunction(xa)
    {
        HidePageMenu();
        if (xa.style.backgroundColor=="green" || xa.style.backgroundColor=="red")
        {}
        else
        {
        xa.style.backgroundColor="yellow"

        }
        beforevalue=xa.value
    }

    function inactiveinputFunction(xb)
    {
        aftervalue=xb.value
        if (beforevalue!=aftervalue || xb.style.backgroundColor=="red")
         {
         
         xb.style.backgroundColor="red";
         document.body.style.backgroundColor="FF6666";
         
         }
        else if (xb.style.backgroundColor=="yellow")
         {xb.style.backgroundColor="";}
        else
         {
         
         }
    }

    </script>
<body>
<br><div id="headerandmenu" width="98%"><div id="divpfmtitle"><a id="pfmtitle" class="imlink" href="/"><t>Property Field Management</t></a></div>

'''
DefaultBody=''' '''
DefaultFoot='</div></body></span></html>'

#appcfg.py rollback C:\propertyfieldmanagement
#appcfg.py update C:\propertyfieldmanagement
#Python Code Generated Using E-Commerce Creator.
#includes
import datetime
import logging
import time
import webapp2
from cgi import escape
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.db import Key
from google.appengine.api import users
from google.appengine.api import memcache
from google.appengine.api import namespace_manager
#static
StatusBar= "Welcome"
def get_Refresh():
    data=memcache.get('Refresh')
    if data is not None:
        return data
    else:
        data=1
        memcache.add('Refresh',data,60)
        return data

def get_Page():
    data=memcache.get('Page')
    if data is not None:
        return data
    else:
        try:
            data=db.GqlQuery("SELECT * FROM Page WHERE Selected='true'").get()
            return data
        except:
            pass #entry=Page(ID='1001',Head=DefaultHead,Script=DefaultScript,Body=DefaultBody,Foot=DefaultFoot,Selected='true')
                 #entry.put()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                if (user.nickname()=="chadfernelius@hotmail.com"):
                    global StatusBar
                    StatusBar+=(" Welcome chadfernelius@hotmail.com. Initializing Administrator. Page will automatically reload after 5 seconds.")
                    entry=TheUsers(ID = "1001",UserName = user.nickname(),EmailAddress="chadfernelius@hotmail.com",Type="Administrator")
                else:
                    entry = TheUsers(UserName = user.nickname(),Type = "Visitor")
                    StatusBar+=("Initiating new user. Page will automatically load after 5 seconds.")
                entry.put()
                self.response.out.write(page.Head)
                self.response.out.write(page.Body)
                self.response.out.write(page.Foot)
                time.sleep(5)
                self.redirect('/')
            else:
                memcache.set('WorkOrderGQLWHERE',"",namespace=users.get_current_user().user_id())
                memcache.set('WorkOrderCurrentIndex',-1,namespace=users.get_current_user().user_id())
                MileageData=db.GqlQuery(MileageGQLSelect+get_MileageGQLWHERE()+get_MileageGQLSort())
                global MileageCount
                MileageCount=MileageData.count()
                global StatusBar
                StatusBar=('<br>Signed in as %s .<a href="%s">Click here to sign-out.</a>.' % (user.nickname(),users.create_logout_url('/')))
                if (TheUser.Type=='Visitor'):
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuVisitor)
                    self.response.out.write(page.Body)
                    
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
                if (TheUser.Type=='Customer'):
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuCustomer)
                    self.response.out.write(page.Body)
                    
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
                if (TheUser.Type=='Client'):
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuClient)
                    self.response.out.write(page.Body)
                    
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
                if (TheUser.Type=='Employee'):
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuEmployee)
                    self.response.out.write(page.Body)
                    
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
                if (TheUser.Type=='Machine'):
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuMachine)
                    self.response.out.write(page.Body)
                    
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
                if (TheUser.Type=='Supplier'):
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuSupplier)
                    self.response.out.write(page.Body)
                    
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
                if (TheUser.Type=='Processor'):
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuProcessor)
                    self.response.out.write(page.Body)
                    
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
                if (TheUser.Type=='Manager'):
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuManager)
                    self.response.out.write(page.Body)
                    
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
                if (TheUser.Type=='Administrator'):
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuAdministrator)
                    write_htmlMenuAdministrator(self)
                    self.response.out.write(page.Body)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)

        else: ##Anonymous user.
            global StatusBar
            StatusBar=('<br>')
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(htmlMenuAnonymous)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)
htmlMenuAnonymous="<div class='menu'><a class='menu' href='%s'>Login</a><a class='menu' href='%s'>Become an Employee</a><a class='menu' href='%s'>Become a Supplier/Subcontractor</a></div>" % (users.create_login_url('/'),users.create_login_url('/PersonalEmployeePage'),users.create_login_url('/PersonalSupplierPage'))


class TheUsers(db.Model):
    ID=db.StringProperty()
    userid=db.StringProperty()
    UserName=db.StringProperty()
    EmailAddress=db.StringProperty()
    Type=db.StringProperty()
    date=db.DateTimeProperty(required=True, auto_now=True)

TheUsersGQLSelect="SELECT * FROM TheUsers"
TheUsersCurrentIndex = -1;
TheUsersCount = 0;
TheUsersFieldNames=["ID","userid","UserName","EmailAddress","Type","date",]

def get_TheUsersGQLWHERE():
    data = memcache.get('TheUsersGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('TheUsersGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_TheUsersGQLSort():
    data = memcache.get('TheUsersGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('TheUsersGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_TheUsersCurrentIndex():
    data = memcache.get('TheUsersCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('TheUsersCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

class TheUsersPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                TheUsersData=db.GqlQuery(TheUsersGQLSelect+get_TheUsersGQLWHERE()+get_TheUsersGQLSort())
                global TheUsersCount
                TheUsersCount=TheUsersData.count()
                if get_TheUsersCurrentIndex()==-1:
                    TheUsersCurrentIndex=TheUsersCount
                    memcache.set('TheUsersCurrentIndex',TheUsersCurrentIndex,namespace=users.get_current_user().user_id())
                if TheUsersCount==0:
                    self.redirect('/NewTheUsers')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuAdministrator)
                    self.response.out.write(page.Body)
                    
                    write_TheUsers(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class FirstTheUsers(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstTheUsers')
    def get(self):
        TheUsersCurrentIndex = 1
        memcache.set('TheUsersCurrentIndex',TheUsersCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/TheUsersPage')

class PreviousTheUsers(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousTheUsers')
  def get(self):
    if get_TheUsersCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/TheUsersPage')
    else:
      TheUsersCurrentIndex = get_TheUsersCurrentIndex()-1
      memcache.set('TheUsersCurrentIndex',TheUsersCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/TheUsersPage')

class NextTheUsers(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextTheUsers')
  def get(self):
    if get_TheUsersCurrentIndex() + 1 > TheUsersCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/TheUsersPage')
    else:
      TheUsersCurrentIndex = get_TheUsersCurrentIndex()+1
      memcache.set('TheUsersCurrentIndex',TheUsersCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/TheUsersPage')

class LastTheUsers(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastTheUsers')
    def get(self):
        TheUsersCurrentIndex = TheUsersCount
        memcache.set('TheUsersCurrentIndex',TheUsersCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/TheUsersPage')

class NewTheUsers(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewTheUsers')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newTheUsers(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class TheUsersTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/TheUsersTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                self.response.out.write(htmlMenuAdministrator)
                write_TheUsersTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterTheUsers(webapp2.RequestHandler):
    def post(self):
        memcache.set('TheUsersGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('TheUsersCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/TheUsersPage')

class GotoTheUsers(webapp2.RequestHandler):
    def post(self):
        recordnumber=self.request.get('recordnumber')
        memcache.set('TheUsersCurrentIndex',int(recordnumber),namespace=users.get_current_user().user_id())
        self.redirect('/TheUsersPage')
        

class FilterTheUsers(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        TheUsersGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('TheUsersGQLWHERE',TheUsersGQLWHERE,namespace=users.get_current_user().user_id())
        TheUsersGQLSort=""
        memcache.set('TheUsersGQLSort',TheUsersGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('TheUsersCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/TheUsersPage')

class SortTheUsers(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        TheUsersGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('TheUsersGQLSort',TheUsersGQLSort,namespace=users.get_current_user().user_id())
        TheUsersGQLWHERE=""
        memcache.set('TheUsersGQLWHERE',TheUsersGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('TheUsersCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/TheUsersPage')

class StoreATheUsers(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    userid=self.request.get('userid')
    UserName=self.request.get('UserName')
    EmailAddress=self.request.get('EmailAddress')
    Type=self.request.get('Type')

    self.store_a_TheUsers(ID,userid,UserName,EmailAddress,Type,)
  def store_a_TheUsers(self,ID,userid,UserName,EmailAddress,Type,):
    entry = db.GqlQuery("SELECT * FROM TheUsers where ID = :1", ID).get()#this could write over someone else's stuff if they finished the form first. count and therefore id isn't incremented until entity stored.
    if entry:
      entry.ID=ID
      entry.userid=userid
      entry.UserName=UserName
      entry.EmailAddress=EmailAddress
      entry.Type=Type

    else:
      entry = TheUsers(ID=ID,userid=userid,UserName=UserName,EmailAddress=EmailAddress,Type=Type,)
      entry.ID=str(TheUsersCount+1001)
      global TheUsersCount
      TheUsersCount += 1
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/TheUsersPage')

def write_TheUsers(self):
  if get_TheUsersCurrentIndex()<=0:
      TheUsersOffset=0
  else:
      TheUsersOffset=get_TheUsersCurrentIndex()-1
  TheUsers=db.GqlQuery(TheUsersGQLSelect+get_TheUsersGQLWHERE()+get_TheUsersGQLSort()).get(deadline=60, offset=TheUsersOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <h1 id="recordID">TheUsers</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstTheUsers" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousTheUsers" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextTheUsers" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastTheUsers" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewTheUsers" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterTheUsers" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td>
  <td><form action="/GotoTheUsers" method="post" enctype=application/x-www-form-urlencoded>Goto: <input type="text" name="recordnumber" size="2"> <input type="submit" value="Go"></form></td> 
  <td><a href="/TheUsersTable">Show all in a table.</a></td>
  </tr></table>
  <form id="filterform" action="/FilterTheUsers" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''' %(TheUsersOffset+1,TheUsersCount))
  for f in TheUsersFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortTheUsers" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in TheUsersFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>
  <table border=0>
  <caption></caption>
    <form action="/StoreATheUsers" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if TheUsers.ID:self.response.out.write('<tr><td>ID readonly</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(TheUsers.ID)))
  else:self.response.out.write('<tr><td>ID readonly</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if TheUsers.userid:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(TheUsers.userid)))
  else:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if TheUsers.UserName:self.response.out.write('<tr><td>User Name</td><td><input type="text" name="UserName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(TheUsers.UserName)))
  else:self.response.out.write('<tr><td>User Name</td><td><input type="text" name="UserName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if TheUsers.EmailAddress:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="EmailAddress" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(TheUsers.EmailAddress)))
  else:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="EmailAddress" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if TheUsers.Type:self.response.out.write('<tr><td>Type of User</td><td><input type="text" name="Type" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(TheUsers.Type)))
  else:self.response.out.write('<tr><td>Type of User</td><td><input type="text" name="Type" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if TheUsers.date:self.response.out.write('<tr><td>date of entry. readonly</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(TheUsers.date)))
  else:self.response.out.write('<tr><td>date of entry. readonly</td><td><input type="text" name="date" value=""   readonly></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')

def write_TheUsersTable(self):
    TheUsersData = db.GqlQuery(TheUsersGQLSelect+get_TheUsersGQLWHERE()+get_TheUsersGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>userid</td><td>UserName</td><td>EmailAddress</td><td>Type</td><td>date</td>
</tr>''')
    for c in TheUsersData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.userid,c.UserName,c.EmailAddress,c.Type,c.date,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newTheUsers(self):
  AutoNumber=TheUsersCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New TheUsers</b></caption>
    <form action="/StoreATheUsers" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID readonly</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>User Name</td><td><input type="text" name="UserName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="EmailAddress" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Type of User</td><td><input type="text" name="Type" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>date of entry. readonly</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterTheUsers" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(TheUsersCount)
  self.response.out.write(''' TheUsers(s).</table></body></html>
''')


class Page(db.Model):
    ID=db.StringProperty()
    Head=db.TextProperty()
    Script=db.TextProperty()
    Body=db.TextProperty()
    Foot=db.TextProperty()
    Selected=db.StringProperty()
    date=db.DateTimeProperty(required=True, auto_now=True)

PageGQLSelect="SELECT * FROM Page"
PageCurrentIndex = -1;
PageCount = 0;
PageFieldNames=["ID","Head","Script","Body","Foot","Selected","date",]

def get_PageGQLWHERE():
    data = memcache.get('PageGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('PageGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_PageGQLSort():
    data = memcache.get('PageGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('PageGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_PageCurrentIndex():
    data = memcache.get('PageCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('PageCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

class PagePage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                PageData=db.GqlQuery(PageGQLSelect+get_PageGQLWHERE()+get_PageGQLSort())
                global PageCount
                PageCount=PageData.count()
                if get_PageCurrentIndex()==-1:
                    PageCurrentIndex=PageCount
                    memcache.set('PageCurrentIndex',PageCurrentIndex,namespace=users.get_current_user().user_id())
                if PageCount==0:
                    self.redirect('/NewPage')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuAdministrator)
                    self.response.out.write(page.Body)
                    
                    write_Page(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class FirstPage(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstPage')
    def get(self):
        PageCurrentIndex = 1
        memcache.set('PageCurrentIndex',PageCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/PagePage')

class PreviousPage(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousPage')
  def get(self):
    if get_PageCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/PagePage')
    else:
      PageCurrentIndex = get_PageCurrentIndex()-1
      memcache.set('PageCurrentIndex',PageCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/PagePage')

class NextPage(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextPage')
  def get(self):
    if get_PageCurrentIndex() + 1 > PageCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/PagePage')
    else:
      PageCurrentIndex = get_PageCurrentIndex()+1
      memcache.set('PageCurrentIndex',PageCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/PagePage')

class LastPage(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastPage')
    def get(self):
        PageCurrentIndex = PageCount
        memcache.set('PageCurrentIndex',PageCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/PagePage')

class NewPage(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewPage')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newPage(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class PageTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/PageTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                self.response.out.write(htmlMenuAdministrator)
                write_PageTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterPage(webapp2.RequestHandler):
    def post(self):
        memcache.set('PageGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('PageCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/PagePage')

class FilterPage(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        PageGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('PageGQLWHERE',PageGQLWHERE,namespace=users.get_current_user().user_id())
        PageGQLSort=""
        memcache.set('PageGQLSort',PageGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('PageCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/PagePage')

class SortPage(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        PageGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('PageGQLSort',PageGQLSort,namespace=users.get_current_user().user_id())
        PageGQLWHERE=""
        memcache.set('PageGQLWHERE',PageGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('PageCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/PagePage')

class StoreAPage(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    Head=self.request.get('Head')
    Script=self.request.get('Script')
    Body=self.request.get('Body')
    Foot=self.request.get('Foot')
    Selected=self.request.get('Selected')

    self.store_a_Page(ID,Head,Script,Body,Foot,Selected,)
  def store_a_Page(self,ID,Head,Script,Body,Foot,Selected,):
    entry = db.GqlQuery("SELECT * FROM Page where ID = :1", ID).get()
    if entry:
      entry.ID=ID
      entry.Head=Head
      entry.Script=Script
      entry.Body=Body
      entry.Foot=Foot
      entry.Selected=Selected

    else:
      entry = Page(ID=ID,Head=Head,Script=Script,Body=Body,Foot=Foot,Selected=Selected,)
      entry.ID=str(PageCount+1001)
      global PageCount
      PageCount += 1
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/PagePage')

def write_Page(self):
  if get_PageCurrentIndex()<=0:
      PageOffset=0
  else:
      PageOffset=get_PageCurrentIndex()-1
  Page=db.GqlQuery(PageGQLSelect+get_PageGQLWHERE()+get_PageGQLSort()).get(deadline=60, offset=PageOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <h1 id="recordID">Page</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstPage" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousPage" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextPage" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastPage" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewPage" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterPage" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/PageTable">Show all in a table.</a></td>
  <td><form action="/GotoPage" method="post" enctype=application/x-www-form-urlencoded>Goto: <input type="text" name="recordnumber" size="2"> <input type="submit" value="Go"></form></td>
  </tr></table>
  <form id="filterform" action="/FilterPage" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''' %(PageOffset+1,PageCount))
  for f in PageFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortPage" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in PageFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>
  <table border=0>
  <caption></caption>
    <form action="/StoreAPage" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Page.ID:self.response.out.write('<tr><td>ID readonly</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(Page.ID)))
  else:self.response.out.write('<tr><td>ID readonly</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if Page.Head:self.response.out.write('<tr><td>html header</td><td><textarea cols="40" rows="5" name="Head"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Page.Head))
  else:self.response.out.write('<tr><td>html header</td><td><textarea cols="40" rows="5" name="Head"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if Page.Script:self.response.out.write('<tr><td>html script</td><td><textarea cols="40" rows="5" name="Script"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Page.Script))
  else:self.response.out.write('<tr><td>html script</td><td><textarea cols="40" rows="5" name="Script"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if Page.Body:self.response.out.write('<tr><td>html body</td><td><textarea cols="40" rows="5" name="Body"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Page.Body))
  else:self.response.out.write('<tr><td>html body</td><td><textarea cols="40" rows="5" name="Body"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if Page.Foot:self.response.out.write('<tr><td>html foot</td><td><textarea cols="40" rows="5" name="Foot"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Page.Foot))
  else:self.response.out.write('<tr><td>html foot</td><td><textarea cols="40" rows="5" name="Foot"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if Page.Selected:self.response.out.write('<tr><td>y/n</td><td><input type="text" name="Selected" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Page.Selected)))
  else:self.response.out.write('<tr><td>y/n</td><td><input type="text" name="Selected" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Page.date:self.response.out.write('<tr><td>date readonly</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(Page.date)))
  else:self.response.out.write('<tr><td>date readonly</td><td><input type="text" name="date" value=""   readonly></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')

def write_PageTable(self):
    PageData = db.GqlQuery(PageGQLSelect+get_PageGQLWHERE()+get_PageGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>Head</td><td>Script</td><td>Body</td><td>Foot</td><td>Selected</td><td>date</td>
</tr>''')
    for c in PageData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.Head,c.Script,c.Body,c.Foot,c.Selected,c.date,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newPage(self):
  AutoNumber=PageCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New Page</b></caption>
    <form action="/StoreAPage" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID readonly</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>html header</td><td><textarea cols="40" rows="5" name="Head"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>html script</td><td><textarea cols="40" rows="5" name="Script"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>html body</td><td><textarea cols="40" rows="5" name="Body"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>html foot</td><td><textarea cols="40" rows="5" name="Foot"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>y/n</td><td><input type="text" name="Selected" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>date readonly</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterPage" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(PageCount)
  self.response.out.write(''' Page(s).</table></body></html>
''')


class Visitor(db.Model):
    ID=db.StringProperty()
    date=db.DateTimeProperty(required=True, auto_now=True)
    userid=db.StringProperty()
    FirstName=db.StringProperty()
    LastName=db.StringProperty()
    Address=db.StringProperty()
    Phone=db.StringProperty()
    Email=db.StringProperty()

VisitorGQLSelect="SELECT * FROM Visitor"
VisitorCurrentIndex = -1;
VisitorCount = 0;
VisitorFieldNames=["ID","date","userid","FirstName","LastName","Address","Phone","Email",]

def get_VisitorGQLWHERE():
    data = memcache.get('VisitorGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('VisitorGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_VisitorGQLSort():
    data = memcache.get('VisitorGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('VisitorGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_VisitorCurrentIndex():
    data = memcache.get('VisitorCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('VisitorCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

class VisitorPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                VisitorData=db.GqlQuery(VisitorGQLSelect+get_VisitorGQLWHERE()+get_VisitorGQLSort())
                global VisitorCount
                VisitorCount=VisitorData.count()
                if get_VisitorCurrentIndex()==-1:
                    VisitorCurrentIndex=VisitorCount
                    memcache.set('VisitorCurrentIndex',VisitorCurrentIndex,namespace=users.get_current_user().user_id())
                if VisitorCount==0:
                    self.redirect('/NewVisitor')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuAdministrator)
                    self.response.out.write(page.Body)
                    
                    write_Visitor(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class FirstVisitor(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstVisitor')
    def get(self):
        VisitorCurrentIndex = 1
        memcache.set('VisitorCurrentIndex',VisitorCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/VisitorPage')

class PreviousVisitor(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousVisitor')
  def get(self):
    if get_VisitorCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/VisitorPage')
    else:
      VisitorCurrentIndex = get_VisitorCurrentIndex()-1
      memcache.set('VisitorCurrentIndex',VisitorCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/VisitorPage')

class NextVisitor(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextVisitor')
  def get(self):
    if get_VisitorCurrentIndex() + 1 > VisitorCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/VisitorPage')
    else:
      VisitorCurrentIndex = get_VisitorCurrentIndex()+1
      memcache.set('VisitorCurrentIndex',VisitorCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/VisitorPage')

class LastVisitor(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastVisitor')
    def get(self):
        VisitorCurrentIndex = VisitorCount
        memcache.set('VisitorCurrentIndex',VisitorCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/VisitorPage')

class NewVisitor(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewVisitor')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newVisitor(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class VisitorTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/VisitorTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                self.response.out.write(htmlMenuAdministrator)
                write_VisitorTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterVisitor(webapp2.RequestHandler):
    def post(self):
        memcache.set('VisitorGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('VisitorCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/VisitorPage')

class FilterVisitor(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        VisitorGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('VisitorGQLWHERE',VisitorGQLWHERE,namespace=users.get_current_user().user_id())
        VisitorGQLSort=""
        memcache.set('VisitorGQLSort',VisitorGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('VisitorCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/VisitorPage')

class SortVisitor(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        VisitorGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('VisitorGQLSort',VisitorGQLSort,namespace=users.get_current_user().user_id())
        VisitorGQLWHERE=""
        memcache.set('VisitorGQLWHERE',VisitorGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('VisitorCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/VisitorPage')

class StoreAVisitor(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    userid=self.request.get('userid')
    FirstName=self.request.get('FirstName')
    LastName=self.request.get('LastName')
    Address=self.request.get('Address')
    Phone=self.request.get('Phone')
    Email=self.request.get('Email')

    self.store_a_Visitor(ID,userid,FirstName,LastName,Address,Phone,Email,)
  def store_a_Visitor(self,ID,userid,FirstName,LastName,Address,Phone,Email,):
    entry = db.GqlQuery("SELECT * FROM Visitor where ID = :1", ID).get()
    if entry:
      entry.ID=ID
      entry.userid=userid
      entry.FirstName=FirstName
      entry.LastName=LastName
      entry.Address=Address
      entry.Phone=Phone
      entry.Email=Email

    else:
      entry = Visitor(ID=ID,userid=userid,FirstName=FirstName,LastName=LastName,Address=Address,Phone=Phone,Email=Email,)
      entry.ID=str(VisitorCount+1001)
      global VisitorCount
      VisitorCount += 1
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/VisitorPage')

def write_Visitor(self):
  if get_VisitorCurrentIndex()<=0:
      VisitorOffset=0
  else:
      VisitorOffset=get_VisitorCurrentIndex()-1
  Visitor=db.GqlQuery(VisitorGQLSelect+get_VisitorGQLWHERE()+get_VisitorGQLSort()).get(deadline=60, offset=VisitorOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <h1 id="recordID">Visitor</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstVisitor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousVisitor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextVisitor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastVisitor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewVisitor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterVisitor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/VisitorTable">Show all in a table.</a></td>
  <td><form action="/GotoVisitor" method="post" enctype=application/x-www-form-urlencoded>Goto: <input type="text" name="recordnumber" size="2"> <input type="submit" value="Go"></form></td>
  </tr></table>
  <form id="filterform" action="/FilterVisitor" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''' %(VisitorOffset+1,VisitorCount))
  for f in VisitorFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortVisitor" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in VisitorFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>
  <table border=0>
  <caption></caption>
    <form action="/StoreAVisitor" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Visitor.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(Visitor.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if Visitor.date:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(Visitor.date)))
  else:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value=""   readonly></td><tr>')
  if Visitor.userid:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Visitor.userid)))
  else:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Visitor.FirstName:self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Visitor.FirstName)))
  else:self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Visitor.LastName:self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Visitor.LastName)))
  else:self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Visitor.Address:self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Visitor.Address)))
  else:self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Visitor.Phone:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Visitor.Phone)))
  else:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Visitor.Email:self.response.out.write('<tr><td>Email</td><td><input type="text" name="Email" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Visitor.Email)))
  else:self.response.out.write('<tr><td>Email</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')

def write_VisitorTable(self):
    VisitorData = db.GqlQuery(VisitorGQLSelect+get_VisitorGQLWHERE()+get_VisitorGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>date</td><td>userid</td><td>FirstName</td><td>LastName</td><td>Address</td><td>Phone</td><td>Email</td>
</tr>''')
    for c in VisitorData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.date,c.userid,c.FirstName,c.LastName,c.Address,c.Phone,c.Email,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newVisitor(self):
  AutoNumber=VisitorCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New Visitor</b></caption>
    <form action="/StoreAVisitor" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Email</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterVisitor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(VisitorCount)
  self.response.out.write(''' Visitor(s).</table></body></html>
''')


class PersonalVisitorPage(webapp2.RequestHandler):
    def get(self):
        userid=users.get_current_user().user_id()
        if userid:
            PersonalVisitorQuery=db.GqlQuery("SELECT * FROM Visitor WHERE userid='%s' LIMIT 1" %(userid))
            Person=PersonalVisitorQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = PersonalVisitorQuery.count()
            if (count==0):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_personalnewVisitor(self)
            else:
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_personalVisitor(self)
        else:
            self.redirect('/')

def write_personalnewVisitor(self):
  AutoNumber=VisitorCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>New Visitor Application</b></caption>
    <form action="/StoreAVisitor" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td></td><td><input type="text" name="ID" value="%s" hidden disabled readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td></td><td><input type="text" name="date" value="%s" hidden disabled readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" hidden disabled readonly></td></tr>' %(users.get_current_user().user_id()))
  self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Email</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
 
  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>''')

def write_personalVisitor(self):
  Visitor=db.GqlQuery("SELECT * FROM Visitor WHERE userid='%s'" %(users.get_current_user().user_id())).get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <table border=0>
  <caption><h1 id="recordID">Visitor Profile</h1></caption>
    <form action="/StoreAVisitor" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Visitor.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s" hidden disabled readonly></td><tr>' % escape(str(Visitor.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="" hidden disabled readonly></td><tr>')
  if Visitor.date:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s" hidden disabled readonly></td><tr>' % escape(str(Visitor.date)))
  else:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="" hidden disabled readonly></td><tr>')
  if Visitor.userid:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" size="35" hidden disabled onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Visitor.userid)))
  else:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35" hidden disabled onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Visitor.FirstName:self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Visitor.FirstName)))
  else:self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Visitor.LastName:self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Visitor.LastName)))
  else:self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Visitor.Address:self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Visitor.Address)))
  else:self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Visitor.Phone:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Visitor.Phone)))
  else:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Visitor.Email:self.response.out.write('<tr><td>Email</td><td><input type="text" name="Email" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Visitor.Email)))
  else:self.response.out.write('<tr><td>Email</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
 
  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')


class Customer(db.Model):
    ID=db.StringProperty()
    date=db.DateTimeProperty(required=True, auto_now=True)
    userid=db.StringProperty()
    FirstName=db.StringProperty()
    LastName=db.StringProperty()
    Title=db.StringProperty()
    Address=db.StringProperty()
    BillingAddress=db.StringProperty()
    ShippingAddress=db.StringProperty()
    CreditCardNumber=db.StringProperty()
    CreditCardExpiration=db.StringProperty()
    CreditCardCode=db.StringProperty()
    CreditCardZip=db.StringProperty()
    Phone=db.StringProperty()
    Email=db.StringProperty()

CustomerGQLSelect="SELECT * FROM Customer"
CustomerCurrentIndex = -1;
CustomerCount = 0;
CustomerFieldNames=["ID","date","userid","FirstName","LastName","Title","Address","BillingAddress","ShippingAddress","CreditCardNumber","CreditCardExpiration","CreditCardCode","CreditCardZip","Phone","Email",]

def get_CustomerGQLWHERE():
    data = memcache.get('CustomerGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('CustomerGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_CustomerGQLSort():
    data = memcache.get('CustomerGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('CustomerGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_CustomerCurrentIndex():
    data = memcache.get('CustomerCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('CustomerCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

class CustomerPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                CustomerData=db.GqlQuery(CustomerGQLSelect+get_CustomerGQLWHERE()+get_CustomerGQLSort())
                global CustomerCount
                CustomerCount=CustomerData.count()
                if get_CustomerCurrentIndex()==-1:
                    CustomerCurrentIndex=CustomerCount
                    memcache.set('CustomerCurrentIndex',CustomerCurrentIndex,namespace=users.get_current_user().user_id())
                if CustomerCount==0:
                    self.redirect('/NewCustomer')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuAdministrator)
                    self.response.out.write(page.Body)
                    
                    write_Customer(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class FirstCustomer(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstCustomer')
    def get(self):
        CustomerCurrentIndex = 1
        memcache.set('CustomerCurrentIndex',CustomerCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/CustomerPage')

class PreviousCustomer(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousCustomer')
  def get(self):
    if get_CustomerCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/CustomerPage')
    else:
      CustomerCurrentIndex = get_CustomerCurrentIndex()-1
      memcache.set('CustomerCurrentIndex',CustomerCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/CustomerPage')

class NextCustomer(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextCustomer')
  def get(self):
    if get_CustomerCurrentIndex() + 1 > CustomerCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/CustomerPage')
    else:
      CustomerCurrentIndex = get_CustomerCurrentIndex()+1
      memcache.set('CustomerCurrentIndex',CustomerCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/CustomerPage')

class LastCustomer(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastCustomer')
    def get(self):
        CustomerCurrentIndex = CustomerCount
        memcache.set('CustomerCurrentIndex',CustomerCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/CustomerPage')

class NewCustomer(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewCustomer')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newCustomer(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class CustomerTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/CustomerTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                self.response.out.write(htmlMenuAdministrator)
                write_CustomerTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterCustomer(webapp2.RequestHandler):
    def post(self):
        memcache.set('CustomerGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('CustomerCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/CustomerPage')

class FilterCustomer(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        CustomerGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('CustomerGQLWHERE',CustomerGQLWHERE,namespace=users.get_current_user().user_id())
        CustomerGQLSort=""
        memcache.set('CustomerGQLSort',CustomerGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('CustomerCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/CustomerPage')

class SortCustomer(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        CustomerGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('CustomerGQLSort',CustomerGQLSort,namespace=users.get_current_user().user_id())
        CustomerGQLWHERE=""
        memcache.set('CustomerGQLWHERE',CustomerGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('CustomerCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/CustomerPage')

class StoreACustomer(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    userid=self.request.get('userid')
    FirstName=self.request.get('FirstName')
    LastName=self.request.get('LastName')
    Title=self.request.get('Title')
    Address=self.request.get('Address')
    BillingAddress=self.request.get('BillingAddress')
    ShippingAddress=self.request.get('ShippingAddress')
    CreditCardNumber=self.request.get('CreditCardNumber')
    CreditCardExpiration=self.request.get('CreditCardExpiration')
    CreditCardCode=self.request.get('CreditCardCode')
    CreditCardZip=self.request.get('CreditCardZip')
    Phone=self.request.get('Phone')
    Email=self.request.get('Email')

    self.store_a_Customer(ID,userid,FirstName,LastName,Title,Address,BillingAddress,ShippingAddress,CreditCardNumber,CreditCardExpiration,CreditCardCode,CreditCardZip,Phone,Email,)
  def store_a_Customer(self,ID,userid,FirstName,LastName,Title,Address,BillingAddress,ShippingAddress,CreditCardNumber,CreditCardExpiration,CreditCardCode,CreditCardZip,Phone,Email,):
    entry = db.GqlQuery("SELECT * FROM Customer where ID = :1", ID).get()
    if entry:
      entry.ID=ID
      entry.userid=userid
      entry.FirstName=FirstName
      entry.LastName=LastName
      entry.Title=Title
      entry.Address=Address
      entry.BillingAddress=BillingAddress
      entry.ShippingAddress=ShippingAddress
      entry.CreditCardNumber=CreditCardNumber
      entry.CreditCardExpiration=CreditCardExpiration
      entry.CreditCardCode=CreditCardCode
      entry.CreditCardZip=CreditCardZip
      entry.Phone=Phone
      entry.Email=Email

    else:
      entry = Customer(ID=ID,userid=userid,FirstName=FirstName,LastName=LastName,Title=Title,Address=Address,BillingAddress=BillingAddress,ShippingAddress=ShippingAddress,CreditCardNumber=CreditCardNumber,CreditCardExpiration=CreditCardExpiration,CreditCardCode=CreditCardCode,CreditCardZip=CreditCardZip,Phone=Phone,Email=Email,)
      entry.ID=str(CustomerCount+1001)
      global CustomerCount
      CustomerCount += 1
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/CustomerPage')

def write_Customer(self):
  if get_CustomerCurrentIndex()<=0:
      CustomerOffset=0
  else:
      CustomerOffset=get_CustomerCurrentIndex()-1
  Customer=db.GqlQuery(CustomerGQLSelect+get_CustomerGQLWHERE()+get_CustomerGQLSort()).get(deadline=60, offset=CustomerOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <h1 id="recordID">Customer</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstCustomer" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousCustomer" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextCustomer" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastCustomer" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewCustomer" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterCustomer" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/CustomerTable">Show all in a table.</a></td>
  <td><form action="/GotoCustomer" method="post" enctype=application/x-www-form-urlencoded>Goto: <input type="text" name="recordnumber" size="2"> <input type="submit" value="Go"></form></td>
  </tr></table>
  <form id="filterform" action="/FilterCustomer" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''' %(CustomerOffset+1,CustomerCount))
  for f in CustomerFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortCustomer" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in CustomerFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>
  <table border=0>
  <caption></caption>
    <form action="/StoreACustomer" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Customer.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(Customer.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if Customer.date:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(Customer.date)))
  else:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value=""   readonly></td><tr>')
  if Customer.userid:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.userid)))
  else:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.FirstName:self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.FirstName)))
  else:self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.LastName:self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.LastName)))
  else:self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.Title:self.response.out.write('<tr><td>Title</td><td><input type="text" name="Title" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.Title)))
  else:self.response.out.write('<tr><td>Title</td><td><input type="text" name="Title" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.Address:self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.Address)))
  else:self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.BillingAddress:self.response.out.write('<tr><td>Billing Address</td><td><input type="text" name="BillingAddress" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.BillingAddress)))
  else:self.response.out.write('<tr><td>Billing Address</td><td><input type="text" name="BillingAddress" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.ShippingAddress:self.response.out.write('<tr><td>Shipping Address</td><td><input type="text" name="ShippingAddress" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.ShippingAddress)))
  else:self.response.out.write('<tr><td>Shipping Address</td><td><input type="text" name="ShippingAddress" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.CreditCardNumber:self.response.out.write('<tr><td>Credit Card Number</td><td><input type="text" name="CreditCardNumber" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.CreditCardNumber)))
  else:self.response.out.write('<tr><td>Credit Card Number</td><td><input type="text" name="CreditCardNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.CreditCardExpiration:self.response.out.write('<tr><td>Credit Card Expiration</td><td><input type="text" name="CreditCardExpiration" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.CreditCardExpiration)))
  else:self.response.out.write('<tr><td>Credit Card Expiration</td><td><input type="text" name="CreditCardExpiration" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.CreditCardCode:self.response.out.write('<tr><td>Credit Card Code</td><td><input type="text" name="CreditCardCode" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.CreditCardCode)))
  else:self.response.out.write('<tr><td>Credit Card Code</td><td><input type="text" name="CreditCardCode" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.CreditCardZip:self.response.out.write('<tr><td>Credit Card Zip</td><td><input type="text" name="CreditCardZip" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.CreditCardZip)))
  else:self.response.out.write('<tr><td>Credit Card Zip</td><td><input type="text" name="CreditCardZip" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.Phone:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.Phone)))
  else:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.Email:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.Email)))
  else:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')

def write_CustomerTable(self):
    CustomerData = db.GqlQuery(CustomerGQLSelect+get_CustomerGQLWHERE()+get_CustomerGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>date</td><td>userid</td><td>FirstName</td><td>LastName</td><td>Title</td><td>Address</td><td>BillingAddress</td><td>ShippingAddress</td><td>CreditCardNumber</td><td>CreditCardExpiration</td><td>CreditCardCode</td><td>CreditCardZip</td><td>Phone</td><td>Email</td>
</tr>''')
    for c in CustomerData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.date,c.userid,c.FirstName,c.LastName,c.Title,c.Address,c.BillingAddress,c.ShippingAddress,c.CreditCardNumber,c.CreditCardExpiration,c.CreditCardCode,c.CreditCardZip,c.Phone,c.Email,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newCustomer(self):
  AutoNumber=CustomerCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New Customer</b></caption>
    <form action="/StoreACustomer" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Title</td><td><input type="text" name="Title" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Billing Address</td><td><input type="text" name="BillingAddress" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Shipping Address</td><td><input type="text" name="ShippingAddress" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Credit Card Number</td><td><input type="text" name="CreditCardNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Credit Card Expiration</td><td><input type="text" name="CreditCardExpiration" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Credit Card Code</td><td><input type="text" name="CreditCardCode" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Credit Card Zip</td><td><input type="text" name="CreditCardZip" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterCustomer" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(CustomerCount)
  self.response.out.write(''' Customer(s).</table></body></html>
''')


class PersonalCustomerPage(webapp2.RequestHandler):
    def get(self):
        userid=users.get_current_user().user_id()
        if userid:
            PersonalCustomerQuery=db.GqlQuery("SELECT * FROM Customer WHERE userid='%s' LIMIT 1" %(userid))
            Person=PersonalCustomerQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = PersonalCustomerQuery.count()
            if (count==0):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_personalnewCustomer(self)
            else:
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_personalCustomer(self)
        else:
            self.redirect('/')

def write_personalnewCustomer(self):
  AutoNumber=CustomerCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>New Customer Application</b></caption>
    <form action="/StoreACustomer" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td></td><td><input type="text" name="ID" value="%s" hidden disabled readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td></td><td><input type="text" name="date" value="%s" hidden disabled readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" hidden disabled readonly></td></tr>' %(users.get_current_user().user_id()))
  self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Title</td><td><input type="text" name="Title" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Billing Address</td><td><input type="text" name="BillingAddress" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Shipping Address</td><td><input type="text" name="ShippingAddress" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Credit Card Number</td><td><input type="text" name="CreditCardNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Credit Card Expiration</td><td><input type="text" name="CreditCardExpiration" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Credit Card Code</td><td><input type="text" name="CreditCardCode" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Credit Card Zip</td><td><input type="text" name="CreditCardZip" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
 
  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>''')

def write_personalCustomer(self):
  Customer=db.GqlQuery("SELECT * FROM Customer WHERE userid='%s'" %(users.get_current_user().user_id())).get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <table border=0>
  <caption><h1 id="recordID">Customer Profile</h1></caption>
    <form action="/StoreACustomer" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Customer.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s" hidden disabled readonly></td><tr>' % escape(str(Customer.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="" hidden disabled readonly></td><tr>')
  if Customer.date:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s" hidden disabled readonly></td><tr>' % escape(str(Customer.date)))
  else:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="" hidden disabled readonly></td><tr>')
  if Customer.userid:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" size="35" hidden disabled onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.userid)))
  else:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35" hidden disabled onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.FirstName:self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.FirstName)))
  else:self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.LastName:self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.LastName)))
  else:self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.Title:self.response.out.write('<tr><td>Title</td><td><input type="text" name="Title" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.Title)))
  else:self.response.out.write('<tr><td>Title</td><td><input type="text" name="Title" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.Address:self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.Address)))
  else:self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.BillingAddress:self.response.out.write('<tr><td>Billing Address</td><td><input type="text" name="BillingAddress" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.BillingAddress)))
  else:self.response.out.write('<tr><td>Billing Address</td><td><input type="text" name="BillingAddress" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.ShippingAddress:self.response.out.write('<tr><td>Shipping Address</td><td><input type="text" name="ShippingAddress" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.ShippingAddress)))
  else:self.response.out.write('<tr><td>Shipping Address</td><td><input type="text" name="ShippingAddress" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.CreditCardNumber:self.response.out.write('<tr><td>Credit Card Number</td><td><input type="text" name="CreditCardNumber" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.CreditCardNumber)))
  else:self.response.out.write('<tr><td>Credit Card Number</td><td><input type="text" name="CreditCardNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.CreditCardExpiration:self.response.out.write('<tr><td>Credit Card Expiration</td><td><input type="text" name="CreditCardExpiration" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.CreditCardExpiration)))
  else:self.response.out.write('<tr><td>Credit Card Expiration</td><td><input type="text" name="CreditCardExpiration" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.CreditCardCode:self.response.out.write('<tr><td>Credit Card Code</td><td><input type="text" name="CreditCardCode" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.CreditCardCode)))
  else:self.response.out.write('<tr><td>Credit Card Code</td><td><input type="text" name="CreditCardCode" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.CreditCardZip:self.response.out.write('<tr><td>Credit Card Zip</td><td><input type="text" name="CreditCardZip" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.CreditCardZip)))
  else:self.response.out.write('<tr><td>Credit Card Zip</td><td><input type="text" name="CreditCardZip" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.Phone:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.Phone)))
  else:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Customer.Email:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Customer.Email)))
  else:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
 
  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')


class Client(db.Model):
    ID=db.StringProperty()
    date=db.DateTimeProperty(required=True, auto_now=True)
    userid=db.StringProperty()
    CompanyName=db.StringProperty()
    Phone=db.StringProperty()
    Email=db.StringProperty()
    ContactName=db.StringProperty()
    ContactPhone=db.StringProperty()
    ContactEmail=db.StringProperty()
    Website=db.StringProperty()
    FEIN=db.StringProperty()
    Notes=db.TextProperty()
    Status=db.StringProperty()

ClientGQLSelect="SELECT * FROM Client"
ClientCurrentIndex = -1;
ClientCount = 0;
ClientFieldNames=["ID","date","userid","CompanyName","Phone","Email","ContactName","ContactPhone","ContactEmail","Website","FEIN","Notes","Status",]

def get_ClientGQLWHERE():
    data = memcache.get('ClientGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('ClientGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_ClientGQLSort():
    data = memcache.get('ClientGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('ClientGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_ClientCurrentIndex():
    data = memcache.get('ClientCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('ClientCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

class ClientPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                ClientData=db.GqlQuery(ClientGQLSelect+get_ClientGQLWHERE()+get_ClientGQLSort())
                global ClientCount
                ClientCount=ClientData.count()
                if get_ClientCurrentIndex()==-1:
                    ClientCurrentIndex=ClientCount
                    memcache.set('ClientCurrentIndex',ClientCurrentIndex,namespace=users.get_current_user().user_id())
                if ClientCount==0:
                    self.redirect('/NewClient')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(page.Body)
                    self.response.out.write(htmlMenuAdministrator)
                    write_Client(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class FirstClient(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstClient')
    def get(self):
        ClientCurrentIndex = 1
        memcache.set('ClientCurrentIndex',ClientCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/ClientPage')

class PreviousClient(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousClient')
  def get(self):
    if get_ClientCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/ClientPage')
    else:
      ClientCurrentIndex = get_ClientCurrentIndex()-1
      memcache.set('ClientCurrentIndex',ClientCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/ClientPage')

class NextClient(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextClient')
  def get(self):
    if get_ClientCurrentIndex() + 1 > ClientCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/ClientPage')
    else:
      ClientCurrentIndex = get_ClientCurrentIndex()+1
      memcache.set('ClientCurrentIndex',ClientCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/ClientPage')

class LastClient(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastClient')
    def get(self):
        ClientCurrentIndex = ClientCount
        memcache.set('ClientCurrentIndex',ClientCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/ClientPage')

class NewClient(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewClient')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newClient(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class ClientTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/ClientTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                self.response.out.write(htmlMenuAdministrator)
                write_ClientTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterClient(webapp2.RequestHandler):
    def post(self):
        memcache.set('ClientGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('ClientCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/ClientPage')

class FilterClient(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        ClientGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('ClientGQLWHERE',ClientGQLWHERE,namespace=users.get_current_user().user_id())
        ClientGQLSort=""
        memcache.set('ClientGQLSort',ClientGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('ClientCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/ClientPage')

class SortClient(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        ClientGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('ClientGQLSort',ClientGQLSort,namespace=users.get_current_user().user_id())
        ClientGQLWHERE=""
        memcache.set('ClientGQLWHERE',ClientGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('ClientCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/ClientPage')

class StoreAClient(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    userid=self.request.get('userid')
    CompanyName=self.request.get('CompanyName')
    Phone=self.request.get('Phone')
    Email=self.request.get('Email')
    ContactName=self.request.get('ContactName')
    ContactPhone=self.request.get('ContactPhone')
    ContactEmail=self.request.get('ContactEmail')
    Website=self.request.get('Website')
    FEIN=self.request.get('FEIN')
    Notes=self.request.get('Notes')
    Status=self.request.get('Status')

    self.store_a_Client(ID,userid,CompanyName,Phone,Email,ContactName,ContactPhone,ContactEmail,Website,FEIN,Notes,Status,)
  def store_a_Client(self,ID,userid,CompanyName,Phone,Email,ContactName,ContactPhone,ContactEmail,Website,FEIN,Notes,Status,):
    entry = db.GqlQuery("SELECT * FROM Client where ID = :1", ID).get()
    if entry:
      entry.ID=ID
      entry.userid=userid
      entry.CompanyName=CompanyName
      entry.Phone=Phone
      entry.Email=Email
      entry.ContactName=ContactName
      entry.ContactPhone=ContactPhone
      entry.ContactEmail=ContactEmail
      entry.Website=Website
      entry.FEIN=FEIN
      entry.Notes=Notes
      entry.Status=Status

    else:
      entry = Client(ID=ID,userid=userid,CompanyName=CompanyName,Phone=Phone,Email=Email,ContactName=ContactName,ContactPhone=ContactPhone,ContactEmail=ContactEmail,Website=Website,FEIN=FEIN,Notes=Notes,Status=Status,)
      entry.ID=str(ClientCount+1001)
      global ClientCount
      ClientCount += 1
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/ClientPage')

def write_Client(self):
  if get_ClientCurrentIndex()<=0:
      ClientOffset=0
  else:
      ClientOffset=get_ClientCurrentIndex()-1
  Client=db.GqlQuery(ClientGQLSelect+get_ClientGQLWHERE()+get_ClientGQLSort()).get(deadline=60, offset=ClientOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <h1 id="recordID">Client</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstClient" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousClient" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextClient" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastClient" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewClient" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterClient" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/ClientTable">Show all in a table.</a></td>
  <td><form action="/GotoClient" method="post" enctype=application/x-www-form-urlencoded>Goto: <input type="text" name="recordnumber" size="2"> <input type="submit" value="Go"></form></td>
  </tr></table>
  <form id="filterform" action="/FilterClient" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''' %(ClientOffset+1,ClientCount))
  for f in ClientFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortClient" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in ClientFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>
  <table border=0>
  <caption></caption>
    <form action="/StoreAClient" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Client.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(Client.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if Client.date:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(Client.date)))
  else:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value=""   readonly></td><tr>')
  if Client.userid:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.userid)))
  else:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.CompanyName:self.response.out.write('<tr><td>Company Name</td><td><input type="text" name="CompanyName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.CompanyName)))
  else:self.response.out.write('<tr><td>Company Name</td><td><input type="text" name="CompanyName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.Phone:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.Phone)))
  else:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.Email:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.Email)))
  else:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.ContactName:self.response.out.write('<tr><td>Contact Name</td><td><input type="text" name="ContactName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.ContactName)))
  else:self.response.out.write('<tr><td>Contact Name</td><td><input type="text" name="ContactName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.ContactPhone:self.response.out.write('<tr><td>Contact Phone</td><td><input type="text" name="ContactPhone" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.ContactPhone)))
  else:self.response.out.write('<tr><td>Contact Phone</td><td><input type="text" name="ContactPhone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.ContactEmail:self.response.out.write('<tr><td>Contact Email</td><td><input type="text" name="ContactEmail" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.ContactEmail)))
  else:self.response.out.write('<tr><td>Contact Email</td><td><input type="text" name="ContactEmail" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.Website:self.response.out.write('<tr><td>Website</td><td><input type="text" name="Website" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.Website)))
  else:self.response.out.write('<tr><td>Website</td><td><input type="text" name="Website" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.FEIN:self.response.out.write('<tr><td>FEIN</td><td><input type="text" name="FEIN" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.FEIN)))
  else:self.response.out.write('<tr><td>FEIN</td><td><input type="text" name="FEIN" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.Notes:self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Client.Notes))
  else:self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  Statusselectoptions=["prospective","active","inactive","terminated",]
  if Client.Status:
    self.response.out.write('''<tr><td>Status</td><td><select name="Status" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in Statusselectoptions:
        if Client.Status==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Status</td><td><select name="Status" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Statusselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')

def write_ClientTable(self):
    ClientData = db.GqlQuery(ClientGQLSelect+get_ClientGQLWHERE()+get_ClientGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>date</td><td>userid</td><td>CompanyName</td><td>Phone</td><td>Email</td><td>ContactName</td><td>ContactPhone</td><td>ContactEmail</td><td>Website</td><td>FEIN</td><td>Notes</td><td>Status</td>
</tr>''')
    for c in ClientData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.date,c.userid,c.CompanyName,c.Phone,c.Email,c.ContactName,c.ContactPhone,c.ContactEmail,c.Website,c.FEIN,c.Notes,c.Status,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newClient(self):
  AutoNumber=ClientCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New Client</b></caption>
    <form action="/StoreAClient" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Company Name</td><td><input type="text" name="CompanyName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Contact Name</td><td><input type="text" name="ContactName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Contact Phone</td><td><input type="text" name="ContactPhone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Contact Email</td><td><input type="text" name="ContactEmail" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Website</td><td><input type="text" name="Website" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>FEIN</td><td><input type="text" name="FEIN" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  Statusselectoptions=["prospective","active","inactive","terminated",]
  self.response.out.write('<tr><td>Status</td><td><select name="Status"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in Statusselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterClient" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(ClientCount)
  self.response.out.write(''' Client(s).</table></body></html>
''')


class PersonalClientPage(webapp2.RequestHandler):
    def get(self):
        userid=users.get_current_user().user_id()
        if userid:
            PersonalClientQuery=db.GqlQuery("SELECT * FROM Client WHERE userid='%s' LIMIT 1" %(userid))
            Person=PersonalClientQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = PersonalClientQuery.count()
            if (count==0):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_personalnewClient(self)
            else:
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_personalClient(self)
        else:
            self.redirect('/')

def write_personalnewClient(self):
  AutoNumber=ClientCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>New Client Application</b></caption>
    <form action="/StoreAClient" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td></td><td><input type="text" name="ID" value="%s" hidden disabled readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td></td><td><input type="text" name="date" value="%s" hidden disabled readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" hidden disabled readonly></td></tr>' %(users.get_current_user().user_id()))
  self.response.out.write('<tr><td>Company Name</td><td><input type="text" name="CompanyName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Contact Name</td><td><input type="text" name="ContactName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Contact Phone</td><td><input type="text" name="ContactPhone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Contact Email</td><td><input type="text" name="ContactEmail" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Website</td><td><input type="text" name="Website" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>FEIN</td><td><input type="text" name="FEIN" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td></td><td><textarea cols="40" rows="5" name="Notes" hidden disabled onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  Statusselectoptions=["prospective","active","inactive","terminated",]
  self.response.out.write('<tr><td></td><td><select name="Status" hidden disabled onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in Statusselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')
 
  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>''')

def write_personalClient(self):
  Client=db.GqlQuery("SELECT * FROM Client WHERE userid='%s'" %(users.get_current_user().user_id())).get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <table border=0>
  <caption><h1 id="recordID">Client Profile</h1></caption>
    <form action="/StoreAClient" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Client.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s" hidden disabled readonly></td><tr>' % escape(str(Client.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="" hidden disabled readonly></td><tr>')
  if Client.date:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s" hidden disabled readonly></td><tr>' % escape(str(Client.date)))
  else:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="" hidden disabled readonly></td><tr>')
  if Client.userid:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" size="35" hidden disabled onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.userid)))
  else:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35" hidden disabled onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.CompanyName:self.response.out.write('<tr><td>Company Name</td><td><input type="text" name="CompanyName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.CompanyName)))
  else:self.response.out.write('<tr><td>Company Name</td><td><input type="text" name="CompanyName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.Phone:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.Phone)))
  else:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="Phone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.Email:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.Email)))
  else:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.ContactName:self.response.out.write('<tr><td>Contact Name</td><td><input type="text" name="ContactName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.ContactName)))
  else:self.response.out.write('<tr><td>Contact Name</td><td><input type="text" name="ContactName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.ContactPhone:self.response.out.write('<tr><td>Contact Phone</td><td><input type="text" name="ContactPhone" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.ContactPhone)))
  else:self.response.out.write('<tr><td>Contact Phone</td><td><input type="text" name="ContactPhone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.ContactEmail:self.response.out.write('<tr><td>Contact Email</td><td><input type="text" name="ContactEmail" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.ContactEmail)))
  else:self.response.out.write('<tr><td>Contact Email</td><td><input type="text" name="ContactEmail" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.Website:self.response.out.write('<tr><td>Website</td><td><input type="text" name="Website" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.Website)))
  else:self.response.out.write('<tr><td>Website</td><td><input type="text" name="Website" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.FEIN:self.response.out.write('<tr><td>FEIN</td><td><input type="text" name="FEIN" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Client.FEIN)))
  else:self.response.out.write('<tr><td>FEIN</td><td><input type="text" name="FEIN" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Client.Notes:self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes" hidden disabled onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Client.Notes))
  else:self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes" hidden disabled onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  Statusselectoptions=["prospective","active","inactive","terminated",]
  if Client.Status:
    self.response.out.write('''<tr><td>Status</td><td><select name="Status" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in Statusselectoptions:
        if Client.Status==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Status</td><td><select name="Status" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Statusselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
 
  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')


class Employee(db.Model):
    ID=db.StringProperty()
    date=db.DateTimeProperty(required=True, auto_now=True)
    userid=db.StringProperty()
    FirstName=db.StringProperty()
    LastName=db.StringProperty()
    PhoneNumber=db.StringProperty()
    Email=db.StringProperty()
    SSN=db.StringProperty()
    PayRate=db.StringProperty()
    Deductions=db.StringProperty()
    Type=db.StringProperty()
    Notes=db.TextProperty()
    Status=db.StringProperty()

EmployeeGQLSelect="SELECT * FROM Employee"
EmployeeCurrentIndex = -1;
EmployeeCount = 0;
EmployeeFieldNames=["ID","date","userid","FirstName","LastName","PhoneNumber","Email","SSN","PayRate","Deductions","Type","HireDate","TerminationDate","Notes","Status",]

def get_EmployeeGQLWHERE():
    data = memcache.get('EmployeeGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('EmployeeGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_EmployeeGQLSort():
    data = memcache.get('EmployeeGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('EmployeeGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_EmployeeCurrentIndex():
    data = memcache.get('EmployeeCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('EmployeeCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

class EmployeePage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                EmployeeData=db.GqlQuery(EmployeeGQLSelect+get_EmployeeGQLWHERE()+get_EmployeeGQLSort())
                global EmployeeCount
                EmployeeCount=EmployeeData.count()
                if get_EmployeeCurrentIndex()==-1:
                    EmployeeCurrentIndex=EmployeeCount
                    memcache.set('EmployeeCurrentIndex',EmployeeCurrentIndex,namespace=users.get_current_user().user_id())
                if EmployeeCount==0:
                    self.redirect('/NewEmployee')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(page.Body)
                    self.response.out.write(htmlMenuAdministrator)
                    write_Employee(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class FirstEmployee(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstEmployee')
    def get(self):
        EmployeeCurrentIndex = 1
        memcache.set('EmployeeCurrentIndex',EmployeeCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/EmployeePage')

class PreviousEmployee(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousEmployee')
  def get(self):
    if get_EmployeeCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/EmployeePage')
    else:
      EmployeeCurrentIndex = get_EmployeeCurrentIndex()-1
      memcache.set('EmployeeCurrentIndex',EmployeeCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/EmployeePage')

class NextEmployee(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextEmployee')
  def get(self):
    if get_EmployeeCurrentIndex() + 1 > EmployeeCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/EmployeePage')
    else:
      EmployeeCurrentIndex = get_EmployeeCurrentIndex()+1
      memcache.set('EmployeeCurrentIndex',EmployeeCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/EmployeePage')

class LastEmployee(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastEmployee')
    def get(self):
        EmployeeCurrentIndex = EmployeeCount
        memcache.set('EmployeeCurrentIndex',EmployeeCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/EmployeePage')

class NewEmployee(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewEmployee')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newEmployee(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class EmployeeTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/EmployeeTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                self.response.out.write(htmlMenuAdministrator)
                write_EmployeeTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterEmployee(webapp2.RequestHandler):
    def post(self):
        memcache.set('EmployeeGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('EmployeeCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/EmployeePage')

class FilterEmployee(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        EmployeeGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('EmployeeGQLWHERE',EmployeeGQLWHERE,namespace=users.get_current_user().user_id())
        EmployeeGQLSort=""
        memcache.set('EmployeeGQLSort',EmployeeGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('EmployeeCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/EmployeePage')

class SortEmployee(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        EmployeeGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('EmployeeGQLSort',EmployeeGQLSort,namespace=users.get_current_user().user_id())
        EmployeeGQLWHERE=""
        memcache.set('EmployeeGQLWHERE',EmployeeGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('EmployeeCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/EmployeePage')

class StoreAEmployee(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    userid=self.request.get('userid')
    FirstName=self.request.get('FirstName')
    LastName=self.request.get('LastName')
    PhoneNumber=self.request.get('PhoneNumber')
    Email=self.request.get('Email')
    SSN=self.request.get('SSN')
    PayRate=self.request.get('PayRate')
    Deductions=self.request.get('Deductions')
    Type=self.request.get('Type')
    HireDate=self.request.get('HireDate')
    TerminationDate=self.request.get('TerminationDate')
    Notes=self.request.get('Notes')
    Status=self.request.get('Status')

    self.store_a_Employee(ID,userid,FirstName,LastName,PhoneNumber,Email,SSN,PayRate,Deductions,Type,HireDate,TerminationDate,Notes,Status,)
  def store_a_Employee(self,ID,userid,FirstName,LastName,PhoneNumber,Email,SSN,PayRate,Deductions,Type,HireDate,TerminationDate,Notes,Status,):
    entry = db.GqlQuery("SELECT * FROM Employee where ID = :1", ID).get()    
    if entry:
      entry.ID=ID
      entry.userid=userid
      entry.FirstName=FirstName
      entry.LastName=LastName
      entry.PhoneNumber=PhoneNumber
      entry.Email=Email
      entry.SSN=SSN
      entry.PayRate=PayRate
      entry.Deductions=Deductions
      entry.Type=Type
      entry.HireDate=HireDate
      entry.TerminationDate=TerminationDate
      entry.Notes=Notes
      entry.Status=Status

    else:
      entry = Employee(ID=ID,userid=userid,FirstName=FirstName,LastName=LastName,PhoneNumber=PhoneNumber,Email=Email,SSN=SSN,PayRate=PayRate,Deductions=Deductions,Type=Type,HireDate=HireDate,TerminationDate=TerminationDate,Notes=Notes,Status=Status,)
      entry.ID=str(EmployeeCount+1001)
      global EmployeeCount
      EmployeeCount += 1
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/EmployeePage')

def write_Employee(self):
  if get_EmployeeCurrentIndex()<=0:
      EmployeeOffset=0
  else:
      EmployeeOffset=get_EmployeeCurrentIndex()-1
  Employee=db.GqlQuery(EmployeeGQLSelect+get_EmployeeGQLWHERE()+get_EmployeeGQLSort()).get(deadline=60, offset=EmployeeOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <h1 id="recordID">Employee</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstEmployee" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousEmployee" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextEmployee" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastEmployee" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewEmployee" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterEmployee" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/EmployeeTable">Show all in a table.</a></td>
  <td><form action="/GotoEmployee" method="post" enctype=application/x-www-form-urlencoded>Goto: <input type="text" name="recordnumber" size="2"> <input type="submit" value="Go"></form></td>
  </tr></table>
  <form id="filterform" action="/FilterEmployee" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''' %(EmployeeOffset+1,EmployeeCount))
  for f in EmployeeFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortEmployee" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in EmployeeFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>
  <table border=0>
  <caption></caption>
    <form action="/StoreAEmployee" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Employee.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(Employee.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if Employee.date:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(Employee.date)))
  else:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value=""   readonly></td><tr>')
  if Employee.userid:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.userid)))
  else:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.FirstName:self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.FirstName)))
  else:self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.LastName:self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.LastName)))
  else:self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.PhoneNumber:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="PhoneNumber" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.PhoneNumber)))
  else:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="PhoneNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.Email:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.Email)))
  else:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.SSN:self.response.out.write('<tr><td>Social Security Number</td><td><input type="text" name="SSN" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.SSN)))
  else:self.response.out.write('<tr><td>Social Security Number</td><td><input type="text" name="SSN" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.PayRate:self.response.out.write('<tr><td>Pay Rate</td><td><input type="text" name="PayRate" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.PayRate)))
  else:self.response.out.write('<tr><td>Pay Rate</td><td><input type="text" name="PayRate" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.Deductions:self.response.out.write('<tr><td>Deductions</td><td><input type="text" name="Deductions" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.Deductions)))
  else:self.response.out.write('<tr><td>Deductions</td><td><input type="text" name="Deductions" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  Typeselectoptions=["field","fieldsupervisor","office","officesupervisor","fieldmanager","officemanager","administrator",]
  if Employee.Type:
    self.response.out.write('''<tr><td>Type</td><td><select name="Type" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in Typeselectoptions:
        if Employee.Type==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Type</td><td><select name="Type" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Typeselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
  if Employee.Notes:self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Employee.Notes))
  else:self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  Statusselectoptions=["applicant","active","inactive","terminated",]
  if Employee.Status:
    self.response.out.write('''<tr><td>Status</td><td><select name="Status" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in Statusselectoptions:
        if Employee.Status==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Status</td><td><select name="Status" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Statusselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')

def write_EmployeeTable(self):
    EmployeeData = db.GqlQuery(EmployeeGQLSelect+get_EmployeeGQLWHERE()+get_EmployeeGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>date</td><td>userid</td><td>FirstName</td><td>LastName</td><td>PhoneNumber</td><td>Email</td><td>SSN</td><td>PayRate</td><td>Deductions</td><td>Type</td><td>HireDate</td><td>TerminationDate</td><td>Notes</td><td>Status</td>
</tr>''')
    for c in EmployeeData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.date,c.userid,c.FirstName,c.LastName,c.PhoneNumber,c.Email,c.SSN,c.PayRate,c.Deductions,c.Type,c.HireDate,c.TerminationDate,c.Notes,c.Status,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newEmployee(self):
  AutoNumber=EmployeeCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New Employee</b></caption>
    <form action="/StoreAEmployee" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="PhoneNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Social Security Number</td><td><input type="text" name="SSN" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Pay Rate</td><td><input type="text" name="PayRate" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Deductions</td><td><input type="text" name="Deductions" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  Typeselectoptions=["field","fieldsupervisor","office","officesupervisor","fieldmanager","officemanager","administrator",]
  self.response.out.write('<tr><td>Type</td><td><select name="Type"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in Typeselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')
  self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  Statusselectoptions=["applicant","active","inactive","terminated",]
  self.response.out.write('<tr><td>Status</td><td><select name="Status"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in Statusselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterEmployee" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(EmployeeCount)
  self.response.out.write(''' Employee(s).</table></body></html>
''')


class PersonalEmployeePage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        userid=users.get_current_user().user_id()
        if userid:
            #!query for TheUsers, check for userid, if no then make one and go on to personal*new*employee,if yes then just go on.  This will ensure we get the correct menu next / load.
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE userid='%s' LIMIT 1" %(userid))#!!
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)#!!
            MatchingUserCount=TheUserQuery.count()#!!
            if (MatchingUserCount==0):#!!
                entry=TheUsers(ID = str(db.GqlQuery("SELECT * FROM TheUsers").count()+1000),UserName = user.nickname(),userid=users.get_current_user().user_id(),Type="Employee")#!!
                entry.put()#!!
                global TheUsersCount#!!
                TheUsersCount += 1#!!
            elif (TheUser.Type!="Employee" and TheUser.Type!="Administrator"):#!!
                entry=TheUser
                entry.Type="Employee"#!!
                entry.put()#!!
                
                
            PersonalEmployeeQuery=db.GqlQuery("SELECT * FROM Employee WHERE userid='%s' LIMIT 1" %(userid))
            Person=PersonalEmployeeQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = PersonalEmployeeQuery.count()
            if (count==0):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_personalnewEmployee(self)
            else:
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_personalEmployee(self)
        else:
            self.redirect('/')

class StoreAPersonalEmployee(webapp2.RequestHandler):
  def post(self):
    userid=self.request.get('userid')
    FirstName=self.request.get('FirstName')
    LastName=self.request.get('LastName')
    PhoneNumber=self.request.get('PhoneNumber')
    Email=self.request.get('Email')
    SSN=self.request.get('SSN')
    Deductions=self.request.get('Deductions')
    Notes=self.request.get('Notes')

    self.store_a_PersonalEmployee(userid,FirstName,LastName,PhoneNumber,Email,SSN,Deductions,Notes,)
  def store_a_PersonalEmployee(self,userid,FirstName,LastName,PhoneNumber,Email,SSN,Deductions,Notes,):
    entry = db.GqlQuery("SELECT * FROM Employee where userid = :1", userid).get()    #!
    if entry:
      entry.FirstName=FirstName
      entry.LastName=LastName
      entry.PhoneNumber=PhoneNumber
      entry.Email=Email
      entry.SSN=SSN
      entry.Deductions=Deductions
      entry.Notes=Notes

    else:
      entry = Employee(ID=str(EmployeeCount+1000),userid=users.get_current_user().user_id(),FirstName=FirstName,LastName=LastName,PhoneNumber=PhoneNumber,Email=Email,SSN=SSN,PayRate='',Deductions=Deductions,Type='',HireDate='',TerminationDate='',Notes=Notes,Status='Applicant',)#!
      global EmployeeCount#!
      EmployeeCount += 1#!
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/EmployeePage')

def write_personalnewEmployee(self):
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><h1 id="recordID">New Employee Application</h1></caption>
    <form action="/StoreAPersonalEmployee" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td></td><td><input type="text" name="userid" value="%s" hidden></td></tr>' %(users.get_current_user().user_id()))
  self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="PhoneNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Social Security Number</td><td><input type="text" name="SSN" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Deductions</td><td><input type="text" name="Deductions" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>What are you good at?</td><td><textarea cols="40" rows="5" name="Notes" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>') 
  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>''')

def write_personalEmployee(self):
  Employee=db.GqlQuery("SELECT * FROM Employee WHERE userid='%s'" %(users.get_current_user().user_id())).get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <table border=0>
  <caption><h1 id="recordID">Employee Profile</h1></caption>
    <form action="/StoreAPersonalEmployee" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Employee.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s" readonly></td><tr>' % escape(str(Employee.ID)))
  if Employee.userid:self.response.out.write('<tr><td></td><td><input type="text" name="userid" value="%s" size="35" hidden readonly onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.userid)))
  else:self.response.out.write('<tr><td></td><td><input type="text" name="userid" value="error" size="35" readonly onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.FirstName:self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.FirstName)))
  else:self.response.out.write('<tr><td>First Name</td><td><input type="text" name="FirstName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.LastName:self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.LastName)))
  else:self.response.out.write('<tr><td>Last Name</td><td><input type="text" name="LastName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.PhoneNumber:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="PhoneNumber" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.PhoneNumber)))
  else:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="PhoneNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.Email:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.Email)))
  else:self.response.out.write('<tr><td>Email Address</td><td><input type="text" name="Email" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.SSN:self.response.out.write('<tr><td>Social Security Number</td><td><input type="text" name="SSN" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.SSN)))
  else:self.response.out.write('<tr><td>Social Security Number</td><td><input type="text" name="SSN" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.PayRate:self.response.out.write('<tr><td>Pay Rate</td><td><input type="text" name="PayRate" value="%s" size="35" readonly onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.PayRate)))
  else:self.response.out.write('<tr><td>Pay Rate</td><td><input type="text" name="PayRate" value="Not determined" size="35" readonly onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Employee.Deductions:self.response.out.write('<tr><td>Deductions</td><td><input type="text" name="Deductions" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Employee.Deductions)))
  else:self.response.out.write('<tr><td>Deductions</td><td><input type="text" name="Deductions" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  Typeselectoptions=["applicant","field employee","field supervisor","fieldmanager","office employee","office supervisor","office manager","administrator",]
  if Employee.Type:
    self.response.out.write('''<tr><td>Type</td><td><select name="Type" readonly onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in Typeselectoptions:
        if Employee.Type==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Type</td><td><select name="Type" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Typeselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
  if Employee.Notes:self.response.out.write('<tr><td>What are you good at?</td><td><textarea cols="40" rows="5" name="Notes" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Employee.Notes))
  else:self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  Statusselectoptions=["applicant","active","inactive","terminated",]
  if Employee.Status:
    self.response.out.write('''<tr><td>Status</td><td><select name="Status" readonly onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in Statusselectoptions:
        if Employee.Status==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Status</td><td><select name="Status" readonly onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Statusselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
 
  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')


class Supplier(db.Model):
    ID=db.StringProperty()
    date=db.DateTimeProperty(required=True, auto_now=True)
    Name=db.StringProperty()
    PhoneNumber=db.StringProperty()
    Address=db.StringProperty()
    TimeOpen=db.StringProperty()
    ContactName=db.StringProperty()
    ContactPhone=db.StringProperty()
    ContactEmail=db.StringProperty()
    TypeofService=db.StringProperty()
    Trade=db.StringProperty()
    Status=db.StringProperty()
    Notes=db.TextProperty()
    userid=db.StringProperty()

SupplierGQLSelect="SELECT * FROM Supplier"
SupplierCurrentIndex = -1;
SupplierCount = 0;
SupplierFieldNames=["ID","date","Name","PhoneNumber","Address","TimeOpen","ContactName","ContactPhone","ContactEmail","TypeofService","Trade","Status","Notes","userid",]

def get_SupplierGQLWHERE():
    data = memcache.get('SupplierGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('SupplierGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_SupplierGQLSort():
    data = memcache.get('SupplierGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('SupplierGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_SupplierCurrentIndex():
    data = memcache.get('SupplierCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('SupplierCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

class SupplierPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                SupplierData=db.GqlQuery(SupplierGQLSelect+get_SupplierGQLWHERE()+get_SupplierGQLSort())
                global SupplierCount
                SupplierCount=SupplierData.count()
                if get_SupplierCurrentIndex()==-1:
                    SupplierCurrentIndex=SupplierCount
                    memcache.set('SupplierCurrentIndex',SupplierCurrentIndex,namespace=users.get_current_user().user_id())
                if SupplierCount==0:
                    self.redirect('/NewSupplier')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(page.Body)
                    write_Supplier(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class FirstSupplier(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstSupplier')
    def get(self):
        SupplierCurrentIndex = 1
        memcache.set('SupplierCurrentIndex',SupplierCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/SupplierPage')

class PreviousSupplier(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousSupplier')
  def get(self):
    if get_SupplierCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/SupplierPage')
    else:
      SupplierCurrentIndex = get_SupplierCurrentIndex()-1
      memcache.set('SupplierCurrentIndex',SupplierCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/SupplierPage')

class NextSupplier(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextSupplier')
  def get(self):
    if get_SupplierCurrentIndex() + 1 > SupplierCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/SupplierPage')
    else:
      SupplierCurrentIndex = get_SupplierCurrentIndex()+1
      memcache.set('SupplierCurrentIndex',SupplierCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/SupplierPage')

class LastSupplier(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastSupplier')
    def get(self):
        SupplierCurrentIndex = SupplierCount
        memcache.set('SupplierCurrentIndex',SupplierCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/SupplierPage')

class NewSupplier(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewSupplier')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newSupplier(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class SupplierTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/SupplierTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_SupplierTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterSupplier(webapp2.RequestHandler):
    def post(self):
        memcache.set('SupplierGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('SupplierCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/SupplierPage')

class FilterSupplier(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        SupplierGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('SupplierGQLWHERE',SupplierGQLWHERE,namespace=users.get_current_user().user_id())
        SupplierGQLSort=""
        memcache.set('SupplierGQLSort',SupplierGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('SupplierCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/SupplierPage')

class SortSupplier(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        SupplierGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('SupplierGQLSort',SupplierGQLSort,namespace=users.get_current_user().user_id())
        SupplierGQLWHERE=""
        memcache.set('SupplierGQLWHERE',SupplierGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('SupplierCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/SupplierPage')

class StoreASupplier(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    Name=self.request.get('Name')
    PhoneNumber=self.request.get('PhoneNumber')
    Address=self.request.get('Address')
    TimeOpen=self.request.get('TimeOpen')
    ContactName=self.request.get('ContactName')
    ContactPhone=self.request.get('ContactPhone')
    ContactEmail=self.request.get('ContactEmail')
    TypeofService=self.request.get('TypeofService')
    Trade=self.request.get('Trade')
    Status=self.request.get('Status')
    Notes=self.request.get('Notes')
    userid=self.request.get('userid')

    self.store_a_Supplier(ID,Name,PhoneNumber,Address,TimeOpen,ContactName,ContactPhone,ContactEmail,TypeofService,Trade,Status,Notes,userid,)
  def store_a_Supplier(self,ID,Name,PhoneNumber,Address,TimeOpen,ContactName,ContactPhone,ContactEmail,TypeofService,Trade,Status,Notes,userid,):
    entry = db.GqlQuery("SELECT * FROM Supplier where ID = :1", ID).get()
    if entry:
      entry.ID=ID
      entry.Name=Name
      entry.PhoneNumber=PhoneNumber
      entry.Address=Address
      entry.TimeOpen=TimeOpen
      entry.ContactName=ContactName
      entry.ContactPhone=ContactPhone
      entry.ContactEmail=ContactEmail
      entry.TypeofService=TypeofService
      entry.Trade=Trade
      entry.Status=Status
      entry.Notes=Notes
      entry.userid=userid

    else:
      entry = Supplier(ID=ID,Name=Name,PhoneNumber=PhoneNumber,Address=Address,TimeOpen=TimeOpen,ContactName=ContactName,ContactPhone=ContactPhone,ContactEmail=ContactEmail,TypeofService=TypeofService,Trade=Trade,Status=Status,Notes=Notes,userid=userid,)
      entry.ID=str(SupplierCount+1001)
      global SupplierCount
      SupplierCount += 1
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/SupplierPage')

def write_Supplier(self):
  if get_SupplierCurrentIndex()<=0:
      SupplierOffset=0
  else:
      SupplierOffset=get_SupplierCurrentIndex()-1
  Supplier=db.GqlQuery(SupplierGQLSelect+get_SupplierGQLWHERE()+get_SupplierGQLSort()).get(deadline=60, offset=SupplierOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <h1 id="recordID">Supplier</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstSupplier" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousSupplier" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextSupplier" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastSupplier" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewSupplier" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterSupplier" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/SupplierTable">Show all in a table.</a></td>
  <td><form action="/GotoSupplier" method="post" enctype=application/x-www-form-urlencoded>Goto: <input type="text" name="recordnumber" size="2"> <input type="submit" value="Go"></form></td>
  </tr></table>
  <form id="filterform" action="/FilterSupplier" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''' %(SupplierOffset+1,SupplierCount))
  for f in SupplierFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortSupplier" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in SupplierFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>
  <table border=0>
  <caption></caption>
    <form action="/StoreASupplier" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Supplier.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(Supplier.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if Supplier.date:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(Supplier.date)))
  else:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value=""   readonly></td><tr>')
  if Supplier.Name:self.response.out.write('<tr><td>Name</td><td><input type="text" name="Name" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.Name)))
  else:self.response.out.write('<tr><td>Name</td><td><input type="text" name="Name" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Supplier.PhoneNumber:self.response.out.write('<tr><td>PhoneNumber</td><td><input type="text" name="PhoneNumber" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.PhoneNumber)))
  else:self.response.out.write('<tr><td>PhoneNumber</td><td><input type="text" name="PhoneNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Supplier.Address:self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.Address)))
  else:self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Supplier.TimeOpen:self.response.out.write('<tr><td>TimeOpen</td><td><input type="text" name="TimeOpen" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.TimeOpen)))
  else:self.response.out.write('<tr><td>TimeOpen</td><td><input type="text" name="TimeOpen" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Supplier.ContactName:self.response.out.write('<tr><td>Contact Name</td><td><input type="text" name="ContactName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.ContactName)))
  else:self.response.out.write('<tr><td>Contact Name</td><td><input type="text" name="ContactName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Supplier.ContactPhone:self.response.out.write('<tr><td>Contact Phone</td><td><input type="text" name="ContactPhone" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.ContactPhone)))
  else:self.response.out.write('<tr><td>Contact Phone</td><td><input type="text" name="ContactPhone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Supplier.ContactEmail:self.response.out.write('<tr><td>ContactEmail</td><td><input type="text" name="ContactEmail" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.ContactEmail)))
  else:self.response.out.write('<tr><td>ContactEmail</td><td><input type="text" name="ContactEmail" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  TypeofServiceselectoptions=["Product","Service"]
  if Supplier.TypeofService:
    self.response.out.write('''<tr><td>Type of Service</td><td><select name="TypeofService" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in TypeofServiceselectoptions:
        if Supplier.TypeofService==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Type of Service</td><td><select name="TypeofService" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in TypeofServiceselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
  Tradeselectoptions=["Transportation","Plumbing","Electrical","HVAC","Roofing","Excavating","Flooring","Concrete","Exteriors","Paint","Other",]
  if Supplier.Trade:
    self.response.out.write('''<tr><td>Trade</td><td><select name="Trade" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in Tradeselectoptions:
        if Supplier.Trade==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Trade</td><td><select name="Trade" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Tradeselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
  Statusselectoptions=["Active","Inactive","Terminated",]
  if Supplier.Status:
    self.response.out.write('''<tr><td>Status</td><td><select name="Status" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in Statusselectoptions:
        if Supplier.Status==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Status</td><td><select name="Status" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Statusselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
  if Supplier.Notes:self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Supplier.Notes))
  else:self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if Supplier.userid:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.userid)))
  else:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')

def write_SupplierTable(self):
    SupplierData = db.GqlQuery(SupplierGQLSelect+get_SupplierGQLWHERE()+get_SupplierGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>date</td><td>Name</td><td>PhoneNumber</td><td>Address</td><td>TimeOpen</td><td>ContactName</td><td>ContactPhone</td><td>ContactEmail</td><td>TypeofService</td><td>Trade</td><td>Status</td><td>Notes</td><td>userid</td>
</tr>''')
    for c in SupplierData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.date,c.Name,c.PhoneNumber,c.Address,c.TimeOpen,c.ContactName,c.ContactPhone,c.ContactEmail,c.TypeofService,c.Trade,c.Status,c.Notes,c.userid,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newSupplier(self):
  AutoNumber=SupplierCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New Supplier</b></caption>
    <form action="/StoreASupplier" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td>google userid</td><td><input type="text" name="Name" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>TimeOpen</td><td><input type="text" name="TimeOpen" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Contact Name</td><td><input type="text" name="ContactName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Contact Phone</td><td><input type="text" name="ContactPhone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>ContactEmail</td><td><input type="text" name="ContactEmail" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  TypeofServiceselectoptions=["Product","Service",]
  self.response.out.write('<tr><td>Type of Service</td><td><select name="TypeofService"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in TypeofServiceselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')
  Tradeselectoptions=["Transportation","Plumbing","Electrical","HVAC","Roofing","Excavating","Flooring","Concrete","Exteriors","Paint","Other",]
  self.response.out.write('<tr><td>Trade</td><td><select name="Trade"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in Tradeselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')
  Statusselectoptions=["Active","Inactive","Terminated",]
  self.response.out.write('<tr><td>Status</td><td><select name="Status"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in Statusselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')
  self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterSupplier" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(SupplierCount)
  self.response.out.write(''' Supplier(s).</table></body></html>
''')



class PersonalSupplierPage(webapp2.RequestHandler):
    def get(self):
        userid=users.get_current_user().user_id()
        if userid:
            PersonalSupplierQuery=db.GqlQuery("SELECT * FROM Supplier WHERE userid='%s' LIMIT 1" %(userid))
            Person=PersonalSupplierQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = PersonalSupplierQuery.count()
            if (count==0):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_personalnewSupplier(self)
            else:
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_personalSupplier(self)
        else:
            self.redirect('/')

def write_personalnewSupplier(self):
  AutoNumber=SupplierCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>New Supplier Application</b></caption>
    <form action="/StoreASupplier" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" readonly></td></tr>' %(users.get_current_user().user_id()))
  self.response.out.write('<tr><td>Name</td><td><input type="text" name="Name" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="PhoneNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Contact Name</td><td><input type="text" name="ContactName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Contact Phone Number</td><td><input type="text" name="ContactPhone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Contact Email</td><td><input type="text" name="ContactEmail" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  TypeofServiceselectoptions=["Supply","Install","Both",]
  self.response.out.write('<tr><td>Products or Service</td><td><select name="TypeofService"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in TypeofServiceselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')
  Tradeselectoptions=["Supply","Excavation","Foundations","Flatwork","Framing","Plumbing","HVAC","Electrical","Insulation","Drywall","Roofing","Exteriors","FinishCarpentry","Paint","Tile","Cabinets","Flooring","Other",]
  self.response.out.write('<tr><td>Primary Trade Category</td><td><select name="Trade"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in Tradeselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')
  Statusselectoptions=["applicant","active","inactive","terminated",]
  self.response.out.write('<tr><td></td><td><select name="Status" hidden disabled onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in Statusselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')
 
  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>''')

def write_personalSupplier(self):
  Supplier=db.GqlQuery("SELECT * FROM Supplier WHERE userid='%s'" %(users.get_current_user().user_id())).get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <table border=0>
  <caption><h1 id="recordID">Supplier Profile</h1></caption>
    <form action="/StoreASupplier" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Supplier.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s" hidden disabled readonly></td><tr>' % escape(str(Supplier.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="" hidden disabled readonly></td><tr>')
  if Supplier.date:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s" hidden disabled readonly></td><tr>' % escape(str(Supplier.date)))
  else:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="" hidden disabled readonly></td><tr>')
  if Supplier.userid:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" size="35" hidden disabled onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.userid)))
  else:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35" hidden disabled onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Supplier.Name:self.response.out.write('<tr><td>Name</td><td><input type="text" name="Name" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.Name)))
  else:self.response.out.write('<tr><td>Name</td><td><input type="text" name="Name" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Supplier.PhoneNumber:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="PhoneNumber" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.PhoneNumber)))
  else:self.response.out.write('<tr><td>Phone Number</td><td><input type="text" name="PhoneNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Supplier.ContactName:self.response.out.write('<tr><td>Contact Name</td><td><input type="text" name="ContactName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.ContactName)))
  else:self.response.out.write('<tr><td>Contact Name</td><td><input type="text" name="ContactName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Supplier.ContactPhone:self.response.out.write('<tr><td>Contact Phone Number</td><td><input type="text" name="ContactPhone" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.ContactPhone)))
  else:self.response.out.write('<tr><td>Contact Phone Number</td><td><input type="text" name="ContactPhone" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Supplier.ContactEmail:self.response.out.write('<tr><td>Contact Email</td><td><input type="text" name="ContactEmail" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.ContactEmail)))
  else:self.response.out.write('<tr><td>Contact Email</td><td><input type="text" name="ContactEmail" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Supplier.Address:self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Supplier.Address)))
  else:self.response.out.write('<tr><td>Address</td><td><input type="text" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  TypeofServiceselectoptions=["Supply","Install","Both",]
  if Supplier.TypeofService:
    self.response.out.write('''<tr><td>Products or Service</td><td><select name="TypeofService" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in TypeofServiceselectoptions:
        if Supplier.TypeofService==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Products or Service</td><td><select name="TypeofService" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in TypeofServiceselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
  Tradeselectoptions=["Supply","Excavation","Foundations","Flatwork","Framing","Plumbing","HVAC","Electrical","Insulation","Drywall","Roofing","Exteriors","FinishCarpentry","Paint","Tile","Cabinets","Flooring","Other",]
  if Supplier.Trade:
    self.response.out.write('''<tr><td>Primary Trade Category</td><td><select name="Trade" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in Tradeselectoptions:
        if Supplier.Trade==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Primary Trade Category</td><td><select name="Trade" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Tradeselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
  Statusselectoptions=["applicant","active","inactive","terminated",]
  if Supplier.Status:
    self.response.out.write('''<tr><td>Status</td><td><select name="Status" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in Statusselectoptions:
        if Supplier.Status==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Status</td><td><select name="Status" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Statusselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
 
  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')


class Material(db.Model):
    ID=db.StringProperty()
    date=db.StringProperty()
    ProductName=db.StringProperty()
    ProductDescription=db.TextProperty()
    BoxDimension1=db.StringProperty()
    BoxDimension2=db.StringProperty()
    BoxDimension3=db.StringProperty()
    Weight=db.StringProperty()
    AcquisitionCost=db.StringProperty()
    SellCost=db.StringProperty()
    SupplierID=db.StringProperty()

MaterialGQLSelect="SELECT * FROM Material"
MaterialCurrentIndex = -1;
MaterialCount = 0;
MaterialFieldNames=["ID","date","ProductName","ProductDescription","BoxDimension1","BoxDimension2","BoxDimension3","Weight","AcquisitionCost","SellCost","SupplierID",]

def get_MaterialGQLWHERE():
    data = memcache.get('MaterialGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('MaterialGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_MaterialGQLSort():
    data = memcache.get('MaterialGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('MaterialGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_MaterialCurrentIndex():
    data = memcache.get('MaterialCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('MaterialCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

class MaterialPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                MaterialData=db.GqlQuery(MaterialGQLSelect+get_MaterialGQLWHERE()+get_MaterialGQLSort())
                global MaterialCount
                MaterialCount=MaterialData.count()
                if get_MaterialCurrentIndex()==-1:
                    MaterialCurrentIndex=MaterialCount
                    memcache.set('MaterialCurrentIndex',MaterialCurrentIndex,namespace=users.get_current_user().user_id())
                if MaterialCount==0:
                    self.redirect('/NewMaterial')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(page.Body)
                    self.response.out.write(htmlMenuAdministrator)
                    write_Material(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class FirstMaterial(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstMaterial')
    def get(self):
        MaterialCurrentIndex = 1
        memcache.set('MaterialCurrentIndex',MaterialCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/MaterialPage')

class PreviousMaterial(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousMaterial')
  def get(self):
    if get_MaterialCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/MaterialPage')
    else:
      MaterialCurrentIndex = get_MaterialCurrentIndex()-1
      memcache.set('MaterialCurrentIndex',MaterialCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/MaterialPage')

class NextMaterial(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextMaterial')
  def get(self):
    if get_MaterialCurrentIndex() + 1 > MaterialCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/MaterialPage')
    else:
      MaterialCurrentIndex = get_MaterialCurrentIndex()+1
      memcache.set('MaterialCurrentIndex',MaterialCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/MaterialPage')

class LastMaterial(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastMaterial')
    def get(self):
        MaterialCurrentIndex = MaterialCount
        memcache.set('MaterialCurrentIndex',MaterialCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/MaterialPage')

class NewMaterial(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewMaterial')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newMaterial(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class MaterialTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/MaterialTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                self.response.out.write(htmlMenuAdministrator)
                write_MaterialTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterMaterial(webapp2.RequestHandler):
    def post(self):
        memcache.set('MaterialGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('MaterialCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/MaterialPage')

class FilterMaterial(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        MaterialGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('MaterialGQLWHERE',MaterialGQLWHERE,namespace=users.get_current_user().user_id())
        MaterialGQLSort=""
        memcache.set('MaterialGQLSort',MaterialGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('MaterialCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/MaterialPage')

class SortMaterial(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        MaterialGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('MaterialGQLSort',MaterialGQLSort,namespace=users.get_current_user().user_id())
        MaterialGQLWHERE=""
        memcache.set('MaterialGQLWHERE',MaterialGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('MaterialCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/MaterialPage')

class StoreAMaterial(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    ProductName=self.request.get('ProductName')
    ProductDescription=self.request.get('ProductDescription')
    BoxDimension1=self.request.get('BoxDimension1')
    BoxDimension2=self.request.get('BoxDimension2')
    BoxDimension3=self.request.get('BoxDimension3')
    Weight=self.request.get('Weight')
    AcquisitionCost=self.request.get('AcquisitionCost')
    SellCost=self.request.get('SellCost')
    SupplierID=self.request.get('SupplierID')

    self.store_a_Material(ID,ProductName,ProductDescription,BoxDimension1,BoxDimension2,BoxDimension3,Weight,AcquisitionCost,SellCost,SupplierID,)
  def store_a_Material(self,ID,ProductName,ProductDescription,BoxDimension1,BoxDimension2,BoxDimension3,Weight,AcquisitionCost,SellCost,SupplierID,):
    entry = db.GqlQuery("SELECT * FROM Material where ID = :1", ID).get()
    if entry:
      entry.ID=ID
      entry.ProductName=ProductName
      entry.ProductDescription=ProductDescription
      entry.BoxDimension1=BoxDimension1
      entry.BoxDimension2=BoxDimension2
      entry.BoxDimension3=BoxDimension3
      entry.Weight=Weight
      entry.AcquisitionCost=AcquisitionCost
      entry.SellCost=SellCost
      entry.SupplierID=SupplierID

    else:
      entry = Material(ID=ID,ProductName=ProductName,ProductDescription=ProductDescription,BoxDimension1=BoxDimension1,BoxDimension2=BoxDimension2,BoxDimension3=BoxDimension3,Weight=Weight,AcquisitionCost=AcquisitionCost,SellCost=SellCost,SupplierID=SupplierID,)
      entry.ID=str(MaterialCount+1001)
      global MaterialCount
      MaterialCount += 1
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/MaterialPage')

def write_Material(self):
  if get_MaterialCurrentIndex()<=0:
      MaterialOffset=0
  else:
      MaterialOffset=get_MaterialCurrentIndex()-1
  Material=db.GqlQuery(MaterialGQLSelect+get_MaterialGQLWHERE()+get_MaterialGQLSort()).get(deadline=60, offset=MaterialOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <h1 id="recordID">Material</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstMaterial" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousMaterial" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextMaterial" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastMaterial" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewMaterial" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterMaterial" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/MaterialTable">Show all in a table.</a></td>
  <td><form action="/GotoMaterial" method="post" enctype=application/x-www-form-urlencoded>Goto: <input type="text" name="recordnumber" size="2"> <input type="submit" value="Go"></form></td>
  </tr></table>
  <form id="filterform" action="/FilterMaterial" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''' %(MaterialOffset+1,MaterialCount))
  for f in MaterialFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortMaterial" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in MaterialFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>
  <table border=0>
  <caption></caption>
    <form action="/StoreAMaterial" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Material.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(Material.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if Material.date:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(Material.date)))
  else:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value=""   readonly></td><tr>')
  if Material.ProductName:self.response.out.write('<tr><td>Product Name</td><td><input type="text" name="ProductName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Material.ProductName)))
  else:self.response.out.write('<tr><td>Product Name</td><td><input type="text" name="ProductName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Material.ProductDescription:self.response.out.write('<tr><td>Product Description</td><td><textarea cols="40" rows="5" name="ProductDescription"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Material.ProductDescription))
  else:self.response.out.write('<tr><td>Product Description</td><td><textarea cols="40" rows="5" name="ProductDescription"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if Material.BoxDimension1:self.response.out.write('<tr><td>Dimension X</td><td><input type="text" name="BoxDimension1" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Material.BoxDimension1)))
  else:self.response.out.write('<tr><td>Dimension X</td><td><input type="text" name="BoxDimension1" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Material.BoxDimension2:self.response.out.write('<tr><td>Dimension Y</td><td><input type="text" name="BoxDimension2" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Material.BoxDimension2)))
  else:self.response.out.write('<tr><td>Dimension Y</td><td><input type="text" name="BoxDimension2" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Material.BoxDimension3:self.response.out.write('<tr><td>Dimension Z</td><td><input type="text" name="BoxDimension3" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Material.BoxDimension3)))
  else:self.response.out.write('<tr><td>Dimension Z</td><td><input type="text" name="BoxDimension3" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Material.Weight:self.response.out.write('<tr><td>Weight</td><td><input type="text" name="Weight" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Material.Weight)))
  else:self.response.out.write('<tr><td>Weight</td><td><input type="text" name="Weight" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Material.AcquisitionCost:self.response.out.write('<tr><td>Acquisition Cost</td><td><input type="text" name="AcquisitionCost" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Material.AcquisitionCost)))
  else:self.response.out.write('<tr><td>Acquisition Cost</td><td><input type="text" name="AcquisitionCost" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Material.SellCost:self.response.out.write('<tr><td>Sell Cost</td><td><input type="text" name="SellCost" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Material.SellCost)))
  else:self.response.out.write('<tr><td>Sell Cost</td><td><input type="text" name="SellCost" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  SupplierIDselectoptions=db.GqlQuery("SELECT * FROM Supplier")
  if Material.SupplierID:
    self.response.out.write('''<tr><td>Preferred Supplier</td><td><select name="SupplierID"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in SupplierIDselectoptions:
        if Material.SupplierID==c.ID:
            self.response.out.write('<option value="%s" selected>' % escape(c.ID))
            self.response.out.write('%s</option>' % escape(c.Name))
        else:
            self.response.out.write('<option value="%s">' % escape(c.ID))
            self.response.out.write('%s</option>' % escape(c.Name))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Preferred Supplier</td><td><select name="SupplierID"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in SupplierIDselectoptions:
        self.response.out.write('<option value="%s">' % escape(c.ID))
        self.response.out.write('%s</option>' % escape(c.Name))
    self.response.out.write('</select></td><td></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')

def write_MaterialTable(self):
    MaterialData = db.GqlQuery(MaterialGQLSelect+get_MaterialGQLWHERE()+get_MaterialGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>date</td><td>ProductName</td><td>ProductDescription</td><td>BoxDimension1</td><td>BoxDimension2</td><td>BoxDimension3</td><td>Weight</td><td>AcquisitionCost</td><td>SellCost</td><td>SupplierID</td>
</tr>''')
    for c in MaterialData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.date,c.ProductName,c.ProductDescription,c.BoxDimension1,c.BoxDimension2,c.BoxDimension3,c.Weight,c.AcquisitionCost,c.SellCost,c.SupplierID,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newMaterial(self):
  AutoNumber=MaterialCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New Material</b></caption>
    <form action="/StoreAMaterial" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>Product Name</td><td><input type="text" name="ProductName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Product Description</td><td><textarea cols="40" rows="5" name="ProductDescription"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>Dimension X</td><td><input type="text" name="BoxDimension1" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Dimension Y</td><td><input type="text" name="BoxDimension2" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Dimension Z</td><td><input type="text" name="BoxDimension3" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Weight</td><td><input type="text" name="Weight" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Acquisition Cost</td><td><input type="text" name="AcquisitionCost" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Sell Cost</td><td><input type="text" name="SellCost" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterMaterial" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(MaterialCount)
  self.response.out.write(''' Material(s).</table></body></html>
''')


class Processor(db.Model):
    ID=db.StringProperty()
    date=db.DateTimeProperty(required=True, auto_now=True)
    userid=db.StringProperty()
    EmployeeNumber=db.StringProperty()

ProcessorGQLSelect="SELECT * FROM Processor"
ProcessorCurrentIndex = -1;
ProcessorCount = 0;
ProcessorFieldNames=["ID","date","userid","EmployeeNumber",]

def get_ProcessorGQLWHERE():
    data = memcache.get('ProcessorGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('ProcessorGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_ProcessorGQLSort():
    data = memcache.get('ProcessorGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('ProcessorGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_ProcessorCurrentIndex():
    data = memcache.get('ProcessorCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('ProcessorCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

class ProcessorPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' ):
                ProcessorData=db.GqlQuery(ProcessorGQLSelect+get_ProcessorGQLWHERE()+get_ProcessorGQLSort())
                global ProcessorCount
                ProcessorCount=ProcessorData.count()
                if get_ProcessorCurrentIndex()==-1:
                    ProcessorCurrentIndex=ProcessorCount
                    memcache.set('ProcessorCurrentIndex',ProcessorCurrentIndex,namespace=users.get_current_user().user_id())
                if ProcessorCount==0:
                    self.redirect('/NewProcessor')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(page.Body)
                    write_Processor(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class FirstProcessor(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstProcessor')
    def get(self):
        ProcessorCurrentIndex = 1
        memcache.set('ProcessorCurrentIndex',ProcessorCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/ProcessorPage')

class PreviousProcessor(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousProcessor')
  def get(self):
    if get_ProcessorCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/ProcessorPage')
    else:
      ProcessorCurrentIndex = get_ProcessorCurrentIndex()-1
      memcache.set('ProcessorCurrentIndex',ProcessorCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/ProcessorPage')

class NextProcessor(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextProcessor')
  def get(self):
    if get_ProcessorCurrentIndex() + 1 > ProcessorCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/ProcessorPage')
    else:
      ProcessorCurrentIndex = get_ProcessorCurrentIndex()+1
      memcache.set('ProcessorCurrentIndex',ProcessorCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/ProcessorPage')

class LastProcessor(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastProcessor')
    def get(self):
        ProcessorCurrentIndex = ProcessorCount
        memcache.set('ProcessorCurrentIndex',ProcessorCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/ProcessorPage')

class NewProcessor(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewProcessor')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newProcessor(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class ProcessorTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/ProcessorTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_ProcessorTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterProcessor(webapp2.RequestHandler):
    def post(self):
        memcache.set('ProcessorGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('ProcessorCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/ProcessorPage')

class FilterProcessor(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        ProcessorGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('ProcessorGQLWHERE',ProcessorGQLWHERE,namespace=users.get_current_user().user_id())
        ProcessorGQLSort=""
        memcache.set('ProcessorGQLSort',ProcessorGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('ProcessorCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/ProcessorPage')

class SortProcessor(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        ProcessorGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('ProcessorGQLSort',ProcessorGQLSort,namespace=users.get_current_user().user_id())
        ProcessorGQLWHERE=""
        memcache.set('ProcessorGQLWHERE',ProcessorGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('ProcessorCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/ProcessorPage')

class StoreAProcessor(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    userid=self.request.get('userid')
    EmployeeNumber=self.request.get('EmployeeNumber')

    self.store_a_Processor(ID,userid,EmployeeNumber,)
  def store_a_Processor(self,ID,userid,EmployeeNumber,):
    entry = db.GqlQuery("SELECT * FROM Processor where ID = :1", ID).get()
    if entry:
      entry.ID=ID
      entry.userid=userid
      entry.EmployeeNumber=EmployeeNumber

    else:
      entry = Processor(ID=ID,userid=userid,EmployeeNumber=EmployeeNumber,)
      entry.ID=str(ProcessorCount+1001)
      global ProcessorCount
      ProcessorCount += 1
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/ProcessorPage')

def write_Processor(self):
  if get_ProcessorCurrentIndex()<=0:
      ProcessorOffset=0
  else:
      ProcessorOffset=get_ProcessorCurrentIndex()-1
  Processor=db.GqlQuery(ProcessorGQLSelect+get_ProcessorGQLWHERE()+get_ProcessorGQLSort()).get(deadline=60, offset=ProcessorOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <h1 id="recordID">Processor</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstProcessor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousProcessor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextProcessor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastProcessor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewProcessor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterProcessor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/ProcessorTable">Show all in a table.</a></td>
  
  </tr></table>
  <form id="filterform" action="/FilterProcessor" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''' %(ProcessorOffset+1,ProcessorCount))
  for f in ProcessorFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortProcessor" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in ProcessorFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>
  <table border=0>
  <caption></caption>
    <form action="/StoreAProcessor" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Processor.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(Processor.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if Processor.date:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(Processor.date)))
  else:self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value=""   readonly></td><tr>')
  if Processor.userid:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Processor.userid)))
  else:self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Processor.EmployeeNumber:self.response.out.write('<tr><td>Employee Number</td><td><input type="text" name="EmployeeNumber" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Processor.EmployeeNumber)))
  else:self.response.out.write('<tr><td>Employee Number</td><td><input type="text" name="EmployeeNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')

def write_ProcessorTable(self):
    ProcessorData = db.GqlQuery(ProcessorGQLSelect+get_ProcessorGQLWHERE()+get_ProcessorGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>date</td><td>userid</td><td>EmployeeNumber</td>
</tr>''')
    for c in ProcessorData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.date,c.userid,c.EmployeeNumber,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newProcessor(self):
  AutoNumber=ProcessorCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New Processor</b></caption>
    <form action="/StoreAProcessor" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>Modified Date</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td>google userid</td><td><input type="text" name="userid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Employee Number</td><td><input type="text" name="EmployeeNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterProcessor" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(ProcessorCount)
  self.response.out.write(''' Processor(s).</table></body></html>
''')


class PersonalProcessorPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        userid=users.get_current_user().user_id()
        if userid:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE userid='%s' LIMIT 1" %(userid))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            MatchingUserCount=TheUserQuery.count()
            if (MatchingUserCount==0):
                entry=TheUsers(ID = str(db.GqlQuery("SELECT * FROM TheUsers").count()+1000),UserName = user.nickname(),userid=users.get_current_user().user_id(),Type="Processor")
                entry.put()
                global TheUsersCount
                TheUsersCount += 1
            elif (TheUser.Type!="Processor" and TheUser.Type!="Administrator"):
                entry=TheUser
                entry.Type="Processor"
                entry.put()


            PersonalProcessorQuery=db.GqlQuery("SELECT * FROM Processor WHERE userid='%s' LIMIT 1" %(userid))
            Person=PersonalProcessorQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = PersonalProcessorQuery.count()
            if (count==0):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_personalnewProcessor(self)
            else:
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_personalProcessor(self)
        else:
            self.redirect('/')

def write_personalProcessor(self):
  Processor=db.GqlQuery("SELECT * FROM Processor WHERE userid='%s'" %(users.get_current_user().user_id())).get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <table border=0>
  <caption><h1 id="recordID">Processor Profile</h1></caption>
    <form action="/StoreAPersonalProcessor" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
 
  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')
def write_personalnewProcessor(self):
  AutoNumber=ProcessorCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>New Processor Application</b></caption>
    <form action="/StoreAPersonalProcessor" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
 
  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>''')

class StoreAPersonalProcessor(webapp2.RequestHandler):
  def post(self):


    self.store_a_PersonalProcessor()
  def store_a_PersonalProcessor(self,):
    entry = db.GqlQuery("SELECT * FROM Processor where userid = :1", users.get_current_user().user_id()).get()
    if entry:
        StatusBar = "todo: fix code for store_a_PersonalProcessor"
        self.redirect('/ProcessorPage')
    else:
      entry = Processor(ID=str(ProcessorCount+1000),userid=users.get_current_user().user_id(),)
      global ProcessorCount#!
      ProcessorCount += 1#!
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/ProcessorPage')


class Property(db.Model):
    ID=db.StringProperty()
    date=db.DateTimeProperty(required=False, auto_now=True)
    Address=db.StringProperty()
    City=db.StringProperty()
    ClientPropertyID=db.StringProperty()
    HouseNumber=db.StringProperty()
    State=db.StringProperty()
    Zip=db.StringProperty()
    latitude=db.StringProperty()
    longitude=db.StringProperty()
    BidDetails=db.TextProperty()
    Notes=db.TextProperty()
    LotSize=db.TextProperty(indexed=False)

PropertyGQLSelect="SELECT * FROM Property"
PropertyCurrentIndex = -1;
PropertyCount = 0;
PropertyFieldNames=["ID","date","Address","City","ClientPropertyID","HouseNumber","State","Zip","latitude","longitude","BidDetails","Notes","LotSize"]

def get_PropertyGQLWHERE():
    data = memcache.get('PropertyGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('PropertyGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_PropertyGQLSort():
    data = memcache.get('PropertyGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('PropertyGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_PropertyCurrentIndex():
    data = memcache.get('PropertyCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('PropertyCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

class PropertyPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                PropertyData=db.GqlQuery(PropertyGQLSelect+get_PropertyGQLWHERE()+get_PropertyGQLSort())
                global PropertyCount
                PropertyCount=PropertyData.count()
                if get_PropertyCurrentIndex()==-1:
                    PropertyCurrentIndex=PropertyCount
                    memcache.set('PropertyCurrentIndex',PropertyCurrentIndex,namespace=users.get_current_user().user_id())
                if PropertyCount==0:
                    self.redirect('/NewProperty')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    
                    Bid=db.GqlQuery("SELECT * FROM Bid ORDER BY Nominal ASC")
                    TempQuantityCodes=""
                    TempUnitCosts=""
                    for b in Bid:
                        TempQuantityCodes+='"%s",' %(b.QuantityCode)
                        TempUnitCosts+='"%s",' %(b.UnitCost)
                    self.response.out.write('''<script>var QuantityCodes=[%s];
var UnitCosts=[%s];</script>
''' % (TempQuantityCodes,TempUnitCosts))
                    
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuAdministrator)
                    self.response.out.write(page.Body)
                    write_Property(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)
            
class FirstProperty(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstProperty')
    def get(self):
        PropertyCurrentIndex = 1
        memcache.set('PropertyCurrentIndex',PropertyCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/PropertyPage')

class PreviousProperty(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousProperty')
  def get(self):
    if get_PropertyCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/PropertyPage')
    else:
      PropertyCurrentIndex = get_PropertyCurrentIndex()-1
      memcache.set('PropertyCurrentIndex',PropertyCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/PropertyPage')

class NextProperty(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextProperty')
  def get(self):
    if get_PropertyCurrentIndex() + 1 > PropertyCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/PropertyPage')
    else:
      PropertyCurrentIndex = get_PropertyCurrentIndex()+1
      memcache.set('PropertyCurrentIndex',PropertyCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/PropertyPage')

class LastProperty(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastProperty')
    def get(self):
        PropertyCurrentIndex = PropertyCount
        memcache.set('PropertyCurrentIndex',PropertyCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/PropertyPage')

class NewProperty(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewProperty')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newProperty(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class PropertyTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/PropertyTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_PropertyTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterProperty(webapp2.RequestHandler):
    def post(self):
        memcache.set('PropertyGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('PropertyCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/PropertyPage')

class GotoProperty(webapp2.RequestHandler):
    def post(self):
        recordnumber=self.request.get('recordnumber')
        memcache.set('PropertyCurrentIndex',int(recordnumber),namespace=users.get_current_user().user_id())
        self.redirect('/PropertyPage')

class SelectProperty(webapp2.RequestHandler):
    def post(self):
        offset=self.request.get('SelectRecent')
        memcache.set('PropertyCurrentIndex',int(offset)-1000,namespace=users.get_current_user().user_id())
        self.redirect('/PropertyPage')

class FilterProperty(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        PropertyGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('PropertyGQLWHERE',PropertyGQLWHERE,namespace=users.get_current_user().user_id())
        PropertyGQLSort=""
        memcache.set('PropertyGQLSort',PropertyGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('PropertyCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/PropertyPage')

class SortProperty(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        PropertyGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('PropertyGQLSort',PropertyGQLSort,namespace=users.get_current_user().user_id())
        PropertyGQLWHERE=""
        memcache.set('PropertyGQLWHERE',PropertyGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('PropertyCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/PropertyPage')

class StoreAProperty(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    Address=self.request.get('Address')
    City=self.request.get('City')
    ClientPropertyID=self.request.get('ClientPropertyID')
    HouseNumber=self.request.get('HouseNumber')
    State=self.request.get('State')
    Zip=self.request.get('Zip')
    latitude=self.request.get('latitude')
    longitude=self.request.get('longitude')
    BidDetails=self.request.get('BidDetails')
    Notes=self.request.get('Notes')
    LotSize=self.request.get('LotSize')

    self.store_a_Property(ID,Address,City,ClientPropertyID,HouseNumber,State,Zip,latitude,longitude,BidDetails,Notes,LotSize)
  def store_a_Property(self,ID,Address,City,ClientPropertyID,HouseNumber,State,Zip,latitude,longitude,BidDetails,Notes,LotSize):
    entry = db.GqlQuery("SELECT * FROM Property where ID = :1", ID).get()
    if entry:
      entry.ID=ID
      entry.Address=Address
      entry.City=City
      entry.ClientPropertyID=ClientPropertyID
      entry.HouseNumber=HouseNumber
      entry.State=State
      entry.Zip=Zip
      entry.latitude=latitude
      entry.longitude=longitude
      entry.BidDetails=BidDetails
      entry.Notes=Notes
      entry.LotSize=LotSize

    else:
      entry = Property(ID=ID,Address=Address,City=City,ClientPropertyID=ClientPropertyID,HouseNumber=HouseNumber,State=State,Zip=Zip,latitude=latitude,longitude=longitude,BidDetails=BidDetails,Notes=Notes,LotSize=LotSize)
      entry.ID=str(PropertyCount+1001)
      global PropertyCount
      PropertyCount += 1
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/PropertyPage')

def write_Property(self):
  if get_PropertyCurrentIndex()<=0:
      PropertyOffset=0
  else:
      PropertyOffset=get_PropertyCurrentIndex()-1
  RecentProperties=db.GqlQuery('SELECT * FROM Property ORDER BY date DESC LIMIT 40')
  Property=db.GqlQuery(PropertyGQLSelect+get_PropertyGQLWHERE()+get_PropertyGQLSort()).get(deadline=60, offset=PropertyOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)

  Bid=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Interior' AND Category='removal' ORDER BY Location ASC, Nominal ASC")

  BidExtYard=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Interior' AND Category='Yard' ORDER BY Location ASC, Nominal ASC")
  BidExtRemoval=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Interior' AND Category='removal' ORDER BY Location ASC, Nominal ASC")
  BidExtOpenings=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Interior' AND Category='openings' ORDER BY Location ASC, Nominal ASC")
  BidExtLocks=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Interior' AND Category='locks' ORDER BY Location ASC, Nominal ASC")
  BidExtConstruction=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Interior' AND Category='construction' ORDER BY Location ASC, Nominal ASC")
  BidExtPlumbing=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Interior' AND Category='plumbing' ORDER BY Location ASC, Nominal ASC")
  BidExtElectrical=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Interior' AND Category='electrical' ORDER BY Location ASC, Nominal ASC")
  BidExtPool=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Interior' AND Category='pool' ORDER BY Location ASC, Nominal ASC")
  BidIntRemoval=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Exterior' AND Category='removal' ORDER BY Location ASC, Nominal ASC")
  BidIntConstruction=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Exterior' AND Category='construction' ORDER BY Location ASC, Nominal ASC")
  BidIntPlumbing=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Exterior' AND Category='plumbing' ORDER BY Location ASC, Nominal ASC")
  BidIntElectrical=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Exterior' AND Category='electrical' ORDER BY Location ASC, Nominal ASC")
  BidIntMold=db.GqlQuery("SELECT * FROM Bid WHERE Location!='Exterior' AND Category='mold' ORDER BY Location ASC, Nominal ASC")
  self.response.out.write('''
  <h1 id="recordID">Property</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstProperty" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousProperty" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextProperty" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastProperty" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewProperty" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterProperty" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/PropertyTable">Show all in a table.</a></td>
  <td><form action="/GotoProperty" method="post" enctype=application/x-www-form-urlencoded>Goto: <input type="text" name="recordnumber" size="2"> <input type="submit" value="Go"></form></td>
  </tr></table>

  <form id="QuickSelectProperty" action="/SelectProperty" method="post" enctype=application/x-www-form-urlencoded>Select Recent:
  <select name="SelectRecent" id="SelectRecent">''' %(PropertyOffset+1,PropertyCount))
  for r in RecentProperties:
      self.response.out.write('<option value="%s">%s - %s</option>' % (r.ID,r.City,r.Address))
  self.response.out.write('''</select></td><td><input type="submit" value="Go"></form>
  
  <form id="filterform" action="/FilterProperty" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''')
  for f in PropertyFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortProperty" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in PropertyFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>
  <table border=0>
  <caption></caption>
    <form action="/StoreAProperty" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Property.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(Property.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if Property.date:self.response.out.write('<tr><td>date</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(Property.date)))
  else:self.response.out.write('<tr><td>date</td><td><input type="text" name="date" value=""   readonly></td><tr>')
  if Property.Address:self.response.out.write('<tr><td>Address</td><td><input type="text" id="Address" name="Address" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="button" id="googlepropertyaddress" onclick="googleitproperty()" value="google it."></input></td><tr>' % escape(str(Property.Address)))
  else:self.response.out.write('<tr><td>Address</td><td><input type="text" id="Address" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="button" id="googlepropertyaddress" onclick="googleitproperty()" value="google it."></input></td><tr>')
  if Property.City:self.response.out.write('<tr><td>City</td><td><input type="text" name="City" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Property.City)))
  else:self.response.out.write('<tr><td>City</td><td><input type="text" name="City" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Property.ClientPropertyID:self.response.out.write('<tr><td>Client Property ID</td><td><input type="text" name="ClientPropertyID" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Property.ClientPropertyID)))
  else:self.response.out.write('<tr><td>Client Property ID</td><td><input type="text" name="ClientPropertyID" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Property.HouseNumber:self.response.out.write('<tr><td>House Number</td><td><input type="text" name="HouseNumber" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Property.HouseNumber)))
  else:self.response.out.write('<tr><td>House Number</td><td><input type="text" name="HouseNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Property.State:self.response.out.write('<tr><td>State</td><td><input type="text" name="State" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Property.State)))
  else:self.response.out.write('<tr><td>State</td><td><input type="text" name="State" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Property.Zip:self.response.out.write('<tr><td>Zip</td><td><input type="text" name="Zip" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Property.Zip)))
  else:self.response.out.write('<tr><td>Zip</td><td><input type="text" name="Zip" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Property.latitude:self.response.out.write('<tr><td>latitude</td><td><input type="text" name="latitude" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Property.latitude)))
  else:self.response.out.write('<tr><td>latitude</td><td><input type="text" name="latitude" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Property.longitude:self.response.out.write('<tr><td>longitude</td><td><input type="text" name="longitude" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Property.longitude)))
  else:self.response.out.write('<tr><td>longitude</td><td><input type="text" name="longitude" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Property.LotSize:self.response.out.write('<tr><td>LotSize</td><td><input type="text" name="LotSize" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Property.LotSize)))
  else:self.response.out.write('<tr><td>LotSize (43560 per acre)</td><td><input type="text" name="LotSize" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  
  self.response.out.write('''<tr><td>Exterior BIDS:</td></tr>''')
  
  self.response.out.write('''<tr><td>Yard</td><td><select Id="SelectBids1" name="SelectBids1"><option value='0'></option>''')  
  for b in BidExtYard:
      self.response.out.write('''<option value=%s>%s - %s</option>''' % (b.Nominal,b.Nominal,b.Verbiage))
  self.response.out.write('''</select>''')
  
  self.response.out.write('''<tr><td>Removal</td><td><select Id="SelectBids2" name="SelectBids2"><option value='0'></option>''')  
  for b in BidExtRemoval:
      self.response.out.write('''<option value=%s>%s - %s</option>''' % (b.Nominal,b.Nominal,b.Verbiage))
  self.response.out.write('''</select>''')

  
  self.response.out.write('''<tr><td>Quantity</td><td> #1<input type="text" Id="quantity1" value="" size="6"> #2<input type="text" Id="quantity2" value="" size="6"><input type="button" value="Add Bid" onclick="AddBid()"></input></td>''')
  

  if Property.BidDetails:self.response.out.write('<tr><td>Bid Details</td><td><textarea cols="40" rows="5" Id="BidDetails" name="BidDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Property.BidDetails))
  else:self.response.out.write('<tr><td>Bid Details</td><td><textarea cols="40" rows="5" Id="BidDetails" name="BidDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if Property.Notes:self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Property.Notes))
  else:self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')

def write_PropertyTable(self):
    PropertyData = db.GqlQuery(PropertyGQLSelect+get_PropertyGQLWHERE()+get_PropertyGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>date</td><td>Address</td><td>City</td><td>ClientPropertyID</td><td>HouseNumber</td><td>State</td><td>Zip</td><td>latitude</td><td>longitude</td><td>BidDetails</td><td>Notes</td>
</tr>''')
    for c in PropertyData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.date,c.Address,c.City,c.ClientPropertyID,c.HouseNumber,c.State,c.Zip,c.latitude,c.longitude,c.BidDetails,c.Notes,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newProperty(self):
  AutoNumber=PropertyCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New Property</b></caption>
    <form action="/StoreAProperty" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>date</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td>Address</td><td><input type="text" id="Address" name="Address" value="" size="35"   onfocus="activeinputFunction(this)" onblur="parseaddress();inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>City</td><td><input type="text" id="City" name="City" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Client Property ID</td><td><input type="text" name="ClientPropertyID" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>House Number</td><td><input type="text" id="HouseNumber" name="HouseNumber" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>State</td><td><input type="text" id="State" name="State" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Zip</td><td><input type="text" id="Zip" name="Zip" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>latitude</td><td><input type="text" name="latitude" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>longitude</td><td><input type="text" name="longitude" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>LotSize (43560 per acre)</td><td><input type="text" name="LotSize" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')  
  self.response.out.write('<tr><td>Bid Details</td><td><textarea cols="40" rows="5" name="BidDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterProperty" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(PropertyCount)
  self.response.out.write(''' Property(s).</table></body></html>
''')


class WorkOrder(db.Model):
    ID=db.StringProperty()
    date=db.DateTimeProperty(required=True, auto_now=True)
    Client=db.StringProperty()
    ClientWO=db.StringProperty()
    Property=db.StringProperty()
    PropertyAddress=db.StringProperty()
    ManagingEmployee=db.StringProperty()
    DateOrdered=db.StringProperty()
    DateDue=db.StringProperty()
    DateScheduled=db.StringProperty()
    DateCompleted=db.StringProperty()
    DatePaid=db.StringProperty()
    InvoiceDetails=db.TextProperty()
    InvoiceAmount=db.StringProperty()
    DisputeDetails=db.TextProperty()
    MaterialDetails=db.TextProperty()
    CostOfMaterial=db.StringProperty()
    EquipmentDetails=db.TextProperty()
    CostOfEquipment=db.StringProperty()
    LaborDetails=db.TextProperty()
    CostOfLabor=db.StringProperty()
    EarningHours=db.StringProperty()
    Notes=db.TextProperty()
    TaskQueue=db.TextProperty()
    CompletionNote=db.TextProperty()
    MilesDetails=db.TextProperty()
    MilesTotal=db.StringProperty()
    CostOfMiles=db.StringProperty()
    CostOfAdministration=db.StringProperty()

    City=db.StringProperty()
    HouseNumber=db.StringProperty()
    LotSize=db.StringProperty(indexed=False)
    PaidAmount=db.StringProperty()
    Status=db.StringProperty()
    Type=db.StringProperty()
    KickBack=db.StringProperty()
    InDispute=db.StringProperty()

WorkOrderGQLSelect="SELECT * FROM WorkOrder"
WorkOrderCurrentIndex = -1;
WorkOrderCount = 0;
WorkOrderFieldNames=["ID","date","Client","ClientWO","Property","PropertyAddress","ManagingEmployee","DateOrdered","DateDue","DateScheduled","DateCompleted","DatePaid","InvoiceDetails","InvoiceAmount","DisputeDetails","MaterialDetails","CostOfMaterial","EquipmentDetails","CostOfEquipment","LaborDetails","CostOfLabor","EarningHours","Notes","TaskQueue","CompletionNote","MilesDetails","MilesTotal","CostOfMiles","CostOfAdministration","City","HouseNumber","LotSize","PaidAmount","Status","Type","KickBack","InDispute"]

def get_WorkOrderGQLWHERE():
    data = memcache.get('WorkOrderGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('WorkOrderGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_WorkOrderGQLSort():
    data = memcache.get('WorkOrderGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('WorkOrderGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_WorkOrderCurrentIndex():
    data = memcache.get('WorkOrderCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('WorkOrderCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

def getcsv_RecentWorkOrders():
    data = memcache.get('RecentWorkOrders', namespace=users.get_current_user().user_id())
    if data is None:
        data=""
        dbdata = db.GqlQuery('SELECT * FROM WorkOrder ORDER BY ID DESC LIMIT 300')
        for d in dbdata:
            data+=d.ID+"|"+d.ClientWO+"|"+d.Type+"|"+d.Status+"|"+d.PropertyAddress+"|"
        memcache.add('RecentWorkOrders', data, 60, namespace=users.get_current_user().user_id())
    data=data.split("|")
    return data

def getcsv_OpenWorkOrders():
    data = memcache.get('OpenWorkOrders', namespace=users.get_current_user().user_id())
    if data is None:
        data=""
        dbdata = db.GqlQuery('SELECT * FROM WorkOrder ORDER BY ID DESC LIMIT 200')
        for d in dbdata:
            if d.Status=='Ordered' or d.Status=='Scheduled' or d.Status=='KickedBack':
                data+=d.ID+"|"+d.ClientWO+"|"+d.Type+"|"+d.Status+"|"+d.PropertyAddress+"|"+d.DateDue+"|"
        memcache.add('OpenWorkOrders', data, 60, namespace=users.get_current_user().user_id())
    data=data.split("|")
    return data    

def getcsv_Properties():
    data = memcache.get('Propertyselectoptions', namespace=users.get_current_user().user_id())
    if data is None:
        data=""
        dbdata = db.GqlQuery("SELECT * FROM Property ORDER BY Address ASC")
        for d in dbdata:
            data+=d.ID+"|"+d.Address+"|"+d.City+"|"+d.HouseNumber+"|"
        memcache.add('Propertyselectoptions', data, 60, namespace=users.get_current_user().user_id())
    data=data.split("|")
    return data
    

class WorkOrderPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                WorkOrderData=db.GqlQuery("SELECT ID FROM WorkOrder"+get_WorkOrderGQLWHERE()+get_WorkOrderGQLSort())
                global WorkOrderCount
                WorkOrderCount=WorkOrderData.count()
                if get_WorkOrderCurrentIndex()==-1:
                    WorkOrderCurrentIndex=WorkOrderCount
                    memcache.set('WorkOrderCurrentIndex',WorkOrderCurrentIndex,namespace=users.get_current_user().user_id())
                if WorkOrderCount==0:
                    self.redirect('/NewWorkOrder')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuAdministrator)
                    self.response.out.write(page.Body)
                    write_WorkOrder(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)
    

class FirstWorkOrder(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstWorkOrder')
    def get(self):
        WorkOrderCurrentIndex = 1
        memcache.set('WorkOrderCurrentIndex',WorkOrderCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/WorkOrderPage')

class PreviousWorkOrder(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousWorkOrder')
  def get(self):
    if get_WorkOrderCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/WorkOrderPage')
    else:
      WorkOrderCurrentIndex = get_WorkOrderCurrentIndex()-1
      memcache.set('WorkOrderCurrentIndex',WorkOrderCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/WorkOrderPage')

class NextWorkOrder(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextWorkOrder')
  def get(self):
    if get_WorkOrderCurrentIndex() + 1 > WorkOrderCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/WorkOrderPage')
    else:
      WorkOrderCurrentIndex = get_WorkOrderCurrentIndex()+1
      memcache.set('WorkOrderCurrentIndex',WorkOrderCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/WorkOrderPage')

class LastWorkOrder(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastWorkOrder')
    def get(self):
        WorkOrderCurrentIndex = WorkOrderCount
        memcache.set('WorkOrderCurrentIndex',WorkOrderCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/WorkOrderPage')

class NewWorkOrder(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewWorkOrder')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newWorkOrder(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class WorkOrderTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/WorkOrderTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_WorkOrderTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterWorkOrder(webapp2.RequestHandler):
    def post(self):
        memcache.set('WorkOrderGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('WorkOrderCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/WorkOrderPage')

class GotoWorkOrder(webapp2.RequestHandler):
    def post(self):
        recordnumber=self.request.get('recordnumber')
        memcache.set('WorkOrderCurrentIndex',int(recordnumber),namespace=users.get_current_user().user_id())
        self.redirect('/WorkOrderPage')

class SelectWorkOrder(webapp2.RequestHandler):
    def post(self):
        offset=self.request.get('SelectRecent')
        memcache.set('WorkOrderCurrentIndex',int(offset)-1000,namespace=users.get_current_user().user_id())
        self.redirect('/WorkOrderPage')

class SelectOpenWorkOrder(webapp2.RequestHandler):
    def post(self):
        offset=self.request.get('SelectOpen')
        memcache.set('WorkOrderCurrentIndex',int(offset)-1000,namespace=users.get_current_user().user_id())
        self.redirect('/WorkOrderPage')
        
class FilterWorkOrder(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        WorkOrderGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('WorkOrderGQLWHERE',WorkOrderGQLWHERE,namespace=users.get_current_user().user_id())
        WorkOrderGQLSort=" ORDER BY ID ASC"
        memcache.set('WorkOrderGQLSort',WorkOrderGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('WorkOrderCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/WorkOrderPage')

class SortWorkOrder(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        WorkOrderGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('WorkOrderGQLSort',WorkOrderGQLSort,namespace=users.get_current_user().user_id())
        WorkOrderGQLWHERE=""
        memcache.set('WorkOrderGQLWHERE',WorkOrderGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('WorkOrderCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/WorkOrderPage')

class StoreAWorkOrder(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    Client=self.request.get('Client')
    ClientWO=self.request.get('ClientWO')
    Property=self.request.get('Property')
    PropertyAddress=self.request.get('Address')
    ManagingEmployee=self.request.get('ManagingEmployee')
    DateOrdered=self.request.get('DateOrdered')
    DateDue=self.request.get('DateDue')
    DateScheduled=self.request.get('DateScheduled')
    DateCompleted=self.request.get('DateCompleted')
    DatePaid=self.request.get('DatePaid')
    InvoiceDetails=self.request.get('InvoiceDetails')
    InvoiceAmount=self.request.get('InvoiceAmount')
    DisputeDetails=self.request.get('DisputeDetails')
    MaterialDetails=self.request.get('MaterialDetails')
    CostOfMaterial=self.request.get('CostOfMaterial')
    EquipmentDetails=self.request.get('EquipmentDetails')
    CostOfEquipment=self.request.get('CostOfEquipment')
    LaborDetails=self.request.get('LaborDetails')
    CostOfLabor=self.request.get('CostOfLabor')
    EarningHours=self.request.get('EarningHours')
    Notes=self.request.get('Notes')
    TaskQueue=self.request.get('TaskQueue')
    CompletionNote=self.request.get('CompletionNote')
    MilesDetails=self.request.get('MilesDetails')
    MilesTotal=self.request.get('MilesTotal')
    CostOfMiles=self.request.get('CostOfMiles')
    CostOfAdministration=self.request.get('CostOfAdministration')

    City=self.request.get('City')
    HouseNumber=self.request.get('HouseNumber')
    LotSize=self.request.get('LotSize')
    PaidAmount=self.request.get('PaidAmount')
    Status=self.request.get('Status')
    Type=self.request.get('Type')
    KickBack=self.request.get('KickBack')
    InDispute=self.request.get('InDispute')

    self.store_a_WorkOrder(ID,Client,ClientWO,Property,PropertyAddress,ManagingEmployee,DateOrdered,DateDue,DateScheduled,DateCompleted,DatePaid,InvoiceDetails,InvoiceAmount,DisputeDetails,MaterialDetails,CostOfMaterial,EquipmentDetails,CostOfEquipment,LaborDetails,CostOfLabor,EarningHours,Notes,TaskQueue,CompletionNote,MilesDetails,MilesTotal,CostOfMiles,CostOfAdministration,City,HouseNumber,LotSize,PaidAmount,Status,Type,KickBack,InDispute)
  def store_a_WorkOrder(self,ID,Client,ClientWO,Property,PropertyAddress,ManagingEmployee,DateOrdered,DateDue,DateScheduled,DateCompleted,DatePaid,InvoiceDetails,InvoiceAmount,DisputeDetails,MaterialDetails,CostOfMaterial,EquipmentDetails,CostOfEquipment,LaborDetails,CostOfLabor,EarningHours,Notes,TaskQueue,CompletionNote,MilesDetails,MilesTotal,CostOfMiles,CostOfAdministration,City,HouseNumber,LotSize,PaidAmount,Status,Type,KickBack,InDispute):
    entry = db.GqlQuery("SELECT * FROM WorkOrder where ID = :1", ID).get()
    if entry:
      entry.ID=ID
      entry.Client=Client
      entry.ClientWO=ClientWO
      entry.Property=Property
      entry.PropertyAddress=PropertyAddress
      entry.ManagingEmployee=ManagingEmployee
      entry.DateOrdered=DateOrdered
      entry.DateDue=DateDue
      entry.DateScheduled=DateScheduled
      entry.DateCompleted=DateCompleted
      entry.DatePaid=DatePaid
      entry.InvoiceDetails=InvoiceDetails
      entry.InvoiceAmount=InvoiceAmount
      entry.DisputeDetails=DisputeDetails
      entry.MaterialDetails=MaterialDetails
      entry.CostOfMaterial=CostOfMaterial
      entry.EquipmentDetails=EquipmentDetails
      entry.CostOfEquipment=CostOfEquipment
      entry.LaborDetails=LaborDetails
      entry.CostOfLabor=CostOfLabor
      entry.EarningHours=EarningHours
      entry.Notes=Notes
      entry.TaskQueue=TaskQueue
      entry.CompletionNote=CompletionNote
      entry.MilesDetails=MilesDetails
      entry.MilesTotal=MilesTotal
      entry.CostOfMiles=CostOfMiles
      entry.CostOfAdministration=CostOfAdministration
      entry.City=City
      entry.HouseNumber=HouseNumber
      entry.LotSize=LotSize
      entry.PaidAmount=PaidAmount
      entry.Status=Status
      entry.Type=Type
      entry.KickBack=KickBack
      entry.InDispute=InDispute

      if entry.Status!=Status:
          WorkOrderCurrentIndex = get_WorkOrderCurrentIndex()
          if WorkOrderCurrentIndex>1:
              memcache.set('WorkOrderCurrentIndex',WorkOrderCurrentIndex-1,namespace=users.get_current_user().user_id())
          else:
              memcache.set('WorkOrderGQLWHERE',"",namespace=users.get_current_user().user_id())
              memcache.set('WorkOrderCurrentIndex',-1,namespace=users.get_current_user().user_id())
              self.redirect('/WorkOrderPage')

    else:
      entry = WorkOrder(ID=ID,Client=Client,ClientWO=ClientWO,Property=Property,PropertyAddress=PropertyAddress,ManagingEmployee=ManagingEmployee,DateOrdered=DateOrdered,DateDue=DateDue,DateScheduled=DateScheduled,DateCompleted=DateCompleted,DatePaid=DatePaid,InvoiceDetails=InvoiceDetails,InvoiceAmount=InvoiceAmount,DisputeDetails=DisputeDetails,MaterialDetails=MaterialDetails,CostOfMaterial=CostOfMaterial,EquipmentDetails=EquipmentDetails,CostOfEquipment=CostOfEquipment,LaborDetails=LaborDetails,CostOfLabor=CostOfLabor,EarningHours=EarningHours,Notes=Notes,TaskQueue=TaskQueue,CompletionNote=CompletionNote,MilesDetails=MilesDetails,MilesTotal=MilesTotal,CostOfMiles=CostOfMiles,CostOfAdministration=CostOfAdministration,City=City,HouseNumber=HouseNumber,LotSize=LotSize,PaidAmount=PaidAmount,Status=Status,Type=Type,InDispute=InDispute,KickBack=KickBack)
      #entry.ID=str(WorkOrderCount+1001)      
      global WorkOrderCount
      WorkOrderCount += 1
      memcache.set('WorkOrderCurrentIndex',WorkOrderCount,namespace=users.get_current_user().user_id())
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/WorkOrderPage')

def is_number(s):
    if s:        
        try:
            float(s)
            return True
        except ValueError:
            return False

def write_WorkOrder(self):
  if get_WorkOrderCurrentIndex()<=0:
      WorkOrderOffset=0
  else:
      WorkOrderOffset=get_WorkOrderCurrentIndex()-1
  RecentWorkOrders=getcsv_RecentWorkOrders()
  OpenWorkOrders=getcsv_OpenWorkOrders()
  WorkOrders=db.GqlQuery(WorkOrderGQLSelect+get_WorkOrderGQLWHERE()+get_WorkOrderGQLSort())
  WorkOrder=WorkOrders.get(deadline=60, offset=WorkOrderOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  totalinvoice=0;
  totalCostOfAdministration=0;
  totalCostOfEquipment=0;
  totalCostOfLabor=0;
  totalCostOfMaterial=0;
  totalCostOfMiles=0;
  totalEarningHours=0;
##  for w in WorkOrders:
##      if is_number(w.InvoiceAmount):
##          totalinvoice+=float(w.InvoiceAmount)
##      if is_number(w.CostOfAdministration):
##          totalCostOfAdministration+=float(w.CostOfAdministration)
##      if is_number(w.CostOfEquipment):
##          totalCostOfEquipment+=float(w.CostOfEquipment)
##      if is_number(w.CostOfLabor):
##          totalCostOfLabor+=float(w.CostOfLabor)
##      if is_number(w.CostOfMaterial):
##          totalCostOfMaterial+=float(w.CostOfMaterial)
##      if is_number(w.CostOfMiles):
##          totalCostOfMiles+=float(w.CostOfMiles)
##      if is_number(w.EarningHours):
##          totalEarningHours+=float(w.EarningHours)
##  totalCosts=totalCostOfAdministration+totalCostOfEquipment+totalCostOfLabor+totalCostOfMaterial+totalCostOfMiles;  
##  self.response.out.write('''<div id="stats">Total Invoice: %s<br>Total Costs: %s<br>Earning Hours: %s
##
##
##                         </div>''' %(totalinvoice,totalCosts,totalEarningHours))

  Propertyselectoptions=getcsv_Properties()
  
  self.response.out.write('''<script>var selectaddress=[''')  
  for p in xrange(0,len(Propertyselectoptions)-3,4):
      self.response.out.write('"%s",' %(Propertyselectoptions[p+1]))
  self.response.out.write('''] \nvar selectcity=[''')
  for p in xrange(0,len(Propertyselectoptions)-3,4):
      self.response.out.write('"%s",' %(Propertyselectoptions[p+2]))
  self.response.out.write('''] \nvar selecthousenumber=[''')
  for p in xrange(0,len(Propertyselectoptions)-3,4):
      self.response.out.write('"%s",' %(Propertyselectoptions[p+3]))
  self.response.out.write(''']</script>''')
  self.response.out.write('''<span id="content">
  <h1 id="recordID">WorkOrder#%s, ClientWO#%s - %s</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstWorkOrder" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousWorkOrder" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextWorkOrder" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastWorkOrder" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewWorkOrder" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterWorkOrder" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/WorkOrderTable">Show all in a table.</a></td>
  <td><form action="/GotoWorkOrder" method="post" enctype=application/x-www-form-urlencoded>Goto: <input type="text" name="recordnumber" size="2"> <input type="submit" value="Go"></form></td>
  </tr></table>
  
  <div id="quickfilter">Quick Filter:<br><a class="quickf" href='/'>Open</a><br><a class="quickf" href='/'>Invoiced</a><br><a class="quickf" href='/'>Paid</a><br><a class="quickf" href='/'>Per Property</a></div>
  
  <form id="QuickSelectWO" action="/SelectWorkOrder" method="post" enctype=application/x-www-form-urlencoded>Select Recent:
  <select name="SelectRecent" id="SelectRecent"><option value="%s"></option>''' %(WorkOrder.ID,WorkOrder.ClientWO,WorkOrder.Status,WorkOrderOffset+1,WorkOrderCount,WorkOrderCount))
  for r in xrange(0,len(RecentWorkOrders)-4,5):
      self.response.out.write('<option value="%s">%s-%s-%s-%s-%s</option>' % (RecentWorkOrders[r],RecentWorkOrders[r],RecentWorkOrders[r+1],RecentWorkOrders[r+2],RecentWorkOrders[r+3],RecentWorkOrders[r+4]))
  self.response.out.write('''</select></td><td><input type="submit" value="Go"></form>

  <form id="QuickSelectOpenWO" action="/SelectOpenWorkOrder" method="post" enctype=application/x-www-form-urlencoded>Select Open:
  <select name="SelectOpen" id="SelectOpen"><option value="%s"></option>''' %(WorkOrderCount))
  for r in xrange(0,len(OpenWorkOrders)-5,6):
      self.response.out.write('<option value="%s">%s-%s-%s -%s- %s DUE %s</option>' % (OpenWorkOrders[r],OpenWorkOrders[r],OpenWorkOrders[r+1],OpenWorkOrders[r+2],OpenWorkOrders[r+3],OpenWorkOrders[r+4],OpenWorkOrders[r+5]))
  self.response.out.write('''</select></td><td><input type="submit" value="Go"></form>                          
  
  <form id="filterform" action="/FilterWorkOrder" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''')
  for f in WorkOrderFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortWorkOrder" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in WorkOrderFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>''')
  write_htmlMenuAdministrator(self)
  self.response.out.write('''
  <table border=0>
  <caption></caption>
    <form action="/StoreAWorkOrder" method="post"
          enctype=application/x-www-form-urlencoded><tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
          ''')
  
  if WorkOrder.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(WorkOrder.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if WorkOrder.date:self.response.out.write('<tr><td>date modified</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(WorkOrder.date)))
  else:self.response.out.write('<tr><td>date modified</td><td><input type="text" name="date" value=""   readonly></td><tr>')
  Clientselectoptions=db.GqlQuery("SELECT * FROM Client")
  if WorkOrder.Client:
    self.response.out.write('''<tr><td>Client</td><td><select name="Client"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in Clientselectoptions:
        if WorkOrder.Client==c.ID:
            self.response.out.write('<option value="%s" selected>' % escape(c.ID))
            self.response.out.write('%s</option>' % escape(c.CompanyName))
        else:
            self.response.out.write('<option value="%s">' % escape(c.ID))
            self.response.out.write('%s</option>' % escape(c.CompanyName))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Client</td><td><select name="Client"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Clientselectoptions:
        self.response.out.write('<option value="%s">' % escape(c.ID))
        self.response.out.write('%s</option>' % escape(c.CompanyName))
    self.response.out.write('</select></td><td></td><tr>')
  if WorkOrder.ClientWO:self.response.out.write('<tr><td>Client WO</td><td><input type="text" name="ClientWO" value="%s" size="10"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(WorkOrder.ClientWO)))
  else:self.response.out.write('<tr><td>Client WO</td><td><input type="text" name="ClientWO" value="" size="10"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  
  if WorkOrder.PropertyAddress:
    self.response.out.write('<tr><td>Property Address</td><td><input type="text" readonly id="Address" name="Address" value="%s" size="60"   onfocus="activeinputFunction(this)" onblur="parseaddress();inactiveinputFunction(this)"><input type="button" id="googlepropertyaddress" onclick="googleitproperty()" value="google it."></input></td><tr>' %(str(WorkOrder.PropertyAddress)))
  else:
    self.response.out.write('<tr><td>Property Address</td><td><input type="text" readonly id="Address" name="Address" value="" size="60"   onfocus="activeinputFunction(this)" onblur="parseaddress();inactiveinputFunction(this)"><input type="button" id="googlepropertyaddress" onclick="googleitproperty()" value="google it."></input></td><tr>')
  if WorkOrder.City:
    self.response.out.write('<tr><td>City</td><td><input type="text" readonly id="City" name="City" value="%s" size="15"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' %(str(WorkOrder.City)))
  else:
    self.response.out.write('<tr><td>City</td><td><input type="text" readonly id="City" name="City" value="" size="15"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if WorkOrder.HouseNumber:
    self.response.out.write('<tr><td>HouseNumber</td><td><input type="text" readonly id="HouseNumber" name="HouseNumber" value="%s" size="10"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' %(str(WorkOrder.HouseNumber)))
  else:
    self.response.out.write('<tr><td>HouseNumber</td><td><input type="text" readonly id="HouseNumber" name="HouseNumber" value="" size="10"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if WorkOrder.LotSize:
    self.response.out.write('<tr><td>LotSize</td><td><input type="text" readonly id="LotSize" name="LotSize" value="%s" size="10"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' %(str(WorkOrder.LotSize)))
  else:
    self.response.out.write('<tr><td>LotSize</td><td><input type="text" readonly id="LotSize" name="LotSize" value="" size="10"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  
  if WorkOrder.Property:    
    self.response.out.write('''<tr><td>Property</td><td><select id="Property" name="Property"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this);propertyselected()">''')
    
    for p in xrange(0,len(Propertyselectoptions)-3,4):
      if WorkOrder.Property==Propertyselectoptions[p]:
        self.response.out.write('<option value="%s" selected>%s-%s</option>' % (Propertyselectoptions[p],Propertyselectoptions[p],Propertyselectoptions[p+1]))
      else:
        self.response.out.write('<option value="%s">%s-%s</option>' % (Propertyselectoptions[p],Propertyselectoptions[p],Propertyselectoptions[p+1]))
    self.response.out.write('''</select></td><td></td><tr>''')
    
  else:    
    self.response.out.write('<tr><td>Property</td><td><select id="Property" name="Property"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this);propertyselected()">')
    for p in Propertyselectoptions:
        self.response.out.write('<option value="%s">' % escape(p[0]))
        self.response.out.write('%s</option>' % escape(p[1]))
    self.response.out.write('</select></td><td></td><tr>')

  Statusselectoptions=["Ordered","Scheduled","Completed","Invoiced","Paid","Cancelled","Rejected","Follow Up",]
  if WorkOrder.Status:    
    self.response.out.write('''<tr><td>Status</td><td><select id="Status" name="Status"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this);Statusselected()">''')
    for c in Statusselectoptions:
        if WorkOrder.Status==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' %(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' %(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:    
    self.response.out.write('<tr><td>Status</td><td><select id="Status" name="Status"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this);Statusselected()">')
    for c in Statusselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')

  Typeselectoptions=["Initial Grass","Recut","Estimate","Final Condition","Trim Trees","Capping","Windows","CFK","Securing","Post and Store","Debris","Clean","Winterization","Construction","Allow Access","Other"]
  if WorkOrder.Type:    
    self.response.out.write('''<tr><td>Type</td><td><select id="Type" name="Type"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this);Typeselected()">''')
    for c in Typeselectoptions:
        if WorkOrder.Type==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' %(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' %(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:    
    self.response.out.write('<tr><td>Type</td><td><select id="Type" name="Type"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this);Typeselected()">')
    for c in Typeselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
  
  ManagingEmployeeselectoptions=db.GqlQuery("SELECT * FROM Employee")
  if WorkOrder.ManagingEmployee:
    self.response.out.write('''<tr><td>Managing Employee</td><td><select name="ManagingEmployee"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in ManagingEmployeeselectoptions:
        if WorkOrder.ManagingEmployee==c.userid:
            self.response.out.write('<option value="%s" selected>' % escape(c.userid))
            self.response.out.write('%s</option>' % escape(c.FirstName))
        else:
            self.response.out.write('<option value="%s">' % escape(c.userid))
            self.response.out.write('%s</option>' % escape(c.FirstName))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Managing Employee</td><td><select name="ManagingEmployee"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in ManagingEmployeeselectoptions:
        self.response.out.write('<option value="%s">' % escape(c.userid))
        self.response.out.write('%s</option>' % escape(c.FirstName))
    self.response.out.write('</select></td><td></td><tr>')
  if WorkOrder.DateOrdered:self.response.out.write('<tr><td>Date Ordered</td><td><input type="text" id="DateOrdered" name="DateOrdered" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="button" value="Today" onclick="TodayDateOrdered()"></td><tr>' % escape(str(WorkOrder.DateOrdered)))
  else:self.response.out.write('<tr><td>Date Ordered</td><td><input type="text" id="DateOrdered" name="DateOrdered" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="button" value="Today" onclick="TodayDateOrdered()"></td><tr>')
  if WorkOrder.DateDue:self.response.out.write('<tr><td>Date Due</td><td><input type="text" id="DateDue" name="DateDue" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="date" id="duedate" onblur="CalendarDateDue()"></td><tr>' % escape(str(WorkOrder.DateDue)))
  else:self.response.out.write('<tr><td>Date Due</td><td><input type="text" id="DateDue" name="DateDue" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="date" id="duedate" onblur="CalendarDateDue()"></td><tr>')
  if WorkOrder.DateScheduled:self.response.out.write('<tr><td>Date Scheduled</td><td><input type="text" id="DateScheduled" name="DateScheduled" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="date" id="scheduleddate" onblur="CalendarDateScheduled()"></td><tr>' % escape(str(WorkOrder.DateScheduled)))
  else:self.response.out.write('<tr><td>Date Scheduled</td><td><input type="text" id="DateScheduled" name="DateScheduled" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="date" id="scheduleddate" onblur="CalendarDateScheduled()"></td><tr>')
  if WorkOrder.DateCompleted:self.response.out.write('<tr><td>Date Completed</td><td><input type="text" id="DateCompleted" name="DateCompleted" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="button" value="Today" onclick="TodayDateCompleted()"></td><tr>' % escape(str(WorkOrder.DateCompleted)))
  else:self.response.out.write('<tr><td>Date Completed</td><td><input type="text" id="DateCompleted" name="DateCompleted" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="button" value="Today" onclick="TodayDateCompleted()"></td><tr>')
  if WorkOrder.DatePaid:self.response.out.write('<tr><td>Date Paid</td><td><input type="text" name="DatePaid" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(WorkOrder.DatePaid)))
  else:self.response.out.write('<tr><td>Date Paid</td><td><input type="text" name="DatePaid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if WorkOrder.InvoiceDetails:self.response.out.write('<tr><td>Invoice Details</td><td><textarea cols="40" rows="5" name="InvoiceDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(WorkOrder.InvoiceDetails))
  else:self.response.out.write('<tr><td>Invoice Details</td><td><textarea cols="40" rows="5" name="InvoiceDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if WorkOrder.InvoiceAmount:self.response.out.write('<tr><td>Invoice Amount</td><td><input type="text" name="InvoiceAmount" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(WorkOrder.InvoiceAmount)))
  else:self.response.out.write('<tr><td>Invoice Amount</td><td><input type="text" name="InvoiceAmount" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if WorkOrder.PaidAmount:self.response.out.write('<tr><td>Paid Amount</td><td><input type="text" name="PaidAmount" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(WorkOrder.PaidAmount)))
  else:self.response.out.write('<tr><td>Paid Amount</td><td><input type="text" name="PaidAmount" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if WorkOrder.KickBack:
      self.response.out.write('<tr><td>KickBack?</td><td><select name="KickBack"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
      if WorkOrder.KickBack=="yes":
          self.response.out.write('<option value="yes" selected>yes</option><option value=""> </option></select></td></tr>')
      else:self.response.out.write('<option value="yes">yes</option><option value="" selected> </option></select></td></tr>')  
  else:self.response.out.write('<tr><td>KickBack?</td><td><select name="KickBack" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><option value="yes">yes</option><option value="" selected> </option></select></td></tr>')

  if WorkOrder.DisputeDetails:self.response.out.write('<tr><td>Dispute Details</td><td><textarea cols="40" rows="5" name="DisputeDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(WorkOrder.DisputeDetails))
  else:self.response.out.write('<tr><td>Dispute Details</td><td><textarea cols="40" rows="5" name="DisputeDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')

  if WorkOrder.InDispute:
      self.response.out.write('<tr><td>InDispute?</td><td><select name="InDispute"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
      if WorkOrder.InDispute=="yes":
          self.response.out.write('<option value="yes" selected>yes</option><option value=""> </option></select></td></tr>')
      else:self.response.out.write('<option value="yes">yes</option><option value="" selected> </option></select></td></tr>')  
  else:self.response.out.write('<tr><td>InDispute?</td><td><select name="InDispute" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><option value="yes">yes</option><option value="" selected> </option></select></td></tr>')

  if WorkOrder.MaterialDetails:self.response.out.write('<tr><td>Material Details</td><td><textarea cols="40" rows="5" name="MaterialDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(WorkOrder.MaterialDetails))
  else:self.response.out.write('<tr><td>Material Details</td><td><textarea cols="40" rows="5" name="MaterialDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if WorkOrder.CostOfMaterial:self.response.out.write('<tr><td>Cost Of Material</td><td><input type="text" name="CostOfMaterial" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(WorkOrder.CostOfMaterial)))
  else:self.response.out.write('<tr><td>Cost Of Material</td><td><input type="text" name="CostOfMaterial" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if WorkOrder.EquipmentDetails:self.response.out.write('<tr><td>Equipment Details</td><td><textarea cols="40" rows="5" name="EquipmentDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(WorkOrder.EquipmentDetails))
  else:self.response.out.write('<tr><td>Equipment Details</td><td><textarea cols="40" rows="5" name="EquipmentDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if WorkOrder.CostOfEquipment:self.response.out.write('<tr><td>Cost Of Equipment</td><td><input type="text" name="CostOfEquipment" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(WorkOrder.CostOfEquipment)))
  else:self.response.out.write('<tr><td>Cost Of Equipment</td><td><input type="text" name="CostOfEquipment" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if WorkOrder.LaborDetails:self.response.out.write('<tr><td>Labor Details</td><td><textarea cols="40" rows="5" name="LaborDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(WorkOrder.LaborDetails))
  else:self.response.out.write('<tr><td>Labor Details</td><td><textarea cols="40" rows="5" name="LaborDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if WorkOrder.CostOfLabor:self.response.out.write('<tr><td>Cost Of Labor</td><td><input type="text" name="CostOfLabor" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(WorkOrder.CostOfLabor)))
  else:self.response.out.write('<tr><td>Cost Of Labor</td><td><input type="text" name="CostOfLabor" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if WorkOrder.EarningHours:self.response.out.write('<tr><td>Earning Hours</td><td><input type="text" name="EarningHours" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(WorkOrder.EarningHours)))
  else:self.response.out.write('<tr><td>Earning Hours</td><td><input type="text" name="EarningHours" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if WorkOrder.Notes:self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(WorkOrder.Notes))
  else:self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if WorkOrder.TaskQueue:self.response.out.write('<tr><td>Task Queue</td><td><textarea cols="40" rows="5" name="TaskQueue"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(WorkOrder.TaskQueue))
  else:self.response.out.write('<tr><td>Task Queue</td><td><textarea cols="40" rows="5" name="TaskQueue"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if WorkOrder.CompletionNote:self.response.out.write('<tr><td>Completion Note</td><td><textarea cols="40" rows="5" name="CompletionNote"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(WorkOrder.CompletionNote))
  else:self.response.out.write('<tr><td>Completion Note</td><td><textarea cols="40" rows="5" name="CompletionNote"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if WorkOrder.MilesDetails:self.response.out.write('<tr><td>Miles Details</td><td><textarea cols="40" rows="5" name="MilesDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(WorkOrder.MilesDetails))
  else:self.response.out.write('<tr><td>Miles Details</td><td><textarea cols="40" rows="5" name="MilesDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if WorkOrder.MilesTotal:self.response.out.write('<tr><td>Miles Total</td><td><input type="text" name="MilesTotal" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(WorkOrder.MilesTotal)))
  else:self.response.out.write('<tr><td>Miles Total</td><td><input type="text" name="MilesTotal" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if WorkOrder.CostOfMiles:self.response.out.write('<tr><td>Cost Of Miles</td><td><input type="text" name="CostOfMiles" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(WorkOrder.CostOfMiles)))
  else:self.response.out.write('<tr><td>Cost Of Miles</td><td><input type="text" name="CostOfMiles" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if WorkOrder.CostOfAdministration:self.response.out.write('<tr><td>Cost Of Administration</td><td><input type="text" name="CostOfAdministration" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(WorkOrder.CostOfAdministration)))
  else:self.response.out.write('<tr><td>Cost Of Administration</td><td><input type="text" name="CostOfAdministration" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  self.response.out.write('''
  <tr><td><input type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')
##DateCompleted, ClientWO, PropertyAddress, InvoiceDetails, InvoiceAmount, *penalties, PaidAmount, *client comments, DisputeDetails, *adjustment made, *adjustment amount, *client research
def write_WorkOrderTable(self):
    WorkOrderData = db.GqlQuery(WorkOrderGQLSelect+get_WorkOrderGQLWHERE()+get_WorkOrderGQLSort())
    self.response.out.write('''</div><table><tr><td>date completed</td><td>ppw</td><td>address</td><td>work completed</td><td>invoice amount</td><td>penalties</td><td>amount paid</td><td>client comments</td><td>dispute</td><td>adjustment made</td><td>adjustment amount</td><td>client research</td></tr>''')
    for c in WorkOrderData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.DateCompleted,c.ClientWO,c.PropertyAddress,c.InvoiceDetails,c.InvoiceAmount,"",c.PaidAmount,"",c.DisputeDetails,"","",""))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newWorkOrder(self):
  AutoNumber=WorkOrderCount+1001
  Propertyselectoptions=db.GqlQuery("SELECT * FROM Property ORDER BY Address ASC")
  self.response.out.write('''<script>var selectaddress=[''')
  for p in Propertyselectoptions:
      self.response.out.write('"%s",' %(p.Address))
  self.response.out.write(''']</script>''')
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New WorkOrder</b></caption>
    <form action="/StoreAWorkOrder" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>date modified</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td>Client WO</td><td><input type="text" name="ClientWO" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  
  self.response.out.write('<tr><td>Property Address (auto)</td><td><input type="text" id="Address" name="Address" value="" size="60" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="button" id="googlepropertyaddress" onclick="googleitproperty()" value="google it."></input>')
  self.response.out.write('<tr><td>City (auto)</td><td><input type="text" id="City" name="City" value="" size="60" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  self.response.out.write('<tr><td>HouseNumber (auto)</td><td><input type="text" id="HouseNumber" name="HouseNumber" value="" size="60" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  self.response.out.write('<tr><td>LotSize (auto)</td><td><input type="text" id="LotSize" name="LotSize" value="" size="60" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')



  self.response.out.write('<tr><td>Property</td><td><select id="Property" name="Property"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this);propertyselected()">')
  for c in Propertyselectoptions:
    self.response.out.write('<option value="%s">' % escape(c.ID))
    self.response.out.write('%s</option>' % escape(c.Address))
  self.response.out.write('</select></td><td></td><tr>')

  Statusselectoptions=["Ordered","Scheduled","Completed","Invoiced","Paid","Cancelled","Rejected","FollowUp"]
  self.response.out.write('<tr><td>Status</td><td><select id="Status" name="Status"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this);Statusselected()">')
  for c in Statusselectoptions:
    self.response.out.write('<option value="%s">' % escape(c))
    self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><td></td><tr>')

  Typeselectoptions=["Initial Grass","Recut","Estimate","Final Condition","Trim Trees","Capping","Windows","CFK","Securing","Post and Store","Debris","Clean","Winterization","Construction","Allow Access","Other"]
  self.response.out.write('<tr><td>Type</td><td><select id="Type" name="Type"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this);Statusselected()">')
  for c in Typeselectoptions:
    self.response.out.write('<option value="%s">' % escape(c))
    self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><td></td><tr>')

  ManagingEmployeeselectoptions=db.GqlQuery("SELECT * FROM Employee")
  self.response.out.write('<tr><td>Managing Employee</td><td><select name="ManagingEmployee"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in ManagingEmployeeselectoptions:
    self.response.out.write('<option value="%s">' % escape(c.userid))
    self.response.out.write('%s</option>' % escape(c.FirstName))
  self.response.out.write('</select></td><td></td><tr>')
  self.response.out.write('<tr><td>Date Ordered</td><td><input type="text" id="DateOrdered" name="DateOrdered" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="button" value="Today" onclick="TodayDateOrdered()"></td></tr>')
  self.response.out.write('<tr><td>Date Due</td><td><input type="text" id="DateDue" name="DateDue" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="date" id="duedate" onblur="CalendarDateDue()"></td></tr>')
  self.response.out.write('<tr><td>Date Scheduled</td><td><input type="text" id="DateScheduled" name="DateScheduled" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"><input type="date" id="scheduleddate" onblur="CalendarDateScheduled()"></td></tr>')
  self.response.out.write('<tr><td>Date Completed</td><td><input type="text" id="DateCompleted" name="DateCompleted" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Date Paid</td><td><input type="text" id="DateCompleted" name="DatePaid" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Invoice Details</td><td><textarea cols="40" rows="5" name="InvoiceDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>Invoice Amount</td><td><input type="text" name="InvoiceAmount" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Dispute Details</td><td><textarea cols="40" rows="5" name="DisputeDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>Material Details</td><td><textarea cols="40" rows="5" name="MaterialDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>Cost Of Material</td><td><input type="text" name="CostOfMaterial" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Equipment Details</td><td><textarea cols="40" rows="5" name="EquipmentDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>Cost Of Equipment</td><td><input type="text" name="CostOfEquipment" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Labor Details</td><td><textarea cols="40" rows="5" name="LaborDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>Cost Of Labor</td><td><input type="text" name="CostOfLabor" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Earning Hours</td><td><input type="text" name="EarningHours" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Notes</td><td><textarea cols="40" rows="5" name="Notes"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>Task Queue</td><td><textarea cols="40" rows="5" name="TaskQueue"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>Completion Note</td><td><textarea cols="40" rows="5" name="CompletionNote"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>Miles Details</td><td><textarea cols="40" rows="5" name="MilesDetails"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>Miles Total</td><td><input type="text" name="MilesTotal" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Cost Of Miles</td><td><input type="text" name="CostOfMiles" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Cost Of Administration</td><td><input type="text" name="CostOfAdministration" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterWorkOrder" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(WorkOrderCount)
  self.response.out.write(''' WorkOrder(s).</table></body></html>
''')


class TimePunch(db.Model):
    ID=db.StringProperty()
    date=db.DateTimeProperty(required=True, auto_now=True)
    UserID=db.StringProperty()
    InOrOut=db.StringProperty()
    Timestamp=db.StringProperty()

TimePunchGQLSelect="SELECT * FROM TimePunch"
TimePunchCurrentIndex = -1;
TimePunchCount = 0;
TimePunchFieldNames=["ID","date","UserID","InOrOut","Timestamp",]

def get_TimePunchGQLWHERE():
    data = memcache.get('TimePunchGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('TimePunchGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_TimePunchGQLSort():
    data = memcache.get('TimePunchGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('TimePunchGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_TimePunchCurrentIndex():
    data = memcache.get('TimePunchCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('TimePunchCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

class TimePunchPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                TimePunchData=db.GqlQuery(TimePunchGQLSelect+get_TimePunchGQLWHERE()+get_TimePunchGQLSort())
                global TimePunchCount
                TimePunchCount=TimePunchData.count()
                if get_TimePunchCurrentIndex()==-1:
                    TimePunchCurrentIndex=TimePunchCount
                    memcache.set('TimePunchCurrentIndex',TimePunchCurrentIndex,namespace=users.get_current_user().user_id())
                if TimePunchCount==0:
                    self.redirect('/NewTimePunch')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(page.Body)
                    write_TimePunch(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class FirstTimePunch(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstTimePunch')
    def get(self):
        TimePunchCurrentIndex = 1
        memcache.set('TimePunchCurrentIndex',TimePunchCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/TimePunchPage')

class PreviousTimePunch(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousTimePunch')
  def get(self):
    if get_TimePunchCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/TimePunchPage')
    else:
      TimePunchCurrentIndex = get_TimePunchCurrentIndex()-1
      memcache.set('TimePunchCurrentIndex',TimePunchCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/TimePunchPage')

class NextTimePunch(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextTimePunch')
  def get(self):
    if get_TimePunchCurrentIndex() + 1 > TimePunchCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/TimePunchPage')
    else:
      TimePunchCurrentIndex = get_TimePunchCurrentIndex()+1
      memcache.set('TimePunchCurrentIndex',TimePunchCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/TimePunchPage')

class LastTimePunch(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastTimePunch')
    def get(self):
        TimePunchCurrentIndex = TimePunchCount
        memcache.set('TimePunchCurrentIndex',TimePunchCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/TimePunchPage')

class NewTimePunch(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewTimePunch')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newTimePunch(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class TimePunchTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/TimePunchTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_TimePunchTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterTimePunch(webapp2.RequestHandler):
    def post(self):
        memcache.set('TimePunchGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('TimePunchCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/TimePunchPage')

class FilterTimePunch(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        TimePunchGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('TimePunchGQLWHERE',TimePunchGQLWHERE,namespace=users.get_current_user().user_id())
        TimePunchGQLSort=""
        memcache.set('TimePunchGQLSort',TimePunchGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('TimePunchCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/TimePunchPage')

class SortTimePunch(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        TimePunchGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('TimePunchGQLSort',TimePunchGQLSort,namespace=users.get_current_user().user_id())
        TimePunchGQLWHERE=""
        memcache.set('TimePunchGQLWHERE',TimePunchGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('TimePunchCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/TimePunchPage')

class StoreATimePunch(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    UserID=self.request.get('UserID')
    InOrOut=self.request.get('InOrOut')
    Timestamp=self.request.get('Timestamp')

    self.store_a_TimePunch(ID,UserID,InOrOut,Timestamp,)
  def store_a_TimePunch(self,ID,UserID,InOrOut,Timestamp,):
    entry = db.GqlQuery("SELECT * FROM TimePunch where ID = :1", ID).get()
    if entry:
      entry.ID=ID
      entry.UserID=UserID
      entry.InOrOut=InOrOut
      entry.Timestamp=Timestamp

    else:
      entry = TimePunch(ID=ID,UserID=UserID,InOrOut=InOrOut,Timestamp=Timestamp,)
      entry.ID=str(TimePunchCount+1001)
      global TimePunchCount
      TimePunchCount += 1
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/TimePunchPage')

def write_TimePunch(self):
  if get_TimePunchCurrentIndex()<=0:
      TimePunchOffset=0
  else:
      TimePunchOffset=get_TimePunchCurrentIndex()-1
  TimePunch=db.GqlQuery(TimePunchGQLSelect+get_TimePunchGQLWHERE()+get_TimePunchGQLSort()).get(deadline=60, offset=TimePunchOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <h1 id="recordID">TimePunch</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstTimePunch" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousTimePunch" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextTimePunch" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastTimePunch" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewTimePunch" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterTimePunch" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/TimePunchTable">Show all in a table.</a></td>
  </tr></table>
  <form id="filterform" action="/FilterTimePunch" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''' %(TimePunchOffset+1,TimePunchCount))
  for f in TimePunchFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortTimePunch" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in TimePunchFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>
  <table border=0>
  <caption></caption>
    <form action="/StoreATimePunch" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if TimePunch.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(TimePunch.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if TimePunch.date:self.response.out.write('<tr><td>Date Modified</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(TimePunch.date)))
  else:self.response.out.write('<tr><td>Date Modified</td><td><input type="text" name="date" value=""   readonly></td><tr>')
  UserIDselectoptions=db.GqlQuery("SELECT * FROM Employee")
  if TimePunch.UserID:
    self.response.out.write('''<tr><td>Employee User ID</td><td><select name="UserID"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in UserIDselectoptions:
        if TimePunch.UserID==c.userid:
            self.response.out.write('<option value="%s" selected>' % escape(c.userid))
            self.response.out.write('%s</option>' % escape(c.Email))
        else:
            self.response.out.write('<option value="%s">' % escape(c.userid))
            self.response.out.write('%s</option>' % escape(c.Email))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Employee User ID</td><td><select name="UserID"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in UserIDselectoptions:
        self.response.out.write('<option value="%s">' % escape(c.userid))
        self.response.out.write('%s</option>' % escape(c.Email))
    self.response.out.write('</select></td><td></td><tr>')
  InOrOutselectoptions=["in","out",]
  if TimePunch.InOrOut:
    self.response.out.write('''<tr><td>In or Out</td><td><select name="InOrOut" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in InOrOutselectoptions:
        if TimePunch.InOrOut==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>In or Out</td><td><select name="InOrOut" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in InOrOutselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
  if TimePunch.Timestamp:self.response.out.write('<tr><td>Time Stamp</td><td><input type="text" name="Timestamp" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(TimePunch.Timestamp)))
  else:self.response.out.write('<tr><td>Time Stamp</td><td><input type="text" name="Timestamp" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')

def write_TimePunchTable(self):
    TimePunchData = db.GqlQuery(TimePunchGQLSelect+get_TimePunchGQLWHERE()+get_TimePunchGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>date</td><td>UserID</td><td>InOrOut</td><td>Timestamp</td>
</tr>''')
    for c in TimePunchData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.date,c.UserID,c.InOrOut,c.Timestamp,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newTimePunch(self):
  AutoNumber=TimePunchCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New TimePunch</b></caption>
    <form action="/StoreATimePunch" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>Date Modified</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))
  InOrOutselectoptions=["in","out",]
  self.response.out.write('<tr><td>In or Out</td><td><select name="InOrOut"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in InOrOutselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')
  self.response.out.write('<tr><td>Time Stamp</td><td><input type="text" name="Timestamp" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterTimePunch" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(TimePunchCount)
  self.response.out.write(''' TimePunch(s).</table></body></html>
''')


class Ledger(db.Model):
    ID=db.StringProperty()
    date=db.DateTimeProperty(required=True, auto_now=True)
    TransactionDate=db.StringProperty()
    Total=db.StringProperty()
    Type=db.StringProperty()
    Category=db.StringProperty()
    SubCategory=db.StringProperty()
    Details=db.TextProperty()

    #expenses
    allocatedamount=db.StringProperty()
    supplies=db.StringProperty()
    contractlabor=db.StringProperty()
    initialdepreciable=db.StringProperty()
    insurance=db.StringProperty()
    interest=db.StringProperty()
    legal=db.StringProperty()
    office=db.StringProperty()
    rentalequipment=db.StringProperty()
    repairs=db.StringProperty()
    taxandlicense=db.StringProperty()
    salestax=db.StringProperty()
    travel=db.StringProperty()
    mealsandentertainment=db.StringProperty()
    wages=db.StringProperty()
    
    
    Supplier=db.StringProperty()
    FileName=db.StringProperty()
    Expensed=db.StringProperty()
    Allocation=db.StringProperty()
    SyncedAllocation=db.StringProperty()
    

LedgerGQLSelect="SELECT * FROM Ledger"
LedgerCurrentIndex = -1;
LedgerCount = 0;
LedgerFieldNames=["ID","date","TransactionDate","Total","Type","Category","SubCategory","Details","Supplier","FileName","Expensed","Allocation","SyncedAllocation"]

def get_LedgerGQLWHERE():
    data = memcache.get('LedgerGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('LedgerGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_LedgerGQLSort():
    data = memcache.get('LedgerGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('LedgerGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_LedgerCurrentIndex():
    data = memcache.get('LedgerCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('LedgerCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

class LedgerPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                LedgerData=db.GqlQuery(LedgerGQLSelect+get_LedgerGQLWHERE()+get_LedgerGQLSort())
                global LedgerCount
                LedgerCount=LedgerData.count()
                if get_LedgerCurrentIndex()==-1:
                    LedgerCurrentIndex=LedgerCount
                    memcache.set('LedgerCurrentIndex',LedgerCurrentIndex,namespace=users.get_current_user().user_id())
                if LedgerCount==0:
                    self.redirect('/NewLedger')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuAdministrator)
                    self.response.out.write(page.Body)
                    write_Ledger(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)
       
            
class FirstLedger(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstLedger')
    def get(self):
        LedgerCurrentIndex = 1
        memcache.set('LedgerCurrentIndex',LedgerCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/LedgerPage')

class PreviousLedger(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousLedger')
  def get(self):
    if get_LedgerCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/LedgerPage')
    else:
      LedgerCurrentIndex = get_LedgerCurrentIndex()-1
      memcache.set('LedgerCurrentIndex',LedgerCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/LedgerPage')

class NextLedger(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextLedger')
  def get(self):
    if get_LedgerCurrentIndex() + 1 > LedgerCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/LedgerPage')
    else:
      LedgerCurrentIndex = get_LedgerCurrentIndex()+1
      memcache.set('LedgerCurrentIndex',LedgerCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/LedgerPage')

class LastLedger(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastLedger')
    def get(self):
        LedgerCurrentIndex = LedgerCount
        memcache.set('LedgerCurrentIndex',LedgerCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/LedgerPage')

class NewLedger(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewLedger')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newLedger(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class LedgerTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LedgerTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_LedgerTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterLedger(webapp2.RequestHandler):
    def post(self):
        memcache.set('LedgerGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('LedgerCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/LedgerPage')

class FilterLedger(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        LedgerGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('LedgerGQLWHERE',LedgerGQLWHERE,namespace=users.get_current_user().user_id())
        LedgerGQLSort=""
        memcache.set('LedgerGQLSort',LedgerGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('LedgerCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/LedgerPage')

class SortLedger(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        LedgerGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('LedgerGQLSort',LedgerGQLSort,namespace=users.get_current_user().user_id())
        LedgerGQLWHERE=""
        memcache.set('LedgerGQLWHERE',LedgerGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('LedgerCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/LedgerPage')

class StoreALedger(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    TransactionDate=self.request.get('TransactionDate')
    Total=self.request.get('Total')
    Type=self.request.get('Type')
    Category=self.request.get('Category')
    SubCategory=self.request.get('SubCategory')
    Details=self.request.get('Details')
    Supplier=self.request.get('Supplier')
    FileName=self.request.get('FileName')
    Expensed=self.request.get('Expensed')
    Allocation=self.request.get('Allocation')
    SyncedAllocation=self.request.get('SyncedAllocation')
    allocatedamount=self.request.get('allocatedamount')
    supplies=self.request.get('supplies')
    contractlabor=self.request.get('contractlabor')
    initialdepreciable=self.request.get('initialdepreciable')
    insurance=self.request.get('insurance')
    interest=self.request.get('interest')
    legal=self.request.get('legal')
    office=self.request.get('office')
    rentalequipment=self.request.get('rentalequipment')
    repairs=self.request.get('repairs')
    taxandlicense=self.request.get('taxandlicense')
    salestax=self.request.get('salestax')
    travel=self.request.get('travel')
    mealsandentertainment=self.request.get('mealsandentertainment')
    wages=self.request.get('wages')

    self.store_a_Ledger(ID,TransactionDate,Total,Type,Category,SubCategory,Details,Supplier,FileName,Expensed,Allocation,SyncedAllocation,contractlabor,allocatedamount,supplies,initialdepreciable,insurance,interest,legal,office,rentalequipment,repairs,taxandlicense,salestax,travel,mealsandentertainment,wages)
  def store_a_Ledger(self,ID,TransactionDate,Total,Type,Category,SubCategory,Details,Supplier,FileName,Expensed,Allocation,SyncedAllocation,contractlabor,allocatedamount,supplies,initialdepreciable,insurance,interest,legal,office,rentalequipment,repairs,taxandlicense,salestax,travel,mealsandentertainment,wages):
    entry = db.GqlQuery("SELECT * FROM Ledger where ID = :1", ID).get()
    if entry:
      entry.ID=ID
      entry.TransactionDate=TransactionDate
      entry.Total=Total
      entry.Type=Type
      entry.Category=Category
      entry.SubCategory=SubCategory
      entry.Details=Details
      entry.Supplier=Supplier
      entry.FileName=FileName
      entry.Expensed=Expensed
      entry.Allocation=Allocation
      entry.SyncedAllocation=SyncedAllocation
      entry.contractlabor=contractlabor
      entry.allocatedamount=allocatedamount
      entry.supplies=supplies
      entry.initialdepreciable=initialdepreciable
      entry.insurance=insurance
      entry.interest=interest
      entry.legal=legal
      entry.office=office
      entry.rentalequipment=rentalequipment
      entry.repairs=repairs
      entry.taxandlicense=taxandlicense
      entry.salestax=salestax
      entry.travel=travel
      entry.mealsandentertainment=mealsandentertainment
      entry.wages=wages

    else:
      entry = Ledger(ID=ID,TransactionDate=TransactionDate,Total=Total,Type=Type,Category=Category,SubCategory=SubCategory,Details=Details,Supplier=Supplier,FileName=FileName,Expensed=Expensed,Allocation=Allocation,SyncedAllocation=SyncedAllocation,contractlabor=contractlabor,allocatedamount=allocatedamount,supplies=supplies,initialdepreciable=initialdepreciable,insurance=insurance,interest=interest,legal=legal,office=office,rentalequipment=rentalequipment,repairs=repairs,taxandlicense=taxandlicense,salestax=salestax,travel=travel,mealsandentertainment=mealsandentertainment,wages=wages)
      entry.ID=str(LedgerCount+1001)
      global LedgerCount
      LedgerCount += 1
    entry.put()

    ##sync allocatedamount with work order allocated.
    wo_entry=db.GqlQuery("SELECT * FROM WorkOrder where ID = '%s'" %s(Allocation)).get()
    if wo_entry is not None:
        if wo_entry.CostOfMaterial is None:
            wo_entry.CostOfMaterial=allocatedamount
        else:
            wo_entry.CostOfMaterial+=allocatedamount
        wo_entry.put()
    
    global StatusBar
    StatusBar = "saved"
    self.redirect('/LedgerPage')

def write_Ledger(self):
  if get_LedgerCurrentIndex()<=0:
      LedgerOffset=0
  else:
      LedgerOffset=get_LedgerCurrentIndex()-1
  Ledger=db.GqlQuery(LedgerGQLSelect+get_LedgerGQLWHERE()+get_LedgerGQLSort()).get(deadline=60, offset=LedgerOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <h1 id="recordID">Ledger</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstLedger" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousLedger" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextLedger" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastLedger" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewLedger" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterLedger" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/LedgerTable">Show all in a table.</a></td>
  <td><form action="/GotoLedger" method="post" enctype=application/x-www-form-urlencoded>Goto: <input type="text" name="recordnumber" size="2"> <input type="submit" value="Go"></form></td>
  </tr></table>
  <form id="filterform" action="/FilterLedger" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''' %(LedgerOffset+1,LedgerCount))
  for f in LedgerFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortLedger" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in LedgerFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>
  <table border=0>
  <caption></caption>
    <form action="/StoreALedger" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Ledger.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(Ledger.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if Ledger.date:self.response.out.write('<tr><td>Date Modified</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(Ledger.date)))
  else:self.response.out.write('<tr><td>Date Modified</td><td><input type="text" name="date" value=""   readonly></td><tr>')
  if Ledger.TransactionDate:self.response.out.write('<tr><td>TransactionDate</td><td><input type="text" name="TransactionDate" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.TransactionDate)))
  else:self.response.out.write('<tr><td>TransactionDate</td><td><input type="text" name="TransactionDate" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Ledger.Total:self.response.out.write('<tr><td>Total</td><td><input type="text" name="Total" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.Total)))
  else:self.response.out.write('<tr><td>Total</td><td><input type="text" name="Total" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  Typeselectoptions=["Receipt","Expense","DepreciableExpense","Income"]
  if Ledger.Type:
    self.response.out.write('''<tr><td>Type</td><td><select name="Type" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in Typeselectoptions:
        if Ledger.Type==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Type</td><td><select name="Type" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Typeselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')

  Categoryselectoptions=["","Field","Office","Transportation","Overhead"]
  if Ledger.Category:
    self.response.out.write('''<tr><td>Category (deprecated)</td><td><select name="Category" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in Categoryselectoptions:
        if Ledger.Category==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Category (deprecated)</td><td><select name="Category" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Categoryselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')

  SubCategoryselectoptions=["","equipment","supply","service","postage","backgroundcheck","insurance","other"]
  if Ledger.SubCategory:
    self.response.out.write('''<tr><td>Sub Category (deprecated)</td><td><select name="SubCategory" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in SubCategoryselectoptions:
        if Ledger.SubCategory==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Sub Category (deprecated)</td><td><select name="SubCategory" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in SubCategoryselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
  if Ledger.Supplier:self.response.out.write('<tr><td>Supplier</td><td><input type="text" name="Supplier" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.Supplier)))
  else:self.response.out.write('<tr><td>Supplier</td><td><input type="text" name="Supplier" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.FileName:self.response.out.write('<tr><td>FileName</td><td><input type="text" name="FileName" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.FileName)))
  else:self.response.out.write('<tr><td>FileName</td><td><input type="text" name="FileName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.Expensed:self.response.out.write('<tr><td>Expensed</td><td><input type="text" name="Expensed" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.Expensed)))
  else:self.response.out.write('<tr><td>Expensed</td><td><input type="text" name="Expensed" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.Allocation:self.response.out.write('<tr><td>Allocation</td><td><input type="text" name="Allocation" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.Allocation)))
  else:self.response.out.write('<tr><td>Allocation</td><td><input type="text" name="Allocation" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.SyncedAllocation:self.response.out.write('<tr><td>SyncedAllocation</td><td><input type="text" name="SyncedAllocation" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.SyncedAllocation)))
  else:self.response.out.write('<tr><td>SyncedAllocation</td><td><input type="text" name="SyncedAllocation" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.allocatedamount:self.response.out.write('<tr><td>allocatedamount</td><td><input type="text" name="allocatedamount" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.allocatedamount)))
  else:self.response.out.write('<tr><td>allocatedamount</td><td><input type="text" name="allocatedamount" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.Details:self.response.out.write('<tr><td>Details</td><td><textarea cols="40" rows="5" name="Details"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Ledger.Details))
  else:self.response.out.write('<tr><td>Details</td><td><textarea cols="40" rows="5" name="Details"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')

  if Ledger.supplies:self.response.out.write('<tr><td>supplies</td><td><input type="text" name="supplies" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.supplies)))
  else:self.response.out.write('<tr><td>supplies</td><td><input type="text" name="supplies" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.contractlabor:self.response.out.write('<tr><td>contractlabor</td><td><input type="text" name="contractlabor" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.contractlabor)))
  else:self.response.out.write('<tr><td>contractlabor</td><td><input type="text" name="contractlabor" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.initialdepreciable:self.response.out.write('<tr><td>initialdepreciable</td><td><input type="text" name="initialdepreciable" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.initialdepreciable)))
  else:self.response.out.write('<tr><td>initialdepreciable</td><td><input type="text" name="initialdepreciable" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.insurance:self.response.out.write('<tr><td>insurance</td><td><input type="text" name="insurance" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.insurance)))
  else:self.response.out.write('<tr><td>insurance</td><td><input type="text" name="insurance" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.interest:self.response.out.write('<tr><td>interest</td><td><input type="text" name="interest" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.interest)))
  else:self.response.out.write('<tr><td>interest</td><td><input type="text" name="interest" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.legal:self.response.out.write('<tr><td>legal</td><td><input type="text" name="legal" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.legal)))
  else:self.response.out.write('<tr><td>legal</td><td><input type="text" name="legal" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.office:self.response.out.write('<tr><td>office</td><td><input type="text" name="office" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.office)))
  else:self.response.out.write('<tr><td>office</td><td><input type="text" name="office" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.rentalequipment:self.response.out.write('<tr><td>rentalequipment</td><td><input type="text" name="rentalequipment" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.rentalequipment)))
  else:self.response.out.write('<tr><td>rentalequipment</td><td><input type="text" name="rentalequipment" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.repairs:self.response.out.write('<tr><td>repairs</td><td><input type="text" name="repairs" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.repairs)))
  else:self.response.out.write('<tr><td>repairs</td><td><input type="text" name="repairs" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.taxandlicense:self.response.out.write('<tr><td>taxandlicense</td><td><input type="text" name="taxandlicense" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.taxandlicense)))
  else:self.response.out.write('<tr><td>taxandlicense</td><td><input type="text" name="taxandlicense" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.salestax:self.response.out.write('<tr><td>salestax</td><td><input type="text" name="salestax" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.salestax)))
  else:self.response.out.write('<tr><td>salestax</td><td><input type="text" name="salestax" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.travel:self.response.out.write('<tr><td>travel</td><td><input type="text" name="travel" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.travel)))
  else:self.response.out.write('<tr><td>travel</td><td><input type="text" name="travel" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.mealsandentertainment:self.response.out.write('<tr><td>mealsandentertainment</td><td><input type="text" name="mealsandentertainment" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.mealsandentertainment)))
  else:self.response.out.write('<tr><td>mealsandentertainment</td><td><input type="text" name="mealsandentertainment" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  if Ledger.wages:self.response.out.write('<tr><td>wages</td><td><input type="text" name="wages" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Ledger.wages)))
  else:self.response.out.write('<tr><td>wages</td><td><input type="text" name="wages" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  <iframe src="https://app.box.com/embed_widget/ijjkqfp8qt47/s/fgh4mf7et40rptf2qtui?view=list&sort=name&direction=ASC&theme=blue" width="500" height="300" frameborder="0" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>
  ''')

def write_LedgerTable(self):
    LedgerData = db.GqlQuery(LedgerGQLSelect+get_LedgerGQLWHERE()+get_LedgerGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>date</td><td>TransactionDate</td><td>Total</td><td>Type</td><td>Category</td><td>SubCategory</td><td>Details</td>
</tr>''')
    for c in LedgerData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.date,c.TransactionDate,c.Total,c.Type,c.Category,c.SubCategory,c.Details,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newLedger(self):
  AutoNumber=LedgerCount+1001
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New Ledger</b></caption>
    <form action="/StoreALedger" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>Date Modified</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td>TransactionDate</td><td><input type="text" name="TransactionDate" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Total</td><td><input type="text" name="Total" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')

  Typeselectoptions=["Receipt","Expense","DepreciableExpense","Income"]
  self.response.out.write('<tr><td>Type</td><td><select name="Type"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in Typeselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')

  Categoryselectoptions=["","Field","Office","Transportation","Overhead"]
  self.response.out.write('<tr><td>Category (deprecated)</td><td><select name="Category"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in Categoryselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')

  SubCategoryselectoptions=["","equipment","supply","service","postage","backgroundcheck","insurance","other"]
  self.response.out.write('<tr><td>Sub Category (deprecated)</td><td><select name="SubCategory"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in SubCategoryselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')
  self.response.out.write('<tr><td>Supplier</td><td><input type="text" name="Supplier" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>FileName</td><td><input type="text" name="FileName" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Expensed</td><td><input type="text" name="Expensed" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Allocation</td><td><input type="text" name="Allocation" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>allocatedamount</td><td><input type="text" name="allocatedamount" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>') 
  self.response.out.write('<tr><td>Details</td><td><textarea cols="40" rows="5" name="Details"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>supplies</td><td><input type="text" name="supplies" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>contractlabor</td><td><input type="text" name="contractlabor" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>initialdepreciable</td><td><input type="text" name="initialdepreciable" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>insurance</td><td><input type="text" name="insurance" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>interest</td><td><input type="text" name="interest" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>legal</td><td><input type="text" name="legal" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>office</td><td><input type="text" name="office" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>rentalequipment</td><td><input type="text" name="rentalequipment" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>repairs</td><td><input type="text" name="repairs" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>taxandlicense</td><td><input type="text" name="taxandlicense" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>salestax</td><td><input type="text" name="salestax" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>travel</td><td><input type="text" name="travel" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>mealsandentertainment</td><td><input type="text" name="mealsandentertainment" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>wages</td><td><input type="text" name="wages" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
 
  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterLedger" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(LedgerCount)
  self.response.out.write(''' Ledger(s).</table><iframe src="https://app.box.com/embed_widget/ijjkqfp8qt47/s/fgh4mf7et40rptf2qtui?view=list&sort=name&direction=ASC&theme=blue" width="500" height="400" frameborder="0" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>
</body></html>
''')

class Bid(db.Model):
    ID=db.StringProperty()
    date=db.DateTimeProperty(required=True, auto_now=True)
    Nominal=db.StringProperty()
    Verbiage=db.TextProperty()
    QuantityCode=db.StringProperty()
    UnitCost=db.StringProperty()
    Location=db.StringProperty()
    Category=db.StringProperty()

BidGQLSelect="SELECT * FROM Bid"
BidCurrentIndex = -1;
BidCount = 0;
BidFieldNames=["ID","date","Location","Category","Nominal","Verbiage","QuantityCode","UnitCost",]

def get_BidGQLWHERE():
    data = memcache.get('BidGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('BidGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_BidGQLSort():
    data = memcache.get('BidGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('BidGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_BidCurrentIndex():
    data = memcache.get('BidCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('BidCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data

class BidPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                BidData=db.GqlQuery(BidGQLSelect+get_BidGQLWHERE()+get_BidGQLSort())
                global BidCount
                BidCount=BidData.count()
                if get_BidCurrentIndex()==-1:
                    BidCurrentIndex=BidCount
                    memcache.set('BidCurrentIndex',BidCurrentIndex,namespace=users.get_current_user().user_id())
                if BidCount==0:
                    self.redirect('/NewBid')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuAdministrator)
                    self.response.out.write(page.Body)
                    write_Bid(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class FirstBid(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstBid')
    def get(self):
        BidCurrentIndex = 1
        memcache.set('BidCurrentIndex',BidCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/BidPage')

class PreviousBid(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousBid')
  def get(self):
    if get_BidCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/BidPage')
    else:
      BidCurrentIndex = get_BidCurrentIndex()-1
      memcache.set('BidCurrentIndex',BidCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/BidPage')

class NextBid(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextBid')
  def get(self):
    if get_BidCurrentIndex() + 1 > BidCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/BidPage')
    else:
      BidCurrentIndex = get_BidCurrentIndex()+1
      memcache.set('BidCurrentIndex',BidCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/BidPage')

class LastBid(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastBid')
    def get(self):
        BidCurrentIndex = BidCount
        memcache.set('BidCurrentIndex',BidCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/BidPage')

class NewBid(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewBid')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newBid(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class BidTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/BidTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_BidTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterBid(webapp2.RequestHandler):
    def post(self):
        memcache.set('BidGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('BidCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/BidPage')

class GotoBid(webapp2.RequestHandler):
    def post(self):
        recordnumber=self.request.get('recordnumber')
        memcache.set('BidCurrentIndex',int(recordnumber),namespace=users.get_current_user().user_id())
        self.redirect('/BidPage')

class SelectBid(webapp2.RequestHandler):
    def post(self):
        offset=self.request.get('SelectRecent')
        memcache.set('BidCurrentIndex',int(offset)-1000,namespace=users.get_current_user().user_id())
        self.redirect('/BidPage')

class FilterBid(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        BidGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('BidGQLWHERE',BidGQLWHERE,namespace=users.get_current_user().user_id())
        BidGQLSort=" ORDER BY ID ASC"
        memcache.set('BidGQLSort',BidGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('BidCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/BidPage')

class SortBid(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        BidGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('BidGQLSort',BidGQLSort,namespace=users.get_current_user().user_id())
        BidGQLWHERE=""
        memcache.set('BidGQLWHERE',BidGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('BidCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/BidPage')

class StoreABid(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    Nominal=self.request.get('Nominal')
    Verbiage=self.request.get('Verbiage')
    QuantityCode=self.request.get('QuantityCode')
    UnitCost=self.request.get('UnitCost')
    Location=self.request.get('Location')
    Category=self.request.get('Category')

    self.store_a_Bid(ID,Nominal,Verbiage,QuantityCode,UnitCost,Location,Category)
  def store_a_Bid(self,ID,Nominal,Verbiage,QuantityCode,UnitCost,Location,Category):
    entry = db.GqlQuery("SELECT * FROM Bid where ID = :1", ID).get()
    if entry:
      entry.ID=ID
      entry.Nominal=Nominal
      entry.Verbiage=Verbiage
      entry.QuantityCode=QuantityCode
      entry.UnitCost=UnitCost
      entry.Location=Location
      entry.Category=Category

    else:
      entry = Bid(ID=ID,Nominal=Nominal,Verbiage=Verbiage,QuantityCode=QuantityCode,UnitCost=UnitCost,Location=Location,Category=Category)
      entry.ID=str(BidCount+1001)
      global BidCount
      BidCount += 1
    entry.put()
    global StatusBar
    StatusBar = "saved"
    self.redirect('/BidPage')

def write_Bid(self):
  if get_BidCurrentIndex()<=0:
      BidOffset=0
  else:
      BidOffset=get_BidCurrentIndex()-1
  QuickSelectBids=db.GqlQuery('SELECT * FROM Bid ORDER BY Location ASC, Category ASC, Nominal ASC')
  Bid=db.GqlQuery(BidGQLSelect+get_BidGQLWHERE()+get_BidGQLSort()).get(deadline=60, offset=BidOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  self.response.out.write('''
  <h1 id="recordID">Bid</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstBid" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousBid" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextBid" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastBid" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewBid" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterBid" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/BidTable">Show all in a table.</a></td>
  <td><form action="/GotoBid" method="post" enctype=application/x-www-form-urlencoded>Goto: <input type="text" name="recordnumber" size="2"> <input type="submit" value="Go"></form></td>
  </tr></table>
  <form id="filterform" action="/FilterBid" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''' %(BidOffset+1,BidCount))
  for f in BidFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortBid" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in BidFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br></div>
<form id="QuickSelectBid" action="/SelectBid" method="post" enctype=application/x-www-form-urlencoded>Select Recent:
  <select name="SelectRecent" id="SelectRecent">''')
  for q in QuickSelectBids:
      self.response.out.write('<option value="%s">%s - %s - %s</option>' % (q.ID,q.Location,q.Category,q.Nominal))
  self.response.out.write('''</select></td><td><input type="submit" value="Go"></form>

  <table border=0>
  <caption></caption>
    <form action="/StoreABid" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Bid.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(Bid.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if Bid.date:self.response.out.write('<tr><td>date</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(Bid.date)))
  else:self.response.out.write('<tr><td>date</td><td><input type="text" name="date" value=""   readonly></td><tr>')
  if Bid.Nominal:self.response.out.write('<tr><td>Nominal</td><td><input type="text" name="Nominal" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Bid.Nominal)))
  else:self.response.out.write('<tr><td>Nominal</td><td><input type="text" name="Nominal" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  Locationselectoptions=["Exterior","Interior","Both"]
  if Bid.Location:
    self.response.out.write('<tr><td>Location</td><td><select name="Location" id="Location" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Locationselectoptions:
        if Bid.Location==c:
            self.response.out.write('<option value="%s" selected>' %(c))
            self.response.out.write('%s</option>' %(c))
        else:
            self.response.out.write('<option value="%s">' %(c))
            self.response.out.write('%s</option>' %(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Location</td><td><select name="Location" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Locationselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')

  Categoryselectoptions=['yard', 'removal', 'openings', 'locks', 'construction', 'plumbing/hvac', 'electrical', 'pool', 'mold']
  if Bid.Category:
    self.response.out.write('<tr><td>Category</td><td><select name="Category" id="Category" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Categoryselectoptions:
        if Bid.Category==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Category</td><td><select name="Category" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in Categoryselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')


  if Bid.Verbiage:self.response.out.write('<tr><td>Verbiage</td><td><textarea cols="40" rows="5" name="Verbiage"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">%s</textarea></td><tr>' % escape(Bid.Verbiage))
  else:self.response.out.write('<tr><td>Verbiage</td><td><textarea cols="40" rows="5" name="Verbiage"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td><tr>')
  if Bid.QuantityCode:self.response.out.write('<tr><td>Quantity Code</td><td><input type="text" name="QuantityCode" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Bid.QuantityCode)))
  else:self.response.out.write('<tr><td>Quantity Code</td><td><input type="text" name="QuantityCode" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Bid.UnitCost:self.response.out.write('<tr><td>Unit Cost</td><td><input type="text" name="UnitCost" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Bid.UnitCost)))
  else:self.response.out.write('<tr><td>Unit Cost</td><td><input type="text" name="UnitCost" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')

def write_BidTable(self):
    BidData = db.GqlQuery(BidGQLSelect+get_BidGQLWHERE()+get_BidGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>date</td><td>Nominal</td><td>Verbiage</td><td>QuantityCode</td><td>UnitCost</td>
</tr>''')
    for c in BidData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.date,c.Nominal,c.Verbiage,c.QuantityCode,c.UnitCost,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newBid(self):
  AutoNumber=BidCount+1001
  self.response.out.write('''</div>
  <p><br>
  <table border=0>
  <caption><b>Enter New Bid</b></caption>
    <form action="/StoreABid" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>date</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))

  Locationselectoptions=["Exterior","Interior","Both"]
  self.response.out.write('<tr><td>Location</td><td><select name="Location" id="Location" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in Locationselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('''</select></td><td></td><tr>''')

  Categoryselectoptions=['yard', 'removal', 'openings', 'locks', 'construction', 'plumbing/hvac', 'electrical', 'pool', 'mold']
  self.response.out.write('<tr><td>Category</td><td><select name="Category" id="Location" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in Categoryselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('''</select></td><td></td><tr>''')
  
  self.response.out.write('<tr><td>Nominal</td><td><input type="text" name="Nominal" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Verbiage</td><td><textarea cols="40" rows="5" name="Verbiage"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></textarea></td></tr>')
  self.response.out.write('<tr><td>Quantity Code</td><td><input type="text" name="QuantityCode" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Unit Cost</td><td><input type="text" name="UnitCost" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/ClearFilterBid" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(BidCount)
  self.response.out.write(''' Bid(s).</table></body></html>
''')

class Mileage(db.Model):
    ID=db.StringProperty()
    date=db.DateTimeProperty(required=True, auto_now=True)
    OdometerStart=db.StringProperty()
    OdometerEnd=db.StringProperty()
    TotalMiles=db.StringProperty()
    AllocationType=db.StringProperty()
    Allocate=db.StringProperty()

MileageGQLSelect="SELECT * FROM Mileage"
MileageCurrentIndex = -1;
MileageCount = 0;
MileageFieldNames=["ID","date","OdometerStart","OdometerEnd","TotalMiles","AllocationType","Allocate",]

def get_MileageGQLWHERE():
    data = memcache.get('MileageGQLWHERE', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = ""
        memcache.add('MileageGQLWHERE', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_MileageGQLSort():
    data = memcache.get('MileageGQLSort', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = " ORDER BY ID ASC"
        memcache.add('MileageGQLSort', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_MileageCurrentIndex():
    data = memcache.get('MileageCurrentIndex', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        data = -1
        memcache.add('MileageCurrentIndex', data, 60, namespace=users.get_current_user().user_id())
        return data
def get_OdometerStart():
    data = memcache.get('OdometerStart', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        mileagedata=db.GqlQuery("SELECT * FROM Mileage ORDER BY ID ASC")
        miles=mileagedata.get(deadline=60, offset=MileageCount-1, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
        memcache.add('OdometerStart', miles.OdometerStart, 60, namespace=users.get_current_user().user_id())
        return miles.OdometerStart
def get_MilesAllocated():
    data = memcache.get('MilesAllocated', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        mileagedata=db.GqlQuery("SELECT * FROM Mileage ORDER BY ID ASC")
        miles=mileagedata.get(deadline=60, offset=MileageCount-1, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
        memcache.add('MilesAllocated', miles.Allocate, 60, namespace=users.get_current_user().user_id())
        return miles.Allocate
def get_MilesAllocationType():
    data = memcache.get('MilesAllocationType', namespace=users.get_current_user().user_id())
    if data is not None:
        return data
    else:
        mileagedata=db.GqlQuery("SELECT * FROM Mileage ORDER BY ID ASC")
        miles=mileagedata.get(deadline=60, offset=MileageCount-1, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
        memcache.add('MilesAllocationType', miles.AllocationType, 60, namespace=users.get_current_user().user_id())
        return miles.AllocationType

class MileagePage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                MileageData=db.GqlQuery(MileageGQLSelect+get_MileageGQLWHERE()+get_MileageGQLSort())
                global MileageCount
                MileageCount=MileageData.count()
                if get_MileageCurrentIndex()==-1:
                    MileageCurrentIndex=MileageCount
                    memcache.set('MileageCurrentIndex',MileageCurrentIndex,namespace=users.get_current_user().user_id())
                if MileageCount==0:
                    self.redirect('/NewMileage')
                else:
                    self.response.headers['Content-Type'] = 'text/html'
                    self.response.out.write(page.Head)
                    self.response.out.write(page.Script)
                    self.response.out.write(htmlMenuAdministrator)
                    self.response.out.write(page.Body)
                    write_Mileage(self)
                    self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                    self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)
    
            
class FirstMileage(webapp2.RequestHandler):
    def post(self):
        self.redirect('/FirstMileage')
    def get(self):
        MileageCurrentIndex = 1
        memcache.set('MileageCurrentIndex',MileageCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/MileagePage')

class PreviousMileage(webapp2.RequestHandler):
  def post(self):
    self.redirect('/PreviousMileage')
  def get(self):
    if get_MileageCurrentIndex() - 1 < 1:
      global StatusBar
      StatusBar="No previous"
      self.redirect('/MileagePage')
    else:
      MileageCurrentIndex = get_MileageCurrentIndex()-1
      memcache.set('MileageCurrentIndex',MileageCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/MileagePage')

class NextMileage(webapp2.RequestHandler):
  def post(self):
    self.redirect('/NextMileage')
  def get(self):
    if get_MileageCurrentIndex() + 1 > MileageCount:
      global StatusBar
      StatusBar="No next"
      self.redirect('/MileagePage')
    else:
      MileageCurrentIndex = get_MileageCurrentIndex()+1
      memcache.set('MileageCurrentIndex',MileageCurrentIndex,namespace=users.get_current_user().user_id())
      self.redirect('/MileagePage')

class LastMileage(webapp2.RequestHandler):
    def post(self):
        self.redirect('/LastMileage')
    def get(self):
        MileageCurrentIndex = MileageCount
        memcache.set('MileageCurrentIndex',MileageCurrentIndex,namespace=users.get_current_user().user_id())
        self.redirect('/MileagePage')

class NewMileage(webapp2.RequestHandler):
    def post(self):
        self.redirect('/NewMileage')
    def get(self):
        page=get_Page()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(page.Head)
        self.response.out.write(page.Script)
        self.response.out.write(htmlMenuAdministrator)
        self.response.out.write(page.Body)
        write_newMileage(self)
        self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
        self.response.out.write(page.Foot)

class MileageTable(webapp2.RequestHandler):
    def post(self):
        self.redirect('/MileageTable')
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(page.Body)
                write_MileageTable(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
        else:
            global StatusBar
            StatusBar=('<br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

class ClearFilterMileage(webapp2.RequestHandler):
    def post(self):
        memcache.set('MileageGQLWHERE',"",namespace=users.get_current_user().user_id())
        memcache.set('MileageCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/MileagePage')

class GotoMileage(webapp2.RequestHandler):
    def post(self):
        recordnumber=self.request.get('recordnumber')
        memcache.set('MileageCurrentIndex',int(recordnumber),namespace=users.get_current_user().user_id())
        self.redirect('/MileagePage')

class FilterMileage(webapp2.RequestHandler):
    def post(self):
        filtervalue=self.request.get('filtervalue')
        filterfield=self.request.get('filterfield')
        filterequality=self.request.get('filterequality')
        MileageGQLWHERE=" WHERE "+filterfield+filterequality+"'"+filtervalue+"'"
        memcache.set('MileageGQLWHERE',MileageGQLWHERE,namespace=users.get_current_user().user_id())
        MileageGQLSort=""
        memcache.set('MileageGQLSort',MileageGQLSort,namespace=users.get_current_user().user_id())
        memcache.set('MileageCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/MileagePage')

class SortMileage(webapp2.RequestHandler):
    def post(self):
        sortfield=self.request.get('sortfield')
        sortdirection=self.request.get('sortdirection')
        MileageGQLSort=" ORDER BY "+sortfield+" "+sortdirection
        memcache.set('MileageGQLSort',MileageGQLSort,namespace=users.get_current_user().user_id())
        MileageGQLWHERE=""
        memcache.set('MileageGQLWHERE',MileageGQLWHERE,namespace=users.get_current_user().user_id())
        memcache.set('MileageCurrentIndex',-1,namespace=users.get_current_user().user_id())
        self.redirect('/MileagePage')

class StoreAMileage(webapp2.RequestHandler):
  def post(self):
    ID=self.request.get('ID')
    OdometerStart=self.request.get('OdometerStart')
    OdometerEnd=self.request.get('OdometerEnd')
    TotalMiles=self.request.get('TotalMiles')
    AllocationType=self.request.get('AllocationType')
    Allocate=self.request.get('Allocate')

    self.store_a_Mileage(ID,OdometerStart,OdometerEnd,TotalMiles,AllocationType,Allocate,)
  def store_a_Mileage(self,ID,OdometerStart,OdometerEnd,TotalMiles,AllocationType,Allocate,):
    entry = db.GqlQuery("SELECT * FROM Mileage where ID = :1", ID).get()
    if entry:
      entry.ID=ID
      entry.OdometerStart=OdometerStart
      entry.OdometerEnd=OdometerEnd
      entry.TotalMiles=TotalMiles
      entry.AllocationType=AllocationType
      entry.Allocate=Allocate

    else:
      memcache.set('MileageCurrentIndex',-1,namespace=users.get_current_user().user_id())
      entry = Mileage(ID=ID,OdometerStart=OdometerStart,OdometerEnd=OdometerEnd,TotalMiles=TotalMiles,AllocationType=AllocationType,Allocate=Allocate,)
      entry.ID=str(MileageCount+1001)
      
    entry.put()

    ##sync total miles with work order allocated.
##    wo_entry=db.GqlQuery("SELECT * FROM WorkOrder where ID = '%s'" %s(Allocate)).get()
##    if wo_entry is not None:
##        if wo_entry.MilesTotal is None:
##            wo_entry.MilesTotal=TotalMiles
##        else:
##            wo_entry.MilesTotal+=TotalMiles
##        wo_entry.put()
    
    global StatusBar
    StatusBar = "saved"
    self.redirect('/MileagePage')

class AutoStoreAMileage(webapp2.RequestHandler):
  def post(self):
    OdometerStart=get_OdometerStart()
    OdometerEnd=self.request.get('OdometerStart')
    TotalMiles=str(int(OdometerEnd)-int(OdometerStart))
    AllocationType=get_MilesAllocationType()
    Allocate=get_MilesAllocated()
    NewAllocate=self.request.get('Allocate')
    NewAllocationType=self.request.get('AllocationType')
    
    #reset the memcache MileageLog
    memcache.set('OdometerStart',OdometerEnd,namespace=users.get_current_user().user_id())
    memcache.set('MilesAllocated',NewAllocate,namespace=users.get_current_user().user_id())
    memcache.set('MilesAllocationType',NewAllocationType,namespace=users.get_current_user().user_id())

    self.store_a_Mileage(OdometerStart,OdometerEnd,TotalMiles,AllocationType,Allocate,)
  def store_a_Mileage(self,OdometerStart,OdometerEnd,TotalMiles,AllocationType,Allocate,):
    entry = Mileage(OdometerStart=OdometerStart,OdometerEnd=OdometerEnd,TotalMiles=TotalMiles,AllocationType=AllocationType,Allocate=Allocate,)
    entry.ID=str(MileageCount+1001)
    global MileageCount
    MileageCount += 1
    entry.put()
    global StatusBar
    StatusBar = "saved mileage "
    self.redirect('/WorkOrderPage')

def write_Mileage(self):
  if get_MileageCurrentIndex()<=0:
      MileageOffset=0
  else:
      MileageOffset=get_MileageCurrentIndex()-1
  Mileage=db.GqlQuery(MileageGQLSelect+get_MileageGQLWHERE()+get_MileageGQLSort()).get(deadline=60, offset=MileageOffset, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
  WorkOrders=db.GqlQuery("SELECT * FROM WorkOrder ORDER BY ID DESC LIMIT 20")
  self.response.out.write('''
  <h1 id="recordID">Mileage</h1>
  <table id="navigate">
  <tr>
  <td><form action="/FirstMileage" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="|<"></form></td>
  <td><form action="/PreviousMileage" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="<"></form></td>
  <td><form action="/NextMileage" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">"></form></td>
  <td><form action="/LastMileage" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value=">|"></form></td>
  <td><form action="/NewMileage" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="*New"></form></td>
  <td><form action="/ClearFilterMileage" method="post" enctype=application/x-www-form-urlencoded> <input type="submit" value="Clear Filter"></form></td>
  <td>%s of %s records. </td><td><a href="/MileageTable">Show all in a table.</a></td>
  <td><form action="/GotoMileage" method="post" enctype=application/x-www-form-urlencoded>Goto: <input type="text" name="recordnumber" size="2"> <input type="submit" value="Go"></form></td>
  </tr></table>
  <form id="filterform" action="/FilterMileage" method="post" enctype=application/x-www-form-urlencoded>
  Filter: <select name="filterfield">''' %(MileageOffset+1,MileageCount))
  for f in MileageFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="filterequality"><option value="=">=</option><option value=">">></option><option value="<"><</option></select>
  <input type="text" name="filtervalue" value="" size="35">
  <input type="submit" value="Filter"></form>
  <form id="sortform" action="/SortMileage" method="post" enctype=application/x-www-form-urlencoded>
  OR Sort by: <select name="sortfield">''')
  for f in MileageFieldNames:
      self.response.out.write('<option value="%s">' % escape(f))
      self.response.out.write('%s</option>' % escape(f))
  self.response.out.write('''</select>
  <select name="sortdirection"><option value="ASC">+</option><option value="DESC">-</option></select>
  <input type="submit" value="Sort"></form>
<br><br>
  <table border=0>
  <caption></caption>
    <form action="/StoreAMileage" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  if Mileage.ID:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td><tr>' % escape(str(Mileage.ID)))
  else:self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value=""   readonly></td><tr>')
  if Mileage.date:self.response.out.write('<tr><td>modified date</td><td><input type="text" name="date" value="%s"   readonly></td><tr>' % escape(str(Mileage.date)))
  else:self.response.out.write('<tr><td>modified date</td><td><input type="text" name="date" value=""   readonly></td><tr>')
  if Mileage.OdometerStart:self.response.out.write('<tr><td>Odometer Start</td><td><input type="text" id="OdometerStart" name="OdometerStart" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Mileage.OdometerStart)))
  else:self.response.out.write('<tr><td>Odometer Start</td><td><input type="text" id="OdometerStart" name="OdometerStart" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  if Mileage.OdometerEnd:self.response.out.write('<tr><td>Odometer End</td><td><input type="text" id="OdometerEnd" name="OdometerEnd" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="calctotalmiles();inactiveinputFunction(this)"></td><tr>' % escape(str(Mileage.OdometerEnd)))
  else:self.response.out.write('<tr><td>Odometer End</td><td><input type="text" id="OdometerEnd" name="OdometerEnd" value="" size="35"   onfocus="activeinputFunction(this)" onblur="calctotalmiles();inactiveinputFunction(this)"></td><tr>')
  if Mileage.TotalMiles:self.response.out.write('<tr><td>Total Miles</td><td><input type="text" id="TotalMiles" name="TotalMiles" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Mileage.TotalMiles)))
  else:self.response.out.write('<tr><td>Total Miles</td><td><input type="text" id="TotalMiles" name="TotalMiles" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')
  AllocationTypeselectoptions=["Business","Personal",]
  if Mileage.AllocationType:
    self.response.out.write('''<tr><td>Allocation Type</td><td><select name="AllocationType" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">''')
    for c in AllocationTypeselectoptions:
        if Mileage.AllocationType==c:
            self.response.out.write('<option value="%s" selected>' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
        else:
            self.response.out.write('<option value="%s">' % escape(c))
            self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('''</select></td><td></td><tr>''')
  else:
    self.response.out.write('<tr><td>Allocation Type</td><td><select name="AllocationType" onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
    for c in AllocationTypeselectoptions:
        self.response.out.write('<option value="%s">' % escape(c))
        self.response.out.write('%s</option>' % escape(c))
    self.response.out.write('</select></td><td></td><tr>')
#9
  self.response.out.write('''<tr><td>Select Allocation</td><td><select onblur="AllocateMileage()" id="SelectMileageAllocation" name="SelectMileageAllocation">''')
  self.response.out.write('''<option value=""></option><option value="overhead">overhead</option><option value="commute">commute</option>''')
  for w in WorkOrders:
      self.response.out.write('''<option value=%s>%s - %s</option>''' % (w.ID,w.ID,w.PropertyAddress))
  self.response.out.write('''</select>''')
  if Mileage.Allocate:self.response.out.write('<tr><td>Allocated To</td><td><input type="text" name="Allocate" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>' % escape(str(Mileage.Allocate)))
  else:self.response.out.write('<tr><td>Allocated To</td><td><input type="text" id="Allocate" name="Allocate" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td><tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table><br>
  ''')

def write_MileageTable(self):
    MileageData = db.GqlQuery(MileageGQLSelect+get_MileageGQLWHERE()+get_MileageGQLSort())
    self.response.out.write('''<table><tr><td>ID</td><td>date</td><td>OdometerStart</td><td>OdometerEnd</td><td>TotalMiles</td><td>AllocationType</td><td>Allocate</td>
</tr>''')
    for c in MileageData:
        self.response.out.write('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>''' %(c.ID,c.date,c.OdometerStart,c.OdometerEnd,c.TotalMiles,c.AllocationType,c.Allocate,))
        self.response.out.write('''</tr>''')
    self.response.out.write('''</table>''')

def write_newMileage(self):
  AutoNumber=MileageCount+1001
  WorkOrders=db.GqlQuery("SELECT * FROM WorkOrder ORDER BY ID DESC LIMIT 200")
  MostRecentMileageRecord=db.GqlQuery("SELECT * FROM Mileage ORDER BY ID DESC LIMIT 1").get()
  self.response.out.write('''
  <p><br>
  <table border=0>
  <caption><b>Enter New Mileage</b></caption>
    <form action="/StoreAMileage" method="post"
          enctype=application/x-www-form-urlencoded>
          ''')
  self.response.out.write('<tr><td>ID</td><td><input type="text" name="ID" value="%s"   readonly></td></tr>' %AutoNumber)
  self.response.out.write('<tr><td>modified date</td><td><input type="text" name="date" value="%s"   readonly></td></tr>' %('Automatic when saved.'))
  self.response.out.write('<tr><td>Odometer Start</td><td><input type="text" id="OdometerStart" name="OdometerStart" value="%s" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>' %(MostRecentMileageRecord.OdometerEnd))
  self.response.out.write('<tr><td>Odometer End</td><td><input type="text" id="OdometerEnd" name="OdometerEnd" value="" size="35"   onfocus="activeinputFunction(this)" onblur="calctotalmiles();inactiveinputFunction(this)"></td></tr>')
  self.response.out.write('<tr><td>Total Miles</td><td><input type="text" id="TotalMiles" name="TotalMiles" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
  AllocationTypeselectoptions=["Business","Personal",]
  self.response.out.write('<tr><td>Allocation Type</td><td><select name="AllocationType"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
  for c in AllocationTypeselectoptions:
      self.response.out.write('<option value="%s">' % escape(c))
      self.response.out.write('%s</option>' % escape(c))
  self.response.out.write('</select></td><tr>')
#9
  self.response.out.write('''<tr><td>Select Allocation</td><td><select onblur="AllocateMileage()" id="SelectMileageAllocation" name="SelectMileageAllocation">''')
  self.response.out.write('''<option value=""></option><option value="overhead">overhead</option><option value="commute">commute</option>''')
  for w in WorkOrders:
      self.response.out.write('''<option value=%s>%s - %s</option>''' % (w.ID,w.ID,w.PropertyAddress))
  self.response.out.write('''</select>''')
  
  self.response.out.write('<tr><td>Allocated To</td><td><input type="text" id="Allocate" name="Allocate" value="" size="35"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')

  self.response.out.write('''
  <tr><td><input id="saverecord" type="submit" value="Save"></td></tr>
  </form></table>
  <table>
  <tr>
  <td><form action="/MileagePage" method="get" enctype=application/x-www-form-urlencoded> <input type="submit" value="Cancel"></form></td>
  <tr>''')
  self.response.out.write('*')
  self.response.out.write(' of ')
  self.response.out.write(MileageCount)
  self.response.out.write(''' Mileage(s).</table></body></html>
''')

class StatPage(webapp2.RequestHandler):
    def get(self):
        page=get_Page()
        user = users.get_current_user()
        if user:
            TheUserQuery=db.GqlQuery("SELECT * FROM TheUsers WHERE UserName='%s' LIMIT 1" %(user.nickname()))
            TheUser=TheUserQuery.get(deadline=60, offset=0, keys_only=False, projection=None, start_cursor=None, end_cursor=None)
            count = TheUserQuery.count()
            if (count==0):
                entry = TheUsers(UserName = user.nickname(),Type = 'Visitor')
                entry.put()
                self.redirect('/')
            elif(TheUser.Type=='Chad' or TheUser.Type=='Administrator' ):
                self.response.headers['Content-Type'] = 'text/html'
                self.response.out.write(page.Head)
                self.response.out.write(page.Script)
                self.response.out.write(htmlMenuAdministrator)
                self.response.out.write(page.Body)
                write_Stat(self)
                self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
                self.response.out.write(page.Foot)
            else:
                self.redirect('/')
        else:
            global StatusBar
            StatusBar=('<br><br><br><br><a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(page.Head)
            self.response.out.write(page.Script)
            self.response.out.write(page.Body)
            self.response.out.write("<div class='StatusBar'>"+StatusBar+"</div>")
            self.response.out.write(page.Foot)

def write_Stat(self):
    WorkOrders=db.GqlQuery("SELECT * FROM WorkOrder LIMIT 20000")
    Ledgers=db.GqlQuery("SELECT * FROM Ledger LIMIT 20000")
    Mileages=db.GqlQuery("SELECT * FROM Mileage LIMIT 20000")

    MissingInvoiceCount=0 #invoiced or paid but no invoice amount
    MissingInvoiceIDs=''

    TotalInvoice=0
    TotalPaid=0
    TotalPaidAllocated=0
    TotalInvoicePerPaid=0
    TotalEarningHoursPerPaid=0

    MissingHoursCount=0
    MissingHoursIDs=''
    TotalHours=0

    MissingExpenseCount=0
    MissingExpenseIDs=''
    TotalExpense=0
    TotalDepreciableExpense=0
    Totalcontractlabor=0
    Totalinsurance=0
    Totalinterest=0
    Totallegal=0
    Totalmealsandentertainment=0
    Totaloffice=0
    Totalrentalequipment=0
    Totalrepairs=0
    Totalsupplies=0
    Totaltaxandlicense=0
    Totaltravel=0
    Totalwages=0

    MissingMilesCount=0
    MissingMilesIDs=''
    TotalMiles=0
    
    for w in WorkOrders:
        if is_number(w.PaidAmount):
            TotalPaidAllocated+=float(w.PaidAmount)
            if is_number(w.InvoiceAmount):
                TotalInvoicePerPaid+=float(w.InvoiceAmount)
            if is_number(w.EarningHours):
                TotalEarningHoursPerPaid+=float(w.EarningHours)
        if is_number(w.InvoiceAmount):
            TotalInvoice+=float(w.InvoiceAmount)
        else:
            MissingInvoiceCount+=1
            MissingInvoiceIDs+=w.ID+','
        if is_number(w.EarningHours):
            TotalHours+=float(w.EarningHours)
        else:
            MissingHoursCount+=1
            MissingHoursIDs+=w.ID+','
            

    for L in Ledgers:
        if L.Type=='Income':
            if is_number(L.Total):
                TotalPaid+=float(L.Total)
        else:
            if is_number(L.Total):
                TotalExpense+=float(L.Total)
                if is_number(L.initialdepreciable):
                    TotalDepreciableExpense+=float(L.initialdepreciable)
                if is_number(L.contractlabor):
                    Totalcontractlabor+=float(L.contractlabor)    
                if is_number(L.insurance):
                    Totalinsurance+=float(L.insurance)
                if is_number(L.interest):
                    Totalinterest+=float(L.interest)               
                if is_number(L.legal):
                    Totallegal+=float(L.legal)
                if is_number(L.mealsandentertainment):
                    Totalmealsandentertainment+=float(L.mealsandentertainment)
                if is_number(L.office):
                    Totaloffice+=float(L.office)
                if is_number(L.rentalequipment):
                    Totalrentalequipment+=float(L.rentalequipment)
                if is_number(L.repairs):
                    Totalrepairs+=float(L.repairs)
                if is_number(L.supplies):
                    Totalsupplies+=float(L.supplies)
                if is_number(L.taxandlicense):
                    Totaltaxandlicense+=float(L.taxandlicense)
                if is_number(L.travel):
                    Totaltravel+=float(L.travel)
                if is_number(L.wages):
                    Totalwages+=float(L.wages)
            else:
                MissingExpenseCount+=1
                MissingExpenseIDs+=L.ID+','
                
    for M in Mileages:
        if is_number(M.TotalMiles):
            if M.AllocationType=='Business':
                TotalMiles+=int(M.TotalMiles)
        else:
            MissingMilesCount+=1
            MissingMilesIDs+=M.ID+','
    PaidToInvoicedPercentage=TotalPaidAllocated/TotalInvoicePerPaid
    DayOfYear=float(datetime.date.today().strftime("%j"))-56 #!change -56 (delete it) for 2015
    PaymentForecast=PaidToInvoicedPercentage*TotalInvoice*(1+((309-DayOfYear)/309)) #!change 309 to 365 for 2015.
    PeriodExpense=TotalExpense-TotalDepreciableExpense
    SumPeriodExpense=Totalcontractlabor+Totalinsurance+Totalinterest+Totallegal+Totalmealsandentertainment+Totaloffice+Totalrentalequipment+Totalrepairs+Totalsupplies+Totaltaxandlicense+Totaltravel+Totalwages
    MileageCost=TotalMiles*0.56
    NetEarnings=TotalInvoice-TotalExpense-MileageCost-0.75*TotalHours
    self.response.out.write('''<h1>SUMMARY:</h1>
<br>INCOME:
<br>TotalInvoice: %s
<br>TotalPaid: %s
<br>TotalPaid (allocated): %s
<br>Total Invoice where Paid: %s
<br>Total Earnings hours where paid: %s
<br>Percentage of paid amount compared to invoice amount: %s
<br>Business Days %s
<br>Payment Forecast for end of year: %s
<br><br>EXPENSES:
<br>TotalExpense: %s - TotalDepreciableExpense: %s = Period Expense: %s
<br>Totalcontractlabor: %s
<br>Totalinsurance: %s
<br>Totalinterest: %s
<br>Totallegal: %s
<br>Totalmealsandentertainment: %s
<br>Totaloffice: %s
<br>Totalrentalequipment: %s
<br>Totalrepairs: %s
<br>Totalsupplies: %s
<br>Totaltaxandlicense: %s
<br>Totaltravel: %s
<br>Totalwages: %s
<br>Sum (period expense) = %s
<br>
<br>TotalMiles: %s
<br>Mileage Cost: %s
<br><br>COST PERFORMANCE:
<br>Net Estimated Earnings (TotalInvoice-PeriodExpense-MileageCost-$0.75depreciable_allowance): %s
<br>TotalHours: %s
<br>Net Earnings per Hour: %s'''%(str(TotalInvoice),str(TotalPaid),str(TotalPaidAllocated),str(TotalInvoicePerPaid),str(TotalEarningHoursPerPaid),str(PaidToInvoicedPercentage),str(DayOfYear),str(PaymentForecast),str(TotalExpense),str(TotalDepreciableExpense),str(PeriodExpense),str(Totalcontractlabor),str(Totalinsurance),str(Totalinterest),str(Totallegal),str(Totalmealsandentertainment),str(Totaloffice),str(Totalrentalequipment),str(Totalrepairs),str(Totalsupplies),str(Totaltaxandlicense),str(Totaltravel),str(Totalwages),str(SumPeriodExpense),str(TotalMiles),str(MileageCost),str(NetEarnings),str(TotalHours),str(NetEarnings/TotalHours)))
    

htmlMenuVisitor='''<div class="menu"><a class="menu" href="%s">Become an Employee</a><a class="menu" href="%s">Become a Supplier/Subcontractor</a></div>
<br>Open the door to a world of opportunity.  Join the world premiere of mobile-workforce excellence.  
<br><br>Quality - With our cutting edge technology we are able to complete complex work order instructions to provide our clients with the complete results they expect each and every time.
<br><br>Timeliness - No more waiting.  Your urgent results are sent to you as soon as the work order is completed in the field.  
<br><br>Cost - Best value guaranteed.  We work with your standard pricing and provide exceptional dependabilty and workmanship.  We also provide the industry's best value bids for quality work along with low-cost economic alternatives. 
<br><br>Communication - Instantaneous answers to your inquiries about work order status.  Immediate execution for your urgent requests.''' % (users.create_login_url('/PersonalEmployeePage'),users.create_login_url('/PersonalSupplierPage'))
htmlMenuCustomer='<div class="menu"></div></div>'
htmlMenuClient='<div class="menu"></div></div>'
htmlMenuEmployee='<div class="menu"><a class="menu" href="/PersonalEmployeePage">Personal Information</a></div></div>'
htmlMenuMachine='<div class="menu"></div>'
htmlMenuSupplier='<div class="menu"><a class="menu" href="/PersonalSupplierPage">Personal Information</a></div></div>'
htmlMenuProcessor='<div class="menu"></div></div>'
htmlMenuManager='<div class="menu"></div></div>'
htmlMenuAdministrator='''<div id="MainMenu">
<input id="ShowPageMenuButton" type="button" style="display:none" width="165px" value="Pages" onclick="ShowPageMenu()"></input>
<input id="HidePageMenuButton" width="165px" type="button" value="Pages Off" onclick="HidePageMenu()"></input>

<input id="ShowFilterFormButton" type="button" width="165px" style="display:block" value="Filter" onclick="ShowFilterForm()"></input>
<input id="HideFilterFormButton" style="display:none" type="button" width="165px" value="Hide Filter" onclick="HideFilterForm()"></input>

<input id="ShowSortFormButton" type="button" width="165px" style="display:block" value="Sort" onclick="ShowSortForm()"></input><input id="HideSortFormButton" type="button" style="display:none" width="165px" value="Hide Sort" onclick="HideSortForm()"></input></div>
<div class="menu" id="MenuAdministrator"><a class="menu" href="/">Main</a><a class="menu" href="/TheUsersPage">TheUsers</a><a class="menu" href="/PagePage">Page</a><a class="menu" href="/VisitorPage">Visitor</a><a class="menu" href="/ClientPage">Client</a><a class="menu" href="/EmployeePage">Employee</a><a class="menu" href="/SupplierPage">Supplier</a><a class="menu" href="/MaterialPage">Material</a><a class="menu" href="/PropertyPage">Property</a><a class="menu" href="/WorkOrderPage">Work Order</a><a class="menu" href="/TimePunchPage">Time Punch</a><a class="menu" href="/LedgerPage">Ledger</a><a class="menu" href="/BidPage">Bid</a><a class="menu" href="/MileagePage">Mileage</a><a class="menu" href="/StatPage">Stats</a></div></div>'''
def write_htmlMenuAdministrator(self):
    a=0;
##    self.response.out.write('''<br>Previous odometer reading: %s, %s, allocated to: %s.
##<br><form action="/AutoStoreAMileage" method="post" enctype=application/x-www-form-urlencoded>
##Enter new odometer reading: <input type="text" name="OdometerStart" value="" size="6"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">
##''' % (get_OdometerStart(),get_MilesAllocationType(),get_MilesAllocated()))
##    AllocationTypeselectoptions=["Business","Personal",]
##    self.response.out.write('<tr><td>new allocation type: </td><td><select name="AllocationType"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)">')
##    for c in AllocationTypeselectoptions:
##      self.response.out.write('<option value="%s">' % escape(c))
##      self.response.out.write('%s</option>' % escape(c))
##    self.response.out.write('</select></td><tr>')
##    self.response.out.write('<tr><td>start wo#: </td><td><input type="text" name="Allocate" value="" size="10"   onfocus="activeinputFunction(this)" onblur="inactiveinputFunction(this)"></td></tr>')
##    self.response.out.write('''
##    <tr><td><input type="submit" value="Enter Mileage Log"></td></tr>
##    </form>
##    ''')
app = webapp2.WSGIApplication([('/', MainHandler),('/TheUsersPage', TheUsersPage),('/FirstTheUsers', FirstTheUsers),('/PreviousTheUsers', PreviousTheUsers),('/NextTheUsers', NextTheUsers),('/LastTheUsers', LastTheUsers),('/NewTheUsers', NewTheUsers),('/TheUsersTable', TheUsersTable),('/ClearFilterTheUsers',ClearFilterTheUsers),('/GotoTheUsers',GotoTheUsers),('/FilterTheUsers',FilterTheUsers),('/SortTheUsers',SortTheUsers),('/StoreATheUsers', StoreATheUsers),('/PagePage', PagePage),('/FirstPage', FirstPage),('/PreviousPage', PreviousPage),('/NextPage', NextPage),('/LastPage', LastPage),('/NewPage', NewPage),('/PageTable', PageTable),('/ClearFilterPage',ClearFilterPage),('/FilterPage',FilterPage),('/SortPage',SortPage),('/StoreAPage', StoreAPage),('/VisitorPage', VisitorPage),('/FirstVisitor', FirstVisitor),('/PreviousVisitor', PreviousVisitor),('/NextVisitor', NextVisitor),('/LastVisitor', LastVisitor),('/NewVisitor', NewVisitor),('/VisitorTable', VisitorTable),('/ClearFilterVisitor',ClearFilterVisitor),('/FilterVisitor',FilterVisitor),('/SortVisitor',SortVisitor),('/StoreAVisitor', StoreAVisitor),('/CustomerPage', CustomerPage),('/FirstCustomer', FirstCustomer),('/PreviousCustomer', PreviousCustomer),('/NextCustomer', NextCustomer),('/LastCustomer', LastCustomer),('/NewCustomer', NewCustomer),('/CustomerTable', CustomerTable),('/ClearFilterCustomer',ClearFilterCustomer),('/FilterCustomer',FilterCustomer),('/SortCustomer',SortCustomer),('/StoreACustomer', StoreACustomer),('/ClientPage', ClientPage),('/FirstClient', FirstClient),('/PreviousClient', PreviousClient),('/NextClient', NextClient),('/LastClient', LastClient),('/NewClient', NewClient),('/ClientTable', ClientTable),('/ClearFilterClient',ClearFilterClient),('/FilterClient',FilterClient),('/SortClient',SortClient),('/StoreAClient', StoreAClient),('/EmployeePage', EmployeePage),('/FirstEmployee', FirstEmployee),('/PreviousEmployee', PreviousEmployee),('/NextEmployee', NextEmployee),('/LastEmployee', LastEmployee),('/NewEmployee', NewEmployee),('/EmployeeTable', EmployeeTable),('/ClearFilterEmployee',ClearFilterEmployee),('/FilterEmployee',FilterEmployee),('/SortEmployee',SortEmployee),('/StoreAEmployee', StoreAEmployee),('/SupplierPage', SupplierPage),('/FirstSupplier', FirstSupplier),('/PreviousSupplier', PreviousSupplier),('/NextSupplier', NextSupplier),('/LastSupplier', LastSupplier),('/NewSupplier', NewSupplier),('/SupplierTable', SupplierTable),('/ClearFilterSupplier',ClearFilterSupplier),('/FilterSupplier',FilterSupplier),('/SortSupplier',SortSupplier),('/StoreASupplier', StoreASupplier),('/MaterialPage', MaterialPage),('/FirstMaterial', FirstMaterial),('/PreviousMaterial', PreviousMaterial),('/NextMaterial', NextMaterial),('/LastMaterial', LastMaterial),('/NewMaterial', NewMaterial),('/MaterialTable', MaterialTable),('/ClearFilterMaterial',ClearFilterMaterial),('/FilterMaterial',FilterMaterial),('/SortMaterial',SortMaterial),('/StoreAMaterial', StoreAMaterial),('/PersonalVisitorPage',PersonalVisitorPage),('/PersonalCustomerPage',PersonalCustomerPage),('/PersonalClientPage',PersonalClientPage),('/PersonalEmployeePage',PersonalEmployeePage),('/StoreAPersonalEmployee',StoreAPersonalEmployee),('/PersonalSupplierPage',PersonalSupplierPage),('/ProcessorPage', ProcessorPage),('/FirstProcessor', FirstProcessor),('/PreviousProcessor', PreviousProcessor),('/NextProcessor', NextProcessor),('/LastProcessor', LastProcessor),('/NewProcessor', NewProcessor),('/ProcessorTable', ProcessorTable),('/ClearFilterProcessor',ClearFilterProcessor),('/FilterProcessor',FilterProcessor),('/SortProcessor',SortProcessor),('/StoreAProcessor', StoreAProcessor),('/PropertyPage', PropertyPage),('/FirstProperty', FirstProperty),('/PreviousProperty', PreviousProperty),('/NextProperty', NextProperty),('/LastProperty', LastProperty),('/NewProperty', NewProperty),('/PropertyTable', PropertyTable),('/ClearFilterProperty',ClearFilterProperty),('/GotoProperty',GotoProperty),('/SelectProperty',SelectProperty),('/FilterProperty',FilterProperty),('/SortProperty',SortProperty),('/StoreAProperty', StoreAProperty),('/WorkOrderPage', WorkOrderPage),('/FirstWorkOrder', FirstWorkOrder),('/PreviousWorkOrder', PreviousWorkOrder),('/NextWorkOrder', NextWorkOrder),('/LastWorkOrder', LastWorkOrder),('/NewWorkOrder', NewWorkOrder),('/WorkOrderTable', WorkOrderTable),('/ClearFilterWorkOrder',ClearFilterWorkOrder),('/GotoWorkOrder',GotoWorkOrder),('/SelectWorkOrder',SelectWorkOrder),('/SelectOpenWorkOrder',SelectOpenWorkOrder),('/FilterWorkOrder',FilterWorkOrder),('/SortWorkOrder',SortWorkOrder),('/StoreAWorkOrder', StoreAWorkOrder),('/TimePunchPage', TimePunchPage),('/FirstTimePunch', FirstTimePunch),('/PreviousTimePunch', PreviousTimePunch),('/NextTimePunch', NextTimePunch),('/LastTimePunch', LastTimePunch),('/NewTimePunch', NewTimePunch),('/TimePunchTable', TimePunchTable),('/ClearFilterTimePunch',ClearFilterTimePunch),('/FilterTimePunch',FilterTimePunch),('/SortTimePunch',SortTimePunch),('/StoreATimePunch', StoreATimePunch),('/LedgerPage', LedgerPage),('/FirstLedger', FirstLedger),('/PreviousLedger', PreviousLedger),('/NextLedger', NextLedger),('/LastLedger', LastLedger),('/NewLedger', NewLedger),('/LedgerTable', LedgerTable),('/ClearFilterLedger',ClearFilterLedger),('/FilterLedger',FilterLedger),('/SortLedger',SortLedger),('/StoreALedger', StoreALedger),('/BidPage', BidPage),('/FirstBid', FirstBid),('/PreviousBid', PreviousBid),('/NextBid', NextBid),('/LastBid', LastBid),('/NewBid', NewBid),('/BidTable', BidTable),('/ClearFilterBid',ClearFilterBid),('/GotoBid',GotoBid),('/SelectBid',SelectBid),('/FilterBid',FilterBid),('/SortBid',SortBid),('/StoreABid', StoreABid),('/MileagePage', MileagePage),('/FirstMileage', FirstMileage),('/PreviousMileage', PreviousMileage),('/NextMileage', NextMileage),('/LastMileage', LastMileage),('/NewMileage', NewMileage),('/MileageTable', MileageTable),('/ClearFilterMileage',ClearFilterMileage),('/GotoMileage',GotoMileage),('/FilterMileage',FilterMileage),('/SortMileage',SortMileage),('/StoreAMileage', StoreAMileage),('/AutoStoreAMileage', AutoStoreAMileage),('/StatPage', StatPage)], debug=True)
