class MyDB2Router(object):
"""A router to control all database operations on models in
the myapp2 application"""

def db_for_read(self, model, **hints):

    print model._meta.app_label
    
    if model._meta.app_label == 'myapp2':
        return 'my_db2'
    return None

def db_for_write(self, model, **hints):
    if model._meta.app_label == 'myapp2':
        return 'my_db2'
    return None

def allow_relation(self, obj1, obj2, **hints):
    if obj1._meta.app_label == 'myapp2' or obj2._meta.app_label == 'myapp2':
        return True
    return None

def allow_syncdb(self, db, model):

    if db == 'my_db2':
        return model._meta.app_label == 'myapp2'
    elif model._meta.app_label == 'myapp2':
        return False
    return None