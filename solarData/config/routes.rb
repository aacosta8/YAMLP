# Rails.application.reload_routes!
Rails.application.routes.draw do
  root to: 'welcome#index'

  get '/'  => 'welcome#index'
  get '/index' => 'welcome#index'
  get '/about' => 'welcome#about'
  get '/contact' => 'welcome#index'
  get '/icons' => 'welcome#index'
  get '/products' => 'welcome#index'
  get '/services' => 'welcome#index'
  get '/typo' => 'welcome#index'

  get 'graphics/show'

  get 'graphics/submit'
  get 'radiations/buscar'
  get 'radiations/energia'
  get 'radiations/calcular'
  resources :radiations
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
