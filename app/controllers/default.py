from applications.PriceDropMaster.modules.scraper import *
from gluon.tools import Mail

def index():
    form = SQLFORM(db.subscription,
                   fields = ['link', 'email'],
                   submit_button = 'Subscribe')
    if form.process().accepted:
        response.flash = 'form accepted'
        scraper = Scraper(form.vars.link)
        cprice = scraper.scrap()
        db(db.subscription.link == form.vars.link).update(price = cprice)
        session.price = cprice
        session.link = form.vars.link
        session.email = form.vars.email
        redirect(URL('price'))

    return dict(form=form)

def price():
    if session.price == 'not available':
        response.title = 'Sorry, this webstore is not supported.'
    else:
        response.title = 'Success!'
        mail = Mail()
        mail.settings.server = 'smtp.gmail.com:587'
        mail.settings.sender = 'liuhang12388@gmail.com'
        mail.settings.login = 'liuhang12388@gmail.com:t56A2BA08K'
        mail.send(session.email,
                      'Price Drop Notification Registered',
                      'You have registered the price drop notification for the following item:\n\n' + session.link+'\n\n' +
                      'The current price is ' + session.price + '.')
    return dict()
