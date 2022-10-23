import json
# function returns text to send 
def wish_hbd(name):
    return f"@everyone \nHappy Birthday to you, {name}"

# This function returns a list of values 
# based on conditions on moneth and day from the JSON file.
# use to return names of members having their birthday on current date.
def getJsonData(file, name, birth_month, birth_date, current_month, current_date):
     
    # Load the file's data in 'data' variable
    data = json.load(file)
    retv =[]
 
    # If the attributes' value conditions are satisfied,
    # append the name into the list to be returned.
    for i in data:
        if(i[birth_month]== current_month and i[birth_date]== current_date):
           retv.append(i[name])
    return retv
 
