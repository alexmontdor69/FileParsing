import json

def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    parsed_file = []
    i = 0
    while i < len(lines):
        # Store the first line parsed in a variable called manuprod
        manuprod = lines[i].strip()

        # Disregard the line starting by "model" and empty lines
        i += 1
        while i < len(lines) and (lines[i].startswith('Model') or lines[i].strip() == ''):
            i += 1

        # Store in a list called modelids all lines starting with the character "
        # until the line starting by "Value" - do not store the first and last " of the line
        modelids = []
        while i < len(lines) and not lines[i].startswith('Value'):
            if lines[i].startswith('"'):
                modelids.append(lines[i].strip()[1:-1])
            i += 1

        # Disregard the line starting by "Value"
        i += 1
        while i < len(lines) and lines[i].startswith('Value'):
            i += 1

        # Store all the lines starting by a number in a list called buttonevents
        buttonevents = []
        while i < len(lines) and lines[i].strip()[0].isdigit():
            #print (lines[i].strip( ))
            #print (lines[i].split('\t'))
            #print (lines[i].strip().split('\t'))
            if len(lines[i].strip().split('\t')) == 3:
                value, action, button = lines[i].strip().split('\t')
                print ({'value':value, 'action':action, 'button':button})
                buttonevents.append({'value':value, 'action':action, 'button':button})
            i += 1

        # If i is the number of length of modelids[0] and j the length of manuprod,
        # store the first j-i characters of manuprod into manufacturer
        if modelids and len(modelids[0]) > 0:
            k = len(manuprod)
            l = len(modelids[0])
            if k<=l+3:
                manufacturer = manuprod[:k-l-3]
            else:
                manufacturer='n/a'

        else:
            manufacturer ='n/a'

        # Append {manufacturer, modelids, buttonevents} to parsed_file
        parsed_file.append({'manufacturer': manufacturer, 'modelids': modelids, 'buttonevents': buttonevents})

    print (parse_file)
    # Write parsed_file to a JSON file called file.json
    with open('file.json', 'w') as f:
        json.dump(parsed_file, f)

parse_file('filename.txt')
