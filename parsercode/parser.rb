require 'csv'
require 'date'

files = ['6001','6002','6003']

saveFileName = 'allData.csv'
saveFile = CSV.open(saveFileName, "wb")
saveFile << ["station","date and time (UTC)", "image name channel 1","image name channel 2","image name channel 3", "radiation", "clear sky value"]

clr = CSV.read("clr_rad.csv")


count  =0

for file in files
  namefile = file+ '.csv'
  csv = CSV.read(namefile)
  cleanData = CSV.read('cleanData.csv')
  hashMap = Hash.new
  for record in cleanData
    year,month,day,hour,min,name = record
    imageTime = Time.utc(year,month,day,hour,min)
    if hashMap.has_key?(imageTime)
      hashMap[imageTime] << (name)
    else
      hashMap[imageTime] = []
      hashMap[imageTime] << (name)
    end

  end


  for record in csv
    year = record[0][0,4]
    month = record[0][5,2]
    day = record[0][8,2]
    timeStr = record[0].split(' ')[1]
    hour = timeStr[0,2]
    minute = timeStr[3,2]
    second = timeStr[6,2]
    time = Time.local(year,month,day,hour,minute).utc
    rad = record[1]
    if hashMap.has_key?(time)
      arrAll = []
      for thing in hashMap[time]
        arrAll << thing.tr('"', '')
      end
      strAll = arrAll.join(',')
      intFile = (file.to_i)-6000
      saveFile << [intFile,time,strAll.tr('"', ''),rad.tr('"', ''),clr[count][0].tr('"', '')]
      count+=1
    end
  end
end
