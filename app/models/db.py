from gluon import current

db = DAL("sqlite://storage.sqlite")

db.define_table('subscription',
   Field('link', requires = IS_NOT_EMPTY()),
   Field('email', requires = IS_EMAIL()),
   Field('price'))

current.db = db
