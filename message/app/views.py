from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.sqla.filters import FilterEqualFunction, FilterStartsWith
from flask_appbuilder import ModelView,AppBuilder,expose,BaseView,ModelRestApi,has_access
from . import appbuilder, db
from .models import Member
from flask import jsonify,make_response,session
from flask import g

def get_user():
    return g.user.username

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', 
base_template=appbuilder.base_template, appbuilder=appbuilder), 404

class userinfo2(BaseView):
    default_view = 'test'
    @expose('/test/')
    @has_access
    def test(self):
        print (get_user())
        param1 = 'test'
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        # return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder, param1 = param1), 404
        return self.render_template('tt.html', base_template=appbuilder.base_template, appbuilder=appbuilder, param1 = param1)


class MemberModelView(ModelView):
    datamodel = SQLAInterface(Member)
    page_size=10
    base_filters = [['user', FilterEqualFunction, get_user]]
    #修改列名称
    label_columns = {'user':'帳號','nickname':'簽名或寄信者','user_password':'備註','signature':'客戶金鑰','point':'點數','account':'供應商帳號','password':'供應商密碼','extno':'供應商模板ID或寄信者名稱','multiple':'费用倍数'}
    #定义列显示名称
    list_columns = ['user','nickname','user_password','signature','point','account','password','extno','multiple'] #定义视图中要显示的字段
    show_fieldsets = [
        (
            'Summary',
            {'fields':['user','nickname','user_password','signature','point','account','password','extno','multiple']}
        ),
        ] 

class userinfo(BaseView):
    default_view = 'list'
    @expose('/list/')
    @has_access
    def list(self):
        session['bucket'] = 'bucket'
        users = db.session.query(Member).all()
        titleinfo = ['ID號','帳號','日期']
        allinfo = []
        for user in users:
            allinfo.append({'id':user.id, 'infos': [user.name, user.created_at]})
        stack = {  # dict
        'add': './../add', 
        'edit': './../edit', 
        'del': '../del', 
        'main' : '加帳號', 
        'info' : '帳號',
        'titleinfo': titleinfo,
        'allinfo': allinfo
        }
        print (get_user())
        return render_template('shows.twig',base_template=appbuilder.base_template, appbuilder=appbuilder, stack=stack)
    
    @expose('/add/')
    def add(self):
        session['bucket'] = 'bucket'
        users = db.session.query(Member).all()
        titleinfo = ['ID號','帳號','日期']
        allinfo = []
        for user in users:
            allinfo.append({'id':user.id, 'infos': [user.name, user.created_at]})
        stack = {  # dict
        'add': './../add', 
        'edit': './../edit', 
        'del': '../delete', 
        'main' : '加帳號', 
        'info' : '帳號',
        'titleinfo': titleinfo,
        'allinfo': allinfo
        }
        return render_template('shows.twig', stack=stack)   

    @expose('/edit/')
    def edit(self):
        session['bucket'] = 'bucket'
        users = db.session.query(Member).all()
        titleinfo = ['ID號','帳號','日期']
        allinfo = []
        for user in users:
            allinfo.append({'id':user.id, 'infos': [user.name, user.created_at]})
        stack = {  # dict
        'add': './../add', 
        'edit': './../edit', 
        'del': '../delete', 
        'main' : '加帳號', 
        'info' : '帳號',
        'titleinfo': titleinfo,
        'allinfo': allinfo
        }
        return render_template('shows.twig', stack=stack)   
    
    @expose('/delete/')
    def delete(self):
        session['bucket'] = 'bucket'
        users = db.session.query(Member).all()
        titleinfo = ['ID號','帳號','日期']
        allinfo = []
        for user in users:
            allinfo.append({'id':user.id, 'infos': [user.name, user.created_at]})
        stack = {  # dict
        'add': './../add', 
        'edit': './../edit', 
        'del': '../del', 
        'main' : '加帳號', 
        'info' : '帳號',
        'titleinfo': titleinfo,
        'allinfo': allinfo
        }
        return render_template('shows.twig', stack=stack)   
    
db.create_all()
appbuilder.add_view(userinfo,'記錄',icon = 'fa-address-card-o',category = '回填')
appbuilder.add_view(userinfo2,'記錄2',icon = 'fa-address-card-o',category = '回填')
appbuilder.add_view(MemberModelView,'會員列表',icon = 'fa-address-card-o',category = '會員資訊')

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

class ApiView(BaseView):
    route_base = "/api"
    @expose('/', methods=['GET', 'POST'])
    def method(self):
        return jsonify({'error_Code':403,'error_Message':'not support'})

db.create_all()
