require 'test_helper'

class RadiationsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @radiation = radiations(:one)
  end

  test "should get index" do
    get radiations_url
    assert_response :success
  end

  test "should get new" do
    get new_radiation_url
    assert_response :success
  end

  test "should create radiation" do
    assert_difference('Radiation.count') do
      post radiations_url, params: { radiation: { name: @radiation.name, rad_time: @radiation.rad_time, radiation_value: @radiation.radiation_value, station: @radiation.station } }
    end

    assert_redirected_to radiation_url(Radiation.last)
  end

  test "should show radiation" do
    get radiation_url(@radiation)
    assert_response :success
  end

  test "should get edit" do
    get edit_radiation_url(@radiation)
    assert_response :success
  end

  test "should update radiation" do
    patch radiation_url(@radiation), params: { radiation: { name: @radiation.name, rad_time: @radiation.rad_time, radiation_value: @radiation.radiation_value, station: @radiation.station } }
    assert_redirected_to radiation_url(@radiation)
  end

  test "should destroy radiation" do
    assert_difference('Radiation.count', -1) do
      delete radiation_url(@radiation)
    end

    assert_redirected_to radiations_url
  end
end
