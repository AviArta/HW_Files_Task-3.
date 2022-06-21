files_list = ['best_grade.py', 'check_count.py', 'grades.txt', 'hello.py', 'hello.txt', 'test_append.txt', 'test_write.txt', 'warandpeace.txt', 'write_to_file.py']
files_dict = {}
sorted_files_dict = {}
def file_sort(files_list):
    for file_name in files_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            list_str = file.readlines()
            list_str_strip = []
            for str_ in list_str:
                str_ = str_.strip()
                list_str_strip.append(str_)
            files_dict[file_name] = (len(list_str), list_str_strip)
    sorted_files_list = sorted(files_dict.values())
    #print(len(files_dict))
    for element in sorted_files_list:
        for key in files_dict:
            if element[0] == files_dict[key][0]:
                sorted_files_dict[key] = (files_dict[key][0], files_dict[key][1])
    #print(sorted_files_dict)
    return sorted_files_dict
file_sort(files_list)

def files_result(files_list):
    file_sort(files_list)
    for file_name in sorted_files_dict:
        with open('result_task-3.txt', 'a', encoding='utf-8') as result_file:
            result_file.write(f"{file_name}\n {sorted_files_dict[file_name][0]}\n {sorted_files_dict[file_name][1]}\n")
files_result(files_list)




# ____________________________
# result_file.write(file_name + '\n')
            # result_file.write(str(sorted_files_dict[file_name][0]) + '\n')
            # result_file.write(f" {sorted_files_dict[file_name][1][:5]} \n")

            # for str_ in sorted_files_dict[file_name][1][:5]:
            #     if str_ == file_name[1][1][-1]:
            #         result_file.write(str_ + '\n')
            #     else:
            #         result_file.write(str_)
#_____________________________
        #     for string in list_str:
        #         string = string.strip()
        #     print(string)
        # list_str_strip.append(string)
 #____________________________
    #print(len(list_str_strip))
                #list_str_final = ','.join(list_str_strip)
            #files_dict[file_name] = (len(list_str), list_str_strip)
    #sorted_files_list = sorted(files_dict.values())
    # for element in sorted_files_list:
    #     for key in files_dict:
    #         if element[0] == files_dict[key][0]:
    #             sorted_files_dict[key] = (files_dict[key][0], files_dict[key][1])
    #print(type(sorted_files_dict))
#_____________________________
    #print(len(sorted_files_list))
    #sorted_files_list = sorted(files_dict.items(), key=lambda x: x[1][0])
#list_str_final = '\n'.join(list_str_strip)