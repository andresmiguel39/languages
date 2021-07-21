#Validates PIN number for 4 and 5 digits

def validate_pin(pin)
  if pin =~ /\A\d{4}\z/ or pin =~ /\A\d{6}\z/ 
    return true
  else 
    return false
  end
end

