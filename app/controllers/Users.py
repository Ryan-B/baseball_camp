from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')

    def index(self):
        return self.load_view('users/index.html')

    def register_show(self):
        return self.load_view('users/register_form.html')

    def create(self):
        user_info = request.form
        result = self.models['User'].create(user_info)
        if result['status']:
            session['id'] = result['user']['id']
            session['camper_first'] = result['user']['camper_first']
            session['parent_first'] = result['user']['parent_first']
            session['camper_last'] = result['user']['camper_last']
            session['parent_last'] = result['user']['parent_last']
            return redirect('/player')
        else:
            for msg in result['errors']:
                flash(msg)
            return redirect('/register_show')

    def player_favorite(self, id):
        print "hello woorld"
        favorite_info = request.form
        print favorite_info
        self.models['User'].favorite(favorite_info, id)
        return redirect('/player')



    def player(self):
        return redirect('/all_players')

    def all_players(self):
        camper = self.models['User'].get_all_campers()
        return self.load_view('/users/player.html', camper=camper)

    def show_sign_in(self):
        return self.load_view('/users/sign_in.html')

    def camper_page(self, id):
        camper = self.models['User'].get_one_camper(id)
        print camper
        return self.load_view('/users/camper_page.html', camper=camper)

    def sign_in(self): 
        user_info = request.form
        print user_info
        result = self.models['User'].sign_in(user_info)
        if result['status'] is True:
            session['id'] = result['user']['id']
            session['camper_first'] = result['user']['camper_first']
            session['parent_first'] = result['user']['parent_first']
            session['camper_last'] = result['user']['camper_last']
            session['parent_last'] = result['user']['parent_last']
            return redirect('/')
        else:
            flash('Invalid email or password')
            return redirect('/')

    def pay(self):
        return self.load_view('/left_list/payment_options.html')

    def faq(self):
        return self.load_view('/left_list/FAQ.html')

    def extra_bens(self):
        return self.load_view('/left_list/extra_bens.html')

    def maps(self):
        return self.load_view('/left_list/maps.html')

    def alki(self):
        return self.load_view('/alki/alki.html')

    def history(self):
        return self.load_view('/alki/history.html')


    def logout(self):
        session.pop('id')
        session.pop('camper_first')
        session.pop('parent_first')
        session.pop('camper_last')
        session.pop('parent_last')
        return redirect('/')