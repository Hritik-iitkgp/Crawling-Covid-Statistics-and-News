import ply.lex as lex
import ply.yacc as yacc
import random
import io
import re
data1=[]
###DEFINING TOKENS###
tokens = ('BEGINTABLE', 'ENDTABLE',
          'OPENDIV','CLOSEDIV',
          'OPENTABLE','CLOSETABLE',
          'OPENFIGURE','CLOSEFIGURE',
          'OPENPARA', 'CLOSEPARA', 
          'OPENH3','CLOSEH3',
          'CLOSEH2', 'OPENH2',         
          'GARBAGE', 
          'OPENSPAN', 'CLOSESPAN',
          'OPENHREF', 'CLOSEHREF',
          'OPENLI','CLOSELI',
          'OPENUL','CLOSEUL',
          'OPENAV','CLOSENAV','CLOSEHEADER',
          'OPENSUP','CLOSESUP','CONTENT')
t_ignore = '\t'

###############Tokenizer Rules################

# def t_ENDTABLE(t):
#     r'<h2>+\s+<span.class="mw-headline".id="See_also">See.also</span>+\s'
#     return t

# import re

def t_ENDTABLE(t):
    r'<span.class="mw-headline".id="See_also">See.also</span>'
    return t

def t_OPENPARA(t):
    r'<p[^>]*>'
    return t

def t_CLOSEPARA(t):
    r'</p[^>]*>'
    return t

def t_OPENSUP(t):
    r'<sup[^>]*>'
    return t

def t_CLOSESUP(t):
    r'</sup[^>]*>'
    return t

def t_BEGINTABLE(t):
    r'<span.class="mw-page-title-main">Responses.to.the.COVID-19.pandemic.in[^>]*'
    return t

def t_OPENH3(t):
    r'<h3[^>]*>'
    return t

def t_CLOSEH3(t):
    r'</h3[^>]*>'
    return t

def t_OPENH2(t):
    r'<h2[^>]*>'
    return t

def t_CLOSEH2(t):
    r'</h2[^>]*>'
    return t

def t_OPENDIV(t):
    r'<div[^>]*>'
    return t

def t_CLOSEDIV(t):
    r'</div[^>]*>'
    return t

def t_OPENTABLE(t):
    r'<tbody[^>]*>'
    return t

def t_CLOSETABLE(t):
    r'</tbody[^>]*>'
    return t

def t_OPENFIGURE(t):
    r'<figure[^>]*>'
    return t

def t_CLOSEFIGURE(t):
    r'</figure[^>]*>'
    return t

def t_OPENSPAN(t):
    r'<span[^>]*>'
    return t

def t_CLOSESPAN(t):
    r'</span[^>]*>'
    return t

def t_CLOSEHEADER(t):
    r'</header[^>]*'
    return t

def t_OPENUL(t):
    r'<ul[^>]*>'
    return t

def t_CLOSEUL(t):
    r'</ul[^>]*>'
    return t

def t_OPENLI(t):
    r'<li[^>]*>'
    return t

def t_CLOSELI(t):
    r'</li[^>]*>'
    return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    return t

def t_CLOSEHREF(t):
    r'</a[^>]*>'
    return t

def t_OPENAV(t):
    r'<nav[^>]*>'
    return t

def t_CLOSENAV(t):
    r'</nav[^>]*>'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9 ]+'
    return t

def t_GARBAGE(t):
    r'<[^>]*>'
    return t

def t_error(t):
    t.lexer.skip(1)

# def t_CONTENT(t):
#     r'[A-Za-z0-9 \/ \- \[ \] \. \( \) \, \" \' \# \& \:  ]+'
#     return t
def check_special_characters(input_string):
    """Check if special characters #, $, and ^ appear in the string."""
    special_characters = ['#', '$', '&', '^','<']
    for char in special_characters:
        if char in input_string:
            return True
    return False
####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : response'''
    p[0] = p[1]
    #print(p[0])

def p_review(p):
    '''response : test '''  
    
   #print(p[1])

def p_test(p):
    '''test : h3handle parahandle OPENH2 test
     | OPENH2 test
     | OPENLI CONTENT test
     | '''  
def p_h3handle(p):
    '''h3handle : OPENH3 CONTENT CLOSEH3 '''
    global data1
    data1.append(p[2])
def p_parahandle(p):
    '''parahandle : OPENLI content CLOSELI h3handle parahandle
    | OPENPARA content CLOSEPARA h3handle parahandle
    | OPENLI content CLOSELI parahandle 
    | OPENPARA content CLOSEPARA parahandle
    | OPENLI content CLOSELI
    | OPENPARA content CLOSEPARA'''

def p_content(p):
    '''content : CONTENT content
               | '''
    global data1
    if len(p)==3:
        if(len(p[1])>3):             
            data1.append(p[1])
            
        else:
            p[0]=p[2]
    else:
        p[0]=''
      

def p_error(p):
    print(p,"ERRRRRRRRerror")
    #pass  

#########DRIVER FUNCTION#######


def history(month,year):
    # with open("output.txt", "w", encoding="utf-8") as f:
    # for tok in lexer:
        
    with open('response.html', 'r') as file_obj:
        data = file_obj.read()

    lexer = lex.lex()
    lexer.input(data)
    filter_tok=[]
    filter_str=''
    flag=0
    flag1=0
    flag2=0
    flag3=0
    for tok in lexer:
        if(tok.type=='OPENH3' ):
            flag=1
            flag2=1
            filter_tok.append(tok)
            filter_str+= tok.value+ '\n'
        if(flag and tok.type != 'CLOSEH3' and tok.type=='CONTENT'):
            filter_tok.append(tok)
            filter_str+= tok.value+ '\n'
            flag=0
        if(flag2 and tok.type == 'CLOSEH3'):
            filter_tok.append(tok)
            filter_str+= tok.value+ '\n'
        if(flag2 and (tok.type=='OPENPARA' or tok.type=='OPENLI' ) ):
            flag1=1
            filter_tok.append(tok)
            filter_str+= tok.value+ '\n'
        if(flag2 and flag1 and tok.type=='CONTENT' ):
            filter_tok.append(tok)
            filter_str+= tok.value+ '\n'
        if(flag2 and (tok.type=='CLOSEPARA'  or tok.type=='CLOSELI' ) ):
            flag1=0
            filter_tok.append(tok)
            filter_str+= tok.value+ '\n'
        if(flag2 and tok.type=='OPENH2' ):
            filter_tok.append(tok)
            filter_str+= tok.value+ '\n'
            flag3=1
        if(flag3 and tok.type=='CONTENT'):
            if(tok.value=='Timeline of the COVID'):
                break
    #print(filter_str)
    lexer1 = lex.lex()
    lexer1.input(filter_str)
    #for tok in lexer1:
        #print(tok)
    parser = yacc.yacc()
    parser.parse(filter_str)
    file_obj.close()
    global data1
    flag=1
    final_data=[]
    temp=[]
    date=data1[0]
    for i in data1[1:]:
        if len(i.split())==2 and (i.split()[0]==month or i.split()[1]==month):
            flag=0
            final_data.append((date,temp))
            date=i
            temp=[]
        else:
            flag=1
        if(flag):
            temp.append(i)
    final_data.append((date,temp))
    with open(year+month+".txt", "w") as file:
    # Write each element of the list as a separate line in the file
        for content in final_data:
            file.write(content[0] + ":")
            content[1].reverse()
            file.write(' '.join(content[1]) + "\n")
history("February",'2021')

