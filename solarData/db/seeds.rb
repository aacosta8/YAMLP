# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
require 'csv'
#Open File
# workbook = RubyXL::Parser.parse("db/6001crossimage1.csv")
csv_text = File.read(Rails.root.join('lib', 'seeds', '6001crossimage1.csv'))
csv = CSV.parse(csv_text, :headers => true, :encoding => 'ISO-8859-1')
csv.each do |row|
  rad = Radiation.new
  rad.station = 1
  rad.name = row["image name"]
  rad.rad_time = row["date and time (UTC)"]
  rad.radiation_value = row["radiation"]
  rad.save
  puts row.to_hash
end

csv_text = File.read(Rails.root.join('lib', 'seeds', '6002crossimage1.csv'))
csv = CSV.parse(csv_text, :headers => true, :encoding => 'ISO-8859-1')
csv.each do |row|
  rad = Radiation.new
  rad.station = 2
  rad.name = row["image name"]
  rad.rad_time = row["date and time (UTC)"]
  rad.radiation_value = row["radiation"]
  rad.save
  puts row.to_hash
end

csv_text = File.read(Rails.root.join('lib', 'seeds', '6003crossimage1.csv'))
csv = CSV.parse(csv_text, :headers => true, :encoding => 'ISO-8859-1')
csv.each do |row|
  rad = Radiation.new
  rad.station = 3
  rad.name = row["image name"]
  rad.rad_time = row["date and time (UTC)"]
  rad.radiation_value = row["radiation"]
  rad.save
  puts row.to_hash
end
