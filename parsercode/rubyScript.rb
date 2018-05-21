#This script requieres the gem rubyXL ---> gem install rubyXL

require 'rubyXL' # Assuming rubygems is already required
require 'date'
#Open File
workbook = RubyXL::Parser.parse("NombresSolarRad.xlsx")

#Select first Sheet
sheet = workbook[0]

class Row

  attr_accessor :name, :date, :rad_estacion_01, :rad_estacion_02, :rad_estacion_03

  def initialize(name, date, rad_estacion_01, rad_estacion_02, rad_estacion_03)
    @name = name
    @date = date
    @rad_estacion_01 = rad_estacion_01
    @rad_estacion_02 = rad_estacion_02
    @rad_estacion_03 = rad_estacion_03
   end

end
# fila i
# columna j
dataset = []
for i in 2..1314
  for j in 3..14
    name = sheet[i][j].value
    if name != ""
      year = sheet[i][0].value
      day = sheet[i][1].value - 1
      date = Date.new(year) + day
      name_div = name.split("_")
      start_t = name_div[3]
      start_hour,start_minute = start_t[8..9] , start_t[10..11]
      date_start= Time.utc(year,date.month,date.day,start_hour,start_minute)
      # puts date_start

      end_t = name_div[4]
      end_hour,end_minute = end_t[8..9] , end_t[10..11]
      date_end= Time.utc(year,date.month,date.day,end_hour,end_minute)
      # puts date_end

      average_date = Time.at((date_start.to_i + date_end.to_i)/2).utc
      sec, min, hour, day, month, year, wday, yday, isdst, zone = average_date.to_a
      final_date = Time.utc(year,month,day,hour,min)
      print year,',', month,',',day,',',hour,',',min,','
      puts name
      r = Row.new(name,final_date,"","","")
      dataset << r
    end
  end
end
