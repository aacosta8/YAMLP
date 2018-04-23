class GraphicsController < ApplicationController
  def show
  end

  def submit
    @start_date = date_params[:start_date]
    @end_date = date_params[:end_date]

    @date = [['Date', 'Radiation']]
    # ['2017-07-19 11:05:00',  3],['2017-07-19 11:20:00',  18],['2017-07-19 11:35:00',  35],['2017-07-19 11:50:00',  137]

    rad = Radiation.created_between(@start_date,@end_date)
    rad.each { |r| @date << [r.rad_time,r.radiation_value]}
    gon.date =@date
  end

  private

  def date_params
    params.permit(:start_date, :end_date)
  end
end
