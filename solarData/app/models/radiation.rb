class Radiation < ApplicationRecord

  scope :created_between, lambda {|start_date, end_date| where("rad_time >= ? AND rad_time <= ?", start_date, end_date )}

end
