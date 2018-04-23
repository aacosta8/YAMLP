class RadiationsController < ApplicationController
  before_action :set_radiation, only: [:show, :edit, :update, :destroy]

  # GET /radiations
  # GET /radiations.json
  def index
    @radiations = Radiation.all
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
end
