# Author: Allen Sallinger
# Date: Feb 25th 2018
# create_dayily_notes.py
# creates note outlines for notes I take daily, saves about a minute each day
from datetime import date

def main():
  today = date.today()
  year = str(today.year)
  month = str(today.month)
  if len(str(month)) < 2:
    month = "0" + str(month)

  day = str(today.day)
  if len(str(day)) < 2:
    day = "0" + str(month)

  noteDate = year + month + day
  fileName = "notes_{}.md".format(noteDate)
  template="## notes_{}.md\n\n### TODO\n\n### INPOGRESS\n\n###TODONE\n\n###TOMORROW\n\n###NOTES\n".format(noteDate)

  # write to the note file
  print("=== Creating your notes file ===")
  f = open(fileName, "w")
  f.write(template)
  f.close()

if __name__ == '__main__':
  main()