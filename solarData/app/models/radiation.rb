class Radiation < ApplicationRecord

  scope :created_between, lambda {|start_date, end_date| where("rad_time >= ? AND rad_time <= ?", start_date, end_date )}
  scope :created_between_est, lambda {|start_date, end_date,estacion| where("rad_time >= ? AND rad_time <= ? AND station = ? ", start_date, end_date,estacion)}
end
