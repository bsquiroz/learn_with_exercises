import data as info

def messageCode(code, message): 
    message = message.lower()
    codeMessage = ''

    for char in message:
        codeMessage += code[char]
    
    return codeMessage

print(messageCode(info.my_dict, info.data1)) # *[_!|~=;+$[~%¿:%~%¿~=(~=%+¿!)%~#[$(^(#!$[
print(messageCode(info.my_dict, info.data2)) # $%¿$%~%+%}[~¿%~¿(%+:%~];%~,(%+%~$(#(%=@}%
print(messageCode(info.my_dict, info.data3)) # *[_!~¿[>~@}!>!+~>~:%~!{;%¿:[~];%~¿(~%}%¿~#!{!?