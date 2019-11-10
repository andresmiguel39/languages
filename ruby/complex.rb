#!\workspace\ruby\Ruby26-x64\bin\ruby

# Create an array of hashes

users =
    [   {:name => "andres", :age => 31, :cargo => "esto es algo grande" },
        {:name => "jonathan", :age => 25, :cargo => "esto es algo pequeño" },
        {:name => "jimmy", :age => 85, :cargo => "esto es algo muy glande" }
    ]

# print over    
puts users[0][:name]
puts users[1][:age]
puts users[2][:cargo]

#loop for printiing 
users.each do |item|
    puts "#{item[:name]}: #{item[:age]}" 
end

# other example
langs = {
    :lang => "legniajes",
    :langs => ["Bash", "Python", "Ruby", "Shell"]
}

for leng in langs do
    puts "key is #{leng[0]} and the value is #{leng[1]}"
end
