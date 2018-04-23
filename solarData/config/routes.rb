Rails.application.routes.draw do
  get 'graphics/show'

  get 'graphics/submit'

  resources :radiations
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
