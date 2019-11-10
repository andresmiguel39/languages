#!\workspace\ruby\Ruby26-x64\bin\ruby

usuari = ['jdoe', 'peter', 'mary', 'bob']

usuari.each do |u|
    puts u
end

usuari.each {|u| puts u}

i = 0
while i < usuari.length
    puts usuari[i]
    i = i + 1
end

for y in 1..5 do
    puts "hello #{y}"
end

5.times do |n|
    puts  "hello #{n}"
end

0.upto(2) do |y|
    puts "intex #{y} user #{usuari[y]}"
end

3.downto(1) do |here|
    puts "index #{here}  user #{usuari[here]}"
end

