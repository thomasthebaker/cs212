ta_data = [['Peter', 'USA', 'CS262'],
           ['Andy', 'USA', 'CS212'],
           ['Sarah', 'England', 'CS101'],
           ['Gundega', 'Latvia', 'CS373'],
           ['Job', 'USA', 'CS387'],
           ['Sean', 'USA', 'CS253']]

ta_300 = [name +' is the TA for '+ course
          for name, country, course in ta_data
          if course.find('CS3') >=0]
print(ta_300)
# your code here
