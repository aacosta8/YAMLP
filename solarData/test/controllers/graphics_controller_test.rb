require 'test_helper'

class GraphicsControllerTest < ActionDispatch::IntegrationTest
  test "should get show" do
    get graphics_show_url
    assert_response :success
  end

  test "should get submit" do
    get graphics_submit_url
    assert_response :success
  end

end
