class RadiationsController < ApplicationController
  before_action :set_radiation, only: [:show, :edit, :update, :destroy]

  # GET /radiations
  # GET /radiations.json
  def index
    @radiations = Radiation.take(10)
  end

  def buscar
    start = Date.strptime(busqueda_params[:start_date], "%m/%d/%Y")
    end_date = Date.strptime(busqueda_params[:end_date], "%m/%d/%Y")
    estacion = busqueda_params[:estacion]
    @radiations = Radiation.created_between_est(start, end_date,estacion)
    @date = [['Date', 'Radiation']]
    # ['2017-07-19 11:05:00',  3],['2017-07-19 11:20:00',  18],['2017-07-19 11:35:00',  35],['2017-07-19 11:50:00',  137]

    rad = Radiation.created_between_est(start, end_date,estacion)
    rad.each { |r| @date << [r.rad_time,r.radiation_value]}
    gon.date =@date
  end

  def energia

  end

  def calcular
    start = Date.strptime(calcular_params[:start_date], "%m/%d/%Y")
    end_date = Date.strptime(calcular_params[:end_date], "%m/%d/%Y")
    rad = Radiation.created_between_est(start, end_date,1)
    sum = 0
    rad.each { |r| sum += r.radiation_value.to_f*15}
    @energia = (sum*calcular_params[:area].to_f*0.15).to_i/100  
  end

  # GET /radiations/1
  # GET /radiations/1.json
  def show
  end

  # GET /radiations/new
  def new
    @radiation = Radiation.new
  end

  # GET /radiations/1/edit
  def edit
  end

  # POST /radiations
  # POST /radiations.json
  def create
    @radiation = Radiation.new(radiation_params)

    respond_to do |format|
      if @radiation.save
        format.html { redirect_to @radiation, notice: 'Radiation was successfully created.' }
        format.json { render :show, status: :created, location: @radiation }
      else
        format.html { render :new }
        format.json { render json: @radiation.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /radiations/1
  # PATCH/PUT /radiations/1.json
  def update
    respond_to do |format|
      if @radiation.update(radiation_params)
        format.html { redirect_to @radiation, notice: 'Radiation was successfully updated.' }
        format.json { render :show, status: :ok, location: @radiation }
      else
        format.html { render :edit }
        format.json { render json: @radiation.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /radiations/1
  # DELETE /radiations/1.json
  def destroy
    @radiation.destroy
    respond_to do |format|
      format.html { redirect_to radiations_url, notice: 'Radiation was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_radiation
      @radiation = Radiation.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def radiation_params
      params.require(:radiation).permit(:station, :name, :rad_time, :radiation_value)
    end

    def busqueda_params
      params.permit(:start_date,:end_date,:estacion)
    end

    def calcular_params
      params.permit(:start_date,:end_date,:area,:rendimiento, :lat, :lon)
    end

end
