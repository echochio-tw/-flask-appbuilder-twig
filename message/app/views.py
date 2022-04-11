from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView,AppBuilder,expose,BaseView,ModelRestApi,has_access
from . import appbuilder, db
from .models import Member
from flask import jsonify,make_response,session

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
        return render_template('shows.twig', stack=stack)
    
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
