#!\workspace\ruby\Ruby26-x64\bin\ruby

users =
    [   {:name => "andres", :age => 31, :cargo => "esto es algo grande" },
        {:name => "jonathan", :age => 25, :cargo => "esto es algo pequeño" },
        {:name => "jimmy", :age => 85, :cargo => "esto es algo muy glande" }
    ]


puts users[0][:name]
puts users[1][:age]
puts users[2][:cargo]


users.each do |item|
    puts "#{item[:name]}: #{item[:age]}" 
end

langs = {
    :lang => "legniajes",
    :langs => ["Bash", "Python", "Ruby", "Shell"]
}

for leng in langs do
    puts "key is #{leng[0]} and the value is #{leng[1]}"
end
