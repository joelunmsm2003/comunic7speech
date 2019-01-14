class CdrRouter(object):
    """
    A router to control all database operations on models in
    the myapp2 application
    """
 
    def db_for_read(self, model, **hints):
        """
        Point all operations on myapp2 models to 'my_db_2'
        """
        if model._meta.app_label == 'cdr':
            return 'cdr'

        if model._meta.app_label == 'discador':
            return 'discador'

        return None
 
    def db_for_write(self, model, **hints):
        """
        Point all operations on myapp models to 'other'
        """
        if model._meta.app_label == 'cdr':
            return 'cdr'

        if model._meta.app_label == 'discador':
            return 'discador'
        return None
 
    def allow_syncdb(self, db, model):
        if db == 'cdr':
            return model._meta.app_label == 'cdr'

        if db == 'discador':
            return model._meta.app_label == 'discador'
        elif model._meta.app_label == 'cdr':
            return False
