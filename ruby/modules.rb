#!\workspace\ruby\Ruby26-x64\bin\ruby

require "./function"
require "json"

Function.hola
Function.inicio

archivo = File.read("jason.json")
info = JSON.parse(archivo)
puts info["name"] 
