from system.core.router import routes

routes['default_controller'] = 'Users'
routes['GET']['/register_show'] = 'Users#register_show'
routes['POST']['/create'] = 'Users#create'
routes['POST']['/sign_in'] = 'Users#sign_in'
routes['GET']['/logout'] = 'Users#logout'
routes['GET']['/player'] = 'Users#player'
routes['GET']['/all_players'] = 'Users#all_players'
routes['GET']['/show_sign_in'] = 'Users#show_sign_in'
routes['GET']['/camper_page/<id>'] = 'Users#camper_page'
routes['GET']['/pay'] = "Users#pay"
routes['GET']['/faq'] ='Users#faq'
routes['GET']['/extra_bens'] = 'Users#extra_bens'
routes['GET']['/maps'] ='Users#maps'
routes['GET']['/alki'] ='Users#alki'
routes['POST']['/player_favorite/<id>'] = 'Users#player_favorite'
routes['GET']['/history'] = 'Users#history'