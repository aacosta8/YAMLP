class CreateRadiations < ActiveRecord::Migration[5.1]
  def change
    create_table :radiations do |t|
      t.integer :station
      t.string :name
      t.datetime :rad_time
      t.float :radiation_value

      t.timestamps
    end
  end
end
