# received file from user
while True:
    try:
        path = input('Enter a file name:')
        file = open(path, 'r', encoding='utf-8')
        lines = file.read()
        
    # print the length of the content
        print('The length of text:' , len(lines))



    #delimiter     
        delimiter = input('Enter delimiter')
        if delimiter == '':
            line_split1 = lines.split('\n')
        elif delimiter.isspace():
            line_split1 = lines.split()
        else:
            line_split1 = lines.split(delimiter)
            
        print('*'*30)
        print('The Number of sentences: ',len(line_split1))
        
        valid_sen = [i for i in line_split1 if i.strip()]
        
        print('The Number of Valid Sentence is:',len(valid_sen))
        
     # create a dictionary   
        
        my_dict = dict(enumerate(valid_sen, start=1))
        #print(type(my_dict))
        print(my_dict)
    # received the number from user and print from list
        while True:
            try:
                dict_line = int(input("Enter a sentence number to print: "))
                print(dict_line)
            
                if dict_line > 0 and dict_line < 35:
                    print(my_dict[dict_line])
                    break
                else:
                    print('wrong sentence number. it must be between 1 and 34')
                    continue

            except ValueError:
                print("not a number")
                continue

    # random sentence number
        import random
        dict_random = random.randint(1,34)
        print('\n','*'*20, 'A Quote For You','*'*20)
        print(str(dict_random) +" "+ my_dict[dict_random],'\n')


    # start with letter
        while True:
            #start_letter = input('Enter a character')
            #out_list = [i.strip() for i in valid_sen] 
            #final = [j for j in out_list if j[0]== start_letter]
            #print(final)

            start_letter = input('Enter a character')
            out_list = [j for j in [i.strip() for i in valid_sen] if j[0] == start_letter ]
            print(*out_list,'\n')
            if out_list : break
            else: continue

   

    except IOError:
        print('Please Check File Location Again')
        continuea
    
    break












    
    



    
