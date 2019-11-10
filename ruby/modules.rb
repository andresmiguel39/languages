#!\workspace\ruby\Ruby26-x64\bin\ruby

# How to use files and functions from other file

require "./function"
require "json"

# It uses the functions from the file functions 

Function.hola
Function.inicio

# Use a file and do a parse ever the file with the functions called "read" and "parse"

archivo = File.read("jason.json")
info = JSON.parse(archivo)
puts info["name"] 

