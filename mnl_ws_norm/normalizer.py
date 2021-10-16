'''
Copyright 2021 Rairye
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

'''

def get_category(char):
    if char.isspace():
        return "SPACE"

    return "NOTSPACE"

def norm_spaces(input_str, space_type, remove_extra_spaces = False):
    if type(input_str) != str or type(space_type) != str:
        return input_str

    if len(input_str) == 0:
        return input_str
    
    result = ""
    last_category = ""
    last_char = ""

    for i in range (len(input_str)):
        current_char = input_str[i]
        current_category = get_category(current_char)

        if current_category == "SPACE":
            if (last_category == "SPACE" and remove_extra_spaces == False) or (last_category == "NOTSPACE" or current_char != last_char):
                result+=space_type

            last_category = current_category
            last_char = current_char
            continue
            
        last_category = current_category
        last_char = current_char
        result+=current_char
    
    return result

def split_by_spaces(input_str):
    if type(input_str) != str:
        return input_str

    words = []
    last_category = ""
    i = 0
    j = 0

    while j < len(input_str):
        current_char = input_str[j]
        current_category = get_category(current_char)

        if current_category == "SPACE" and last_category == "NOTSPACE":
            words.append(input_str[i:j])
            j+=1
            i=j

        elif current_category == "NOTSPACE" and last_category == "SPACE":
            i=j
            j+=1
            
        else:
            j+=1

        last_category = current_category

    words.append(input_str[i:])

    return words
    
