def get_total_word(text):
  temp = text.split()
  return len(temp)

def get_total_char(text):
  text2 = text.lower()
  text2 = text2.split() 
  char_dict = {} 
  for x in text2:
    for y in x:
      if y not in char_dict:
        char_dict[y] = 1
      else:
        char_dict[y] += 1
  return char_dict

def sort_on(dict):
  return dict["num"]

def sorted_dict(char_dict):
 final_list= []
 for x,y in char_dict.items():
   new_dict = {}
   new_dict["char"] = x
   new_dict["num"] = y
   final_list.append(new_dict)
 final_list.sort(reverse=True, key=sort_on)
 return final_list
